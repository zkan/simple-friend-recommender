# Credit: https://www.dataquest.io/blog/k-nearest-neighbors-in-python/
import math

import pandas as pd


def get_euclidean_distance(row, selected_person):
    """
    A simple euclidean distance function
    """
    distance_columns = [
        'data-engineer',
        'data-scientist',
        'cat',
        'dog',
        'mountain',
        'sea',
        'java',
        'python',
        'blackpink',
        'gong-yoo',
    ]
    inner_value = 0
    for k in distance_columns:
        inner_value += (row[k] - selected_person[k]) ** 2
    return math.sqrt(inner_value)


df = pd.read_csv('airflow/dags/survey_responses_transformed.csv')

selected_person = df[df['name'] == 'Beauti'].iloc[0]

df['distance'] = df.apply(get_euclidean_distance, args=(selected_person,), axis='columns')
sorted_df = df[['name', 'distance']].sort_values(by='distance')[:6]

print(sorted_df)
