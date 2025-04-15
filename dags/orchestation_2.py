from airflow import DAG
from datetime import datetime
from airflow.operators.empty import EmptyOperator

with DAG(dag_id='orchestation_2',
        description='notre orchestation avec empty',
        schedule_interval="0 7 * * 1",
        start_date=datetime(2025, 1, 1),
        end_date= datetime(2025,4,1)
        
        # default_args={"depends_on_past": False},
        # max_active_runs=5,
        # catchup=False 
) as dag: 

    t1 = EmptyOperator(task_id= "work_1")
        # bash_command="sleep 2 && echo 'work_1'"
    t2 = EmptyOperator(task_id= "work_2")
        # bash_command= "sleep 2 && echo 'work_2'"
    t3 = EmptyOperator(task_id= "work_3")
        # bash_command= "sleep 2 && echo 'work_3' "
    t4 = EmptyOperator(task_id= "work_4")
        # bash_command= "sleep 2 && echo 'work_4'"

    t1 >> t2 >> t3 >> t4
