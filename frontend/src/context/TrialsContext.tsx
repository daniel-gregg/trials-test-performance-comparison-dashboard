import React, { createContext, useContext, useState, ReactNode } from 'react';
import { TrialData, PriceData, ComparisonResult, TrialsContextType } from '../types';

const TrialsContext = createContext<TrialsContextType | undefined>(undefined);

export const useTrials = () => {
  const context = useContext(TrialsContext);
  if (!context) {
    throw new Error('useTrials must be used within a TrialsProvider');
  }
  return context;
};

interface TrialsProviderProps {
  children: ReactNode;
}

export const TrialsProvider: React.FC<TrialsProviderProps> = ({ children }) => {
  const [trials, setTrials] = useState<TrialData[]>([]);
  const [priceData, setPriceData] = useState<PriceData | null>(null);
  const [comparisonResults, setComparisonResults] = useState<ComparisonResult[] | null>(null);
  const [isLoading, setIsLoading] = useState(false);

  const addTrialData = (trial: TrialData) => {
    const newTrial = {
      ...trial,
      id: Date.now().toString() // Simple ID generation
    };
    setTrials(prev => [...prev, newTrial]);
  };

  const updatePrices = (prices: PriceData) => {
    setPriceData(prices);
  };

  const calculateTotalCost = (trial: TrialData): number => {
    const { costs } = trial;
    return costs.seed + costs.fertilizer + costs.pesticides + 
           costs.labor + costs.machinery + costs.other;
  };

  const calculateRevenue = (trial: TrialData, prices: PriceData): number => {
    const pricePerUnit = prices[trial.crop as keyof PriceData] || 0;
    return trial.yield * pricePerUnit;
  };

  const runComparison = async () => {
    if (!priceData || trials.length === 0) {
      alert('Please add trial data and set prices before running comparison.');
      return;
    }

    setIsLoading(true);
    
    // Simulate API call delay
    await new Promise(resolve => setTimeout(resolve, 1500));

    const results: ComparisonResult[] = trials.map(trial => {
      const totalCost = calculateTotalCost(trial);
      const revenue = calculateRevenue(trial, priceData);
      const profit = revenue - totalCost;
      const roi = totalCost > 0 ? (profit / totalCost) * 100 : 0;

      return {
        trial,
        totalCost,
        revenue,
        profit,
        roi,
        rank: 0 // Will be set after sorting
      };
    });

    // Sort by profit (descending) and assign ranks
    results.sort((a, b) => b.profit - a.profit);
    results.forEach((result, index) => {
      result.rank = index + 1;
    });

    setComparisonResults(results);
    setIsLoading(false);
  };

  const clearTrials = () => {
    setTrials([]);
    setComparisonResults(null);
  };

  const value: TrialsContextType = {
    trials,
    priceData,
    comparisonResults,
    isLoading,
    addTrialData,
    updatePrices,
    runComparison,
    clearTrials
  };

  return (
    <TrialsContext.Provider value={value}>
      {children}
    </TrialsContext.Provider>
  );
};