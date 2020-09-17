https://marshmallow.readthedocs.io/en/stable/examples.html#quotes-api-flask-sqlalchemy
https://marshmallow.readthedocs.io/en/stable/marshmallow.fields.html?highlight=dump_only#marshmallow.fields.Nested

https://gist.github.com/subfuzion/08c5d85437d5d4f00e58

curl -d '{"email":"pablo@mail.com", "password":"casado"}' -H "Content-Type: application/json" -X POST http://127.0.0.1:5000/user

curl -d '{"password":"12345"}' -H "Content-Type: application/json" -X POST http://127.0.0.1:5000/user

curl -d '{"email":"pablo@mail.com", "password":"casado"}' -H "Content-Type: application/json" -X POST http://127.0.0.1:5000/login

curl -d '{"email":"pedro@mail.com", "password":"sanchez"}' -H "Content-Type: application/json" -X POST http://127.0.0.1:5000/login

curl -d '{"email":"puturru@mail.com", "password":"defoi"}' -H "Content-Type: application/json" -X POST http://127.0.0.1:5000/user

curl -d '{"email":"marra@mail.com", "password":"miau"}' -H "Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE2MDAzNzM1MjcsIm5iZiI6MTYwMDM3MzUyNywianRpIjoiYjA4MGQ5ZTAtZGY3MC00OGQ1LWJlMTgtNTQ0OTFmMWU1YmZhIiwiZXhwIjoxNjAwMzc0NDI3LCJpZGVudGl0eSI6ImFkcmlAbWFpbC5jb20iLCJmcmVzaCI6ZmFsc2UsInR5cGUiOiJhY2Nlc3MifQ.nZFEmKH4ftEyyT4sdHCg3FSJZhGwWbbx3b6eB5Ihi6Y" -X PUT http://127.0.0.1:5000/user/17

curl -d '{"email":"marra@mail.com", "password":"miau"}' -X PUT http://127.0.0.1:5000/user/17

curl -d '{"email":"ines@mail.com", "password":"arrimadas"}' -H "Content-Type: application/json" -X PUT http://127.0.0.1:5000/user/18

curl -d '{"email":"gabriel@mail.com", "password":"rufian"}' -H "Content-Type: application/json" -X PUT http://127.0.0.1:5000/user/10
