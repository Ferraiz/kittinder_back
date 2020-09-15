https://marshmallow.readthedocs.io/en/stable/examples.html#quotes-api-flask-sqlalchemy
https://marshmallow.readthedocs.io/en/stable/marshmallow.fields.html?highlight=dump_only#marshmallow.fields.Nested

curl -d '{"email":"adri@mail.com", "password":"12345"}' -H "Content-Type: application/json" -X POST http://127.0.0.1:5000/user

curl -d '{"email":"hhhh@fff.com", "password":"12345"}' -H "Content-Type: application/json" -X POST http://127.0.0.1:5000/user
