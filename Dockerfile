# Utilisez une image de base appropriée pour votre application Django
FROM python:3.9

# Définissez le répertoire de travail
WORKDIR /app

# Installez les dépendances de l'application Django
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Installez MariaDB
RUN apt-get update && apt-get install -y mariadb-server

# Copiez les fichiers de configuration de la base de données
COPY my.cnf /etc/mysql/my.cnf

# Copiez le reste de votre application
COPY . /app/

# Exposez le port de la base de données
EXPOSE 3306

# Démarrez la base de données MariaDB
CMD ["mysqld"]
