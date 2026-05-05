# FUSS
File Upload Software System - FUSS

## Getting Started ##
For this project, Django is run with PostgreSQL in a Docker container. 
<br/>_Assumes you have PostgreSQL up and running._

### First Time - Docker Build
1. Clone the repo
<br/>`git clone https://github.com/adalysg/FUSS.git`

3. Navigate to the backend folder
<br/>`cd FUSS_Django_Backend`

4. Copy the required fields of the `.env` file using the `.env.example` template file and fill in your own values
<br/>`cp .env.example .env  `

5. Build the docker image
<br/>`docker compose up --build`

### Daily Workflow
`git pull && docker compose up` to start container and run server

<br/>OR...
<br/>`git pull && docker compuse up --build` whenever a package is added to `requirements.txt`

<br/>_*make changes and push to the repo*_

`docker compose down` when logging off for the day

### Testing with Pytest Inside the Container
1. Navigate to the `FUSS_Django_Backend` Folder
2. Run the following command:
<br/> `docker exec -it fuss_django_backend-django-web-1 pytest path_to_test_file`

### Useful Commands to Run Inside the Container
<br/>`docker compose logs django-web`
<br/>`docker compose exec django-web python manage.py makemigrations`
<br/>`docker compose exec django-web python manage.py migrate`
<br/>`docker compose exec django-web python manage.py createsuperuser`
<br/>`docker compose exec django-web python manage.py shell`