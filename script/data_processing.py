import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder, StandardScaler, MinMaxScaler

def load_and_clean_data(filepath):
    data = pd.read_csv(filepath)
    # Removing duplicates
    data = data.drop_duplicates(keep="first")
    return data

def handle_missing_data(data):
    # Impute missing values with mean for numerical columns
    for col in data.select_dtypes(include=[np.number]).columns:
        data[col].fillna(data[col].mean(), inplace=True)
    # Impute missing values with mode for categorical columns
    for col in data.select_dtypes(include=[object]).columns:
        data[col].fillna(data[col].mode()[0], inplace=True)
    return data

def feature_engineering(data):
    # Example feature engineering: Create a new feature 'Risk'
    data['Risk'] = data['TotalClaims'] / data['TotalPremium']
    return data

def handle_datetime_columns(data):
    # Convert datetime columns to numeric
    for col in data.select_dtypes(include=[object]):
        try:
            data[col] = pd.to_datetime(data[col])
            data[col] = data[col].astype(int) / 10**9  # Convert to Unix timestamp
        except ValueError:
            continue
    return data

def encoder(dataframe, columns_label, columns_onehot):
    df_lbl = dataframe.copy()
    for col in columns_label:
        label = LabelEncoder()
        label.fit(list(dataframe[col].values))
        df_lbl[col] = label.transform(df_lbl[col].values)
    
    df_oh = pd.get_dummies(data=df_lbl, prefix='ohe', prefix_sep='_',
                           columns=columns_onehot, drop_first=True, dtype='int8')
    return df_oh

def scaler(method, data, columns_scaler):    
    if method == 'standardScaler':        
        Standard = StandardScaler()
        df_standard = data.copy()
        df_standard[columns_scaler] = Standard.fit_transform(df_standard[columns_scaler])        
        return df_standard
        
    elif method == 'minMaxScaler':        
        MinMax = MinMaxScaler()
        df_minmax = data.copy()
        df_minmax[columns_scaler] = MinMax.fit_transform(df_minmax[columns_scaler])        
        return df_minmax
    
    elif method == 'npLog':        
        df_nplog = data.copy()
        df_nplog[columns_scaler] = np.log(df_nplog[columns_scaler])        
        return df_nplog
    
    return data