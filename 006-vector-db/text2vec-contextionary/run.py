from langchain.vectorstores import Weaviate
import weaviate
import json
import time

client = weaviate.Client(
  url="http://localhost:8080",
  additional_headers={
        "X-HuggingFace-Api-Key": "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"
    }
)

client.schema.delete_all()

schema = {
    "classes": [
        {
            "class": "News",
            "description": "This contains various news",
            "moduleConfig": {
                "text2vec-contextionary": {
                    "vectorizeClassName": False
                }
            },
            "properties": [
                {
                    "name": "link",
                    "dataType": ["string"],
                    "moduleConfig": {
                        "text2vec-contextionary": {
                        "vectorizePropertyName": False
                        }
                    },
                },
                {
                    "name": "headline",
                    "dataType": ["string"]
                },
                {
                    "name": "category",
                    "dataType": ["string"]
                },
                {
                    "dataType": ["text"],
                    "description": "The short_description of the news",
                    "name": "short_description",
                },
                {
                    "name": "authors",
                    "dataType": ["string"],
                    "moduleConfig": {
                        "text2vec-contextionary": {
                        "vectorizePropertyName": False
                        }
                    },
                },
                {
                    "name": "date",
                    "dataType": ["string"],
                    "moduleConfig": {
                        "text2vec-contextionary": {
                        "vectorizePropertyName": False
                        }
                    },
                }
            ],
         "vectorizer":"text2vec-contextionary"
        },
    ]
}

client.schema.create(schema)

# Read the file line by line and store each line as a dictionary in a list
newsReadData = []
with open('../data/News_Category_Dataset_v3.json', 'r') as file:
    for line in file:
        entry = json.loads(line)
        newsReadData.append(entry)

# Now, 'data' contains a list of dictionaries, each representing a line of your file
print(len(newsReadData))

def insertIntoDB(d, className):
    properties = {
            "link": d['link'],
            "headline":  d['headline'],
            "category": d['category'],
            "short_description": d['short_description'],
            "authors": d['authors'],
            "date": d['date']
        }
    
    #client.batch.add_data_object(properties, className)


with client.batch as batch:
    batch.batch_size=50
    batchCount = 0
    for i, d in enumerate(newsReadData):
        insertIntoDB(d, "News")
        print(i)
        batchCount = batchCount+1
        print(f"processing batch {batchCount}")