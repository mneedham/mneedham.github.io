from elastic_app_search import Client
import requests as r

engine_name = 'meals'
api_key = "private-kwicp7mhwssdxv54as9buzen"

client = Client(
    api_key=api_key,
    base_endpoint='localhost:3002/api/as/v1',
    use_https=False
)

response = r.get("https://www.themealdb.com/api/json/v1/1/search.php?f=a").json()
documents = []
for entry in response["meals"]:
    documents.append(entry)
    if len(documents) % 50 == 0:
        res = client.index_documents(engine_name, documents)
        print(res)
        documents = []

res = client.index_documents(engine_name, documents)
print(res)
