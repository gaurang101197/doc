from airflow import models, settings
from airflow.executors.executor_loader import ExecutorLoader
from airflow.models import TaskInstance, DagRun
from airflow.utils.state import DagRunState, State, TaskInstanceState

session = settings.Session()
tis = session.query(TaskInstance).filter(TaskInstance.state == None, TaskInstance.dag_id=='dag_id', TaskInstance.run_id=='run_id').all()
dagbag = models.DagBag()
for ti in tis:
  dag = dagbag.get_dag(ti.dag_id)
  task = dag.get_task(ti.task_id)
  ti.refresh_from_task(task)
  executor = ExecutorLoader.get_default_executor()
  executor.job_id = "manual"
  executor.start()
  executor.queue_task_instance(ti, ignore_all_deps=False, ignore_task_deps=False, ignore_ti_state=False)
  executor.heartbeat()


#  querying tasks
queued_tasks = session.query(TaskInstance).filter(TaskInstance.state == None, TaskInstance.dag_id=='dag_id', TaskInstance.run_id=='scheduled__2023-07-18T03:00:00+00:00').all()

queued_tasks = session.query(TaskInstance).filter(TaskInstance.dag_id=='dag_id', TaskInstance.run_id=='scheduled__2023-07-18T03:00:00+00:00', TaskInstance.task_id=='task_id').all()

[print(t) for t in queued_tasks]

# updaing status of tasks
session.query(TaskInstance).filter(TaskInstance.state == None, TaskInstance.dag_id=='dag_id', TaskInstance.run_id=='scheduled__2023-07-18T03:00:00+00:00', TaskInstance.task_id=='task_id').update({TaskInstance.state: State.SCHEDULED})

# querying dag run
dag = session.query(DagRun).filter(DagRun.dag_id=='dag_id', DagRun.run_id=='scheduled__2023-07-18T03:00:00+00:00')

[print(d) for d in dag]

# updating status of dag
session.query(DagRun).filter(DagRun.dag_id=='dag_id', DagRun.run_id=='scheduled__2023-07-18T03:00:00+00:00').update({DagRun.state: DagRunState.RUNNING})
