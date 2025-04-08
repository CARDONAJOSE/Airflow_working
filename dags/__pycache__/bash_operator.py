# mi_proyecto_airflow/dags/bash_operator.py

from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

with DAG(
    dag_id="bash_operator",
    description= "explorando bashoperator",
    start_date=datetime(2022, 8, 1),
    schedule_interval=None,  # Para ejecución manual
    catchup=False,          # Evita ejecuciones históricas
    tags=["ejemplo", "bash"]
    
) as dag:
    t1 = BashOperator(
        task_id="print_hello", 
        bash_command="echo '¡Hola desde Docker!'")
    t1
