"""
Jenkins settings file
"""
from base import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

INSTALLED_APPS = INSTALLED_APPS + ('django_jenkins',)

JENKINS_TASKS = (
    'django_jenkins.tasks.run_pep8',
    'django_jenkins.tasks.run_pyflakes',
    # 'django_jenkins.tasks.run_jshint',
    #'django_jenkins.tasks.run_csslint',
    'django_jenkins.tasks.run_sloccount'
)
