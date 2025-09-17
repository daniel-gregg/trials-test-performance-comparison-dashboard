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
DATA_FILE = DATA_DIR / "data.csv"

def load_data():
    """Load main data from CSV"""
    df = pd.read_csv(DATA_FILE)
    return df

## utility functions
def get_unique_sites(df):
    """ Get a list of unique field sites from the plot column """
    return list(set([i.split('_')[0] for i in df['plot']] ))

def get_unique_systems(df, site=None):
    """ Get a list of unique systems from the plot column
        If site is provided, filter by that site
    """
    if site is None:
        return list(set([i.split('_')[1] for i in df['plot']] ))
    else:
        return list(set([i.split('_')[1] for i in df['plot'] if i.split('_')[0] == site]))

def get_unique_phases(df, site=None, system=None):
    """ Get a list of unique phases from the plot column
        If site is provided, filter by that site
        If system is provided, filter by that system
    """
    if site is None and system is None:
        return list(set([i.split('_')[2] for i in df['plot']] ))
    elif site is not None and system is None:
        return list(set([i.split('_')[2] for i in df['plot'] if i.split('_')[0] == site]))
    elif site is not None and system is not None:
        return list(set([i.split('_')[2] for i in df['plot'] if i.split('_')[0] == site and i.split('_')[1] == system]))
    else:
        raise ValueError("If system is provided, site must also be provided")

def get_plot_id_values(df, site=None, system=None, phase=None):
    """ Splits the ID fields and returns
        a list of plotIDs that match the constaining terms (if any)
        particular search terms
        For example, HART_XXX_AAA_BBB and HART_YYY_AAA_CCC will be included as values for the key 'HART' (one of the field sites)
    """

    """ Example plot ID
        STREATHAM_S11_P0000_R7
        Splits into:
        ['STREATHAM', 'S11', 'P0000', 'R7']
        'STREATHAM' is the overall field site
        'S11' is the system - the overall treatment applied to the plot
        'P0000' references the phase-order of crops. This allows for a system treatment to have different orderings of crops
        'R7' refers to a replication of the treatment/phase-order combination
    """

    """
        We are interested only NOT in replications
        And MOSTLY in system comparisons.
        In the future it is EXPECTED that a system-mapping across sites will be provided to allow cross-site comparisons for systems
    """

    ids = [*set(df['plot'])]

    if site is None and system is None and phase is None:
        return ids

    # Check that site is provided if system of phase is provided
    if (system is not None or phase is not None) and site is None:
        raise ValueError("If system or phase is provided, site must also be provided")

    # Check that if phase is provided, system must also be provided
    if phase is not None and system is None:
        raise ValueError("If phase is provided, system must also be provided")

    # else check constraints and sort by that.
    if site is not None:
        ids = [i for i in ids if i.split('_')[0] == site]

    if system is not None:
        ids = [i for i in ids if i.split('_')[1] == system]

    if phase is not None:
        ids = [i for i in ids if i.split('_')[2] == phase]

    return ids

# utility function for the get_plotting_data function
def filter_data_by_plot_id(df, plot_ids):
    """Filter the DataFrame by a list of plot IDs"""

    # Filter DataFrame to only include rows with the specified plot IDs
    filtered_df = df[df['plot'].isin(plot_ids)]

    # Check if we found any data
    if filtered_df.empty:
        raise ValueError("No data found for the specified plot_ids")

    return filtered_df

# used to pre-fill the variable selection dropdown
def get_variable_list(df):
    """Get a list of variables (columns) in the DataFrame excluding 'plot'"""
    return [col for col in df.columns if col != 'plot']

# the final function to return plotting data to the user
def get_plotting_data(df, plot_ids, variable):
    """Get data for plotting based on plot IDs and variable"""
    filtered_df = filter_data_by_plot_id(df, plot_ids)
    if variable not in filtered_df.columns:
        raise ValueError(f"Variable {variable} not found in DataFrame columns")
    return filtered_df[['plot', variable]]

##### API Endpoints #####

# Main dashboard route
@app.get("/", response_class=HTMLResponse)
async def dashboard(request: Request):
    """Serve the main dashboard"""
    return templates.TemplateResponse("dashboard.html", {"request": request})

# API endpoints to get unique sites, systems, and phases for dropdown menus
@app.get("/api/sites", response_class=HTMLResponse)
async def get_sites(request: Request):
    """API endpoint to get unique sites"""
    df = load_data()
    sites = get_unique_sites(df)
    return templates.TemplateResponse("sites.html", {"request": request, "sites": sites})

@app.get("/api/sites-json")
async def get_sites_json():
    """API endpoint to get unique sites as JSON"""
    df = load_data()
    sites = get_unique_sites(df)
    return {"sites": sites}

@app.get("/api/systems", response_class=HTMLResponse)
async def get_systems(request: Request, site: str):
    """API endpoint to get unique systems for a given site"""
    df = load_data()
    systems = get_unique_systems(df, site)
    return templates.TemplateResponse("systems.html", {"request": request, "systems": systems})

@app.get("/api/systems-json")
async def get_systems_json(site: str):
    """API endpoint to get unique systems for a given site as JSON"""
    df = load_data()
    systems = get_unique_systems(df, site)
    return {"systems": systems}

@app.get("/api/phases", response_class=HTMLResponse)
async def get_phases(request: Request, site: str, system: str):
    """API endpoint to get unique phases for a given site and system"""
    df = load_data()
    phases = get_unique_phases(df, site, system)
    return templates.TemplateResponse("phases.html", {"request": request, "phases": phases})

