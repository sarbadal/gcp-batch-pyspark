# Batch Job with PySpark on GCP

This project demonstrates how to build and run a PySpark-based batch job on Google Cloud Platform (GCP) using Docker and Google Batch.

## Prerequisites

- Python 3.10+
- Docker
- Google Cloud SDK (`gcloud`)
- A GCP project with Google Batch API enabled

## Setup Instructions

### 1. Build the Docker Image
Build the Docker image using the provided `Dockerfile`:
```bash
docker build -t gcr.io/<YOUR_PROJECT_ID>/batch-pyspark .
## Project Structure

### 2. Push the Docker Image to Google Container Registry
Push the Docker image to GCR:
docker push gcr.io/<YOUR_PROJECT_ID>/batch-pyspark

### 3. Submit the Batch Job
Submit the batch job to GCP:
gcloud batch jobs submit <JOB_NAME> \
  --project <YOUR_PROJECT_ID> \
  --location <LOCATION> \
  --config [job.json](http://_vscodecontentref_/1)

# Key Components
Dockerfile
The Dockerfile sets up the environment with:

Ubuntu 22.04 as the base image
OpenJDK 17 for Spark
Python 3.10 and required dependencies
Apache Spark 3.5.5
main.py
The main script performs the following:

Loads sample sales data using PySpark.
Adds an alphanumeric ID to each row.
Writes the processed data to a GCS bucket.
Utility Functions
generate_alphanumeric_id: Generates unique alphanumeric IDs.
make_folder_name: Creates a timestamped folder name for output.
Example Output
The processed data is written to a GCS bucket in the format:
gs://<BUCKET_NAME>/<FOLDER_NAME>.csv

