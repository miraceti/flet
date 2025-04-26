
import requests
import matplotlib.pyplot as plt
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

print(planetes_tries_sy_dist[0:10])

#data année de decouverte
planetes_avec_annee = [p for p in data_table_dict if p['disc_year'] is not None]
planetes_tries_disc_year = sorted(    planetes_avec_annee,     key=lambda x: (x.get('disc_year') is None, x.get('disc_year') if x.get('disc_year') is not None else float('inf')))

    