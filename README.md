
# Welcome to SPA Admin.

##### How to install ? 
1. You have to have docker and docker-compose installed.
2. In your terminal put "export COMPOSE_FILE=local.yml" for run the project in a local envioroment.
3. Run docker-compose up --build.
4. Run (in a terminal with COMPOSE_FILE configured) docker-compose exec app ./manage.py migrate
5. Now the project is running in your localhost:8000! :D
