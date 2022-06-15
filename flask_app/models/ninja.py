from unittest import result
from flask_app.config.mysqlconnection import connectToMySQL

class Ninja:

    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
        self.likes=data['likes']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.users_who_liked=[]

    @classmethod
    def get_one(cls,data):
        query = "SELECT * FROM ninjas WHERE id = %(ninja_id)s;"
        results = connectToMySQL('dojos_and_ninjas').query_db(query,data)
        return cls( results[0] )

    @classmethod
    def save(cls, data):
        query = 'INSERT INTO ninjas (first_name, last_name, age, dojo_id) VALUES ( %(first_name)s, %(last_name)s, %(age)s, %(dojo_id)s);'
        return connectToMySQL('dojos_and_ninjas').query_db(query, data)

    @classmethod
    def addLike(cls, data):
        query = "INSERT INTO ninjas_was_like_from_users (ninjas_id,users_id) VALUES (%(ninja_id)s,%(user_id)s);"
        return connectToMySQL('dojos_and_ninjas').query_db(query,data)

    @classmethod
    def destroy(cls,data):
        query = "DELETE FROM ninjas WHERE id = %(id)s;"
        return connectToMySQL('dojos_and_ninjas').query_db(query,data)

    @classmethod
    def getUsersWhoLiked(cls, data):
        query = "SELECT * FROM ninjas_was_like_from_users LEFT JOIN ninjas ON ninjas_was_like_from_users.ninjas_id = ninjas.id LEFT JOIN users ON ninjas_was_like_from_users.users_id = users.id WHERE ninjas.id = %(ninja_id)s;"
        results = connectToMySQL('dojos_and_ninjas').query_db(query,data)
        myNinja = Ninja.get_one(data)
        for row in results:
            myNinja.users_who_liked.append(row['email'])
        return myNinja.users_who_liked