# wallet-api
Uses sqlite3 database

To run:

pip install -r requirements.txt

python manage.py makemigrations
python manage.py migrate


python manage.py runserver

To insert initial user:
sqlite3
.tables #should display all the tables after migration
insert into walletapi_user (user_id, name, phone) values ('124','testuser',9999999999);

API collection: https://www.getpostman.com/collections/d9a16c0254796503ab7f 