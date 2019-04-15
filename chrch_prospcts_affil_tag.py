# -*- coding: utf-8 -*-
"""
Created on Tue Apr  2 08:50:58 2019

@author: Guest
"""

import pandas as pd
import arda_gis_denom
import json
fields = ['id',
          'name',
          'billing_address_street_prospect',
          'billing_address_city_prospect',
          'billing_address_state_prospect',
          'billing_address_postalcode_prospect'
          ]
renamed_dict = {'billing_address_street_prospect': "street",
                'billing_address_city_prospect': "city",
                'billing_address_state_prospect': "state",
                'billing_address_postalcode_prospect': "zipcode"}
df_prospecting = pd.read_csv("df_gpcdb_prospects.csv",
                             encoding="ISO-8859-1",
                             usecols=fields,
                             dtype="object",
                             index_col=0
                             )

with open('keywords_churches.json', 'w') as infile:
    keyword_affiliation = json.load(infile)
# maybe add again later:"united": "methodist",


def add_keyword(keyword, value):
    """add_keyword to dictionary"""
    if keyword in keyword_affiliation:
        print('error, keyword already in dictionary with value')
        print(keyword_affiliation[keyword])
    else:
        keyword_affiliation[keyword] = value
        with open('keywords_churches.json', 'w') as outfile:
            json.dump(keyword_affiliation, outfile)



def preprocess_crm_prospects(df):
    """ preprocess prospect dataframe df for join with the ARDA dataframe"""
    df = df.rename(index=str, columns=renamed_dict)
    df = df.apply(lambda x: x.str.strip())
    df = df.apply(lambda x: x.str.lower())
    return df.dropna()


def preprocess_arda(df):
    """ preprocess prospect dataframe df for join with the ARDA dataframe"""
    df = df.apply(lambda x: x.str.strip())
    df = df.apply(lambda x: x.str.lower())
    return df.dropna()


def prospect_arda_match(df_prospecting, df_arda):
    """ match prospect df with arda df"""
    left_columns = ['street',
                    'city',
                    'zipcode'
                    ]
    right_columns = ['street address',
                     'city',
                     'zip code'
                     ]
    df_arda = df_arda.drop_duplicates(subset=right_columns)
    df_prospect_merged = df_prospecting.reset_index().merge(
            df_arda,
            how='left',
            left_on=left_columns,
            right_on=right_columns
            ).set_index('id')
    return df_prospect_merged


def map_affil(church_name):
    """ determine church afilliation from church_name """
    default_val = None
    keyword_iter = (x for x in keyword_affiliation if x in church_name)
    key = next(keyword_iter, default_val)
    if key is not None:
        return keyword_affiliation[key]
    else:
        return None


def bible_to_christian(church_name):
    """determine if church contains 'bible' in name"""
    if "bible" in church_name:
        return "christian"
    else:
        return None


def bible_fill(row):
    if pd.isnull(row['filled_aux']):
        return bible_to_christian(row['name'])
    else:
        return row.denom


def get_affiliation(df, df_arda):
    """ get affiliation from a row in df. The procedure first selects
    tries to find the affiliation using map_affil, and if it isn't found,
    it proceeds to get it from the dataframe join with df_arda
    """
    df_merged = prospect_arda_match(df, df_arda)
    df_merged['denom'] = df_merged['name'].apply(map_affil)
    df_merged['filled_aux'] = df_merged['denom'].fillna(
            df_merged['denomination'])
    df_merged['filled'] = df_merged.apply(bible_fill, axis=1)
    return df_merged['filled']


def test(df_prospect, city_test):
    df_arda = arda_gis_denom.create_df_city(city_test)
    print(len(df_arda))
    df_prospect = preprocess_crm_prospects(df_prospect)
    print(len(df_prospect))
    df_arda_fields = ['church name',
                      'city',
                      'state',
                      'street address',
                      'zip code']
    df_arda[df_arda_fields] = preprocess_arda(df_arda[df_arda_fields])
    print(len(df_arda))
    df_arda = df_arda[df_arda['city'] == city_test]
    print(len(df_arda))

    df_prospect = df_prospect[df_prospect['city'] == city_test]
    print(len(df_prospect))
    df_prospect2 = df_prospect.copy()
    df_prospect2['affili'] = get_affiliation(df_prospect, df_arda)
    return df_prospect2


def create_arda_csvs(top_cities2):
    """create a csv for every city in top_cities2"""
    for city in top_cities2:
        csv_name = "ardachurches_{}.csv".format(city)
        df_arda = arda_gis_denom.create_df_city(city)
        df_arda.to_csv(csv_name)
