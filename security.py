from werkzeug.security import safe_str_cmp
from user import User


# after importing the user class, we can simply do the following

users = [User(1,"Bob", "asdf"), User(2,"riz","dghh")]

# username_mapping = { "bob" : { 
#         "id" : 1,
#         "username" : "bob",
#         "password" : "asdf"
#     }
# }
# userid_mapping = {1 : {
#         "id" : 1,
#         "username" : "bob",
#         "password" : "asdf"
#    }
# }

# We can simplyfy the above process of making dictionary using 
# for loop as done below with `username_mapping`

# We can choose any field from the user object to be the key and assign the full user object to it
# like the same code is used for making `userid_mapping` but with a different key `u.id`

username_mapping = {u.username: u for u in users}
print(username_mapping)
userid_mapping = {u.id: u for u in users}
print(userid_mapping)

# to get the key 1 from the dictionary and 
# print the values of the user object attached to it

# print(userid_mapping.get(1).password)
# print(userid_mapping.get(1).username) 
# print(userid_mapping.get(1).id) 

# Also we can get the user object 
# user = userid_mapping.get(1)
# and access all the keys of the user received like:
# user.id
# user.password
# user.username



# this function accepts username and password from the user request 
# and then it finds the user details via username
# if the user exists, it compares the password from the request with 
# the password stored in the database (dummy list in our case)

def authenticate(username , password):
    
    # get is a method to access dictionary    
    user = username_mapping.get(username , None)
    if user and safe_str_cmp(user.password, password):
        return user

# identity function is unique to flask-jwt
# This function accepts the JWT encrypted token and decodes it 
# (payload is a dictionary here after decoding is done)
# The payload dictionary has `identity` field (with value `user id` in this case)
# Then we are returning the user from the DB (dummy list here)
# If the user id is valid, a user object will be returned else None will be returned

def identity(payload):
    user_id = payload["identity"]
    return userid_mapping.get(user_id , None)










