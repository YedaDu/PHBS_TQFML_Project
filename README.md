# PHBS_TQFML_Project

## Final Project: Specific Market Value factor: explaining market value by machine learning
Written by <br> 
* Junjie Zhou 1601213672<br> 
* Shixin Chen 1601213497<br> 
* Sheng Gu 1601213529<br> 
* Yeda Du 1601213511<br> 

## Idea
At a given specific time point, market value explanition models think market values of listed firms can be explained by theirs financial informations and market factors.<br>
Under such assumptions, these models will induce an intrinsic market value of a listed firms at a specific time, however, there's always a residue term, which is also the difference between intrinsic value and current market value.<br>
We name this residue term as Specific Market Value Factor (SMVF), larger this factor is, indicating more upper bias is between current firm value and intrinsic value, by the idea of mean-reverting, it is more likely for the stock price to drop.<br>
In other words, this is a way of relative valuation and a smaller SMVF indicates a better performance of the stock.<br>

## PLan
We plan to construct SMVF by both linear model and machine learning methods including adaline, random forests and AdaBoost method.<br>
Then by using the SMVF we construct, predicting the firms value and compare the result of above methods.

## Data
We are going to use Full Index of SHSE & SZSE stocks as our sample.<br>
Time period is from 2007.01~2016.12, monthly data.<br>
The data we use include market value, type of industry, net asset, net income, leverage ratio, revenue growth rate and R&D expense.<br>
The data process methods we plan to use include standardized and PCA methods (subject to change).<br>

## Reference
1. Rhodes–Kropf, M., Robinson, D. T., & Viswanathan, S. (2005). Valuation waves and merger activity: The empirical evidence. Journal of Financial Economics, 77(3), 561-603.<br>
2. Hulten, C. R., & Hao, X. (2008). What is a Company Really Worth? Intangible Capital and the" Market to Book Value" Puzzle (No. w14548). National Bureau of Economic Research.<br>
3. 朱剑涛（2017）.特异市值因子.东方证券系列研报（因子选系列28）.<br>
