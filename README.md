# Crop Field Trials Performance Comparison Dashboard

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

## Deployment on Railway Platform

This application is configured for easy deployment on [Railway](https://railway.app/), a modern cloud platform. Follow these steps to deploy:

### Prerequisites
- GitHub account
- Railway account (sign up at [railway.app](https://railway.app/))

### Deployment Steps

#### 1. Prepare Your Repository
The repository already includes the necessary Railway configuration files:
- `Procfile` - Defines the web process command
- `railway.json` - Railway-specific configuration and build settings
- `.railwayignore` - Files to exclude from deployment
- Updated `main.py` - Uses Railway's PORT environment variable

#### 2. Deploy to Railway

**Option A: Deploy via Railway Dashboard**
1. Go to [railway.app](https://railway.app/) and sign in
2. Click "New Project"
3. Select "Deploy from GitHub repo"
4. Choose this repository from your GitHub account
5. Railway will automatically detect it's a Python project and use the configuration files

**Option B: Deploy via Railway CLI**
1. Install Railway CLI:
   ```bash
   npm install -g @railway/cli
   ```
2. Login to Railway:
   ```bash
   railway login
   ```
3. Initialize project in your repository:
   ```bash
   railway init
   ```
4. Deploy:
   ```bash
   railway up
   ```

#### 3. Configuration Details

The deployment uses these configuration files:

**Procfile:**
```
web: uvicorn main:app --host 0.0.0.0 --port $PORT
```

**railway.json:**
- Uses NIXPACKS builder for automatic Python environment setup
- Configures health checks on the root path (`/`)
- Sets restart policy for reliability
- Installs dependencies from `requirements.txt`

#### 4. Environment Variables (Optional)
Railway automatically provides the `PORT` environment variable. If you need to add custom environment variables:
1. Go to your project dashboard on Railway
2. Navigate to the "Variables" tab
3. Add any required environment variables

#### 5. Custom Domain (Optional)
1. In your Railway project dashboard, go to "Settings"
2. Click "Domains"
3. Add your custom domain
4. Configure your DNS provider to point to Railway's servers

#### 6. Monitoring and Logs
- **Logs**: View real-time logs in the Railway dashboard under "Deployments"
- **Metrics**: Monitor CPU, memory, and network usage
- **Health Checks**: Railway automatically monitors the `/` endpoint

### Deployment Workflow Summary

1. **Code Push**: Push code changes to your GitHub repository
2. **Auto Deploy**: Railway automatically detects changes and redeploys
3. **Build Process**: 
   - Railway clones the repository
   - Installs Python dependencies from `requirements.txt`
   - Starts the application using the Procfile command
4. **Live App**: Your app is available at `https://<your-app-name>.railway.app`

### Troubleshooting

**Common Issues:**
- **Build Failures**: Check that all dependencies in `requirements.txt` are valid
- **App Won't Start**: Verify the Procfile command is correct
- **Port Issues**: Ensure the app uses the `PORT` environment variable

**Checking Logs:**
```bash
railway logs
```

**Local Testing with Railway:**
```bash
railway run python main.py
```

### Cost Considerations
- Railway offers a free tier with usage limits
- Monitor your usage in the Railway dashboard
- Consider upgrading to a paid plan for production applications

For more information, visit the [Railway Documentation](https://docs.railway.app/).
