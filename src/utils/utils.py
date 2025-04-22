from pyspark.sql.functions import udf
from pyspark.sql.types import StringType
import uuid
from datetime import datetime


def get_fullname(first_name: str, last_name: str) -> str:
    return f"{first_name} {last_name}"


full_name = udf(get_fullname, StringType())


def generate_alphanumeric_id(length: int = 8) -> str:
    return uuid.uuid4().hex[:length]


alphanumeric_id = udf(generate_alphanumeric_id, StringType())


def make_folder_name(prefix: str) -> str:
    now = datetime.now()
    return f"{prefix}_{now.strftime('%Y%m%d-%H%M%S')}"
