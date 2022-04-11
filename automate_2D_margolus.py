# -*- coding: utf-8 -*-
"""
Created on Thu Apr 23 19:16:23 2020

@author: NEM'S
"""

def margolus(matris , regle):
   # matrisRetour
    for i in range(0,len(matris)-1,2):
        for j in range(0,len(matris[i])-1,2):
            chaine_binaire=matris[i][j]*8 +matris[i][j+1]*4 +matris[i+1][j+1]*2+ matris[i+1][j]*0
            nbr=int(chaine_binaire)
            nouv_ch=regle[nbr]
            nouv_ch_binaire=bin(nouv_ch)[2:].zfill(4)
            matris[i][j]=int(nouv_ch_binaire[0])
            matris[i][j+1]=int(nouv_ch_binaire[1])
            matris[i+1][j+1]=int(nouv_ch_binaire[2])
            matris[i+1][j]=int(nouv_ch_binaire[3])
    return matris
    
T=[[0,1,0,1,1,1,0,1],[1,1,0,0,0,1,0,1],[0,0,0,1,1,1,1,0],[1,1,1,1,1,1,0,0]]
regl=[1,12,13,4,8,9,15,14,6,10,3,11,2,7,5,0]
tabretour=margolus(T,regl)
for i in range(len(tabretour)):
    #for j in range(len(tabretour[i])-1):
        print(tabretour[i])
