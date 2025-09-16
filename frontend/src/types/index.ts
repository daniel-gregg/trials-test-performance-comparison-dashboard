export interface TrialData {
  id?: string;
  name: string;
  crop: string;
  variety?: string;
  yield: number;
  area: number;
  location?: string;
  year: number;
  costs: {
    seed: number;
    fertilizer: number;
    pesticides: number;
    labor: number;
    machinery: number;
    other: number;
  };
}

export interface PriceData {
  corn: number;
  soybeans: number;
  wheat: number;
  rice: number;
  cotton: number;
  other: number;
}

export interface ComparisonResult {
  trial: TrialData;
  totalCost: number;
  revenue: number;
  profit: number;
  roi: number;
  rank: number;
}

export interface TrialsContextType {
  trials: TrialData[];
  priceData: PriceData | null;
  comparisonResults: ComparisonResult[] | null;
  isLoading: boolean;
  addTrialData: (trial: TrialData) => void;
  updatePrices: (prices: PriceData) => void;
  runComparison: () => void;
  clearTrials: () => void;
}