from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import flash
from pprint import pprint

DATABASE = 'cars_schema'

class Car:
    
    def __init__(self, data):
        self.id = data['id']
        self.make = data['make']
        self.model = data['model']
        self.year = data['year']
        self.user_id = data['user_id']
        self.number_of_service = data['number_of_service']
        self.first_name = data['first_name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at'] 
    
    @classmethod
    def save(cls, data):
        query = "INSERT INTO cars (make, model, year, number_of_sevice, user_id) VALUES (%(make)s, %(model)s, %(year)s, %(numer_of_service)s, %(user_id)s);"
        return connectToMySQL(DATABASE).query_db(query, data)

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM cars JOIN users ON users.id = cars.user_id;"
        results = connectToMySQL(DATABASE).query_db(query)
        pprint(results)
        cars = []
        for car in results:
            cars.append(cls(car))
        return cars

    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM cars JOIN users ON users.id = cars.user_id WHERE cars.id = %(id)s;"
        result = connectToMySQL(DATABASE).query_db(query, data)
        pprint(result[0])
        return Car(result[0])
    
    @classmethod
    def update(cls, data):
        query = "UPDATE cars SET make = %(make)s, model = %(model)s, year = %(year)s, numer_of_service = %(number_of_sevice)s, WHERE cars.id = %(id)s;"
        return connectToMySQL(DATABASE).query_db(query, data)
    
    @classmethod
    def delete(cls, data):
        query = "DELETE FROM cars WHERE id = %(id)s;"
        return connectToMySQL(DATABASE).query_db(query, data)
        
    
    @staticmethod
    def validate_car(car):
        is_valid = True
        if len(car['make']) < 2:
            flash("Name must be three chars")
            is_valid = False
        if len(car['model']) < 2:
            flash("Model must be three chars")
            is_valid = False
        if len(car['year']) < 2:
            flash("Year must be four chars")
            is_valid = False
        # if not 'under_30' in car:
        #     flash("must select option for under 30 min.")
        #     is_valid = False
        # if car['year'] == '':
        #     flash("Please select a year")
        #     is_valid = False
        if int(car['number_of_service']) <= 0:
            flash("Car has to service at least 1 person")
            is_valid = False    
        return is_valid
    