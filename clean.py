import pandas as pd
import numpy as np

def prep_ufo_data(df):
    
    def custom_to_datetime (date):
        if date[11:13] == '24':
            x = date[:11] + '23:59'
        elif date[10:12] == '24':
            x = date[:10] + '23:59'
        elif date [9:11] =='24':
            x = date[:9] + '23:59'
        else:
            return pd.to_datetime(date)
        return pd.to_datetime(x)
    
    df ['latitude'] = pd.to_numeric(df['latitude'], errors='coerce')
    df['longitude'] = pd.to_numeric(df['longitude'], errors='coerce')

    df.loc[:, 'latitude'].replace({0: np.nan}, inplace=True)
    df.loc[:, 'longitude'].replace({0: np.nan}, inplace=True)
    df.index = np.arange(0, len(df))
    df['datetime'] = df['datetime'].apply(custom_to_datetime)
    df['date posted'] = pd.to_datetime(df['date posted'])

    df['month'] = pd.DatetimeIndex (df['datetime']).month
    df['year'] = pd.DatetimeIndex (df['datetime']).year
    df['day'] = pd.DatetimeIndex (df['datetime']).day
    df['hour'] = pd.DatetimeIndex (df['datetime']).hour

    return df