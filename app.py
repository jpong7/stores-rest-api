import os

from flask import Flask
from flask_restful import Api
from flask_jwt import JWT

from security import authenticate, identity
from resources.user import UserRegister
from resources.item import Item, ItemList
from resources.store import Store, StoreList

#from datetime import timedelta

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('postgresql://lvmugkjuslrpax:95b6e793cea469d9a0c0aea43d15978842853475b2b657ad2dea12a69a7fdbc4@ec2-44-194-113-156.compute-1.amazonaws.com:5432/d8c868pqe4op0n', 'sqlite:///data.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#app.config['JWT_EXPIRATION_DELTA'] = timedelta(seconds=1800) # config JWT to expire within half an hour
app.secret_key = 'jose'
api = Api(app)

jwt = JWT(app, authenticate, identity) # /auth

api.add_resource(Store, '/store/<string:name>')
api.add_resource(Item, '/item/<string:name>')
api.add_resource(StoreList, '/stores')
api.add_resource(ItemList, '/items')
api.add_resource(UserRegister, '/register')

if __name__ == '__main__':
    from db import db
    db.init_app(app)
    #app.run(...)
    app.run(port=5000, debug=True)