#!/bin/bash
celery -A school_management_system worker --loglevel=debug --logfile=/school_management_system/logs/celery.log
