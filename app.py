from flask import Flask, request
from flask_restful import Api
from flask_jwt import JWT
from security import authenticate,identity
import os
from resources.user import UserRegister
from resources.item import Item, ItemList

app = Flask(__name__)
api = Api(app)

jwt = JWT(app,authenticate,identity)



        
    
api.add_resource(Item,'/item/<string:name>')
api.add_resource(ItemList,'/items')
api.add_resource(UserRegister,'/register')


#Use this if your running web server on cloud9
if __name__ == '__main__':
    app.secret_key = 'super_secret_key'
    app.debug = True
    app.run(host=os.getenv('IP', '0.0.0.0'), port=int(os.getenv('PORT', 8080))) 