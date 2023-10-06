# docker-django-gunicorn-nginx

###### This docker container is intended to run with a remote postgres database, or failing that, with sqlite.
###### If you want to run the container with postgres, [THIS](https://github.com/ezevic/docker-postgres-django-gunicorn-nginx) following repository is what you are looking for.

## Prerequisites

Make sure you have the following requirements installed before proceeding:

- Docker: [Docker Installation](https://docs.docker.com/get-docker/)
- Docker Compose: [Docker Compose Installation](https://docs.docker.com/compose/install/)

## Configuration

1. Clone this repository on your local machine:
 ```shell
git clone https://github.com/ezevic/docker-django-gunicorn-nginx.git
```

2. Configure your environment variables. Copy the example environment file `create-.env.prod-here` and rename it to `.env.prod`. Modify the variables in `.env.prod` with the appropriate values.

## Usage

1. Start your services using Docker Compose:
```shell
docker-compose -f docker-compose.prod-no-db.yml up -d
```

This will build Docker images, run containers, and start your application.

2. To stop the services, you can use:
 ```shell
docker-compose -f .\docker-compose.prod-no-db.yml down
```

3. If you want to run a command, you can use:
```shell
sudo docker-compose -f docker-compose.prod-no-db.yml run web python manage.py migrate
```

## Accessing the Application
- Your application will be available at http://localhost.
- Static files are automatically served through Nginx on port 80.

## Contribution
If you wish to contribute to this project, follow the standard contribution steps:

1. Fork the repository.
2. Create a new branch for your contribution: git checkout -b my-contribution.
3. Make your changes and commit: git commit -m "Added a new feature".
4. Push to your branch: git push origin my-contribution.
5. Create a pull request on GitHub.