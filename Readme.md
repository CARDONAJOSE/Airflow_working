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

### 1. Configuration de l'environnement virtuel
```bash
# Créer l'environnement virtuel
python -m venv .venv

# Activer l'environnement virtuel
# Windows
.venv\Scripts\activate
# Linux/MacOS
source .venv/bin/activate
```

### 2. Installation des dépendances
```bash
# Installer les dépendances
pip install -r requirements.txt

# Pour mettre à jour requirements.txt
pip freeze > requirements.txt
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


## Licence
[Spécifiez votre licence ici]