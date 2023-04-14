from flask_app import app, render_template, redirect, session, request
from flask_app.models.car import Car

@app.route('/cars')
def cars():
    if 'user_id' not in session:
        return redirect('/logout')
    return render_template('cars.html', cars = Car.get_all())

@app.route('/cars/new')
def new_car():
    return render_template('new_car.html')

@app.route('/cars/create', methods = ['POST'])
def create_car():
    print(request.form)
    if not Car.validate_car(request.form):
        return redirect('/cars/new')
    Car.save(request.form)
    return redirect('/cars')

@app.route('/cars/<int:id>')
def show_car(id):
    data = {'id': id}
    return render_template("show_car.html", car = Car.get_one(data))

@app.route("/cars/edit/<int:id>")
def edit_car(id):
    data = {'id': id}
    return render_template("edit.html", car = Car.get_one(data))

@app.route('/cars/update', methods = ["POST"])
def update_car():
    print(request.form)
    if not Car.validate_car(request.form):
        return redirect(f"/cars/edit/{request.form['id']}")
    Car.update(request.form)
    return redirect('/cars') 

@app.route('/cars/delete/<int:id>')
def delete_car(id):
    data = {'id': id}
    Car.delete(data)
    return redirect('/cars')
