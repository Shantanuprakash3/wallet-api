# wallet-api
Uses sqlite3 database

To run:

# virtual env
source venv/bin/activate

pip install -r requirements.txt

python manage.py makemigrations
python manage.py migrate

# To run single process server:
python manage.py runserver

# To run multi process server on uwsgi:
uwsgi --http 127.0.0.1:3031 --chdir /Users/shantanuprakash/Code/myWallet/myWallet --wsgi-file myWallet/wsgi.py --master --processes 4 --threads 2 --stats 127.0.0.1:9191

# To test parallel requests:

xargs -I % -P 8 curl -X POST \
  http://127.0.0.1:3031/transaction/credit \
  -H 'cache-control: no-cache' \
  -H 'content-type: application/json' \
  -d '{
	"wallet_id" : 20,
	"amount" : 100
}' < <(printf '%s\n' {1..400})


# To insert initial user:
sqlite3
.tables 
# should display all the tables after migration
insert into walletapi_user (user_id, name, phone) values ('124','testuser',9999999999);

# Port number needs to be changed to 3031 if using above uwsgi command
API collection: https://www.getpostman.com/collections/d9a16c0254796503ab7f 