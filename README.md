Lets encrypt SSL
Non-root for web, db, and nginx

Add logout
Add signup

Flush tables for a clean slate:
python manage.py flush --no-input

Build without caching:
docker build --no-cache -t customer-data:TEST .

Create virtual network:
docker network create my-django-postgres-network

Loging to postgres:
psql -U your_admin_username -d your_database_name -h your_host

Setup dev db and user:
CREATE USER testuser WITH PASSWORD 'dragon';
CREATE DATABASE testdb OWNER testuser;
GRANT ALL PRIVILEGES ON DATABASE testdb TO testuser;


Run postgres:
docker run --name my-postgres -p 5432:5432 --rm --env-file .env.db --network my-django-postgres-network -v postgres-data:/var/lib/postgresql/data -d postgres:17.2-alpine3.21

Run application:
docker run --name customer-data --rm --env-file .env -p 8000:8000 --network my-django-postgres-network -d customer-data:TEST


 docker-compose up -d --build
 docker-compose down
