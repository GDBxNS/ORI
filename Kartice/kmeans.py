import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import  KMeans
import sys
#iscrtavanje tacaka
def iscrtavanje(x, y, kmeans, unos, x1, x2, xlabel, ylabel):

    # Lista predefinisanih boja
    colmap = np.array(['red',
                       '#0195e5',
                       '#bba740',
                       'darkgrey',
                       'green',
                       '#3cd1ac',
                       '#bd53d6',
                       '#76f29d',
                       '#d4a045',
                       '#3fc64b',
                       '#672558',
                       '#390b1b',
                       '#2fc8fa',
                       '#374e3c',
                       '#88ece2'
                       ])

    #Iscrtavanje tacaka
    fig, ax = plt.subplots()
    ax.scatter(x=x, y=y, color=colmap[kmeans.labels_])
    ax.set_ylabel(ylabel)
    ax.set_xlabel(xlabel)

    labels = kmeans.labels_

    indeksi = []
    for i in list(labels):
        if(i not in indeksi):
            indeksi.append(i)

    labele = ['Uvek malo potrose do 5 000', 'Cesta, ali skupa kupovina(>10 000)', 'Cesta kupovina od 5 000 do 10 000']


    #iscrtavanje centroida klastera
    brojac = 0
    for i in kmeans.cluster_centers_:
        lista = []
        counter = 0
        for item in i:
            if(counter == x1):
                lista.append((item))
            if (counter == x2):
                lista.append((item))

            counter+=1

        ax.scatter([],[], color=colmap[indeksi[brojac]], label=labele[indeksi[brojac]])
        ax.legend()
        # ax.scatter(*lista, color='black')
        brojac+=1


    plt.show()


# k - broj klastera
def ucitavanje(k):
    # Ucitavanje podataka iz fajla
    podaci = pd.read_csv("credit_card_data.csv")

    # Zamenjuje prazna polja nulama
    podaci.fillna(0, inplace=True)
    x = pd.DataFrame(podaci)

    kmeans = KMeans(n_clusters=k, max_iter=100, random_state=5)

    # Uzimamo sve iz tabele sem CUST_ID
    kmeans.fit(x.iloc[:, 1:])
    return kmeans, x


if __name__ == '__main__':

    unos = ''
    while(True):
        print('\n')
        print("MENI:")
        print("1. GRAFIK PURCHASES-PURCHASES_FREQUENCY")
        print('X  ZA IZLAZ')
        unos = input(">> ")
        if(unos == '1'):
            kmeans, x = ucitavanje(3)
            iscrtavanje(x.PURCHASES, x.PURCHASES_FREQUENCY, kmeans, unos, 3, 7, 'PURCHASES', 'PURCHASES_FREQUENCY')
        elif(unos == 'x' or unos == 'X'):
            print("Dovidjenja")
            sys.exit() 
        else:
            print("Neispravan unos")