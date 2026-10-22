from datetime import datetime
from airflow import DAG
from airflow.sdk import Param  
from airflow.providers.standard.operators.bash import BashOperator  
from airflow.providers.standard.operators.python import BranchPythonOperator  

with DAG(
    dag_id="project1-workflow",
    start_date=datetime(2015, 12, 1),
    schedule=None,
    params={
        "dags_home": Param(
            "TU UZUPELNIJ SCIEZKE DLA TWOJEGO KATALOGU AIRFLOW/airflow/dags", type="string"
        ),
        "input_dir": Param(
            "TU UZUPELNIJ SCIEZKE DLA TWOICH DANYCH ZRODLOWYCH/input", type="string"
        ),
        "output_mr_dir": Param("/project1/output_mr3", type="string"),
        "output_dir": Param("/project1/output6", type="string"),
        "classic_or_streaming": Param(
            "streaming", enum=["classic", "streaming"]
        ),
    },
    render_template_as_native_obj=True,
    catchup=False,  
) as dag:

    # Usuwanie katalogów z HDFS jeśli istnieją
    clean_output_mr_dir = BashOperator(
        task_id="clean_output_mr_dir",
        bash_command=(
            "if hadoop fs -test -d {{ params.output_mr_dir }}; "
            "then hadoop fs -rm -f -r {{ params.output_mr_dir }}; fi"
        ),
    )

    clean_output_dir = BashOperator(
        task_id="clean_output_dir",
        bash_command=(
            "if hadoop fs -test -d {{ params.output_dir }}; "
            "then hadoop fs -rm -f -r {{ params.output_dir }}; fi"
        ),
    )

    # Wybór trybu wykonania: klasyczny MR lub streaming
    def _pick_classic_or_streaming(params):
        if params["classic_or_streaming"] == "classic":
            return "mapreduce_classic"
        else:
            return "hadoop_streaming"

    pick_classic_or_streaming = BranchPythonOperator(
        task_id="pick_classic_or_streaming",
        python_callable=_pick_classic_or_streaming,
        op_kwargs={"params": dag.params},
    )

    # MapReduce klasyczny
    mapreduce_classic = BashOperator(
        task_id="mapreduce_classic",
        bash_command=(
            "hadoop jar {{ params.dags_home }}/project_files/ . . . "
        ),
    )

    # MapReduce streaming
    hadoop_streaming = BashOperator(
        task_id="hadoop_streaming",
        bash_command=(
            "mapred streaming "
            "-files {{ params.dags_home }}/project_files/ . . ."
        ),
    )

    # Program Hive
    hive = BashOperator(
        task_id="hive",
        bash_command=(
            "beeline -u jdbc:hive2://localhost:10000/default "
            ". . ."
        ),
        trigger_rule="none_failed",
    )

    # Pobranie wyników
    get_output = BashOperator(
        task_id="get_output",
        bash_command=(
            "hadoop fs -getmerge {{ params.output_dir }} output6.json && head output6.json"
        ),
        trigger_rule="none_failed",
    )

    # Zależności
    [clean_output_mr_dir, clean_output_dir] >> pick_classic_or_streaming
    pick_classic_or_streaming >> [mapreduce_classic, hadoop_streaming]
    [mapreduce_classic, hadoop_streaming] >> hive
    hive >> get_output
