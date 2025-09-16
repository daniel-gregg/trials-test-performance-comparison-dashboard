# Trials Test Performance Comparison Dashboard

A comprehensive web application for comparing crop trial performance with customizable pricing inputs. This dashboard allows agricultural researchers, farmers, and agronomists to analyze trial data and make informed decisions based on profitability and performance metrics.

## Features

### Frontend (React + TypeScript)
- **Interactive Dashboard**: Clean, responsive interface for data input and visualization
- **Trial Data Management**: Add and manage multiple crop trials with detailed information
- **Price Input System**: Flexible pricing system for different crops
- **Performance Analysis**: Real-time comparison calculations and ranking
- **Data Visualization**: Charts and tables showing performance metrics
- **Responsive Design**: Works on desktop, tablet, and mobile devices

### Backend (Node.js + Express)
- **REST API**: Structured endpoints for data management
- **Data Processing**: Server-side calculations for performance comparisons
- **Extensible Architecture**: Ready for database integration and additional features

## Quick Start

### Prerequisites
- Node.js (v14 or higher)
- npm or yarn

### Installation
```bash
# Clone the repository
git clone <repository-url>
cd trials-test-performance-comparison-dashboard

# Install all dependencies (root, frontend, and backend)
npm run install-all

# Or install manually:
npm install
cd frontend && npm install
cd ../backend && npm install
```

### Development
```bash
# Run both frontend and backend concurrently
npm run dev

# Or run separately:
# Terminal 1 - Frontend (runs on http://localhost:3000)
npm run frontend

# Terminal 2 - Backend (runs on http://localhost:5000)
npm run backend
```

### Production Build
```bash
npm run build
```

## Project Structure

```
├── README.md
├── package.json              # Root package.json with scripts
├── frontend/                 # React TypeScript application
│   ├── public/
│   ├── src/
│   │   ├── components/       # React components
│   │   │   ├── Header.tsx
│   │   │   ├── Dashboard.tsx
│   │   │   ├── ControlPanel.tsx
│   │   │   ├── ResultsArea.tsx
│   │   │   ├── TrialDataForm.tsx
│   │   │   ├── PriceInputForm.tsx
│   │   │   ├── ComparisonTable.tsx
│   │   │   └── ChartVisualization.tsx
│   │   ├── context/          # React context for state management
│   │   │   └── TrialsContext.tsx
│   │   ├── types/            # TypeScript type definitions
│   │   │   └── index.ts
│   │   ├── App.tsx
│   │   ├── App.css          # Comprehensive styling
│   │   └── index.tsx
│   └── package.json
└── backend/                  # Node.js Express API
    ├── server.js            # Main server file with API endpoints
    ├── package.json
    └── .env.example
```

## Usage

### 1. Set Up Pricing
- Navigate to the "Price Inputs" tab in the control panel
- Enter current market prices for different crops
- Prices are used for calculating revenue and profitability

### 2. Add Trial Data
- Switch to the "Trial Data" tab
- Fill in trial information including:
  - Trial name and basic info (crop, variety, location, year)
  - Yield data (bushels per acre)
  - Production costs (seed, fertilizer, pesticides, labor, machinery, other)
- Submit to add to the comparison dataset

### 3. Run Analysis
- Once you have trials and prices configured, click "Run Performance Analysis"
- View results in the results area with:
  - Comparison table with profit, ROI, and rankings
  - Visual charts showing performance metrics
  - Summary statistics

## API Endpoints

### Backend API Structure
```
GET  /api/health           # Health check
GET  /api/trials           # Get all trials
POST /api/trials           # Add new trial
GET  /api/prices           # Get current prices
POST /api/prices           # Update prices
POST /api/compare          # Run performance comparison
```

## Technology Stack

### Frontend
- **React 18** with TypeScript
- **Context API** for state management
- **CSS3** with modern layout techniques (Grid, Flexbox)
- **Responsive Design** principles

### Backend
- **Node.js** with Express framework
- **CORS** enabled for frontend communication
- **Helmet** for security headers
- **Morgan** for request logging
- **dotenv** for environment configuration

## Key Features in Detail

### Data Input Forms
- **Trial Data Form**: Comprehensive form for entering trial information with validation
- **Price Input Form**: Simple interface for updating crop prices
- **Form Validation**: Client-side validation to ensure data quality

### Analysis & Visualization
- **Performance Calculations**: Automatic calculation of costs, revenue, profit, and ROI
- **Ranking System**: Trials ranked by profitability
- **Visual Charts**: Bar charts for profit and yield comparison
- **Data Tables**: Sortable tables with performance metrics

### User Experience
- **Tabbed Interface**: Clean organization of input forms
- **Loading States**: Visual feedback during analysis
- **Empty States**: Helpful guidance when no data is available
- **Responsive Design**: Works across all device sizes

## Future Enhancements

The application is designed to be easily extensible:

### Backend Enhancements
- Database integration (PostgreSQL, MongoDB)
- User authentication and authorization
- Data persistence and history
- Advanced analytics and reporting
- File upload for bulk data import

### Frontend Enhancements
- Advanced charting with libraries like Chart.js or D3.js
- Export functionality (PDF, Excel)
- Data filtering and search capabilities
- Advanced comparison features
- Real-time data updates

### Integration Possibilities
- Weather data integration
- Market price APIs
- GIS mapping capabilities
- Machine learning predictions
- Mobile app development

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## License

This project is licensed under the ISC License - see the LICENSE file for details.
