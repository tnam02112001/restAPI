from flask import Flask
from flask import request
from flask import jsonify
from flask_cors import CORS
import random
import string
app = Flask(__name__)
CORS(app)

def id_generator():
   randomID = ''.join(random.choice(string.ascii_lowercase) for i in range(3)) + ''.join(random.choice(string.digits)for i in range(3))
   return randomID

@app.route('/users', methods=['GET', 'POST', 'DELETE'])
def get_users():
   if request.method == 'GET':
      search_username = request.args.get('name') #accessing the value of parameter 'name'
      search_job = request.args.get('job')

      if search_username and search_job:
         subdict = {'users_list' : []}
         for user in users['users_list']:
            if user['name'] == search_username and user['job'] == search_job:
               subdict['users_list'].append(user)
         return subdict
      

      if search_username :
         subdict = {'users_list' : []}
         for user in users['users_list']:
            if user['name'] == search_username:
               subdict['users_list'].append(user)
         return subdict
      
      if search_job :
         subdict = {'users_list' : []}
         for user in users['users_list']:
            if user['job'] == search_job:
               subdict['users_list'].append(user)
         return subdict
      return users


   elif request.method == 'POST':
      userToAdd = request.get_json()
      userToAdd['id'] = id_generator()
      users['users_list'].append(userToAdd)

      #The reponsed content is  the updated representation of the object the user inserted
      resp = jsonify(userToAdd)

      #Set a 201 status code(content created)
      resp.status_code = 201

      #Return
      return resp
   
   elif request.method == 'DELETE':
      userToRemove = request.get_json()
      users['users_list'].remove(userToRemove)
      resp = jsonify(success=True)
      #resp.status_code = 200 #optionally, you can always set a response code. 
      # 200 is the default code for a normal response
      return resp

   

@app.route('/users/<id>')
def get_user(id):
   if id :
      for user in users['users_list']:
         if user['id'] == id:
            return user
      return ({})
   return users

users = { 
   'users_list' :
   [
      { 
         'id' : 'xyz789',
         'name' : 'Charlie',
         'job': 'Janitor',
      },
      {
         'id' : 'abc123', 
         'name': 'Mac',
         'job': 'Bouncer',
      },
      {
         'id' : 'ppp222', 
         'name': 'Mac',
         'job': 'Professor',
      }, 
      {
         'id' : 'yat999', 
         'name': 'Dee',
         'job': 'Aspring actress',
      },
      {
         'id' : 'zap555', 
         'name': 'Dennis',
         'job': 'Bartender',
      }
   ]
}
