# -*- coding: utf-8 -*-
"""
Created on Fri Apr  5 16:48:44 2019

@author: Guest
"""

from pathlib import Path
import pandas as pd
p = Path(r'C:\Users\Guest\Desktop\python_Workstation\arda_folder')

pathnames = list(p.glob("./*.csv"))
dataframes = [
        pd.read_csv(x).drop(columns=['Unnamed: 0'])
        for x in pathnames
        ]
all_dfs = pd.concat(dataframes)
subfld = ['church name',
          'city',
          'denomination',
          'latitude',
          'longitude',
          'state',
          'street address',
          'zip code'
          ]

no_dupl = all_dfs.drop_duplicates(subset=subfld)
no_dupl.to_csv('total_arda_church_backup.csv')
