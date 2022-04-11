# -*- coding: utf-8 -*-
"""
Created on Sat Jan  4 13:18:08 2020

@author: NEM'S
"""

def authentification( pwd):
    p='gagner@'
    if(pwd!=p):
        print('mot de pqsse incorrect')
    else:
        print('Bienvenue dans admin')
        
def menu():
    print("=============================================\n")
    print("++++++++si vous etes: +++++++++++++++++++++++")
    print("\n.......... un admin tapez ....1")
    print("\n .........une pesonne desirant voter tapez ....2")
    print("\n............... paramettre ....3")
    print("\n .............quiter tapez ....0\n")

    
def menu_admin():
    print("===========================================\n")
    print("..........Ajouter candidat tapez ....1\n")
    print(".........Commencer le vote............2\n")
    print("....Achever le vote....................3\n")
    print("......Afficher le vainqueur ...........4\n")
    print("........Afficher le resultat...........5\n")
    print("........Quiter.......0\n")
############################################################################33
def saisie():
    try:
        choix=int(input())
        return choix
    except ValueError:
        return -1
#########################
def saisie_du_choix():
    print("Faites votre choix,please\n")
    return saisie()
####################################
def saisie_du_nom_candidat():
    print("Veillez entrer le nom du condidat:\n")
    return input()
#########################
def menu_vote():
    print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n")
    print("@@@@   Afficher les candidats  ............1    @@@@@@@@@@2@2\n")
    print("@@@@@    Passer le vote ................2      @@@@@@@@@@@@\n")
    print("@@@@@  Quiter ......0                   @@@@@@@@@@@@@@@@@@@@\n")
    print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n")
##########################################################

def Administrateur(liste_candidats,demarrer_vote,acheminer_vote):
    candidats=[]
    while(True):
         menu_admin()
         choix=saisie_du_choix()
         if(choix<0 or choix>5):
             print("Choix incorrect")
         elif(choix==0):
             return candidats, demarrer_vote, acheminer_vote
         elif(choix==1):
             nom= saisie_du_nom_candidat()
             candidats=[nom,0]
             liste_candidats.append(candidats)
         elif(choix==2):
            demarrer_vote=True
         elif(choix==3):
            acheminer_vote=True
         elif(choix==4):
            if(len(liste_candidats)):
                print("Desole ,pas de candidats")
            for candid in liste_candidats:
                print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n")
                print("@@@@  candidat :" +candid[0]+"@@@@@@@@@@@@@@@@@@@\n")
                print("@@@@  nombre de point :" +str(candid[1])+"@@@@@@@@@@@@\n")
                print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@2@\n")
         elif(choix==5):
            nombre_des_voters=-1
            max_des_candidat=[]
            if(len(liste_candidats)):
                print("Desole ,pas de candidats")
            for candid in liste_candidats:
                if(candid[1]>nombre_des_voters):
                    nombre_des_voters=candid[1]
                    
            for candid in liste_candidats:
                if(candid[1]==nombre_des_voters):
                    max_des_candidat.append(candid)
            
            for cand in max_des_candidat:
                print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n")
                print("@@@@  Vainqueur :" +candid[0]+"avec "+str(candid[1])+"points @@@@@@@@@@@\n")
                print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@2@\n")
    
#################################################################################################
#################################################################################################
def vote(liste_candidats,demarrer_vote,acheminer_vote):
  ##  candidats=[]
    while(True):
         menu_vote()
         choix=saisie_du_choix()
         if(choix<0 or choix>3):
             print("Choix incorrect")
         elif(choix==0):
             return liste_candidats
             break
         elif(choix==1):
             if(len(liste_candidats)):
                print("Desole ,pas de candidats")
                # aaffichage de la liste des candidats
             for candid in liste_candidats:
                print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n")
                print("@@@@  candidat :" +candid[0]+"      @@@@@@@@@@@@@@@@@@@\n")
                print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@2@\n")
             
         elif(choix==2):
    #on cherche ici a effectue le vote
            if(demarrer_vote==False):
                print("le vote n'a pas encore commence  \n")
            elif(acheminer_vote==True):
                print("Le vote est deja arrete")
            else:
                print(" Veillez saisir le nom de votre candidat \n")
                sortie=False
                nom=input()
                for candid in liste_candidats:
                    if(candid[0]==nom):
                        sortie==True
                        candid[1]=candid[1]+1
                if(sortie==False):
                    print(nom+"n'est pas un nom d'un candidat\n")
                else:
                    print("Vote tres bien effectue \n")
##########################################################################################
##########################################################################################
def parametre(passeword_admin ,changer_password_admin):
    if(changer_password_admin==12345):
        mdp=input("Veillez initialiser le mot de passe admin\n")
        mdpc=input("Veillez confirmer le mot de passe\n")
        if(mdp==mdpc):
            return mdp,1
        else:
            #ici c'est quand on a une erreur de confirmation de mot de passe
            return mdp,-1
    else:
        mdpa=input("Veillez saisir le mot de passe admin\n")
        if(mdpa==passeword_admin):
            mdpass=input("Saisir le nouveau mot de passe")
            mdpac=input("Saisir le nouveau mot de passe")
            if(mdpass==mdpac):
                return mdpass,2
            else:
                return passeword_admin,-2
        else:
            #s'il ya une erreur d'authentification
            return passeword_admin,-3
        
            
###########################################################################################################
#####################le programme principal################################################################
def main():
    
    changer_password_admin=12345
    choix=0
    
    debuter_vote=False
    terminer_vote=False
    
    passeword_admin=""
    #condidat=[]
    liste_candidat_vote=[]
    
    while(True):
         menu()
         choix=saisie_du_choix()
         if(choix<0 or choix>3):
             print("Choix incorrect\n")
         elif(choix==0):
             print("operation bien faite\n")
             break
         elif(choix==1):
             if(len(liste_candidat_vote)):
                print("Desole ,pas de candidats")
             if(changer_password_admin!=12345):
                 mdp=input("Veillez saisir le mot de passe admin\n")
                 if (mdp==passeword_admin):
                     (liste_candidat_vote,debuter_vote,terminer_vote)=  Administrateur(liste_candidat_vote,debuter_vote,terminer_vote)
                 else:
                     print("mot de passe different\n")
             else:
                 (liste_candidat_vote,debuter_vote,terminer_vote)=  Administrateur(liste_candidat_vote,debuter_vote,terminer_vote)
         elif(choix==2):
             liste_candidat_vote=vote(liste_candidat_vote,debuter_vote,terminer_vote)
         elif(choix==3):
             (passeword_admin,new_pass)=parametre(passeword_admin ,changer_password_admin)
             if(new_pass==1):
                 print("le mot de passe est bien initialise\n")
                 changer_password_admin=changer_password_admin+1
             elif(new_pass==2):
                 print("le mot de passe a bien ete change\n" )
             elif(new_pass==-1 or new_pass==-2):
                print("le mot de passe de confirmation  ne correspond pas au vrai mot de passe\n")
             elif(new_pass==-3):
                print("le mot de passe saisi est incorrect\n")

    
    
    
    
        