# How-Are-You

# Setup

- make a virtual enviroment.

- `pip install -r requirements.txt`

# Run

```
cd howareyou
python manage.py runserver
```

# Run using run.sh

```
chmod +x run.sh
./run.sh
```

# Using Data pump

- first uncomment the part you want to add to database

- put relevant data

```
python manage.py shell < data_pump.py
```

# Deleting the whole database ( If above fails)

```
python manage.py flush
python manage.py shell < data_pump.py
python manage.py createsuperuser --username admin --email "abc@abc.com"

```

# To-Do

- Test Inputs by moderator
- Patient can submit test
- Psychiatrist can varify test
- Patient can see test

