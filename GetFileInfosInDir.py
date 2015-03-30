# -*- coding: utf8 -*-

import os, time

#List All Files in DIR + get Size + get Creation

folder_path = "C:\\Users\\Arnaud\\Documents\\Projets\\4A_SI2\\Forensic\\test"
print(folder_path)

for path, dirs, files in os.walk(folder_path):
    for filename in files:
        count=0
        print("Nom Long : "+path+"\\"+filename)
        #Taille
        print("Taille: "+str(os.path.getsize(path+"\\"+filename))+" Octets")
        #Date création
        print("Date de Création: "+str(time.ctime(os.path.getctime(path+"\\"+filename))))
        #Date Modification
        print("Date de Modification: "+str(time.ctime(os.path.getmtime(path+"\\"+filename))))
        #Taille Fichier
        f=open(path+"\\"+filename)
        for line in f : count+=1
        print("Le fichier fait %d lignes"% count)
        f.close()
