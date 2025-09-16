import React, { useState } from 'react';
import { useTrials } from '../context/TrialsContext';
import { PriceData } from '../types';

const PriceInputForm: React.FC = () => {
  const { updatePrices, priceData } = useTrials();
  const [formData, setFormData] = useState<PriceData>(
    priceData || {
      corn: 4.50,
      soybeans: 12.00,
      wheat: 6.00,
      rice: 14.00,
      cotton: 0.75,
      other: 0.00
    }
  );

  const handleInputChange = (crop: string, value: string) => {
    setFormData(prev => ({
      ...prev,
      [crop]: parseFloat(value) || 0
    }));
  };

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    updatePrices(formData);
  };

  const cropInfo = {
    corn: { unit: '$/bushel', description: 'Corn price per bushel' },
    soybeans: { unit: '$/bushel', description: 'Soybean price per bushel' },
    wheat: { unit: '$/bushel', description: 'Wheat price per bushel' },
    rice: { unit: '$/cwt', description: 'Rice price per hundredweight' },
    cotton: { unit: '$/pound', description: 'Cotton price per pound' },
    other: { unit: '$/unit', description: 'Other crop price per unit' }
  };

  return (
    <form onSubmit={handleSubmit}>
      <div className="mb-3">
        <h4>Current Market Prices</h4>
        <p className="text-info">
          Enter current market prices for accurate profitability analysis.
          Prices will be applied to all trials for comparison calculations.
        </p>
      </div>

      {Object.entries(cropInfo).map(([crop, info]) => (
        <div key={crop} className="form-group">
          <label>
            {crop.charAt(0).toUpperCase() + crop.slice(1)} ({info.unit})
          </label>
          <input
            type="number"
            step="0.01"
            min="0"
            value={formData[crop as keyof PriceData]}
            onChange={(e) => handleInputChange(crop, e.target.value)}
            placeholder={`Enter ${crop} price`}
          />
          <small className="text-info">{info.description}</small>
        </div>
      ))}

      <div className="mt-3">
        <div className="card">
          <div className="card-header">Price Update Summary</div>
          <div className="card-body">
            <p>
              Current prices will be applied to all trial calculations. 
              Make sure to update prices regularly for accurate analysis.
            </p>
            <small>
              Last updated: {priceData ? 'Previously set' : 'Not set'}
            </small>
          </div>
        </div>
      </div>

      <button type="submit" className="btn btn-primary mt-3" style={{ width: '100%' }}>
        Update Prices
      </button>
    </form>
  );
};

export default PriceInputForm;