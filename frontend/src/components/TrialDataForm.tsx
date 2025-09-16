import React, { useState } from 'react';
import { useTrials } from '../context/TrialsContext';
import { TrialData } from '../types';

const TrialDataForm: React.FC = () => {
  const { addTrialData } = useTrials();
  const [formData, setFormData] = useState<Partial<TrialData>>({
    name: '',
    crop: '',
    variety: '',
    yield: 0,
    area: 0,
    location: '',
    year: new Date().getFullYear(),
    costs: {
      seed: 0,
      fertilizer: 0,
      pesticides: 0,
      labor: 0,
      machinery: 0,
      other: 0
    }
  });

  const handleInputChange = (field: string, value: any) => {
    if (field.startsWith('costs.')) {
      const costField = field.split('.')[1];
      setFormData(prev => ({
        ...prev,
        costs: {
          ...prev.costs!,
          [costField]: parseFloat(value) || 0
        }
      }));
    } else {
      setFormData(prev => ({
        ...prev,
        [field]: value
      }));
    }
  };

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    if (formData.name && formData.crop && formData.yield) {
      addTrialData(formData as TrialData);
      // Reset form
      setFormData({
        name: '',
        crop: '',
        variety: '',
        yield: 0,
        area: 0,
        location: '',
        year: new Date().getFullYear(),
        costs: {
          seed: 0,
          fertilizer: 0,
          pesticides: 0,
          labor: 0,
          machinery: 0,
          other: 0
        }
      });
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <div className="form-group">
        <label>Trial Name *</label>
        <input
          type="text"
          value={formData.name}
          onChange={(e) => handleInputChange('name', e.target.value)}
          placeholder="e.g., North Field Corn Trial 2024"
          required
        />
      </div>

      <div className="form-group">
        <label>Crop *</label>
        <select
          value={formData.crop}
          onChange={(e) => handleInputChange('crop', e.target.value)}
          required
        >
          <option value="">Select Crop</option>
          <option value="corn">Corn</option>
          <option value="soybeans">Soybeans</option>
          <option value="wheat">Wheat</option>
          <option value="rice">Rice</option>
          <option value="cotton">Cotton</option>
          <option value="other">Other</option>
        </select>
      </div>

      <div className="form-group">
        <label>Variety/Hybrid</label>
        <input
          type="text"
          value={formData.variety}
          onChange={(e) => handleInputChange('variety', e.target.value)}
          placeholder="e.g., DeKalb DKC64-69RIB"
        />
      </div>

      <div className="form-group">
        <label>Yield (bu/acre) *</label>
        <input
          type="number"
          step="0.1"
          value={formData.yield}
          onChange={(e) => handleInputChange('yield', e.target.value)}
          required
        />
      </div>

      <div className="form-group">
        <label>Area (acres)</label>
        <input
          type="number"
          step="0.1"
          value={formData.area}
          onChange={(e) => handleInputChange('area', e.target.value)}
        />
      </div>

      <div className="form-group">
        <label>Location</label>
        <input
          type="text"
          value={formData.location}
          onChange={(e) => handleInputChange('location', e.target.value)}
          placeholder="e.g., Iowa, USA"
        />
      </div>

      <div className="form-group">
        <label>Year</label>
        <input
          type="number"
          value={formData.year}
          onChange={(e) => handleInputChange('year', parseInt(e.target.value))}
        />
      </div>

      <h4 className="mb-2">Production Costs ($/acre)</h4>
      
      <div className="form-group">
        <label>Seed</label>
        <input
          type="number"
          step="0.01"
          value={formData.costs?.seed}
          onChange={(e) => handleInputChange('costs.seed', e.target.value)}
        />
      </div>

      <div className="form-group">
        <label>Fertilizer</label>
        <input
          type="number"
          step="0.01"
          value={formData.costs?.fertilizer}
          onChange={(e) => handleInputChange('costs.fertilizer', e.target.value)}
        />
      </div>

      <div className="form-group">
        <label>Pesticides</label>
        <input
          type="number"
          step="0.01"
          value={formData.costs?.pesticides}
          onChange={(e) => handleInputChange('costs.pesticides', e.target.value)}
        />
      </div>

      <div className="form-group">
        <label>Labor</label>
        <input
          type="number"
          step="0.01"
          value={formData.costs?.labor}
          onChange={(e) => handleInputChange('costs.labor', e.target.value)}
        />
      </div>

      <div className="form-group">
        <label>Machinery</label>
        <input
          type="number"
          step="0.01"
          value={formData.costs?.machinery}
          onChange={(e) => handleInputChange('costs.machinery', e.target.value)}
        />
      </div>

      <div className="form-group">
        <label>Other Costs</label>
        <input
          type="number"
          step="0.01"
          value={formData.costs?.other}
          onChange={(e) => handleInputChange('costs.other', e.target.value)}
        />
      </div>

      <button type="submit" className="btn btn-primary" style={{ width: '100%' }}>
        Add Trial Data
      </button>
    </form>
  );
};

export default TrialDataForm;