# FUSS
File Upload Software System - FUSS

## Getting Started ##
For this project, Django is run with PostgreSQL in a Docker container. 
<br/>_Assumes you have PostgreSQL up and running._

### First Time - Docker Build to Run Django Server
1. Clone the repo
<br/>`git clone https://github.com/adalysg/FUSS.git`

3. Navigate to the backend folder
<br/>`cd FUSS_Django_Backend`

4. Copy the required fields of the `.env` file using the `.env.example` template file and fill in your own values
<br/>`cp .env.example .env  `

5. Build the docker image
<br/>`docker compose up --build`

### Daily Workflow
1. `git pull && docker compose up` to start container and run server
2. `git pull && docker compuse up --build` whenever a package is added to `requirements.txt`
3. `docker compose down` when logging off for the day
