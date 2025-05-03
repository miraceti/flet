
import requests
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

##########################################
#code de recuperation des données externes
urlexo_pllist = "https://exoplanetarchive.ipac.caltech.edu/TAP/sync?query=select+distinct+\
pl_name,disc_year,sy_dist,discoverymethod,pl_bmasse,pl_rade,pl_orbper,pl_eqt,pl_dens\
+from+ps+&format=json"
response = requests.get(urlexo_pllist)
data_pllist = response.json()
#######################
#### ECRAN1
#######################
data_nbpl = list({(item['pl_name']) for item in data_pllist})
nb_exoplanets= len(data_nbpl)

# Regrouper par 'pl_name' et garder les valeurs maximales pour les autres colonnes
aggregated_data = {}
for row in data_pllist:
    pl_name = row['pl_name']
    if pl_name not in aggregated_data:
        aggregated_data[pl_name] = row
    else:
        for key in row:
            if key != 'pl_name' and row[key] is not None:
                # Conserver la valeur maximale pour les autres colonnes
                aggregated_data[pl_name][key] = max(aggregated_data[pl_name][key], row[key]) if aggregated_data[pl_name][key] is not None else row[key]

# Convertir en une liste de tuples pour MDDataTable
data_table_tuple = [
    (row['pl_name'], row['disc_year'], row['sy_dist'], row['discoverymethod'], row['pl_bmasse'], row['pl_rade'], row['pl_orbper'], row['pl_eqt'], row['pl_dens'])
    for row in aggregated_data.values()
]    

#cle associés
keys = ["pl_name","disc_year","sy_dist","discoverymethod","pl_bmasse","pl_rade","pl_orbper","pl_eqt","pl_dense"]

#conversion en liste de dict
data_table_dict = [dict(zip(keys, tpl)) for tpl in data_table_tuple]

#extraction des tuples (pl_name, disc_year) sans doublons
unique_data = list(set(map(lambda x: (x['pl_name'], x['disc_year']), data_table_dict)))

#creation du comptage par année
from collections import Counter
#comptage decouverte par annee
discovery_counts = Counter(item['disc_year'] for item in data_table_dict)
#tri par annee
sorted_discovery_counts = sorted(discovery_counts.items())

#separation resultat en 2 listes
liste_annee, liste_nb = zip(*sorted_discovery_counts)

liste_annee = list(liste_annee)
liste_nb = list(liste_nb)

#########
#comptage des ocurence
discovery_methods = [item['discoverymethod'] for item in data_table_dict]
method_counts = Counter(discovery_methods)

#preparation données
labels = list(method_counts.keys())
counts = list(method_counts.values())

#palette de couleurs pour les barres
colors_barres = plt.cm.Paired.colors[:len(labels)]



#
# Remplacer les valeurs None pour pl_rade par une valeur par défaut
for item in data_table_dict:
    if item['pl_rade'] is None:
        item['pl_rade'] = 1  # Remplacez par une valeur par défaut

# Extraire les données
x = [item['sy_dist'] for item in data_table_dict]
y = [item['pl_bmasse'] for item in data_table_dict]
sizes = [item['pl_rade'] * 10 for item in data_table_dict]  # Ajuster la taille des points
methods = [item['discoverymethod'] for item in data_table_dict]

# Générer une palette de couleurs pour les méthodes
unique_methods = list(set(methods))
colors_methods = {method: plt.cm.tab10(i) for i, method in enumerate(unique_methods)}

#data distances
planetes_avec_distance = [p for p in data_table_dict if p['sy_dist'] is not None]
planetes_tries_sy_dist = sorted(    planetes_avec_distance,     key=lambda x: (x.get('sy_dist') is None, x.get('sy_dist') if x.get('sy_dist') is not None else float('inf')))


#data année de decouverte
planetes_avec_annee = [p for p in data_table_dict if p['disc_year'] is not None]
planetes_tries_disc_year = sorted(    planetes_avec_annee,     key=lambda x: (x.get('disc_year') is None, x.get('disc_year') if x.get('disc_year') is not None else float('inf')))

#data rayon
planetes_avec_rayon = [p for p in data_table_dict if p['pl_rade'] is not None]
planetes_tries_pl_rade = sorted(    planetes_avec_rayon,     key=lambda x: (x.get('pl_rade') is None, x.get('pl_rade') if x.get('pl_rade') is not None else float('inf')))

#data masse
planetes_avec_masse = [p for p in data_table_dict if p['pl_bmasse'] is not None]
planetes_tries_pl_masse = sorted(    planetes_avec_masse,     key=lambda x: (x.get('pl_bmasse') is None, x.get('pl_bmasse') if x.get('pl_bmasse') is not None else float('inf')))

#data densite
planetes_avec_densite = [p for p in data_table_dict if p['pl_dense'] is not None]
planetes_tries_pl_dense = sorted(    planetes_avec_densite,     key=lambda x: (x.get('pl_dense') is None, x.get('pl_dense') if x.get('pl_dense') is not None else float('inf')))

#data temperature
planetes_avec_temperature = [p for p in data_table_dict if p['pl_eqt'] is not None]
planetes_tries_pl_temperature = sorted(    planetes_avec_temperature,     key=lambda x: (x.get('pl_eqt') is None, x.get('pl_eqt') if x.get('pl_eqt') is not None else float('inf')))

#data temperature
planetes_avec_periode = [p for p in data_table_dict if p['pl_eqt'] is not None]
planetes_tries_pl_orbper = sorted(    planetes_avec_periode,     key=lambda x: (x.get('pl_orbper') is None, x.get('pl_orbper') if x.get('pl_orbper') is not None else float('inf')))

