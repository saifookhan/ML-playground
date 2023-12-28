from langchain.vectorstores import Weaviate
import weaviate
import json
import time

client = weaviate.Client(
  url="http://localhost:8080",
  additional_headers={
        "X-HuggingFace-Api-Key": ""
    }
)
print(len(client.data_object.get(class_name="News",
                           with_vector=True)['objects']))

print(client.data_object.get(limit=1,class_name="News",
                           with_vector=True)['objects'])