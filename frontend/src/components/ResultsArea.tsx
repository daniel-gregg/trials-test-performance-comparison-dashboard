import React from 'react';
import { useTrials } from '../context/TrialsContext';
import ComparisonTable from './ComparisonTable';
import ChartVisualization from './ChartVisualization';

const ResultsArea: React.FC = () => {
  const { comparisonResults, isLoading } = useTrials();

  if (isLoading) {
    return (
      <div className="results-area">
        <h3>Analysis Results</h3>
        <div className="loading">
          <div>Running performance analysis...</div>
          <div style={{ marginTop: '1rem', color: '#3498db' }}>
            Please wait while we process your data
          </div>
        </div>
      </div>
    );
  }

  if (!comparisonResults) {
    return (
      <div className="results-area">
        <h3>Analysis Results</h3>
        <div className="empty-state">
          <h3>Ready for Analysis</h3>
          <p>
            Configure your trial data and pricing information in the control panel,
            then click "Run Performance Analysis" to see results here.
          </p>
          <div style={{ marginTop: '2rem', opacity: 0.7 }}>
            <p>📊 Performance comparison tables</p>
            <p>📈 Interactive charts and graphs</p>
            <p>💰 ROI and profitability analysis</p>
            <p>📋 Detailed trial reports</p>
          </div>
        </div>
      </div>
    );
  }

  return (
    <div className="results-area">
      <h3>Analysis Results</h3>
      
      <div className="results-content">
        <div className="mb-3">
          <h4>Performance Summary</h4>
          <div className="card">
            <div className="card-body">
              <p>Analysis completed successfully! Review the detailed comparison below.</p>
              <small className="text-info">
                Last updated: {new Date().toLocaleString()}
              </small>
            </div>
          </div>
        </div>

        <ComparisonTable results={comparisonResults} />
        <ChartVisualization results={comparisonResults} />
      </div>
    </div>
  );
};

export default ResultsArea;