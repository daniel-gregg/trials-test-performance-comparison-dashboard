import React from 'react';
import { ComparisonResult } from '../types';

interface ChartVisualizationProps {
  results: ComparisonResult[];
}

const ChartVisualization: React.FC<ChartVisualizationProps> = ({ results }) => {
  if (!results || results.length === 0) {
    return (
      <div className="card">
        <div className="card-header">Performance Visualization</div>
        <div className="card-body">
          <p>No data available for visualization. Add trial data to see charts.</p>
        </div>
      </div>
    );
  }

  // Simple bar chart representation using CSS
  const maxProfit = Math.max(...results.map(r => Math.abs(r.profit)));
  const maxYield = Math.max(...results.map(r => r.trial.yield));

  return (
    <div className="card">
      <div className="card-header">Performance Visualization</div>
      <div className="card-body">
        
        {/* Profit Comparison Chart */}
        <div className="chart-container mb-4">
          <h5>Profit per Acre Comparison</h5>
          <div style={{ padding: '1rem 0' }}>
            {results.map((result, index) => (
              <div key={index} className="mb-2">
                <div style={{ 
                  display: 'flex', 
                  alignItems: 'center',
                  marginBottom: '0.5rem'
                }}>
                  <div style={{ 
                    width: '120px', 
                    fontSize: '0.9rem',
                    textAlign: 'right',
                    paddingRight: '10px'
                  }}>
                    {result.trial.name}
                  </div>
                  <div style={{ 
                    flex: 1,
                    height: '30px',
                    background: '#f0f0f0',
                    position: 'relative',
                    borderRadius: '4px'
                  }}>
                    <div style={{
                      height: '100%',
                      width: `${Math.abs(result.profit) / maxProfit * 100}%`,
                      background: result.profit >= 0 
                        ? 'linear-gradient(90deg, #27ae60, #2ecc71)' 
                        : 'linear-gradient(90deg, #e74c3c, #c0392b)',
                      borderRadius: '4px',
                      display: 'flex',
                      alignItems: 'center',
                      justifyContent: 'center',
                      color: 'white',
                      fontSize: '0.8rem',
                      fontWeight: 'bold'
                    }}>
                      ${result.profit.toFixed(0)}
                    </div>
                  </div>
                </div>
              </div>
            ))}
          </div>
        </div>

        {/* Yield Comparison Chart */}
        <div className="chart-container mb-4">
          <h5>Yield Comparison (bu/acre)</h5>
          <div style={{ padding: '1rem 0' }}>
            {results.map((result, index) => (
              <div key={index} className="mb-2">
                <div style={{ 
                  display: 'flex', 
                  alignItems: 'center',
                  marginBottom: '0.5rem'
                }}>
                  <div style={{ 
                    width: '120px', 
                    fontSize: '0.9rem',
                    textAlign: 'right',
                    paddingRight: '10px'
                  }}>
                    {result.trial.name}
                  </div>
                  <div style={{ 
                    flex: 1,
                    height: '30px',
                    background: '#f0f0f0',
                    position: 'relative',
                    borderRadius: '4px'
                  }}>
                    <div style={{
                      height: '100%',
                      width: `${result.trial.yield / maxYield * 100}%`,
                      background: 'linear-gradient(90deg, #3498db, #2980b9)',
                      borderRadius: '4px',
                      display: 'flex',
                      alignItems: 'center',
                      justifyContent: 'center',
                      color: 'white',
                      fontSize: '0.8rem',
                      fontWeight: 'bold'
                    }}>
                      {result.trial.yield.toFixed(1)}
                    </div>
                  </div>
                </div>
              </div>
            ))}
          </div>
        </div>

        {/* ROI Scatter Plot Representation */}
        <div className="chart-container">
          <h5>ROI vs Cost Analysis</h5>
          <div style={{ 
            display: 'grid', 
            gridTemplateColumns: 'repeat(auto-fit, minmax(200px, 1fr))',
            gap: '1rem',
            padding: '1rem 0'
          }}>
            {results.map((result, index) => (
              <div key={index} style={{
                background: result.roi >= 0 ? '#e8f5e8' : '#f5e8e8',
                border: `2px solid ${result.roi >= 0 ? '#27ae60' : '#e74c3c'}`,
                borderRadius: '8px',
                padding: '1rem',
                textAlign: 'center'
              }}>
                <div style={{ fontWeight: 'bold', marginBottom: '0.5rem' }}>
                  {result.trial.name}
                </div>
                <div style={{ fontSize: '1.2rem', fontWeight: 'bold', color: result.roi >= 0 ? '#27ae60' : '#e74c3c' }}>
                  {result.roi.toFixed(1)}% ROI
                </div>
                <div style={{ fontSize: '0.9rem', color: '#666' }}>
                  Cost: ${result.totalCost.toFixed(0)}/acre
                </div>
              </div>
            ))}
          </div>
        </div>

        <div className="mt-3 text-center text-info">
          <small>
            💡 Charts show relative performance. Higher bars indicate better performance.
            Green indicates profitable trials, red indicates losses.
          </small>
        </div>
      </div>
    </div>
  );
};

export default ChartVisualization;