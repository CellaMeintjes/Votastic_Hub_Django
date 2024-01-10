# Votastic Hub Django

Votastic Hub Django is a web application built with Django, providing a platform for users to participate in polls and voting.

## Description

Votastic Hub Django allows users to create and participate in polls on various topics. Users can register, log in, and cast their votes in different polls. The application provides a clean and user-friendly interface for an engaging voting experience.

## Table of Contents

- [Prerequisites](#prerequisites)
- [Getting Started](#getting-started)
  - [Running with venv](#running-with-venv)
  - [Running with Docker](#running-with-docker)
- [Configuration](#configuration)
  - [Environment Variables](#environment-variables)
  - [Acquiring Secrets](#acquiring-secrets)
- [Usage](#usage)
- [Contributing](#contributing)

## Prerequisites

- Python 3.x
- Docker (if you prefer running the app in a container)

## Getting Started

### Running with venv

1. Clone the repository:

    ```bash
    git clone https://github.com/your-username/votastic-hub-django.git
    cd votastic-hub-django
    ```

2. Create and activate a virtual environment:

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Apply database migrations:

    ```bash
    python manage.py migrate
    ```

5. Create a superuser:

    ```bash
    python manage.py createsuperuser
    ```

6. Run the development server:

    ```bash
    python manage.py runserver
    ```

   Your application will be accessible at http://127.0.0.1:8000/.

### Running with Docker

1. Clone the repository:

    ```bash
    git clone https://github.com/your-username/votastic-hub-django.git
    cd votastic-hub-django
    ```

2. Build the Docker image:

    ```bash
    docker build -t votastic-hub-django .
    ```

3. Run the Docker container:

    ```bash
    docker run -p 8000:8000 votastic-hub-django
    ```

   Your application will be accessible at http://127.0.0.1:8000/.

## Configuration

### Environment Variables

- `SECRET_KEY`: Django secret key. You can generate one [here](https://djecrety.ir/).
- `DEBUG`: Set to `True` for development, `False` for production.
- `DJANGO_DB_HOST`, `DJANGO_DB_PORT`, `DJANGO_DB_NAME`, `DJANGO_DB_USER`, `DJANGO_DB_PASSWORD`: Database connection details.

### Acquiring Secrets

1. Create a file named `.env` in the project root.
2. Add the following content, replacing placeholders:

    ```env
    SECRET_KEY=your_secret_key
    DEBUG=True
    DJANGO_DB_HOST=db_host
    DJANGO_DB_PORT=db_port
    DJANGO_DB_NAME=db_name
    DJANGO_DB_USER=db_user
    DJANGO_DB_PASSWORD=db_password
    ```

   Make sure to keep your `.env` file secure and don't commit it to version control.

## Usage

...

## Contributing

...

