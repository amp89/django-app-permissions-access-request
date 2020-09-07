from setuptools import (
    setup,
    find_packages,
)



setup(
    name='django-app-permissions-access-request',
    version='0.0.5',
    url='https://github.com/amp89/django-app-permissions-access-request',
    download_url="https://github.com/amp89/django-app-permissions-access-request/blob/master/dist/django-app-permissions-access-request-0.0.5.tar.gz",
    license='MIT',
    description='App level authentication management for django, with access requests and approvals',
    long_description=open('README.rst', 'r', encoding='utf-8').read(),
    author='Alex Peterson',
    author_email='contact@alexpeterson.tech',
    install_requires=[
        'django',
        'djangorestframework',
        'django-drf-advanced-token',
        'django-app-permissions',
    ],
    python_requires='>=3.6',
    
)
