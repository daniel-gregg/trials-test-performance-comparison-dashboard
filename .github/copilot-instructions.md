# Crop Field Trials Performance Comparison Dashboard

A FastAPI-based web application that provides an interactive dashboard for comparing crop trial performance data across multiple sites, systems, phases, and variables. The backend serves data from CSV files containing crop trial results, yield data, cost analysis, and price simulations.

Always reference these instructions first and fallback to search or bash commands only when you encounter unexpected information that does not match the info here.

## Working Effectively

### Prerequisites and Installation
- Python 3.8 or higher required (Python 3.12+ recommended)
- Install dependencies:
  ```bash
  pip install -r requirements.txt
  ```
  Takes ~30 seconds to complete. All dependencies install successfully.

### Build and Run Commands
- **Start the application**:
  ```bash
  python main.py
  ```
  Application starts in ~2-3 seconds. NEVER CANCEL - wait for "Application startup complete" message.
  
- **Development mode with auto-reload**:
  ```bash
  uvicorn main:app --reload --host 0.0.0.0 --port 8000
  ```
  Development server starts in ~3-5 seconds. NEVER CANCEL.
  
- **Access the application**:
  - Main dashboard: http://localhost:8000
  - Legacy dashboard: http://localhost:8000/legacy
  - API documentation: http://localhost:8000/docs (FastAPI auto-generated)

### Test and Validation Commands
- **Test Railway deployment setup**:
  ```bash
  ./test-railway-setup.sh
  ```
  Takes ~10 seconds. NEVER CANCEL. Script validates all deployment files and tests PORT environment variable handling.

- **Check Python syntax**:
  ```bash
  python -m py_compile main.py src/data_utilities.py src/prices.py
  ```
  
- **Validate module imports**:
  ```bash
  python -c "import main; import src.data_utilities; import src.prices; print('All modules import successfully')"
  ```

## Validation

### Manual Testing Scenarios
ALWAYS run through these scenarios after making changes to ensure functionality:

1. **Basic Application Access**:
   - Start application with `python main.py`
   - Wait for "Application startup complete" message (2-3 seconds)
   - Verify HTTP 200 response: `curl -s -o /dev/null -w "%{http_code}" http://localhost:8000`
   - Check dashboard loads HTML content: `curl -s http://localhost:8000 | head -20`

2. **API Endpoint Testing**:
   ```bash
   # Test sites API (should return 9 sites including STREATHAM, HART, MANANG)
   curl -s http://localhost:8000/api/sites-json
   
   # Test variables API (should return 14 variables including plot_gross_margin_dollars)
   curl -s http://localhost:8000/api/variables-json
   
   # Test systems for a specific site (STREATHAM has systems like S1.2, S6.2, S4)
   curl -s "http://localhost:8000/api/systems-json?site=STREATHAM"
   
   # Test plot data generation (should return actual crop trial data)
   curl -s "http://localhost:8000/api/plot-data-json?variable=plot_gross_margin_dollars&sites=STREATHAM"
   ```

3. **Complete User Workflow**:
   - Load dashboard in browser at http://localhost:8000
   - Select a site from dropdown (e.g., STREATHAM - has the most data)
   - Select a system (e.g., S1.2 - well-populated system)
   - Select a phase (e.g., P1212 - common phase)
   - Select a variable (e.g., plot_gross_margin_dollars - key economic indicator)
   - Generate plot data and verify results display with actual numerical values

4. **Railway Deployment Validation**:
   - Run `./test-railway-setup.sh` - NEVER CANCEL, takes ~10 seconds
   - Verify all files are present and PORT environment variable works
   - Check HTTP 200 response on custom port (script tests port 3001)
   - Confirm "All tests passed!" message appears

### Data Validation
- **Data file location**: `data/data.csv` (1426 rows of crop trial data)
- **Data structure**: Plot-based data with format SITE_SYSTEM_PHASE_REPLICATION (e.g., STREATHAM_S1.2_P1212_R3)
- **Available sites**: WALLUP, MANANG, APPILA, HART, ROSEWORTHY, KINNABULLA, STREATHAM, EDILLILIE, WARRAMBINE (9 total)
- **Key variables**: operational_costs_dollars, plot_revenue_dollars, plot_gross_margin_dollars, crop yields
- **Most data-rich site**: STREATHAM (best for testing scenarios)
- **Data integrity**: All numeric values are properly formatted, some NaN values are expected for unused crop slots

