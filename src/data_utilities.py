"""
Module for loading and filtering data for plotting
"""

from pathlib import Path
import pandas as pd

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
