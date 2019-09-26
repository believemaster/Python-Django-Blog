# for mac its curl for windows it's different
# this is jwt jason web token for rest framework
'''
note for rest framework-jwt: (url for documentation : https://getblimp.github.io/django-rest-framework-jwt/)
$ curl -X POST -d "username=yanik&password=2103" http://127.0.0.1:8000/api/token/auth/ # get token for the user and do the stuff usign cmd in json format  read docs
$ curl -H "Authorization: JWT <your_token>" http://localhost:8000/api/comments

'''
