import multiprocessing
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print(f">>>. setting chmod to {BASE_DIR}")

# Gunicorn config variables
bind = '0.0.0.0:8000'
workers = multiprocessing.cpu_count() * 2 + 1
worker_class = 'gthread'
threads = 2

# Django app config variables
pythonpath = '/home/sarvesh_jain_96742/testProject'
chdir = BASE_DIR
module = BASE_DIR