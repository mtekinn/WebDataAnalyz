# WebDataAnalyz

WebDataAnalyz is a web application developed using Django and Scrapy, designed to crawl and analyze websites based on user input. 

## Features

- Simple and user-friendly web interface
- Efficient web crawling using Scrapy
- Integration with Django for managing and displaying crawl results
- Asynchronous task processing with Celery and Redis
- Test-driven development approach
- Git version control and CI/CD with GitHub Actions

## Installation and Setup

1. Clone the repository: https://github.com/mtekinn/WebDataAnalyz.git
cd WebDataAnalyz

2. Create a virtual environment and activate it: python -m venv venv  source venv/bin/activate

3. Install the required packages: pip install -r requirements.txt

4. Apply migrations: python manage.py migrate

5. Run the Redis server: redis-server

6. Start the Celery worker: celery -A WebDataAnalyz worker --loglevel=info

7. Start the Django development server: python manage.py runserver

8. Visit `http://127.0.0.1:8000/` in your web browser to use the application.

## Running Tests

To run the test suite, execute the following command: python manage.py test









