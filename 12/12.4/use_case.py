from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS
import random
import time

# Configuración
bucket = "megaplazadb"
org = "UNI"
url = "http://localhost:8086"
token = "r-E9shDSArNp9ybXwfJ-MszqgxO1vAGNes7gFMAXRJKeRdaEou5WHGqpigWgHQBxeEXlCM6Iyu4M4l2qH49WIg=="

client = InfluxDBClient(url=url, token=token, org=org)
write_api = client.write_api(write_options=SYNCHRONOUS)

# Ejemplo de datos de locales
locales = [
    {"local_id": "L001", "floor": "1", "type_of_store": "restaurant"},
    {"local_id": "L002", "floor": "1", "type_of_store": "clothing"},
    {"local_id": "L003", "floor": "2", "type_of_store": "electronics"},
]

for i in range(10):
    for local in locales:
        point = (
            Point("energy_usage")
            .tag("local_id", local["local_id"])
            .tag("floor", local["floor"])
            .tag("type_of_store", local["type_of_store"])
            .field("electricity_kwh", random.uniform(50, 500))
            .field("water_liters", random.uniform(100, 1000))
            .field("gas_cubic_meters", random.uniform(5, 50))
            .time(time.time_ns(), WritePrecision.NS)
        )
        write_api.write(bucket=bucket, org=org, record=point)
        print(f"Registro guardado para {local['local_id']}")
    time.sleep(5)
