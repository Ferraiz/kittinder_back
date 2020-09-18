https://marshmallow.readthedocs.io/en/stable/examples.html#quotes-api-flask-sqlalchemy
https://marshmallow.readthedocs.io/en/stable/marshmallow.fields.html?highlight=dump_only#marshmallow.fields.Nested

https://gist.github.com/subfuzion/08c5d85437d5d4f00e58

# PETICIONES

## POST /user

curl -d '{"email":"pablo@mail.com", "password":"casado"}' -H "Content-Type: application/json" -X POST http://127.0.0.1:5000/user

curl -d '{"email":"puturru@mail.com", "password":"defoi"}' -H "Content-Type: application/json" -X POST http://127.0.0.1:5000/user

curl -d '{"password":"12345"}' -H "Content-Type: application/json" -X POST http://127.0.0.1:5000/user

## POST /login

curl -d '{"email":"pablo@mail.com", "password":"casado"}' -H "Content-Type: application/json" -X POST http://127.0.0.1:5000/login

curl -d '{"email":"pedro@mail.com", "password":"sanchez"}' -H "Content-Type: application/json" -X POST http://127.0.0.1:5000/login

## PUT /user

### Sin token

curl -d '{"email":"adita@mail.com", "password":"12345"}' -H "Content-Type: application/json" -X PUT http://127.0.0.1:5000/user/9

curl -d '{"email":"jordi@mail.com", "password":"pujol"}' -H "Content-Type: application/json" -X PUT http://127.0.0.1:5000/user/11

### Con token

curl -H "Authorization: Bearer \$ACCESS" http://localhost:5000/protected
