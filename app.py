from flask import Flask, request
from flask_restful import Api
from flask_jwt import JWT
from security import authenticate,identity
import os
from resources.user import UserRegister
from resources.item import Item, ItemList

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
api = Api(app)


@app.before_first_request
def create_tables():
    db.create_all()
    
jwt = JWT(app,authenticate,identity)



        
    
api.add_resource(Item,'/item/<string:name>')
api.add_resource(ItemList,'/items')
api.add_resource(UserRegister,'/register')


#Use this if your running web server on cloud9
if __name__ == '__main__':
    from db import db
    db.init_app(app)
    app.secret_key = 'super_secret_key'
    app.debug = True
    app.run(host=os.getenv('IP', '0.0.0.0'), port=int(os.getenv('PORT', 8080))) 