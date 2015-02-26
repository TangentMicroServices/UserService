[![Build Status](http://jenkins.tangentme.com/buildStatus/icon?job=Build UserService)](http://jenkins.tangentme.com/view/MicroServices/job/Build%20UserService/)
[![Documentation Status](https://readthedocs.org/projects/userservice/badge/?version=latest)](https://readthedocs.org/projects/userservice/?badge=latest)

# User Service


User management service authenticates users for all the other micro services projects. 

The documentation is hosted at [http://userservice.readthedocs.org/en/latest/]()

## Setting Up

1. Start and activate environment
		
		virtualenv env
		source env/bin/activate

1. Run the requirements 

		pip install -r requirements.txt
		
1. Install the database

		python manage.py syncdb
		
1. Run the initial data (if required - this is test data only)

		python manage.py loaddata data/initial.json

1. Run the tests to ensure the project is up and running correctly

		python manage.py test
		
## Build the Docs

### Run the requirements

	pip install -r requirements-dev.txt
	
### Manually Build the Docs

    cd docs     
    make html

### Auto Build the Docs as you Edit

	cd docs
	sphinx-autobuild source build/html -p3000
