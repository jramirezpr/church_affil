# -*- coding: utf-8 -*-
"""
Created on Thu Mar 28 15:22:50 2019

@author: Guest
"""
import json
import requests
import pandas as pd
URLplaces = ("http://maps.nazarene.org/arcgis/rest/services/"
             + "ARDA/InfoGroupChurches/MapServer/0/query")
URLcandidates = ("https://geocode.arcgis.com/arcgis/rest/services/"
                 + "World/GeocodeServer/findAddressCandidates")


def arda_gis_geometry_dict(city, url, state="Illinois", country="USA"):
    """get geometry from a city using the rest API"""
    querystring = {"f": "json",
                   "outFields": "Loc_nam",
                   "city": city,
                   "countryCode": country,
                   "region": state}
    response = requests.request("GET",
                                url,
                                params=querystring)
    resp_json = response.json()
    geom_json = resp_json["candidates"][0]["extent"]
    geom_json["spatialReference"] = {"wkid": 4326}
    return geom_json


def arda_gis_churches(geom_dict, url):
    """ get churches for city from arda api."""
    geom_string = json.dumps(geom_dict)
    querystring = {"f": "json",
                   "where": "",
                   "returnGeometry": "true",
                   "spatialRel": "esriSpatialRelIntersects",
                   "geometryType": "esriGeometryEnvelope",
                   "geometry": geom_string,
                   "inSR": "4326",
                   "outFields": "COMPANY_NA,ADDRESS,CITY,STATE,ZIP_CODE,DENOM_DESC",
                   "outSR": "4326"}
    response = requests.request("GET",
                                url,
                                params=querystring)
    return response


def json_crawl(json_dict):
    """ crawl_through arcgis church json, return
    list of dictionaries of reshaped data """
    feature_list = json_dict['features']
    church_list = []
    for feature in feature_list:
        lat = feature['geometry']['y']
        long = feature['geometry']['x']
        name = feature['attributes']['COMPANY_NA']
        street_address = feature['attributes']['ADDRESS']
        city = feature['attributes']['CITY']
        state = feature['attributes']['STATE']
        zipcode = feature['attributes']['ZIP_CODE']
        denomination = feature['attributes']['DENOM_DESC']
        re_dict = {"latitude": lat,
                   "longitude": long,
                   "church name": name,
                   "street address": street_address,
                   "city": city,
                   "state": state,
                   "zip code": zipcode,
                   "denomination": denomination
                   }
        church_list.append(re_dict)
    return church_list


def strip_zipcode(zip_code):
    """ function returns the zipcode part
    from an entry that
    might be a normal zipcode or a zip+4 entry
    (everything before the dash)"""
    if "-" in zip_code:
        zip_c = zip_code.split('-')[0]
    elif len(zip_code) != 5:
        print("error " + zip_code + "is not correct length")
        zip_c = None
    elif not zip_code.isdigit():
        print("error " + zip_code + "contains nondigits")
        zip_c = None
    else:
        zip_c = zip_code
    return zip_c


def create_df_city(city):
    """ create DataFrame with church info in given city"""
    dicc = arda_gis_geometry_dict(city, URLcandidates)
    respo = arda_gis_churches(dicc, URLplaces)
    church_list = json_crawl(respo.json())
    df_church = pd.DataFrame(church_list)
    if not df_church.empty:
        df_church['zip code'] = df_church['zip code'].apply(strip_zipcode)
    return df_church
