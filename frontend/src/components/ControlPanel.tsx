import React, { useState } from 'react';
import { useTrials } from '../context/TrialsContext';
import TrialDataForm from './TrialDataForm';
import PriceInputForm from './PriceInputForm';

const ControlPanel: React.FC = () => {
  const [activeTab, setActiveTab] = useState<'trials' | 'prices'>('trials');
  const { runComparison, isLoading } = useTrials();

  return (
    <div className="control-panel">
      <h3>Control Panel</h3>
      
      <div className="tab-navigation mb-3">
        <button 
          className={`btn ${activeTab === 'trials' ? 'btn-primary' : 'btn-secondary'} mr-2`}
          onClick={() => setActiveTab('trials')}
        >
          Trial Data
        </button>
        <button 
          className={`btn ${activeTab === 'prices' ? 'btn-primary' : 'btn-secondary'}`}
          onClick={() => setActiveTab('prices')}
        >
          Price Inputs
        </button>
      </div>

      <div className="tab-content">
        {activeTab === 'trials' && <TrialDataForm />}
        {activeTab === 'prices' && <PriceInputForm />}
      </div>

      <div className="mt-3">
        <button 
          className="btn btn-success"
          onClick={runComparison}
          disabled={isLoading}
          style={{ width: '100%' }}
        >
          {isLoading ? 'Running Analysis...' : 'Run Performance Analysis'}
        </button>
      </div>
    </div>
  );
};

export default ControlPanel;