#data methode
planetes_avec_methode = [p for p in data_table_dict if p['discoverymethod'] is not None]
planetes_tries_discoverymethod = sorted(    planetes_avec_methode,     key=lambda x: (x.get('discoverymethod') is None, x.get('discoverymethod') if x.get('discoverymethod') is not None else ''))

print(planetes_tries_discoverymethod[0:10])        

#pour graphique nombre de planetes par methode et par période
data_nb_planete_methode_periode = data_table_dict

# Convertir en DataFrame
df = pd.DataFrame(data_nb_planete_methode_periode)

# Définir les tranches d'années
bins = list(range(1990, 2026, 5))  # de 1990 à 2025 tous les 5 ans
labels_tra = [f"{bins[i]}-{bins[i+1]}" for i in range(len(bins)-1)]

# Ajouter une colonne pour la tranche d'années
df['year_bin'] = pd.cut(df['disc_year'], bins=bins, labels=labels_tra, right=False)

# Filtrer les données si besoin
df = df.dropna(subset=['year_bin', 'discoverymethod'])  # enlever les données sans année ou méthode

# Grouper
grouped = df.groupby(['year_bin', 'discoverymethod'],observed=False).size().unstack(fill_value=0)

print(grouped)



########################################PAGE 4
# Liste des planètes
planets42 = data_table_dict

# Convertir la liste en DataFrame
df4 = pd.DataFrame(planets42)

# Filtrer les planètes ayant une valeur 'none' ou 1 dans la colonne 'pl_bmasse'
df4_filtered = df4[(df4['pl_bmasse'] != 'none') & ((df4['pl_bmasse'] >= 0.99) & (df4['pl_bmasse'] <= 1.01)) & (df4['pl_bmasse'] > 0.00) & (df4['pl_bmasse'] < 1000.00)].copy()
df4_filtered_moins1 = df4[(df4['pl_bmasse'] != 'none') &  (df4['pl_bmasse'] > 0.00) & (df4['pl_bmasse'] < 1000.00)].copy()

# Convertir 'pl_bmasse' en type numérique si nécessaire
df4_filtered.loc[:, 'pl_bmasse'] = pd.to_numeric(df4_filtered['pl_bmasse'], errors='coerce')
df4_filtered_moins1.loc[:, 'pl_bmasse'] = pd.to_numeric(df4_filtered_moins1['pl_bmasse'], errors='coerce')

# Définir les tranches
bins4 = [0, 2, 4, 6, 8, 10, 12]
labels4 = ['0-2', '2-4', '4-6', '6-8', '8-10','10-12']

# Diviser les données en tranches
df4_filtered.loc[:, 'mass_bin'] = pd.cut(df4_filtered['pl_bmasse'], bins=bins4, labels=labels4, include_lowest=True)
df4_filtered_moins1.loc[:, 'mass_bin'] = pd.cut(df4_filtered_moins1['pl_bmasse'], bins=bins4, labels=labels4, include_lowest=True)

# Compter le nombre de planètes dans chaque tranche
bin4_counts = df4_filtered['mass_bin'].value_counts().sort_index()
bin4_counts_moins1 = df4_filtered_moins1['mass_bin'].value_counts().sort_index()


print("Nombre de planètes avec masse = 1 :", len(df4[(df4['pl_bmasse'] >= 0.90) & (df4['pl_bmasse'] <= 1.10)]))
print("Graphique 1 (sans 1T) :\n", bin4_counts)
print("Graphique 2 (avec 1T) :\n", bin4_counts_moins1)
print(df4['pl_bmasse'].sort_values().unique()[0:20])  # voir les plus petites
print(df4['pl_bmasse'].sort_values().unique()[-20:]) # voir les plus grandes
print(df4[df4['pl_bmasse'] < 2]['pl_bmasse'].sort_values())


#masse
# Liste des planètes
planets43 = data_table_dict

# Convertir la liste en DataFrame
df43 = pd.DataFrame(planets43)

# Filtrer les planètes ayant une valeur 'none' ou 1 dans la colonne 'pl_bmasse'
df43_filtered = df43[(df43['pl_rade'] != 'none') & ((df43['pl_rade'] >= 0.99) & (df43['pl_rade'] <= 1.01)) & (df43['pl_rade'] > 0.00) & (df43['pl_rade'] < 1000.00)].copy()

# Convertir 'pl_bmasse' en type numérique si nécessaire
df43_filtered.loc[:, 'pl_rade'] = pd.to_numeric(df43_filtered['pl_rade'], errors='coerce')

# Définir les tranches
bins43 = [0, 2, 4, 6, 8, 10, 12]
labels43 = ['0-2', '2-4', '4-6', '6-8', '8-10','10-12']

# Diviser les données en tranches
df43_filtered.loc[:, 'rade_bin'] = pd.cut(df43_filtered['pl_rade'], bins=bins43, labels=labels43, include_lowest=True)

# Compter le nombre de planètes dans chaque tranche
bin43_counts = df43_filtered['rade_bin'].value_counts().sort_index()

print("MASSE")
print(df43['pl_rade'].sort_values().unique()[0:20])  # voir les plus petites
print(df43['pl_rade'].sort_values().unique()[-20:]) # voir les plus grandes

###########page 1
###PIE amber

#TABLEAU purple
planetes_tries_sy_dist = sorted(
    planetes_avec_distance,
    key=lambda x: (x.get('sy_dist') is None, x.get('sy_dist') if x.get('sy_dist') is not None else float('inf'))
)

plus_proches_planetes = planetes_tries_sy_dist[:5]

