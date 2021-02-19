import pandas as pd
import requests
import time

#Search npi registry for specific taxonomy and return bulk - Sample call: https://npiregistry.cms.hhs.gov/api/?number=&enumeration_type=&taxonomy_description=&first_name=&use_first_name_alias=&last_name=&organization_name=&address_purpose=&city=&state=&postal_code=&country_code=&limit=&skip=&version=2.1
#Output to csv
#Full NPI Registry API documentation (using v2.1): https://npiregistry.cms.hhs.gov/registry/help-api
#NPPES :National Plan and Provider Enumeration System
def get_results(taxonomy, result_set, skip, limit, max_results):
    url='https://npiregistry.cms.hhs.gov/api/?number=&enumeration_type=&taxonomy_description={}&state=AR&limit=200&skip={}&pretty=on&version=2.1'.format(taxonomy, skip)

    if skip < max_results:
        r = requests.get(url)
        data = r.json()
        result_count = int(data["result_count"])

        if result_count > 0:
            data = data["results"]
            df = pd.json_normalize(data)
            result_set = pd.concat([result_set, df], axis=0)
            if result_count == limit:
                skip = skip+limit
                print("found {}. fetching {} more".format(skip, limit))
                # Wait for 5 seconds...don't want to anger U.S. Centers for Medicare & Medicaid Services
                time.sleep(5)
                return get_results(taxonomy, result_set, skip, limit, 1000)

        else:
            print("no remaining matches")
    return result_set

full_result_set = pd.DataFrame()
full_result_set = get_results(taxonomy='Dentist', result_set=full_result_set, skip=0, limit=200, max_results=1000)
full_result_set.to_csv ('nppes.csv', index = None, header=True)