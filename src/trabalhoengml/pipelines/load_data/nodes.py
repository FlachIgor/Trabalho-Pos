"""
This is a boilerplate pipeline 'LeituraDados'
generated using Kedro 0.18.7
"""
import pandas as pd

def load_data():
    df = pd.read_csv('data/01_raw/kobe_dataset.csv')
    return df
