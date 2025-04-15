# mi_proyecto_airflow/dags/mi_dag.py
from airflow import DAG
from airflow.operators.empty import EmptyOperator
from datetime import datetime

with DAG(
    dag_id="primer_dag",
    description= "notre premier dags avec airflow",
    start_date=datetime(2024, 1, 1),
    schedule_interval="@once",
) as dag:
    t1 = EmptyOperator(task_id="print_hello")
    t1
    