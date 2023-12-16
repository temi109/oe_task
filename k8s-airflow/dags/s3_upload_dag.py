from datetime import datetime, timedelta
import sqlite3
import pandas as pd
import logging

from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.providers.postgres.hooks.postgres import PostgresHook
from airflow.providers.amazon.aws.hooks.s3 import S3Hook

default_args = {
    'owner': 'tem109',
    'retries': 5,
    'retry_delay' : timedelta(minutes=10)
}

S3_bucket_name = "oe-task-bucket"

case_study_db = 'case_study.db'
conn = sqlite3.connect(case_study_db )
c = conn.cursor()

## Load data in to dfs
agreement_df = pd.read_sql_query("SELECT * FROM agreement", conn)
meterpoint_df = pd.read_sql_query("SELECT * FROM meterpoint", conn)
product_df = pd.read_sql_query("SELECT * FROM product", conn)

def agreement_df_upload():
    # Save into csv file
    agreement_df.to_csv('agreements.csv', index = False)
    logging.info("Saved agreements data")
    # then upload to s3
    s3_hook = S3Hook(aws_conn_id = "s3_conn")
    s3_hook.load_file(
        filename = "dags/get_circuits.csv",
        key = "circuits.csv",
        bucket_name = S3_bucket_name,
        replace = True     ## Replace file if already exists
    )

# def constructors_upload():
#     # query data from postgres db and save into txt file
    
#     hook = PostgresHook(postgres_conn_id="postgres_localhost")
#     conn = hook.get_conn()
#     cursor = conn.cursor()
#     cursor.execute("select * from constructors")

#     with open(f"dags/get_constructors.csv", "w") as f:
#         csv_writer = csv.writer(f)
#         csv_writer.writerow([i[0] for i in cursor.description])
#         csv_writer.writerows(cursor)
#         f.flush()
#     cursor.close()
#     conn.close()
#     logging.info("Saved constructors data")
#     # then upload to s3
#     s3_hook = S3Hook(aws_conn_id = "s3_conn")
#     s3_hook.load_file(
#         filename = "dags/get_constructors.csv",
#         key = "constructors.csv",
#         bucket_name = S3_bucket_name,
#         replace = True     ## Replace file if already exists
#     )

# def races_upload():
#     hook = PostgresHook(postgres_conn_id="postgres_localhost")
#     conn = hook.get_conn()
#     cursor = conn.cursor()
#     cursor.execute("select * from races")

#     with open(f"dags/get_races.csv", "w") as f:
#         csv_writer = csv.writer(f)
#         csv_writer.writerow([i[0] for i in cursor.description])
#         csv_writer.writerows(cursor)
#         f.flush()
#     cursor.close()
#     conn.close()
#     logging.info("Saved races data")
#     # then upload to s3
#     s3_hook = S3Hook(aws_conn_id = "s3_conn")
#     s3_hook.load_file(
#         filename = "dags/get_races.csv",
#         key = "races.csv",
#         bucket_name = S3_bucket_name,
#         replace = True     ## Replace file if already exists
#     )

with DAG(
    dag_id="upload_tables_to_s3_1",
    default_args=default_args,
    start_date=datetime(2023, 12, 15),
    catchup = False,
    schedule_interval='@daily'
) as dag:
    pass
    # task1 = PythonOperator(
    #     task_id="agreement_df_upload",
    #     python_callable=agreement_df_upload
    # )

    # task2 = PythonOperator(
    #     task_id="constructors_upload",
    #     python_callable=constructors_upload
    # )

    # task3 = PythonOperator(
    #     task_id="races_upload",
    #     python_callable=races_upload
    # )
    # task4 = PythonOperator(
    #     task_id="results_upload",
    #     python_callable=results_upload
    # )

