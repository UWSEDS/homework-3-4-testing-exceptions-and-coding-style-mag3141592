'''
HW 3-4: Unit tests for dataframe.py
'''
import unittest
import pandas as pd
import dataframe

# Downloads New York City's demographics by Zip and saves to a dataframe
DATA_URL = "https://data.cityofnewyork.us/api/views/kku6-nxdu/rows.csv?accessType=DOWNLOAD"
DATA = pd.read_csv(DATA_URL)

# Dataset code was designed around
DATA_SUB = DATA.iloc[:, 0:6]
DATA_COLUMNS = sorted(DATA_SUB.columns)

# Different subsets of datasource
NAME_TEST = DATA.iloc[:, 1:8]
ROW_TEST = DATA.iloc[:9, 0:6]
TYPE_TEST = DATA.iloc[:, 1:7]
TYPE_TEST.columns = DATA_COLUMNS

# Define a class in which the tests will run
class UnitTests(unittest.TestCase):
    '''
    Class contains 5 unit tests for various structural problems in
    dataframe.test_create_dataframe
    '''
    # Each method executes a different unit test to validate dataframes' structure
    def test_exact_df(self):
        '''
        Tests valid structure
        '''
        self.assertTrue(dataframe.test_create_dataframe(DATA_SUB))

    def test_diff_colnames(self):
        '''
        Tests dataframe with different column names
        '''
        self.assertRaises(ValueError, dataframe.test_create_dataframe, NAME_TEST)

    def test_diff_datatypes(self):
        '''
        Tests dataframe with invalid test_diff_datatypes
        '''
        self.assertRaises(ValueError, dataframe.test_create_dataframe, TYPE_TEST)

    def test_rows(self):
        '''
        Tests dataframe with less than 10 rows
        '''
        self.assertRaises(ValueError, dataframe.test_create_dataframe, ROW_TEST)

    def test_nans(self):
        '''
        Tests dataframe has no null values
        '''
        self.assertFalse(DATA_SUB.isnull().values.any())

SUITE = unittest.TestLoader().loadTestsFromTestCase(UnitTests)
_ = unittest.TextTestRunner().run(SUITE)
