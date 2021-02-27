import pandas as pd
import requests
from configparser import ConfigParser

config = ConfigParser()

config.read('config.ini')
your_api_key = config.get('auth', 'google_api_key')

query = 'Baptist Health Urgent Care - Fort Smith'

result_set = pd.DataFrame()
r = requests.get(url='https://maps.googleapis.com/maps/api/place/findplacefromtext/json?input={}&inputtype=textquery&fields={}&key={}'.format(query,'photos,formatted_address,name,rating,opening_hours,geometry','AIzaSyAjNiryxVRJ_eyAxbzxqIlJAXNEXwRKFLE'))

data = r.json()
if data["candidates"]:
    data = data["candidates"]
    df = pd.json_normalize(data)
    df.to_csv('google_data.csv', index = None, header=True)
else:
    print("no match")