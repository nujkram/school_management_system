import os
import random
import string

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
USERNAME_REGEX = "^[a-zA-Z0-9.-]*$"

try:
    with open(os.path.join(BASE_DIR, 'ADMIN_URL')) as f:
        ADMIN_URL = f.read().strip()
except FileNotFoundError:   
    generated_key = ''.join(random.choice(string.ascii_lowercase) for i in range(50))
    secret = open(os.path.join(BASE_DIR, 'ADMIN_URL'), 'w')
    secret.write(generated_key)
    secret.close()
    ADMIN_URdL = generated_key

SUPERADMIN = 'SU'
ADMIN = 'ADM'
USER = 'USR'
FACULTY = 'FCT'
STUDENT = 'STD'

USER_TYPE_CHOICES = (
    (ADMIN, 'Admin'),
    (FACULTY, 'Faculty'),
    (STUDENT, 'Student'),
)

USER_DASHBOARD_ROOTS = {
    SUPERADMIN: ADMIN_URL,
    ADMIN: 'admin',
    USER: 'user',
    FACULTY: 'faculty',
    STUDENT: 'student',
}
