
from hdfs import InsecureClient

client = InsecureClient("http://namenode:50070")

# Do something to prepare the data for HDFS
data = {"example": "data"}

with client.write("/data/example.json", encoding="utf-8") as writer:
        writer.write(str(data))
