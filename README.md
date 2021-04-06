# Simple Friend Recommender

Project to demonstrate stuff a data engineer should know

## Getting Started

### Starting the Project

```sh
./start.sh
```

### Stopping the Project

```sh
./stop.sh
```

### Testing an Airflow Task

```sh
airflow tasks test survey_data_processing transform_data_for_recommender 2021-04-04
```

### Setting Up the Airflow's Connections

In this talk, we'll set up 2 connections as follows:

1. Postgres connection:

    ![Survey DB Conn](survey_db_conn.png)

1. File system connection:

    ![Survey File Conn](survey_file_conn.png)