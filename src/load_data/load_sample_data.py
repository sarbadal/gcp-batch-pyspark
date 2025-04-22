from pyspark.sql import SparkSession, DataFrame


def load_data(spark: SparkSession) -> DataFrame:
    data = [
        ("John", "Doe", 30),
        ("Jane", "Smith", 25),
        ("Sam", "Brown", 35),
        ("Alice", "Johnson", 28),
        ("Bob", "Davis", 40), 
        ("Charlie", "Miller", 22)
    ]
    columns = ["first_name", "last_name", "age"]
    df = spark.createDataFrame(data, schema=columns)
    return df


def load_sales_data(spark: SparkSession) -> DataFrame:
    data = [
        (1, "John Doe", "Laptop", 1, 1200, 1200, "2025-04-01"),
        (2, "Jane Smith", "Smartphone", 2, 800, 1600, "2025-04-02"),
        (3, "Sam Brown", "Tablet", 1, 500, 500, "2025-04-03"),
        (4, "Alice Johnson", "Headphones", 3, 100, 300, "2025-04-04"),
        (5, "Bob Davis", "Smartwatch", 1, 250, 250, "2025-04-05"),
        (6, "Charlie Miller", "Monitor", 2, 300, 600, "2025-04-06"),
        (7, "Emily Clark", "Keyboard", 4, 50, 200, "2025-04-07"),
        (8, "Michael Scott", "Mouse", 5, 25, 125, "2025-04-08"),
        (9, "Sarah Lee", "Printer", 1, 150, 150, "2025-04-09"),
        (10, "David Wilson", "Camera", 1, 700, 700, "2025-04-10"),
        (11, "Laura Adams", "Speaker", 2, 120, 240, "2025-04-11"),
        (12, "Chris Evans", "Router", 1, 80, 80, "2025-04-12"),
        (13, "Anna White", "Hard Drive", 3, 100, 300, "2025-04-13"),
        (14, "James Brown", "USB Drive", 10, 15, 150, "2025-04-14"),
        (15, "Olivia Green", "Webcam", 1, 60, 60, "2025-04-15"),
        (16, "Liam Harris", "Microphone", 2, 75, 150, "2025-04-16"),
        (17, "Emma Walker", "Charger", 3, 20, 60, "2025-04-17"),
        (18, "Noah Hall", "Power Bank", 1, 40, 40, "2025-04-18"),
        (19, "Ava Young", "Projector", 1, 500, 500, "2025-04-19"),
        (20, "Isabella King", "Desk Lamp", 2, 30, 60, "2025-04-20"),
        (21, "Ethan Wright", "Chair", 1, 150, 150, "2025-04-21"),
        (22, "Sophia Scott", "Desk", 1, 300, 300, "2025-04-22"),
        (23, "Mason Lewis", "TV", 1, 1000, 1000, "2025-04-23"),
        (24, "Mia Robinson", "Air Conditioner", 1, 1200, 1200, "2025-04-24"),
        (25, "Lucas Martinez", "Fan", 2, 50, 100, "2025-04-25"),
    ]
    columns = ["transaction_id", "customer_name", "product", "quantity", "price", "total_amount", "date"]
    df = spark.createDataFrame(data, schema=columns)
    return df