"""
This is a boilerplate pipeline 'transform_data'
generated using Kedro 0.18.7
"""
import pandas as pd
from sklearn.model_selection import train_test_split

def transform_data(df):
    df2PT = df[df['shot_type'] == '2PT Field Goal']
    df2PT = df2PT[['lat','lon','minutes_remaining','period', 'playoffs', 'shot_distance','shot_made_flag']]
    df2PT.dropna(inplace = True)
    df3PT = df[df['shot_type'] == '2PT Field Goal']
    df3PT = df3PT[['lat','lon','minutes_remaining','period', 'playoffs', 'shot_distance','shot_made_flag']]
    df3PT.dropna(inplace = True)
    return df2PT,df3PT

def metric_data(df):
    metrics = {'n_total': df.shape[0]}

    for klass, count in df['shot_made_flag'].value_counts().items():
        metrics[f'n_{klass}'] = count

    return {
        key: {'value': value, 'step': 1}
        for key, value in metrics.items()
    }

def split_train(df, test_size,random_state):
    train, test = train_test_split(
        df,
        test_size=test_size,
        random_state=random_state
    )
    return train, test