from google.cloud import batch_v1
from datetime import datetime
import uuid


def generate_alphanumeric_id(length: int = 8) -> str:
    return uuid.uuid4().hex[:length]


def get_options(options: dict) -> str:
    vars = []
    for k, v in options.items():
        itm = f"--env={k}={v}"
        vars.append(itm)
    
    return " ".join(vars)


def get_folder_name() -> None:
    now = datetime.now()
    file_name = f"{now.strftime('%Y%m%d-%H')}/process-data-{now.strftime('%Y%m%d-%H%M%S')}"
    
    env_vars = {
        "BUCKET_NAME": "batch-job-outputs",
        "FOLDER_PREFIX": "results",
        "OUTFILE_NAME": file_name
    }
    result = get_options(options=env_vars)
    return result


def create_script_job(project_id: str, region: str, job_name: str, container_image: str, options: str = None) -> batch_v1.Job:
    client = batch_v1.BatchServiceClient()

    # Define what will be done as part of the job.
    task = batch_v1.TaskSpec()
    runnable = batch_v1.Runnable()
    runnable.container = batch_v1.Runnable.Container()
    runnable.container.image_uri = container_image
    if options is not None:
        runnable.container.options = options

    # runnable.container.options = "--env=BUCKET_NAME=batch-job-outputs --env=FOLDER_PREFIX=result"

    task.runnables = [runnable]

    # We can specify what resources are requested by each task.
    resources = batch_v1.ComputeResource()
    resources.cpu_milli = 1000  # in milliseconds per cpu-second. This means the task requires 2 whole CPUs.
    resources.memory_mib = 16
    task.compute_resource = resources

    task.max_retry_count = 2
    task.max_run_duration = "3600s"

    # Tasks are grouped inside a job using TaskGroups.
    # Currently, it's possible to have only one task group.
    group = batch_v1.TaskGroup()
    group.task_count = 1
    group.task_spec = task

    allocation_policy = batch_v1.AllocationPolicy()
    policy = batch_v1.AllocationPolicy.InstancePolicy()
    policy.machine_type = "e2-standard-4"
    instances = batch_v1.AllocationPolicy.InstancePolicyOrTemplate()
    instances.policy = policy
    allocation_policy.instances = [instances]

    job = batch_v1.Job()
    job.task_groups = [group]
    job.allocation_policy = allocation_policy
    job.labels = {"env": "testing", "type": "container-image"}
    # We use Cloud Logging as it's an out of the box available option
    job.logs_policy = batch_v1.LogsPolicy()
    job.logs_policy.destination = batch_v1.LogsPolicy.Destination.CLOUD_LOGGING

    create_request = batch_v1.CreateJobRequest()
    create_request.job = job
    create_request.job_id = job_name
    # The job's parent is the region in which the job will run
    create_request.parent = f"projects/{project_id}/locations/{region}"

    return client.create_job(create_request)


def main() -> None:
    id = generate_alphanumeric_id(length=8)

    project_id = "project-55302-456910"
    region = "us-central1"
    job_name = f"create-job-from-python-{id}"
    container_image = "gcr.io/project-55302-456910/batch-pyspark@sha256:d90865eacf0d804e0f4a7f27b270bd13388a1467b5d28fe264f5c42ceb3329b3"
    
    create_script_job(
        project_id=project_id, 
        region=region, 
        job_name=job_name, 
        container_image=container_image, 
        options=get_folder_name()
    )


if __name__ == "__main__":
    main()
