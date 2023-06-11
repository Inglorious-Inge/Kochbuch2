# Kochbuch2

Requirements:

    * Python 3 (Tested with 3.9.6)
    * SQLite 3
___

Getting started:

1. Create virtualenv:
```bash
python3 -m venv venv
```
2. Activate virtualenv
```bash
source venv/bin/activate
```
3. Apply migrations
```
python manage.py migrate
```
4. Run server
```
python manage.py runserver
```
5. Create superuser
```
python manage.py createsuperuser
```

You can now log in at http://localhost:8000/admin/.
To access the API visit http://localhost:8000/.


API endpoints:

* /recipes
* /recipes/{id}
* /recipes/search
* /favorites
* /shoppinglists
* /shoppinglists/{id}



