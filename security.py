from werkzeug.security import safe_str_cmp
from user import User


# users = [
#     # {
#     #     "id" : 1,
#     #     "username" : "bob",
#     #     "password" : "asdf"
#     # }
# ]
# after importing the user class, we can simply do the following

users = [User [ 1, "Bob", "asdf"]]

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

username_mapping = {u.username: u for u in users}
userid_mapping = {u.id: u for u in users}



# get is a method to access dictionary
def authenticate(username , password):
    user = username_mapping.get(username , None)
    if user and safe_str_cmp(user.password, password):
        return user

# identity function is unique to flask-jwt
# it takes in payload, which is the content of jwt token
def identity(payload):
    user_id = payload["identity"]
    return userid_mapping.get(user_id , None)










