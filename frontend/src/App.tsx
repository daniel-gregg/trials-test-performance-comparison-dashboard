import React from 'react';
import './App.css';
import Header from './components/Header';
import Dashboard from './components/Dashboard';
import { TrialsProvider } from './context/TrialsContext';

function App() {
  return (
    <TrialsProvider>
      <div className="App">
        <Header />
        <main className="main-content">
          <Dashboard />
        </main>
      </div>
    </TrialsProvider>
  );
}

export default App;
