# -*- coding: utf-8 -*-
"""
Created on Sat Apr 21 22:36:55 2018

@author: sxchen0705
"""

import numpy as np
import pandas as pd
import datetime

def quarter2month(tdate,data,factorname):
    datadate=list(data.columns[2:])
    datayear=np.array([x.year for x in datadate])
    datamonth=np.array([x.month for x in datadate])
    for i in range(len(tdate)):
        tdate_sel=str(tdate[i])
        tdate_sel=datetime.datetime(int(tdate_sel[:4]),int(tdate_sel[4:6]),int(tdate_sel[6:]),0,0)
        if tdate_sel.month<=3:
            ix=np.where((datayear==tdate_sel.year-1) & (datamonth==9))[0] # 去年3季报
        elif tdate_sel.month>=4 and tdate_sel.month<=7:
            ix=np.where((datayear==tdate_sel.year) & (datamonth==3))[0] # 今年1季报
        elif tdate_sel.month>=8 and tdate_sel.month<=9:
            ix=np.where((datayear==tdate_sel.year) & (datamonth==6))[0] # 今年半年报
        elif tdate_sel.month>=10:
            ix=np.where((datayear==tdate_sel.year) & (datamonth==9))[0] # 今年3季报
        data_sel=data.iloc[:,[0,ix+2]]
        data_sel.columns=['code',factorname]
        data_sel['date']=tdate[i]
        if i==0:
            factor_frm=data_sel
        else:
            factor_frm=pd.concat([factor_frm,data_sel],axis=0)
    return factor_frm