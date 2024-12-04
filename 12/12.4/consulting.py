from use_case import client, org

query_api = client.query_api()

query = """
from(bucket: "megaplazadb")
    |> range(start: -1h)
    |> filter(fn: (r) => r._measurement == "energy_usage")
    |> filter(fn: (r) => r._field == "electricity_kwh")
    |> group(columns: ["local_id"])
    |> sum()
"""
tables = query_api.query(query=query, org=org)

for table in tables:
    for record in table.records:
        print(f"Local: {record['local_id']}, Consumo total de electricidad: {record.get_value()} kWh")