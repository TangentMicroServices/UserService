[![Build Status](http://jenkins.tangentme.com/buildStatus/icon?job=Build UserService)](http://jenkins.tangentme.com/view/MicroServices/job/Build%20UserService/)

# User Service


User management service authenticates users for all the other micro services projects.

## Setting Up

1. Start and activate environment
		
		Virtualenv env
		source env/bin/activate

1. Run the requirements 

		pip install -r requirements.txt
		
1. Install the database

		python manage.py syncdb

1. Run the tests to ensure the project is up and running correctly

		python manage.py test