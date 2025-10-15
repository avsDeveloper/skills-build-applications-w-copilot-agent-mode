
import React from 'react';
import ReactDOM from 'react-dom/client';
import 'bootstrap/dist/css/bootstrap.min.css';
import './index.css';
import App from './App';
import reportWebVitals from './reportWebVitals';

console.log('Octofit Tracker React app is starting.');
console.log('Backend REST API base URL:', `https://${process.env.REACT_APP_CODESPACE_NAME}-8000.app.github.dev/api/`);

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
);

reportWebVitals();
