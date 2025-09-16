from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import pandas as pd
import json
from pathlib import Path

app = FastAPI(title="Commodity Performance Dashboard")

# Mount static files
app.mount("/static", StaticFiles(directory="static"), name="static")

# Templates setup
templates = Jinja2Templates(directory="templates")

# Data file paths
DATA_DIR = Path("data")
COMMODITY_PRICES_FILE = DATA_DIR / "commodity_prices.csv"
YIELDS_COSTS_FILE = DATA_DIR / "yields_costs.csv"

# Load data
def load_commodity_prices():
    """Load commodity prices data from CSV"""
    df = pd.read_csv(COMMODITY_PRICES_FILE)
    return df

def load_yields_costs():
    """Load yields and costs data from CSV"""
    df = pd.read_csv(YIELDS_COSTS_FILE)
    return df

@app.get("/", response_class=HTMLResponse)
async def dashboard(request: Request):
    """Main dashboard page"""
    return templates.TemplateResponse("dashboard.html", {"request": request})

@app.get("/api/commodity-prices")
async def get_commodity_prices():
    """API endpoint to get commodity prices data"""
    df = load_commodity_prices()
    return {
        "data": df.to_dict('records'),
        "columns": df.columns.tolist()
    }

@app.get("/api/yields-costs")
async def get_yields_costs():
    """API endpoint to get yields and costs data"""
    df = load_yields_costs()
    return {
        "data": df.to_dict('records'),
        "columns": df.columns.tolist()
    }

@app.get("/tables/commodity-prices")
async def commodity_prices_table(request: Request):
    """HTMX endpoint to render commodity prices table"""
    df = load_commodity_prices()
    return templates.TemplateResponse(
        "commodity_prices_table.html", 
        {
            "request": request,
            "data": df.to_dict('records'),
            "columns": df.columns.tolist()
        }
    )

@app.get("/tables/yields-costs")
async def yields_costs_table(request: Request):
    """HTMX endpoint to render yields and costs table"""
    df = load_yields_costs()
    return templates.TemplateResponse(
        "yields_costs_table.html", 
        {
            "request": request,
            "data": df.to_dict('records'),
            "columns": df.columns.tolist()
        }
    )

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)