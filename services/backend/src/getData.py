import requests
import pandas as pd
import requests

url = 'http://localhost:8000/problem/all'
r = requests.get(url)
json = r.json()
# k = json.keys()
print(json)

df = pd.DataFrame(json)
print(df)