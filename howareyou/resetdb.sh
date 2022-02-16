rm db.sqlite3
./manage.py migrate
./manage.py createsuperuser --username admin --email "abc@abc.com"
