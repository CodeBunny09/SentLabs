import React, { useState } from 'react';
import './App.css';
import dummyResponses from './dummy_responses.json';

function App() {
  const [inputText, setInputText] = useState('');
  const [error, setError] = useState('');
  const [showOutput, setShowOutput] = useState(false);

  const handleInputChange = (e) => {
    setInputText(e.target.value);
  };

  const handleSubmit = () => {
    if (inputText.trim().length === 0) {
      setError('Input text cannot be empty.');
      return;
    }

    setError('');
    setShowOutput(true);
  };

  return (
    <div className="App">
      <header className="App-header">
        <h1 className="app-title">SentLabs</h1>
      </header>
      {!showOutput ? (
        <div className="input-container">
          <textarea
            value={inputText}
            onChange={handleInputChange}
            placeholder="Enter your text here..."
          />
          <button onClick={handleSubmit}>Submit</button>
          {error && <p className="error-message">{error}</p>}
        </div>
      ) : (
        <div className="output-container">
          <div className="summary-container">
            <div className="summary-text">
              <div className="summary-text-inner">{dummyResponses.summary}</div>
            </div>
          </div>
          <div className="wordcloud-container">
            <img src={dummyResponses.wordcloud} alt="Word Cloud" className="wordcloud-image" />
          </div>
        </div>
      )}
    </div>
  );
}

export default App;
