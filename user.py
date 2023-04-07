from flask_login import UserMixin

class User(UserMixin):
    def __init__(self, user_dict):
        self.id = str(user_dict['_id'])
        self.email = user_dict['email']
        self.name = user_dict['name']
        self.password_hash = user_dict['password']
    
    def get_id(self):
        return self.id
    
    def is_active(self):
        return True
    
    @staticmethod
    def get(user_id):
        user_dict = users.find_one({'_id': ObjectId(user_id)})
        if user_dict is not None:
            return User(user_dict)
        else:
            return None
