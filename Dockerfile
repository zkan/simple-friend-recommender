FROM apache/airflow:2.0.1

RUN pip install --upgrade pip
RUN pip install apache-airflow-providers-papermill ipykernel
