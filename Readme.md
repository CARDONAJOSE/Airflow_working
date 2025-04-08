# Project Airflow avec Docker

## 📋 Table des matières
- [Prérequis](#prérequis)
- [Installation](#installation)
- [Configuration de l'environnement](#configuration-de-lenvironnement)
- [Utilisation](#utilisation)
- [Structure du projet](#structure-du-projet)
- [Dépannage](#dépannage)

## Prérequis
- Python 3.8 ou supérieur
- Docker Desktop
- Git

## Installation

### 1. Cloner le projet
```bash
git clone [URL_DU_REPO]
cd [NOM_DU_PROJET]
```

### 2. Configuration de l'environnement virtuel
```bash
# Créer l'environnement virtuel
python -m venv .venv

# Activer l'environnement virtuel
# Windows
.venv\Scripts\activate
# Linux/MacOS
source .venv/bin/activate
```

### 3. Installation des dépendances
```bash
# Installer les dépendances
pip install -r requirements.txt

# Pour mettre à jour requirements.txt
pip freeze > requirements.txt
```

## Configuration de l'environnement

### Variables d'environnement
Créez un fichier `.env` à la racine du projet avec les variables suivantes :
```env
AIRFLOW_UID=50000
AIRFLOW_GID=50000
```

## Utilisation

### Démarrer les services
```bash
# Démarrer tous les conteneurs
docker-compose up -d
```

Les services suivants seront disponibles :
- Airflow Webserver: http://localhost:8080
- Airflow Scheduler
- Airflow Worker (si Celery est configuré)
- Base de données PostgreSQL

### Arrêter les services
```bash
docker-compose down
```

## Structure du projet
```
project_airflow/
├── dags/                  # Dossier contenant vos DAGs Airflow
├── logs/                  # Logs Airflow
├── plugins/              # Plugins personnalisés
├── .env                  # Variables d'environnement
├── docker-compose.yml    # Configuration Docker
└── requirements.txt      # Dépendances Python
```

## Dépannage

### Problèmes courants

1. **Docker Desktop ne démarre pas**
   - Vérifiez que Docker Desktop est installé
   - Redémarrez Docker Desktop
   - Vérifiez les logs Docker

2. **Erreurs de connexion à la base de données**
   - Vérifiez que PostgreSQL est en cours d'exécution
   - Vérifiez les variables d'environnement

3. **Problèmes avec l'environnement virtuel**
   - Supprimez le dossier `.venv` et recréez-le
   - Réinstallez les dépendances

### Commandes utiles
```bash
# Vérifier l'état des conteneurs
docker-compose ps

# Voir les logs
docker-compose logs -f

# Redémarrer un service spécifique
docker-compose restart [service_name]
```

## Contribution
1. Fork le projet
2. Créez une branche pour votre fonctionnalité
3. Committez vos changements
4. Poussez vers la branche
5. Ouvrez une Pull Request

## Licence
[Spécifiez votre licence ici]