### Codebase Navigation
After making changes, always check these key files:
- **API changes**: Check `main.py` endpoints (lines 27-152) 
- **Data processing**: Check `src/data_utilities.py` functions (especially `load_data()`, `get_plotting_data()`)
- **Frontend updates**: Check templates in `templates/` directory
- **Validation**: Always run `./test-railway-setup.sh` before deployment
- **New features**: Add corresponding API endpoints in `main.py` following existing patterns

## Common Tasks

### File Structure Overview
```
trials-test-performance-comparison-dashboard/
├── main.py                    # FastAPI application with all endpoints
├── requirements.txt           # Python dependencies
├── Procfile                   # Railway deployment command
├── railway.json              # Railway configuration
├── test-railway-setup.sh     # Deployment validation script
├── data/
│   ├── data.csv              # Main crop trial dataset (1426 rows)
│   └── 2025-09-15.csv        # Additional data file
├── src/
│   ├── data_utilities.py     # Data loading and filtering functions
│   └── prices.py             # Price simulation functions for crops
├── templates/                # HTML templates
│   ├── modular_dashboard.html # Main dashboard (default route)
│   ├── dashboard.html        # Legacy dashboard (/legacy route)
│   └── *.html                # API response templates
└── static/                   # CSS and static assets
```

### Key Functions and Modules
- **Data Loading**: `src.data_utilities.load_data()` - loads main CSV data
- **Site Filtering**: `src.data_utilities.get_unique_sites(df)` - gets available sites
- **Plot Data**: `src.data_utilities.get_plotting_data(df, plot_ids, variable)` - generates plot data
- **Price Simulations**: `src.prices.*_price_sim()` - functions for various crops (wheat, barley, canola, etc.)

### Making Changes
- **Backend API changes**: Edit `main.py` - contains all FastAPI endpoints
- **Data processing changes**: Edit `src/data_utilities.py`
- **Price simulation updates**: Edit `src/prices.py`
- **Frontend changes**: Edit templates in `templates/` directory
- **Styling changes**: Edit CSS files in `static/css/`

### Deployment
- **Railway Platform**: Repository is pre-configured for Railway deployment
- **Required files**: Procfile, railway.json, .railwayignore (all present)
- **Environment**: Uses PORT environment variable (default 8000 for local development)
- **Validation**: Always run `./test-railway-setup.sh` before deploying

## Important Notes

### Timing Expectations
- **Dependency installation**: ~30 seconds - NEVER CANCEL
- **Application startup**: ~2-3 seconds - wait for "Application startup complete" message
- **Development server startup**: ~3-5 seconds - NEVER CANCEL, wait for reloader process message
- **Railway test script**: ~10 seconds - NEVER CANCEL, wait for "All tests passed" message
- **API response times**: <1 second for all endpoints
- **Data loading**: Instantaneous (1426 rows load immediately from CSV)

### Do NOT do these things
- Do not try to build or compile - this is a Python application that runs directly
- Do not look for traditional test files - testing is done via API calls and the Railway script
- Do not expect linting configuration - no explicit linting setup exists (repository has no .flake8, .pylint, etc.)
- Do not cancel long-running commands - all commands complete quickly but wait for completion messages
- Do not skip validation steps - always run the test scenarios after making changes
- Do not ignore startup messages - wait for "Application startup complete" before testing

### Known Working Commands Summary
```bash
# Setup and installation
pip install -r requirements.txt

# Run application (choose one)
python main.py                                           # Production mode
uvicorn main:app --reload --host 0.0.0.0 --port 8000   # Development mode

# Testing and validation
./test-railway-setup.sh                                 # Railway deployment test
curl -s -o /dev/null -w "%{http_code}" http://localhost:8000  # HTTP test
python -m py_compile main.py src/data_utilities.py src/prices.py  # Syntax check

# API testing examples
curl -s http://localhost:8000/api/sites-json
curl -s http://localhost:8000/api/variables-json
curl -s "http://localhost:8000/api/plot-data-json?variable=plot_gross_margin_dollars&sites=STREATHAM"
```

### Troubleshooting
- **Import errors**: Verify you're in the repository root directory
- **Port conflicts**: Change port with `export PORT=8001` before running
- **Data loading issues**: Check `data/data.csv` exists and is readable
- **API errors**: Verify application is running and check logs for FastAPI error messages