import multiprocessing

# Gunicorn config variables
bind = '0.0.0.0:8000'
workers = multiprocessing.cpu_count() * 2 + 1
worker_class = 'gthread'
threads = 2

# Django app config variables
pythonpath = '/app'
chdir = '/app'
module = 'testProject.wsgi:application'
