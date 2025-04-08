from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.bash import BashOperator
from datetime import datetime

with DAG(dag_id='dependence',
        description='notre DAG avec dependence ',
        start_date=datetime(2024, 8, 4),
        schedule_interval='@once',
        tags=['dependece', 'python']
) as dag:

    t1 = PythonOperator(
        task_id="work_1",
        python_callable=lambda: print('Hi from python dependence'),
    )
    t2 = BashOperator(
        task_id= "work_2",
        bash_command= "echo 'work_2' "
    )
    t3 = BashOperator(
        task_id= "work_3",
        bash_command= "echo 'work_3' "
    )
    t4 = BashOperator(
        task_id= "work_4",
        bash_command= "echo 'work_4' "
    )

t1.set_downstream([t2,t3])
t2.set_upstream(t4)
t3.set_downstream(t4)
# t1 >> [t2, t3] >> t4