Getting Started with the UserService 
=====================================

**Base URL:** http://userservice.tangentme.com

Getting an auth token
----------------------

    curl -X POST http://127.0.0.1:8000/ -d

Authorizing with an auth token
-------------------------------

To identify yourself in consequent requests, set the `Authorization` header like below:

    curl -X GET http://127.0.0.1:8000/api/example/ -H 'Authorization: Token 9944b09199c62bcf9418ad846dd0e4bbdfc6ee4b'
