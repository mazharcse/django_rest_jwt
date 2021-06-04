# API Project Overview
It is simple Django REST api project.
This project has 4 api to return countries, states and address information which are stored in Database.

### Project Requirements
- All project requirements are mentioned in requirements.txt such as **Python 3.8**, django, djangorestframework etc.
After installation of **Python and pip**, create and activate virtual environment.
  `python -m venv env`
- For windows run `env\Scripts\activate.bat` , for linux `source env/bin/activate`
    
  
### Project Setup 
- create a folder zs_project
- `cd zs_project`
- `$ git clone https://github.com/mazharcse/zs_project.git`
- `cd apiproject`
- `pip install -r requirements.txt`
- `python manage.py migrate`
- `python manage.py makemigrations`
- `python manage.py migrate`
- `python manage.py runserver`

### Usage
I use HTTPie to consume the API endpoints via the command prompt. You can use cURL or other tools to test APIs.
`pip install httpie`

Then Getting the tokens

   `http post http://127.0.0.1:8000/projectapi/token/ username=mazhar password=zsproject`

After Running that command, you will get two tokens.

    `{
        "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjIyODMzODg1LCJqdGkiOiI2OTRmZWVmNTczMjY0YzA3YmMyYjhjZGQ1NjAzYTBlYyIsInVzZXJfaWQiOjF9.dt8F0Ugfs8gNgwNWoPaSrPffiV-Fis6VgOPXDMX6Xmg",
        "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTYyMjkxOTk4NSwianRpIjoiZmM4MGMzZGI4OWQwNDNmMzgzMzE3NWQ3N2E2ZGY2NmQiLCJ1c2VyX2lkIjoxfQ.1TWAwL4pnpQCdLHRLK66eJv27YO0BhpM_mr3e4aINXk"
    }`

Now using the access token you can, use all APIs like

    `http http://127.0.0.1:8000/projectapi/countries/ "Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNTQ1MjI0MjAwLCJqdGkiOiJlMGQxZDY2MjE5ODc0ZTY3OWY0NjM0ZWU2NTQ2YTIwMCIsInVzZXJfaWQiOjF9.9eHat3CvRQYnb5EdcgYFzUyMobXzxlAVh_IAgqyvzCE"`

You can use this access token for the **next five minutes**.

After five min, the token will expire, and if you try to access the view again, you are going to get error.

###Refresh Token
To get a new access token, you should use the refresh token:

    `http post http://127.0.0.1:8000/projectapi/token/refresh/ refresh=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTU0NTMwODIyMiwianRpIjoiNzAyOGFlNjc0ZTdjNDZlMDlmMzUwYjg3MjU1NGUxODQiLCJ1c2VyX2lkIjoxfQ.Md8AO3dDrQBvWYWeZsd_A1J39z6b6HEwWIUZ7ilOiPE`

##API List
- http://localhost:8000/projectapi/countries/
- http://localhost:8000/projectapi/countries/?name=Bangladesh
- http://localhost:8000/projectapi/countries/?code=970
- http://localhost:8000/projectapi/states/?country__name=Palestine
- http://localhost:8000/projectapi/states/
- http://localhost:8000/projectapi/states/?name=Gaza
- http://localhost:8000/projectapi/address/
- http://localhost:8000/projectapi/address_detail/

For calling any api, you have to use "Authorization: Bearer _access_token_"` 

Again writing another example, 

    `http http://127.0.0.1:8000/projectapi/states/ "Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNTQ1MjI0MjAwLCJqdGkiOiJlMGQxZDY2MjE5ODc0ZTY3OWY0NjM0ZWU2NTQ2YTIwMCIsInVzZXJfaWQiOjF9.9eHat3CvRQYnb5EdcgYFzUyMobXzxlAVh_IAgqyvzCE"`