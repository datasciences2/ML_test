# -*- coding: utf-8 -*-
"""
Created on Thu Mar 25 15:33:31 2021

@author: NEM'S
"""

import  numpy  as  np 
import  matplotlib.pyplot  as  plt 


#F(x)=ax +b  avec sigma(a,b)
def model(X, sigma):
    return X.dot(sigma)

def fonction_cout(X,y ,sigma):
    longueur=len(y)
    return 1/(2*longueur) * np.sum((model(X, sigma) - y)**2)

#fonction de gradiant
def grad(X, y, sigma):
    lgueur= len(y)
    return 1/lgueur* X.T.dot(model(X,sigma)-y)

def gradiant_descent(X,y, sigma,echec_apprendre,nb_iterat):
    sauvegarde= np.zeros(nb_iterat)# tableau de stockage pour enregistrer l'évolution
    
    for i in range(0,nb_iterat):
        sigma= sigma - echec_apprendre*grad(X, y, sigma)# ici c'est le mise à jour
        sauvegarde [i]= fonction_cout(X, y, sigma)# on stocke
    return sigma,sauvegarde


np.random.seed(0) #pour avoir le meme dataset 

n_echan=150 #nombre d'échantillons à gener

x=np.linspace(0,10,n_echan).reshape((n_echan,1))
y=x + np.random.randn(n_echan,1)


plt.figure()
plt.scatter(x,y)
plt.ylabel('data')
plt.show()
plt.savefig('image.png')

#Ajout de la colonne à X
X=np.hstack((x, np.ones(x.shape)))
print('table de X',x.shape)

#Création d'un vecteur sigma paramétré
sigma= np.random.randn(2, 1)
print(sigma)


#test en guise d'exemp
print('cout de fonction:',fonction_cout(X, y, sigma))#aucun erreur ,return un réel

nb_iterat=10
echec_apprendre= 0.01

sigma_final,sauvegarde= gradiant_descent(X, y, sigma, echec_apprendre, nb_iterat)

print('valeur final de sigma:',sigma_final) # on voit les derniers parametres du model qui ont evolue quand la machine a été entrainé

prediction= model(X, sigma_final)#un tableau de prediction qui contient les predictions du model à la fin

#affichage
plt.scatter(x,y)
plt.plot(x,prediction, 'g')
plt.show()

# cette partie permmet d'avoir l'allure de la courbe 
plt.plot(range(nb_iterat), sauvegarde-1 , 'y')
plt.show()















