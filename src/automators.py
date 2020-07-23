import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors


""" us_state_abbrev = {
'alabama': 'AL', 'alaska': 'AK', 'arizona': 'AZ', 'arkansas': 'AR', 'california': 'CA', 'colorado': 'CO',
'connecticut': 'CT', 'delaware': 'DE', 'florida': 'FL', 'georgia': 'GA', 'hawaii': 'HI', 'idaho': 'ID',
'illinois': 'IL', 'indiana': 'IN', 'iowa': 'IA', 'kansas': 'KS', 'kentucky': 'KY', 'louisiana': 'LA',
'maine': 'ME', 'maryland': 'MD', 'massachusetts': 'MA', 'michigan': 'MI', 'minnesota': 'MN', 'mississippi': 'MS',
'missouri': 'MO', 'montana': 'MT', 'nebraska': 'NE', 'nevada': 'NV', 'new hampshire': 'NH', 'new Jersey': 'NJ',
'new mexico': 'NM', 'new york': 'NY', 'north carolina': 'NC', 'north dakota': 'ND', 'ohio': 'OH', 'oklahoma': 'OK',
'oregon': 'OR', 'pennsylvania': 'PA', 'phode island': 'RI', 'south carolina': 'SC', 'south dakota': 'SD',
'tennessee': 'TN', 'texas': 'TX', 'utah': 'UT', 'vermont': 'VT', 'virginia': 'VA', 'washington': 'WA',
'west virginia': 'WV', 'wisconsin': 'WI', 'wyoming': 'WY'} """


class pawtomators():
    """Initialize automator class"""
    def __init_self(self):
        pass

    def bringin(self, ext, file_path):
        ''' Read in a file'''
        
        # if str(ext) == 'csv':
        #     df = pd.read_csv(file_path)
        #     return df
        # elif str(ext) == 'xlsx':
        #     df = pd.read_excel(file_path)
        #     return df
        # elif str(ext) == 'txt':
        #     df = pd.read_csv(file_path)

        # df = pd.read_csv(file_path)
        # return df
        pass

    def getout(self):
        '''Save a file out'''
        # pd.to_csv()
        pass

    def dcol(self):
        '''Drop column'''
        pass

    def dcols(self):
        '''Drop columns'''
        # df = df.rename({"Mod_col": "Col_1", "B": "Col_2"})
        pass
    
    def drow(self):
        '''Drop row by index'''
        # df.drop([0,1])
        pass
    
    def remap_col(self):
        '''Remap column names'''
        # ac_df['state'] = ac_df['state'].map(us_state_abbrev)
        pass

    def changecols(self):
        '''Change column name'''
        # df.columns =['Col_1', 'Col_2']
        pass

    def changerow(self):
        '''Change row name'''
        # df.index = ['Row_1', 'Row_2', 'Row_3', 'Row_4']
        pass

    def idrop(self):
        """Drop index value that is not level"""
        # df.drop(index='length', level=1)
        pass