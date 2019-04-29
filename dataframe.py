"""
HW 3-4: Coding style and Unit tests.

Loads a dataset into dataframe, has a function to validate the
dataframes' structure with detailed exceptions
"""
import pandas as pd

def test_create_dataframe(dataframe):
    """
    Takes a dataframe, validates the structure, and returns a Boolean.

    It checks that the column names and data types match predefined
    global variables and that the dataframe is a least 10 rows.
    """
    results = True
    rows = dataframe.shape[0]
    column_names = sorted(dataframe.columns)
    column_datatypes = list(dataframe[column_names].dtypes)

    # Checks columns match those specified in #1
    if column_names != DATA_COLUMNS:
        raise ValueError("DataFrame does not have necessary datatypes: " + str(DATA_COLUMNS))
    # Checks column datatypes match
    if column_datatypes != DATA_DATATYPES:
        raise ValueError("DataFrame does not have necessary column names: " + str(DATA_DATATYPES))
    # Checks for a least 3 rows in DataFrame
    if rows < 10:
        raise ValueError("DataFrame does not have enough rows of data (>=10).")

    return results

# Downloads New York City's demographics by Zip and saves to a dataframe
DATA_URL = "https://data.cityofnewyork.us/api/views/kku6-nxdu/rows.csv?accessType=DOWNLOAD"
DATA = pd.read_csv(DATA_URL)

# Subset of the dataframe to reduce dimensionality for assignment
DATA_SUB = DATA.iloc[:, 0:6]

# Gets the imported dataframe's column names and datatypes.
DATA_COLUMNS = sorted(DATA_SUB.columns)
DATA_DATATYPES = list(DATA_SUB[DATA_COLUMNS].dtypes)
