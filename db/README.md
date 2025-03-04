
Préparer l'environnement
```
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

Démarrer une base MariaDB
```
docker run --name db --rm -e MYSQL_ROOT_PASSWORD=my-secret-pw -e MYSQL_USER=user -e MYSQL_PASSWORD=pass -e MYSQL_DATABASE=db  -p 3306:3306  mysql
```