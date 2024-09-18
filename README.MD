# API HighCast

Cette API permet de calculer l'empreinte carbone en fonction de la consommation d'électricité (exprimée en kWh) et du pays, en utilisant FastAPI.

## Installation et exécution

### Prérequis

- [Git](https://git-scm.com/)
- [Python 3.8+](https://www.python.org/downloads/)
- [FastAPI](https://fastapi.tiangolo.com/)

### Étapes d'installation.

#### 1. Cloner le projet.

Dans votre terminal, exécutez la commande suivante pour cloner le projet depuis GitHub :

```bash
git clone git@github.com:belkacem-oussama/api-highcast.git
```

#### 2. Installer les dépendances.

Accédez au répertoire cloné et installez les dépendances nécessaires :

```
cd api-highcast
pip install -r requirements.txt
```

#### 3. Configurer les variables d'environnement.

Créez un fichier .env dans le répertoire racine du projet et ajoutez vos configurations, telles que l'URL de l'API et les clés API.

```
CARBON_API_URL=<url_de_l_api>
CARBON_API_KEY=<cle_de_l_api>
```

#### 4. Lancer le projet.

Pour exécuter le serveur FastAPI, utilisez cette commande :

`fastapi run main.py`

Le serveur sera lancé sur http://localhost:8000.

## Utilisation de l'API

Vous pouvez utiliser un outil comme Postman pour tester l'API.

#### 1. Endpoint

L'API expose un endpoint pour calculer l'empreinte carbone :

`POST http://localhost:8000/calculate`

#### 2. Exemple de requête

Dans l'onglet "Body" de Postman, sélectionnez "raw" et choisissez le format JSON. Vous devez passer un objet similaire à celui-ci :

```json
{
  "type": "electricity",
  "electricity_unit": "kwh",
  "electricity_value": 1000,
  "country": "fr"
}
```

#### 3. Description des champs

`type` : Le type de consommation, ici "electricity".

`electricity_unit` : L'unité de consommation électrique (par exemple, "kwh").

`electricity_value` : La valeur de la consommation (par exemple, 1000 kWh).

`country` : Le code du pays (par exemple, "fr" pour la France).

#### 4. Réponse

L'API renverra une réponse avec l'empreinte carbone calculée en fonction des données fournies :

```json
{
  "message": "Voici votre empreinte carbone.",
  "emission_carbone": 55.0,
  "unité": "kgCO2e"
}
```

## Test

Les tests unitaires pour ce projet sont disponibles dans le répertoire test. Vous pouvez les exécuter avec la commande suivante :

`python3 -m pytest`
