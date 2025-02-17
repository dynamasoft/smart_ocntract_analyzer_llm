import './App.css';
import React, { useState } from 'react';

function App() {
  const [text, setText] = useState('');

  const handleAnalyze = () => {
    // Add logic to analyze the smart contract
    console.log('Analyzing:', text);
  };

  const handleClear = () => {
    setText('');
  };

  return (
    <div className="App">
      <header className="App-header">
        <textarea
          value={text}
          onChange={(e) => setText(e.target.value)}
          placeholder="Insert smart contract here..."
          rows="10"
          cols="50"
        />
        <div>          
          <button onClick={handleClear}>Clear</button>
          <button onClick={handleAnalyze}>Analyze</button>
        </div>
      </header>
    </div>
  );
}

export default App;
