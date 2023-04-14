from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import flash
from pprint import pprint

DATABASE = 'paintings'

class Painting:
    
    def __init__(self, data):
        self.id = data['id']
        self.title = data['title']
        self.description = data['description']
        self.price = data['price']
        self.quantity = data['quantity']
        self.first_name = data['first_name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user_id = data['user_id']  
    
    @classmethod
    def save(cls, data):
        query = "INSERT INTO paintings (title, description, price, user_id) VALUES (%(title)s, %(description)s, %(price)s, %(user_id)s);"
        return connectToMySQL(DATABASE).query_db(query, data)

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM paintings JOIN users ON users.id = paintings.user_id;"
        results = connectToMySQL(DATABASE).query_db(query)
        pprint(results)
        paintings = []
        for painting in results:
            paintings.append(cls(painting))
        return paintings

    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM paintings JOIN users ON users.id = paintings.user_id WHERE paintings.id = %(id)s;"
        result = connectToMySQL(DATABASE).query_db(query, data)
        pprint(result[0])
        return Painting(result[0])
    
    @classmethod
    def update(cls, data):
        query = "UPDATE paintings SET title = %(title)s, description = %(description)s, price = %(price)s WHERE paintings.id = %(id)s;"
        return connectToMySQL(DATABASE).query_db(query, data)
    
    @classmethod
    def delete(cls, data):
        query = "DELETE FROM paintings WHERE id = %(id)s;"
        return connectToMySQL(DATABASE).query_db(query, data)
        
    

    @staticmethod
    def validate_painting(painting):
        is_valid = True
        if len(painting['title']) < 2:
            flash("Name must be three chars")
            is_valid = False
        if len(painting['description']) < 10:
            flash("Desc must be ten chars")
            is_valid = False
        if int(painting['price']) <= 0:
            flash("Price must be at least greater than 0")
            is_valid = False  
        return is_valid
    