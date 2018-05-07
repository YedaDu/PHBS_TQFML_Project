# -*- coding: utf-8 -*-
"""
Created on Sun Apr 22 12:05:16 2018

@author: sxchen0705
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

def Winsorize_Fillna_Neutralize(data,factorname):
    tdate=list(data.date.drop_duplicates())
    for i in range(len(tdate)):
        data_sel=data[data.date==tdate[i]]
        ix_isan=~np.isnan(data_sel[factorname])
        factor_sel=data_sel[ix_isan][factorname]
        # 去极值
        md=np.median(factor_sel)
        mad=np.median(np.abs(np.array(factor_sel)-md))
        lowbound=md-5*mad
        highbound=md+5*mad
        factor_sel[factor_sel>highbound]=highbound
        factor_sel[factor_sel<lowbound]=lowbound
        data_sel[ix_isan][factorname]=factor_sel
        # 中位数填补缺失值
        data_sel[factorname]=data_sel[factorname].fillna(np.median(factor_sel))
        # zscore
        data_sel[factorname]=(np.array(data_sel[factorname])-np.mean(data_sel[factorname]))/np.std(data_sel[factorname])
        # 行业市值中性化
        industrydummies=pd.get_dummies(data_sel['industry'])
        y=np.array(data_sel[factorname])
        x=np.array(pd.concat([data_sel['logmv'],industrydummies],axis=1))
        lm=LinearRegression(fit_intercept=False)
        lm.fit(x,y)
        residuals=y-lm.predict(x)
        # 残差zscore
        data_sel[factorname]=(residuals-np.mean(residuals))/np.std(residuals)
        if i==0:
            factor_frm=data_sel
        else:
            factor_frm=pd.concat([factor_frm,data_sel],axis=0)
    return factor_frm