python manage.py migrate
sqlite3 db.sql -init db\sqlite-sakila-schema.sql
sqlite3 db.sql -init db\sqlite-sakila-insert-data.sql.sql