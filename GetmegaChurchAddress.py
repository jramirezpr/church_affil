# -*- coding: utf-8 -*-
"""
Created on Thu Nov 29 14:26:30 2018

@author: Guest
"""
import pandas as pd
dfMChurch=pd.read_excel('Megachurches.xlsx',dtype={'ChurchName':str})
dfMChurch['ChurchName2']=dfMChurch['ChurchName'].str.replace('\xa0','')
dfMChurch['ChurchName2']=dfMChurch['ChurchName2'].str.upper()
dfMChurch['City']=dfMChurch['City'].str.upper()
megachurchsingleDict={}
megachurchmultiDict={}
megachurchNoMatchDict={}
megachurchApproxMatch={}
stillnomatch={}
dfIRS=pd.read_csv('eo_ca.csv')
for index, row in dfMChurch.iterrows():
    dfcity=dfIRS[dfIRS['CITY']==row['City']]
    dfMATCH=dfcity[dfcity['NAME']==row['ChurchName2']]
    if(len(dfMATCH.index)>1):
        megachurchmultiDict[
                row['ChurchName2']
                ]=list(dfMATCH['CITY'])
    elif(len(dfMATCH.index)==1):
        megachurchsingleDict[
                row['ChurchName2']
                ]=[dfMATCH['STREET'].item(),dfMATCH['CITY'].item()]
    else: 
        megachurchNoMatchDict[
                row['ChurchName2']
                ]=row['City']
        dfMATCH=dfcity[dfcity['NAME'].str.startswith(row['ChurchName2'])]
        if(len(dfMATCH.index)>1):
             megachurchmultiDict[
                row['ChurchName2']
                ]=list(dfMATCH['CITY'])
        elif(len(dfMATCH.index)==1):
            megachurchApproxMatch[
                row['ChurchName2']
                ]=[dfMATCH['STREET'].item(),dfMATCH['CITY'].item()]
        else:
            stillnomatch[
            row['ChurchName2']
            ]=row['City']
        

    
        
    
    

