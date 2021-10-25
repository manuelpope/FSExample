
from Factory import db

class UserModel(object):

    def __init__(self, username, password, mail, country):
        self.username = username
        self.password = password
        self.mail = mail
        self.country = country

    def json(self):
        return {
            'id': self.id,
            'username': self.username
        }

    def save_to_db(self):
        dictUser = {'username': self.username,
                    'password': self.password,
                    'mail': self.mail,
                    'country': self.country
                    }
        db.Users.insert_one(dictUser)

    def update_to_db(self):
        dictUser = {'username': self.username,
                    'password': self.password,
                    'mail': self.mail,
                    'country': self.country
                    }

        myquery = {"username": self.username}
        newvalues = {"$set": {"password": self.password}}

        db.Users.update_one(myquery, newvalues)

    def delete_from_db(self):
        db.session.delete(self)

    @classmethod
    def find_by_username(cls, username):
        user = [x for x in db.Users.find({"username": str(username)})]
        if user:
            return user[0]
        return None

    @classmethod
    def find_by_id(cls, _id):
        return [x for x in db.Users.find({"_id": str(id)})][0]

    @classmethod
    def find_by_mail(cls, mail):
        user = [x for x in db.Users.find({"mail": str(mail)})]
        if user:
            return user[0]
        return None
