from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime


with DAG(dag_id='pythonoperator',
        description='notre DAG avec python',
        start_date=datetime(2024, 8, 4),
        schedule_interval='@once',
        catchup=False,
        tags=['']
) as dag:

    t1= python_task = PythonOperator(
        task_id="pythonopera",
        python_callable=lambda: print('Hi from python operator'),
        
    )
    t1
