# We are making User class here to avoid manually adding users
# again and again with 3 keys, like shown below:

# users = [
#     # {
#     #     "id" : 1,
#     #     "username" : "bob",
#     #     "password" : "asdf"
#     # }
# ]

# Using this class we can simply do the following:
# users = [User(1,"Bob", "asdf"), User(2,"riz","dghh")]


class User:
    def __init__(self, _id, username, password):
        self.id = _id
        self.username = username
        self.password = password
