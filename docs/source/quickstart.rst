Getting Started with the UserService 
=====================================

**URLS**

* **Production:** http://userservice.tangentme.com
* **Staging:** http://staging.userservice.tangentme.com

Getting an auth token
----------------------
**Request**::

    curl -X POST http://127.0.0.1:8000/api-token-auth/ -d username=joe&password=test

Authorizing with an auth token
-------------------------------

To identify yourself in consequent requests, set the `Authorization` header like below::

    curl -X GET http://127.0.0.1:8000/api/example/ -H 'Authorization: Token 9944b09199c62bcf9418ad846dd0e4bbdfc6ee4b'
