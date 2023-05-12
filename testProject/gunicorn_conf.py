import multiprocessing
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print(f">>>. Setting chdir value to {BASE_DIR}")

# Gunicorn config variables
bind = '0.0.0.0:8000'
workers = multiprocessing.cpu_count() * 2 + 1
worker_class = 'gthread'
threads = 2

# Django app config variables
pythonpath = BASE_DIR
chdir = BASE_DIR
module = 'workspace.testProjct.wsgi:application'
print(f">>>. Setting module value to {module}")
