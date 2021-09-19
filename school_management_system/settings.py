import os
from split_settings.tools import include

try:
    with open('school_management_system/ENV') as f:
        ENV = f.read().strip()
except FileNotFoundError:
    ENV = 'prod'
    env_file = open('school_management_system/ENV', 'w')
    env_file.write(ENV)
    env_file.close()

include('apps.py')
include(f'environments/{ENV}.py')
