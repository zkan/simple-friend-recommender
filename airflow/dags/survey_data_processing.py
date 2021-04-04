import csv
import json

from airflow.models import DAG
from airflow.operators.dummy import DummyOperator
from airflow.operators.python import PythonOperator
from airflow.providers.postgres.hooks.postgres import PostgresHook
from airflow.utils import timezone

import pandas as pd


DAGS_FOLDER = '/opt/airflow/dags'


def _dump_survey_data():
    table = 'questions_surveyresponse'
    pg_hook = PostgresHook(postgres_conn_id='survey_db_conn', schema='postgres')
    pg_hook.bulk_dump(table, f'{DAGS_FOLDER}/{table}_export.tsv')

    return f'{DAGS_FOLDER}/{table}_export.tsv'


def _count_survey_answers():
    pg_hook = PostgresHook(postgres_conn_id='survey_db_conn', schema='postgres')
    connection = pg_hook.get_conn()
    cursor = connection.cursor()

    sql = """
        SELECT * FROM questions_surveyresponse
    """
    cursor.execute(sql)
    rows = cursor.fetchall()
    results = {}
    for _, _, each in rows:
        for value in each.values():
            if value in results:
                results[value] += 1
            else:
                results[value] = 1

    with open(f'{DAGS_FOLDER}/survey_answer_count.csv', 'w') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['answer', 'value'])
        writer.writerows(results.items())

    return f'{DAGS_FOLDER}/survey_answer_count.csv'


def _transform_and_convert_into_csv(ti):
    filepath = ti.xcom_pull(key='return_value', task_ids=['dump_survey_data'])[0]
    columns = ['id', 'name', 'answers']
    df = pd.read_csv(filepath, sep='\t', names=columns)
    new_df = df.join(df['answers'].apply(json.loads).apply(pd.Series)).drop('answers', axis='columns')
    new_df.to_csv(f'{DAGS_FOLDER}/survey_responses.csv', index=False)

    return f'{DAGS_FOLDER}/survey_responses.csv'


def _transform_data_using_one_hot_encoding(ti):
    filepath = ti.xcom_pull(key='return_value', task_ids=['transform_and_convert_into_csv'])[0]
    df = pd.read_csv(filepath)
    new_df = df.join(pd.get_dummies(df['question-1'])) \
        .join(pd.get_dummies(df['question-2'])) \
        .join(pd.get_dummies(df['question-3'])) \
        .join(pd.get_dummies(df['question-4'])) \
        .join(pd.get_dummies(df['question-5'])) \
        .drop(['question-1', 'question-2', 'question-3', 'question-4', 'question-5'], axis='columns')

    new_df.to_csv(f'{DAGS_FOLDER}/survey_responses_transformed.csv', index=False)

    return f'{DAGS_FOLDER}/survey_responses_transformed.csv'


default_args = {
    'owner': 'zkan',
    'start_date': timezone.datetime(2017, 5, 5),
}
with DAG(dag_id='survey_data_processing',
         default_args=default_args,
         schedule_interval='*/30 * * * *',
         catchup=False,
         tags=['ODDS']) as dag:

    start = DummyOperator(task_id='start')

    count_survey_answers = PythonOperator(
        task_id='count_survey_answers',
        python_callable=_count_survey_answers,
    )

    dump_survey_data = PythonOperator(
        task_id='dump_survey_data',
        python_callable=_dump_survey_data,
    )

    transform_and_convert_into_csv = PythonOperator(
        task_id='transform_and_convert_into_csv',
        python_callable=_transform_and_convert_into_csv,
    )

    transform_data_using_one_hot_encoding = PythonOperator(
        task_id='transform_data_using_one_hot_encoding',
        python_callable=_transform_data_using_one_hot_encoding,
    )

    start >> count_survey_answers
    start >> dump_survey_data >> transform_and_convert_into_csv >> transform_data_using_one_hot_encoding
