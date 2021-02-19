import pandas as pd
import requests

#Search npi registry for specific taxonomy - Sample call: https://npiregistry.cms.hhs.gov/api/?number=&enumeration_type=&taxonomy_description=&first_name=&use_first_name_alias=&last_name=&organization_name=&address_purpose=&city=&state=&postal_code=&country_code=&limit=&skip=&version=2.1
#Output to csv
#Full NPI Registry API documentation (using v2.1): https://npiregistry.cms.hhs.gov/registry/help-api
#NPPES :National Plan and Provider Enumeration System
taxonomy = 'Dentist'

r = requests.get(url='https://npiregistry.cms.hhs.gov/api/?number=&enumeration_type=&taxonomy_description={}&state=AR&limit=200&skip=&pretty=on&version=2.1'.format(taxonomy))
data = r.json()
if data["result_count"] > 0:
    data = data["results"]
    df = pd.json_normalize(data)
    df.to_csv('nppes.csv', index = None, header=True)
else:
    print("no match")

    # "NPI" = number
    # "Entity Type Code" = enumeration_type
    # "Replacement NPI" = basic.replacement_npi
    # "Employer Identification Number (EIN)" = basic.ein
    # "Provider Organization Name (Legal Business Name)" = basic.organization_name
    # "Provider Last Name (Legal Name)" = basic.last_name
    # "Provider First Name" = basic.first_name
    # "Provider Middle Name" = basic.middle_name
    # "Provider Name Prefix Text" = basic.name_prefix
    # "Provider Name Suffix Text" = basic.name_suffix
    # "Provider Credential Text" = basic.credential
    # "Provider Other Organization Name" = other_names[0].organization_name" = Version 1 Only. Version 2 uses Other Name file for Other Organization Names
    # "Provider Other Organization Name Type Code" = other_names[0].code
    # "Provider Other Last Name" = other_names[0].last_name
    # "Provider Other First Name" = other_names[0].first_name
    # "Provider Other Middle Name" = other_names[0].middle_name
    # "Provider Other Name Prefix Text" = other_names[0].prefix
    # "Provider Other Name Suffix Text" = other_names[0].suffix
    # "Provider Other Credential Text" = other_names[0].credential
    # "Provider Other Last Name Type Code" = other_names[0].code
    # "DERIVED VALUE" = other_names[0].type" = Derived from code
    # "Provider First Line Business Mailing Address" = addresses[1].address_1
    # "Provider Second Line Business Mailing Address" = addresses[1].address_2
    # "Provider Business Mailing Address City Name" = addresses[1].city
    # "Provider Business Mailing Address State Name" = addresses[1].state
    # "Provider Business Mailing Address Postal Code" = addresses[1]. postal_code
    # "Provider Business Mailing Address Country Code (If outside U.S.)" = addresses[1].country_code
    # "Provider Business Mailing Address Telephone Number" = addresses[1].telephone_number
    # "Provider Business Mailing Address Fax Number" = addresses[1]. fax_number
    # "CONSTANT VALUE" = addresses[1].address_purpose" = "MAILING"
    # "Provider First Line Business Practice Location Address" = addresses[0].address_1
    # "Provider Second Line Business Practice Location Address" = addresses[0].address_2
    # "Provider Business Practice Location Address City Name" = addresses[0].city
    # "Provider Business Practice Location Address State Name" = addresses[0].state
    # "Provider Business Practice Location Address Postal Code" = addresses[0]. postal_code
    # "Provider Business Practice Location Address Country Code (If outside U.S.)" = addresses[0].country_code
    # "Provider Business Practice Location Address Telephone Number" = addresses[0].telephone_number
    # "Provider Business Practice Location Address Fax Number" = addresses[0]. fax_number
    # "CONSTANT VALUE" = addresses[0].address_purpose" = "LOCATION"
    # "Provider Enumeration Date" = basic.enumeration_date
    # "DERIVED VALUE" = created_epoch" = Derived from Col 37
    # "Last Update Date" = basic.last_updated
    # "DERIVED VALUE" = last_updated_epoch" = Derived from Col 38
    # "NPI Deactivation Reason Code" = basic.deactivation_reason_code
    # "NPI Deactivation Date" = basic.deactivation_date
    # "NPI Reactivation Date" = basic.reactivation_date
    # "Provider Gender Code" = basic.gender
    # "Authorized Official Last Name" = basic.authorized_official_last_name
    # "Authorized Official First Name" = basic.authorized_official_first_name
    # "Authorized Official Middle Name" = basic.authorized_official_middle_name
    # "Authorized Official Title or Position" = basic.authorized_official_title_or_position
    # "Authorized Official Telephone Number" = basic.authorized_official_telephone_number
    # "Healthcare Provider Taxonomy Code_1" = taxonomies[0].code
    # "Provider License Number_1" = taxonomies[0].license
    # "Provider License Number State Code_1" = taxonomies[0].state
    # "Healthcare Provider Primary Taxonomy Switch_1" = taxonomies[0].primary
    # "DERIVED VALUE" = taxonomies[0].desc" = Derived from code
    # "Healthcare Provider Taxonomy Code_15" = taxonomies[14].code
    # "Provider License Number_15" = taxonomies[14].license
    # "Provider License Number State Code_15" = taxonomies[14].state
    # "Healthcare Provider Primary Taxonomy Switch_15" = taxonomies[14].primary
    # "DERIVED VALUE" = taxonomies[14].desc" = Derived from code
    # "Other Provider Identifier_1" = identifiers[0].identifier
    # "Other Provider Identifier Type Code_1" = identifiers[0].code
    # "Other Provider Identifier State_1" = identifiers[0].state
    # "Other Provider Identifier Issuer_1" = identifiers[0].issuer
    # "DERIVED VALUE" = identifiers[0].desc" = Derived from code
    # "Other Provider Identifier_50" = identifiers[49].identifier
    # "Other Provider Identifier Type Code_50" = identifiers[49].code
    # "Other Provider Identifier State_50" = identifiers[49].state
    # "Other Provider Identifier Issuer_50" = identifiers[49].issuer
    # "DERIVED VALUE" = identifiers[49].desc" = Derived from code
    # "Is Sole Proprietor" = basic.sole_proprietor
    # "Is Organization Subpart" = basic.organizational_subpart
    # "Parent Organization LBN" = basic.parent_organization_legal_business_name
    # "Parent Organization TIN" = basic.parent_organization_ein
    # "Authorized Official Name Prefix Text" = basic.authorized_official_name_prefix
    # "Authorized Official Name Suffix Text" = basic.authorized_official_name_suffix
    # "Authorized Official Credential Text" = basic.authorized_official_credential
    # "Healthcare Provider Taxonomy Group_1" = taxonomies[0].taxonomy_group
    # "Healthcare Provider Taxonomy Group_15" = taxonomies[14].taxonomy_group
    # "Certification Date" = basic.certification_date
