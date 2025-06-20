import React from 'react';
import JobList from './components/JobList';
import './App.css';

function App() {
  return (
    <div className="container mx-auto p-4">
      <h1 className="text-2xl font-bold mb-4">Job Aggregator</h1>
      <JobList />
    </div>
  );
}

export default App;
