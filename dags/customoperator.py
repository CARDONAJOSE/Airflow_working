from airflow import DAG
from datetime import datetime
from hellooperator import HelloOperator

with DAG(dag_id='customoperator',
        description='notre DAG avec customoperator',
        start_date=datetime(2024, 8, 4),
        catchup=False,
        tags=['']
) as dag:

    t1= HelloOperator(
        task_id="hello",
        name= 'jose'
    )
    t1
