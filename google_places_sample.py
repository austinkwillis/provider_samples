import pandas as pd
import requests


query = 'Baptist Health Urgent Care - Fort Smith'
your_api_key = ''
result_set = pd.DataFrame()
r = requests.get(url='https://maps.googleapis.com/maps/api/place/findplacefromtext/json?input={}&inputtype=textquery&fields={}&key={}'.format(query,'photos,formatted_address,name,rating,opening_hours,geometry',your_api_key))

data = r.json()
if data["candidates"]:
    data = data["candidates"]
    df = pd.json_normalize(data)
    df.to_csv('google_data.csv', index = None, header=True)
else:
    print("no match")