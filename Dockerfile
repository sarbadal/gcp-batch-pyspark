FROM ubuntu:22.04 AS base
# "sarbadal.pal@annalect.com"

ARG spark_version="3.5.5"
ARG openjdk_version="17"
ARG python_version="3.10"
ENV workdir="/app"
# ENV SPARK_HOME=/opt/spark
# ENV PATH=$PATH:$SPARK_HOME/bin:$SPARK_HOME/sbin
# ENV PYSPARK_PYTHON=/usr/bin/python3

# Set WorkDir
WORKDIR $workdir

RUN apt update && \
    apt install -y openjdk-${openjdk_version}-jdk python${python_version} python3-pip wget && \
    ln -s /usr/bin/python3 /usr/bin/python && \
    rm -rf /var/lib/apt/lists/*

# Install Spark
RUN wget https://archive.apache.org/dist/spark/spark-${spark_version}/spark-${spark_version}-bin-hadoop3.tgz && \
    tar xvf spark-${spark_version}-bin-hadoop3.tgz && \
    mv spark-${spark_version}-bin-hadoop3/ /opt/spark && \
    export SPARK_HOME=/opt/spark && \
    export PATH=$PATH:$SPARK_HOME/bin:$SPARK_HOME/sbin && \
    export PYSPARK_PYTHON=/usr/bin/python3 && \
    rm spark-${spark_version}-bin-hadoop3.tgz

# Copy Requirements
COPY requirements.txt .

# Install Python Dependencys
RUN pip install -r requirements.txt

COPY src ${workdir}
 
ENTRYPOINT ["python3", "main.py"]