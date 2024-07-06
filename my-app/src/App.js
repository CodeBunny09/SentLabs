import React, { useState } from 'react';
import './App.css';

function App() {
  const [inputText, setInputText] = useState('');
  const [error, setError] = useState('');
  const [showOutput, setShowOutput] = useState(false);
  const [response, setResponse] = useState({});

  const handleInputChange = (e) => {
    setInputText(e.target.value);
  };

  const handleSubmit = () => {
    if (inputText.trim().length === 0) {
      setError('Input text cannot be empty.');
      return;
    }

    setError('');
    
    // Make the API call
    fetch('http://localhost:8000/api/summarize/', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ text: inputText }),
    })
      .then(response => {
        if (!response.ok) {
          throw new Error(`HTTP error! Status: ${response.status}`);
        }
        return response.json();
      })
      .then(data => {
        setResponse(data);
        setShowOutput(true);
      })
      .catch((error) => {
        console.error('Error:', error);
        setError('An error occurred while fetching the summary. See console for details.');
      });
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
              <div className="summary-text-inner">{response.summary}</div>
            </div>
          </div>
          <div className="wordcloud-container">
            <img src={response.wordcloud} alt="Word Cloud" className="wordcloud-image" />
          </div>
        </div>
      )}
    </div>
  );
}

export default App;
