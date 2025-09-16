import React from 'react';
import { ComparisonResult } from '../types';

interface ComparisonTableProps {
  results: ComparisonResult[];
}

const ComparisonTable: React.FC<ComparisonTableProps> = ({ results }) => {
  if (!results || results.length === 0) {
    return (
      <div className="card">
        <div className="card-header">Performance Comparison Table</div>
        <div className="card-body">
          <p>No comparison data available. Add trial data to see results.</p>
        </div>
      </div>
    );
  }

  return (
    <div className="card mb-3">
      <div className="card-header">Performance Comparison Table</div>
      <div className="card-body">
        <div style={{ overflowX: 'auto' }}>
          <table className="table">
            <thead>
              <tr>
                <th>Trial Name</th>
                <th>Crop</th>
                <th>Variety</th>
                <th>Yield (bu/acre)</th>
                <th>Total Cost ($/acre)</th>
                <th>Revenue ($/acre)</th>
                <th>Profit ($/acre)</th>
                <th>ROI (%)</th>
                <th>Rank</th>
              </tr>
            </thead>
            <tbody>
              {results.map((result, index) => (
                <tr key={result.trial.name + index}>
                  <td>{result.trial.name}</td>
                  <td>{result.trial.crop}</td>
                  <td>{result.trial.variety || 'N/A'}</td>
                  <td>{result.trial.yield.toFixed(1)}</td>
                  <td>${result.totalCost.toFixed(2)}</td>
                  <td>${result.revenue.toFixed(2)}</td>
                  <td>
                    <span className={result.profit >= 0 ? 'text-success' : 'text-danger'}>
                      ${result.profit.toFixed(2)}
                    </span>
                  </td>
                  <td>
                    <span className={result.roi >= 0 ? 'text-success' : 'text-danger'}>
                      {result.roi.toFixed(1)}%
                    </span>
                  </td>
                  <td>
                    <span className="badge badge-primary">
                      #{result.rank}
                    </span>
                  </td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
        
        <div className="mt-3">
          <h5>Summary Statistics</h5>
          <div className="row">
            <div className="col-md-3">
              <div className="text-center">
                <strong>Total Trials</strong>
                <div className="text-info">{results.length}</div>
              </div>
            </div>
            <div className="col-md-3">
              <div className="text-center">
                <strong>Avg Profit</strong>
                <div className="text-success">
                  ${(results.reduce((sum, r) => sum + r.profit, 0) / results.length).toFixed(2)}
                </div>
              </div>
            </div>
            <div className="col-md-3">
              <div className="text-center">
                <strong>Best ROI</strong>
                <div className="text-success">
                  {Math.max(...results.map(r => r.roi)).toFixed(1)}%
                </div>
              </div>
            </div>
            <div className="col-md-3">
              <div className="text-center">
                <strong>Profitable Trials</strong>
                <div className="text-info">
                  {results.filter(r => r.profit > 0).length}/{results.length}
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default ComparisonTable;