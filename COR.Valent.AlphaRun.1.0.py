#!/usr/bin/env python

# COR Valent Alpha Run 1.0
#
#

import numpy as np
import pandas as pd


APPCORValentAllocation=200000  #COR February 9, 2018

matrixInputs=pd.read_csv('matrix_alpha_run_1.csv')


CO=np.array(matrixInputs[["CO"]])
CO=CO[:,0]
CI=np.array(matrixInputs[["CI"]])
CI=CI[:,0]
Activity=np.array(matrixInputs[["Activity"]])
Activity=Activity[:,0] #Activity=np.add(np.add(Tweets,10*ReTweets),np.add(Tickets,10*Workshards))

ActivityRandomFactor=np.random.randint(1,1041,size=len(Activity))  

CCV=np.sqrt(np.square(CO)+np.square(CI)+np.square(Activity))

RawScore=np.add(np.multiply(Activity,ActivityRandomFactor),CCV)

ScaledScore = RawScore/np.sum(RawScore)

print('Scaled Scores Are: \n',ScaledScore)

CORTOASSIGN=APPCORValentAllocation*0.0025

CORVALENTAWARD=CORTOASSIGN*ScaledScore

checkValentSum=np.sum(CORVALENTAWARD)

print('checkValentSum: \n',checkValentSum)

matrixInputs['Valent COR']=CORVALENTAWARD
matrixInputs['CCV']=CCV

matrixInputs.to_csv('matrixInputs_COR_Awarded.csv')

print('matrixInputs_COR_Awarded: \n',matrixInputs)






