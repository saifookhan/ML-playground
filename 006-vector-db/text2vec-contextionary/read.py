from langchain.vectorstores import Weaviate
import weaviate
import json
import time

allCategories = [
  "POLITICS",
  "SPORTS",
  "SCIENCE",
  "TECH",
  "BUSINESS",
  "ENTERTAINMENT",
  "WORLD NEWS",
  "WEIRD NEWS",
  "RELIGION",
  "ARTS",
  "ENVIRONMENT"
]


client = weaviate.Client(
  url="http://localhost:8080",
  additional_headers={
        "X-HuggingFace-Api-Key": ""
    }
)
#print(len(client.data_object.get(class_name="News",
                           #with_vector=True)['objects']))

#print(client.data_object.get(limit=1,class_name="News",
                           #with_vector=True)['objects'])

response = (
    client.query
    .get("News", ["category", "short_description", "headline"])
    .with_near_text({"concepts": ["AMERICA"]})
    .with_where({
        "operator": "And",
        "operands": [
            {
                "path": ["category"],
                "operator": "Equal",
                "valueText": "SPORTS",
            }
        ]
    })
    .with_limit(10)
    .do()
)

print(json.dumps(response, indent=2))