@app.get("/api/phases-json")
async def get_phases_json(site: str, system: str):
    """API endpoint to get unique phases for a given site and system as JSON"""
    df = load_data()
    phases = get_unique_phases(df, site, system)
    return {"phases": phases}

# API endpoint to get unique variables
@app.get("/api/variables", response_class=HTMLResponse)
async def get_variables(request: Request):
    """API endpoint to get unique variables for a given site, system, and phase"""
    df = load_data()
    variables = get_variable_list(df)
    return templates.TemplateResponse("variables.html", {"request": request, "variables": variables})

@app.get("/api/variables-json")
async def get_variables_json():
    """API endpoint to get unique variables as JSON"""
    df = load_data()
    variables = get_variable_list(df)
    return {"variables": variables}

# API endpoint to get plot data
@app.get("/api/plot-data", response_class=HTMLResponse)
async def get_plot_data(request: Request, site: str, system: str, phase: str, variable: str):
    """API endpoint to get plot data for a given site, system, phase, and variable"""
    df = load_data()
    plot_ids = get_plot_id_values(df, site, system, phase)
    data = get_plotting_data(df, plot_ids, variable)
    return templates.TemplateResponse("plot_data.html", {"request": request, "data": data})

@app.get("/api/plot-data-json")
async def get_plot_data_json(variable: str, sites: str = None, system: str = None, phase: str = None):
    """API endpoint to get plot data as JSON for plotting at any level of selection"""
    df = load_data()
    plot_data = []
    
    # If no sites specified, use all sites
    if not sites:
        site_list = get_unique_sites(df)
    else:
        site_list = [s.strip() for s in sites.split(',')]
    
    for site in site_list:
        try:
            # Get plot IDs based on the level of filtering
            if system and phase:
                # Site + System + Phase level
                plot_ids = get_plot_id_values(df, site, system, phase)
            elif system:
                # Site + System level
                plot_ids = get_plot_id_values(df, site, system, None)
            elif sites:
                # Site level only
                plot_ids = get_plot_id_values(df, site, None, None)
            else:
                # No filtering - get all plots for this site
                plot_ids = get_plot_id_values(df, site, None, None)
            
            if plot_ids:  # Only process if we have plot IDs
                site_data = get_plotting_data(df, plot_ids, variable)
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

@app.get("/api/boxplot-data-json")
async def get_boxplot_data_json(variable: str, site: str, systems: str = None, phases: str = None):
    """API endpoint to get boxplot data for compare mode"""
    df = load_data()
    
    if not site:
        return {"error": "Site is required for boxplot data"}
    
    # Parse systems and phases
    selected_systems = [s.strip() for s in systems.split(',')] if systems else []
    selected_phases = [p.strip() for p in phases.split(',')] if phases else []
    
    # Determine comparison type
    if len(selected_systems) >= 2:
        comparison_type = "systems"
        comparison_items = selected_systems
    elif len(selected_phases) >= 2:
        comparison_type = "phases" 
        comparison_items = selected_phases
    else:
        return {"error": "Need at least 2 systems OR 2 phases for comparison"}
    
    boxplot_data = {}
    
    try:
        for item in comparison_items:
            if comparison_type == "systems":
                # Get all phases for this system
                if selected_phases:
                    # Specific phases requested
                    for phase in selected_phases:
                        plot_ids = get_plot_id_values(df, site, item, phase)
                        key = f"{item}_{phase}" if len(selected_phases) > 1 else item
                        if plot_ids:
                            site_data = get_plotting_data(df, plot_ids, variable)
                            boxplot_data[key] = []
                            for _, row in site_data.iterrows():
                                if not pd.isna(row[variable]):
                                    boxplot_data[key].append({
                                        'plot': row['plot'],
                                        'value': float(row[variable])
                                    })
                else:
                    # All phases for this system
                    plot_ids = get_plot_id_values(df, site, item, None)
                    if plot_ids:
                        site_data = get_plotting_data(df, plot_ids, variable)
                        boxplot_data[item] = []
                        for _, row in site_data.iterrows():
                            if not pd.isna(row[variable]):
                                boxplot_data[item].append({
                                    'plot': row['plot'],
                                    'value': float(row[variable])
                                })
            else:  # comparison_type == "phases"
                if selected_systems:
                    # Specific systems requested
                    for system in selected_systems:
                        plot_ids = get_plot_id_values(df, site, system, item)
                        key = f"{system}_{item}" if len(selected_systems) > 1 else item
                        if plot_ids:
                            site_data = get_plotting_data(df, plot_ids, variable)
                            boxplot_data[key] = []
                            for _, row in site_data.iterrows():
                                if not pd.isna(row[variable]):
                                    boxplot_data[key].append({
                                        'plot': row['plot'],
                                        'value': float(row[variable])
                                    })
                else:
                    # All systems for this phase - get systems for this site first
                    available_systems = get_unique_systems(df, site)
                    combined_data = []
                    for system in available_systems:
                        plot_ids = get_plot_id_values(df, site, system, item)
                        if plot_ids:
                            site_data = get_plotting_data(df, plot_ids, variable)
                            for _, row in site_data.iterrows():
                                if not pd.isna(row[variable]):
                                    combined_data.append({
                                        'plot': row['plot'],
                                        'value': float(row[variable])
                                    })
                    boxplot_data[item] = combined_data
                    
    except Exception as e:
        return {"error": f"Error processing boxplot data: {str(e)}"}
    
    return {
        "data": boxplot_data,
        "comparison_type": comparison_type
    }

if __name__ == "__main__":
    import uvicorn
    import os
    
    # Use Railway's PORT environment variable or default to 8000 for local development
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)