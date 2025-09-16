# Commodity Performance Comparison Dashboard

A HTMX frontend dashboard connected to a simple FastAPI backend for comparing crop trial performance data. The backend serves results from two CSV files containing commodity price data and yield/cost analysis.

## Features

- **Real-time Data Display**: Two interactive tables showing commodity prices over time and yield/cost analysis
- **HTMX Integration**: Dynamic table updates without full page refreshes
- **Responsive Design**: Clean, modern interface that works on desktop and mobile
- **FastAPI Backend**: RESTful API endpoints for data access
- **CSV Data Source**: Easy to update data by modifying CSV files

## Data Tables

1. **Commodity Prices Over Time**: Historical price data for reference commodities (Wheat, Corn, Soybeans, Rice)
2. **Yields and Costs Analysis**: Production data including yield per acre, costs, and profit margins for various commodities

## Installation and Setup

### Prerequisites
- Python 3.8 or higher
- pip (Python package installer)

### Installation Steps

1. Clone the repository:
```bash
git clone https://github.com/daniel-gregg/trials-test-performance-comparison-dashboard.git
cd trials-test-performance-comparison-dashboard
```

2. Install the required dependencies:
```bash
pip install -r requirements.txt
```

3. Run the application:
```bash
python main.py
```

4. Open your browser and navigate to:
```
http://localhost:8000
```

## Project Structure

```
trials-test-performance-comparison-dashboard/
├── main.py                    # FastAPI application
├── requirements.txt           # Python dependencies
├── data/                      # CSV data files
│   ├── commodity_prices.csv   # Historical price data
│   └── yields_costs.csv       # Yield and cost analysis data
├── templates/                 # HTML templates
│   ├── dashboard.html         # Main dashboard page
│   ├── commodity_prices_table.html
│   └── yields_costs_table.html
└── static/                    # Static assets
    └── css/
        └── dashboard.css      # Dashboard styling
```

## API Endpoints

- `GET /` - Main dashboard page
- `GET /api/commodity-prices` - JSON API for commodity prices data
- `GET /api/yields-costs` - JSON API for yields and costs data
- `GET /tables/commodity-prices` - HTML table fragment for commodity prices
- `GET /tables/yields-costs` - HTML table fragment for yields and costs

## Data Format

### Commodity Prices CSV Format
```csv
Date,Wheat,Corn,Soybeans,Rice
2023-01-01,7.50,6.20,14.25,16.80
```

### Yields and Costs CSV Format
```csv
Commodity,Yield_per_Acre,Production_Cost_per_Acre,Net_Profit_per_Acre
Wheat,45.2,320.50,18.90
```

## Customization

To update the data:
1. Edit the CSV files in the `data/` directory
2. Restart the application to see changes
3. Use the refresh buttons in the dashboard to reload data

## Technology Stack

- **Backend**: FastAPI (Python web framework)
- **Frontend**: HTML, CSS, JavaScript (with HTMX-style dynamic loading)
- **Data Processing**: Pandas
- **Server**: Uvicorn ASGI server
- **Templating**: Jinja2

## Development

To run in development mode with auto-reload:
```bash
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```
