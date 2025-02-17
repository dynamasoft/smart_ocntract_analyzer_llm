from dotenv import load_dotenv
import openai
import os
import time
from slither.slither import Slither

# Load environment variables from .env file
load_dotenv()

# Get OpenAI API Key from environment variables
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

if not OPENAI_API_KEY:
    raise ValueError("OpenAI API key not found. Please set it in the .env file.")

# Ensure the `sol/` directory exists
SOL_DIR = "sol"
os.makedirs(SOL_DIR, exist_ok=True)


def save_contract(contract_code):
    """
    Saves the Solidity contract to a file in the `sol/` folder.
    """
    contract_path = os.path.join(SOL_DIR, "contract.sol")
    with open(contract_path, "w") as file:
        file.write(contract_code)
    return contract_path


def analyze_contract(contract_path):
    """
    Analyzes a Solidity contract using Slither and returns a list of vulnerabilities.
    """
    slither = Slither(contract_path)

    contracts = [contract.name for contract in slither.contracts]

    slither.run_detectors()
    vulnerabilities = []

    # Extract detected issues
    for detector in slither.detectors:
        results = detector._detect(slither)
        for result in results:
            vulnerabilities.append(result)

    return vulnerabilities


def get_llm_analysis(vulnerabilities):
    """
    Passes the Slither output to ChatGPT-4 to generate structured recommendations.
    """
    prompt = f"""
    The following vulnerabilities were found in a Solidity smart contract:

    {vulnerabilities}

    Please provide:
    1. A structured list of vulnerabilities.
    2. Recommended actions to fix them.
    """

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {
                "role": "system",
                "content": "You are an expert in Solidity smart contract security.",
            },
            {"role": "user", "content": prompt},
        ],
        api_key=OPENAI_API_KEY,
    )

    return response["choices"][0]["message"]["content"]


if __name__ == "__main__":
    print("Paste your Solidity smart contract below (end with 'EOF'):")
    #     contract_code = """// SPDX-License-Identifier: MIT
    # pragma solidity ^0.8.0;

    # contract VulnerableContract {
    #     mapping(address => uint256) public balances;

    #     function deposit() public payable {
    #         balances[msg.sender] += msg.value;
    #     }

    #     function withdraw(uint256 _amount) public {
    #         require(balances[msg.sender] >= _amount, "Insufficient balance");

    #         (bool success, ) = msg.sender.call{value: _amount}("");
    #         require(success, "Transfer failed");

    #         balances[msg.sender] -= _amount;
    #     }

    #     function getBalance() public view returns (uint256) {
    #         return address(this).balance;
    #     }
    # }
    # """
    #     print("\nSaving contract to sol/contract.sol...\n")

    # contract_path = save_contract(contract_code)

    print("\nRunning security analysis...\n")

    contract_path = "sol/contract.sol"
    vulnerabilities = analyze_contract(contract_path)

    if vulnerabilities:
        print(
            "\nSending vulnerabilities to ChatGPT-4 for structured recommendations...\n"
        )
        structured_output = get_llm_analysis("\n".join(vulnerabilities))
        print("\n==== STRUCTURED SECURITY ANALYSIS ====\n")
        print(structured_output)
    else:
        print("No vulnerabilities found in the contract.")

    # Cleanup: Remove the contract file after analysis
    time.sleep(2)  # Wait for a moment before deleting
    # os.remove(contract_path)
