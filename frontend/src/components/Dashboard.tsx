import React from 'react';
import ControlPanel from './ControlPanel';
import ResultsArea from './ResultsArea';

const Dashboard: React.FC = () => {
  return (
    <div className="dashboard">
      <div className="dashboard-header">
        <h2>Performance Analysis Dashboard</h2>
        <p>
          Input your trial data and pricing information to generate comprehensive 
          performance comparisons and visualizations. Use the control panel to 
          configure parameters and view results in real-time.
        </p>
      </div>
      
      <ControlPanel />
      <ResultsArea />
    </div>
  );
};

export default Dashboard;