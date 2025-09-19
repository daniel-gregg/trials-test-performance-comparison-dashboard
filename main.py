from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import json
from pathlib import Path

# local modules
from src import prices  # for future price simulations
from src import data_utilities  # data loading and filtering functions

# data packages
import pandas as pd

app = FastAPI(title="Commodity Performance Dashboard")

# Mount static files
app.mount("/static", StaticFiles(directory="static"), name="static")

# Templates setup
templates = Jinja2Templates(directory="templates")


##### API Endpoints #####

# Main dashboard route
@app.get("/", response_class=HTMLResponse)
async def dashboard(request: Request):
    """Serve the main dashboard"""
    return templates.TemplateResponse("modular_dashboard.html", {"request": request})

# Legacy dashboard route (for testing/comparison)
@app.get("/legacy", response_class=HTMLResponse)
async def legacy_dashboard(request: Request):
    """Serve the legacy dashboard"""
    return templates.TemplateResponse("dashboard.html", {"request": request})

# API endpoints to get unique sites, systems, and phases for dropdown menus
@app.get("/api/sites", response_class=HTMLResponse)
async def get_sites(request: Request):
    """API endpoint to get unique sites"""
    df = data_utilities.load_data()
    sites = data_utilities.get_unique_sites(df)
    return templates.TemplateResponse("sites.html", {"request": request, "sites": sites})

@app.get("/api/sites-json")
async def get_sites_json():
    """API endpoint to get unique sites as JSON"""
    df = data_utilities.load_data()
    sites = data_utilities.get_unique_sites(df)
    return {"sites": sites}

@app.get("/api/systems", response_class=HTMLResponse)
async def get_systems(request: Request, site: str):
    """API endpoint to get unique systems for a given site"""
    df = data_utilities.load_data()
    systems = data_utilities.get_unique_systems(df, site)
    return templates.TemplateResponse("systems.html", {"request": request, "systems": systems})

@app.get("/api/systems-json")
async def get_systems_json(site: str):
    """API endpoint to get unique systems for a given site as JSON"""
    df = data_utilities.load_data()
    systems = data_utilities.get_unique_systems(df, site)
    return {"systems": systems}

@app.get("/api/phases", response_class=HTMLResponse)
async def get_phases(request: Request, site: str, system: str):
    """API endpoint to get unique phases for a given site and system"""
    df = data_utilities.load_data()
    phases = data_utilities.get_unique_phases(df, site, system)
    return templates.TemplateResponse("phases.html", {"request": request, "phases": phases})

@app.get("/api/phases-json")
async def get_phases_json(site: str, system: str):
    """API endpoint to get unique phases for a given site and system as JSON"""
    df = data_utilities.load_data()
    phases = data_utilities.get_unique_phases(df, site, system)
    return {"phases": phases}

# API endpoint to get unique variables
@app.get("/api/variables", response_class=HTMLResponse)
async def get_variables(request: Request):
    """API endpoint to get unique variables for a given site, system, and phase"""
    df = data_utilities.load_data()
    variables = data_utilities.get_variable_list(df)
    return templates.TemplateResponse("variables.html", {"request": request, "variables": variables})

@app.get("/api/variables-json")
async def get_variables_json():
    """API endpoint to get unique variables as JSON"""
    df = data_utilities.load_data()
    variables = data_utilities.get_variable_list(df)
    return {"variables": variables}

# API endpoint to get plot data
@app.get("/api/plot-data", response_class=HTMLResponse)
async def get_plot_data(request: Request, site: str, system: str, phase: str, variable: str):
    """API endpoint to get plot data for a given site, system, phase, and variable"""
    df = data_utilities.load_data()
    plot_ids = data_utilities.get_plot_id_values(df, site, system, phase)
    data = data_utilities.get_plotting_data(df, plot_ids, variable)
    return templates.TemplateResponse("plot_data.html", {"request": request, "data": data})

@app.get("/api/plot-data-json")
async def get_plot_data_json(variable: str, sites: str = None, system: str = None, phase: str = None):
    """API endpoint to get plot data as JSON for plotting at any level of selection"""
    df = data_utilities.load_data()
    plot_data = []

    # If no sites specified, use all sites
    if not sites:
        site_list = data_utilities.get_unique_sites(df)
    else:
        site_list = [s.strip() for s in sites.split(',')]

    for site in site_list:
        try:
            # Get plot IDs based on the level of filtering
            if system and phase:
                # Site + System + Phase level
                plot_ids = data_utilities.get_plot_id_values(df, site, system, phase)
            elif system:
                # Site + System level
                plot_ids = data_utilities.get_plot_id_values(df, site, system, None)
            elif sites:
                # Site level only
                plot_ids = data_utilities.get_plot_id_values(df, site, None, None)
            else:
                # No filtering - get all plots for this site
                plot_ids = data_utilities.get_plot_id_values(df, site, None, None)

            if plot_ids:  # Only process if we have plot IDs
                site_data = data_utilities.get_plotting_data(df, plot_ids, variable)
                for _, row in site_data.iterrows():
                    plot_id_parts = row['plot'].split('_')
                    value = row[variable]
                    # Skip NaN values
                    if pd.isna(value):
                        continue
                    plot_data.append({
                        'site': plot_id_parts[0],
                        'system': plot_id_parts[1] if len(plot_id_parts) > 1 else 'Unknown',
                        'phase': plot_id_parts[2] if len(plot_id_parts) > 2 else 'Unknown',
                        'plot': row['plot'],
                        'value': float(value)  # Ensure it's a regular float, not numpy float
                    })
        except Exception as e:
            # Skip sites that cause errors (e.g., no matching data)
            continue

    return {"data": plot_data}

if __name__ == "__main__":
    import uvicorn
    import os

    # Use Railway's PORT environment variable or default to 8000 for local development
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)