Getting Started with the UserService 
=====================================

**URLS**

* **Production:** http://userservice.tangentme.com
* **Staging:** http://staging.userservice.tangentme.com

Getting an auth token
----------------------
**Request**::

    curl -X POST http://staging.userservice.tangentme.com/api-token-auth/ --data "username=joe&password=test"

**Response**::

	{"token": "11ce1e89d7e1d23e78e5c922c0cbd24bb2457cec"}

You can use this token to make future authorized requests

Authorizing with an auth token
-------------------------------

To identify yourself in consequent requests, set the `Authorization` header like below::

    curl GET http://staging.userservice.tangentme.com/users/me/ -H 'Authorization: Token 11ce1e89d7e1d23e78e5c922c0cbd24bb2457cec'

**Response**::  

	{
		"id": 5, 
		"first_name": "", 
		"last_name": "", 
		"username": "a", 
		"email": "", 
		"is_staff": true, 
		"profile": {
			"contact_number": "", 
			"status_message": null, 
			"bio": null
		}, 
		"authentications": [], 
		"roles": []
	}
