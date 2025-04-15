from airflow import DAG
from datetime import datetime
from airflow.operators.bash import BashOperator

with DAG(dag_id='orchestation',
        description='notre orchestation',
        start_date=datetime(2025, 1, 1),
        end_date= datetime(2025,4,1),
        schedule_interval="@daily"
        # default_args={"depends_on_past": False},
        # max_active_runs=5,
        # catchup=False 
) as dag:

    t1 = BashOperator(
        task_id= "work_1",
        bash_command="sleep 2 && echo 'work_1'")
    t2 = BashOperator(
        task_id= "work_2",
        bash_command= "sleep 2 && echo 'work_2'")
    t3 = BashOperator(
        task_id= "work_3",
        bash_command= "sleep 2 && echo 'work_3' ")
    t4 = BashOperator(
        task_id= "work_4",
        bash_command= "sleep 2 && echo 'work_4'")

    t1 >> t2 >> t3 >> t4