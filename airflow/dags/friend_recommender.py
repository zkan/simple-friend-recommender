from airflow.models import DAG
from airflow.operators.dummy import DummyOperator
from airflow.operators.python import PythonOperator
from airflow.providers.papermill.operators.papermill import PapermillOperator
from airflow.utils import timezone

import pandas as pd


DAGS_FOLDER = '/opt/airflow/dags'
NOTEBOOKS_FOLDER = f'{DAGS_FOLDER}/notebooks'


def _get_distance_columns():
    df = pd.read_csv(f'{DAGS_FOLDER}/survey_responses_transformed.csv')

    return list(df.columns[2:])


default_args = {
    'owner': 'zkan'
}
with DAG('friend_recommender',
         default_args=default_args,
         schedule_interval='*/30 * * * *',
         start_date=timezone.datetime(2021, 4, 1),
         catchup=False,
         tags=['dataength', 'ODDS']) as dag:

    start = DummyOperator(task_id='start')

    get_distance_columns = PythonOperator(
        task_id='get_distance_columns',
        python_callable=_get_distance_columns,
    )

    execute_friend_recommender = PapermillOperator(
        task_id='execute_friend_recommender',
        input_nb=f'{NOTEBOOKS_FOLDER}/friend_recommender.ipynb',
        output_nb=f'{NOTEBOOKS_FOLDER}/friend_recommender_results.ipynb',
        parameters=dict(
            DAGS_FOLDER=DAGS_FOLDER,
            distance_columns="{{ ti.xcom_pull(key='return_value', task_ids='get_distance_columns') }}"
        ),
    )

    end = DummyOperator(task_id='end')

    start >> get_distance_columns >> execute_friend_recommender >> end
