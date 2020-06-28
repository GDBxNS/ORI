import pandas as pd
from sklearn.cluster import  KMeans
import sys

def ucitavanje():
    # Ucitavanje podataka iz fajla
    podaci = pd.read_csv("credit_card_data.csv")

    # Zamenjuje prazna polja nulama
    podaci.fillna(0, inplace=True)
    x = pd.DataFrame(podaci)

    kmeans = KMeans(n_clusters=6, max_iter=100, random_state=5)

    # Uzimamo sve iz tabele sem CUST_ID
    kmeans.fit(x.iloc[:, 1:])

    labels = kmeans.labels_
    centroids = kmeans.cluster_centers_
    # print(labels)
    # print(centroids)
    return kmeans, x
    

if __name__ == '__main__':

    unos = ''
    while(True):
        print('\n')
        print("MENI:")
        print("1. UCITAVANJE")
        print('X  ZA IZLAZ')
        unos = input(">> ")
        if(unos == '1'):
            kmeans, x = ucitavanje()
            print(x)
        elif(unos == 'x' or unos == 'X'):
            print("Dovidjenja")
            sys.exit() 
        else:
            print("Neispravan unos")
