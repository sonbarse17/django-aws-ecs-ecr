# Hello World Django Application

A simple Hello World application built with Django and Docker.

## Setup Instructions

1. Build the Docker image:
```bash
docker build -t hello-world-django .
```

2. Run the container:
```bash
docker run -p 8000:8000 hello-world-django
```

3. Access the application:
Open your browser and navigate to `http://localhost:8000`

## Development Setup

If you want to run the application locally without Docker:

1. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the development server:
```bash
python manage.py runserver
```

4. Access the application:
Open your browser and navigate to `http://localhost:8000` 