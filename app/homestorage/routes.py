from flask import render_template, url_for, flash, redirect, request
from flask_login import login_user, current_user, logout_user, login_required
from homestorage import app, db, bcrypt
from homestorage.forms import SearchForm, AddImageForm, AddItemForm, LoginForm
from homestorage.models import Item, ItemSchema, User
from homestorage.predict import Predictor
from homestorage.helpers import save_image_and_thumbnail

import os

items_schema = ItemSchema(many=True, strict=True)

@app.route("/")
def main():
    return render_template("main.html", title="Main Page")

@app.route("/items", methods=["GET", "POST"])
@login_required
def items():
    form = SearchForm()

    all_items = Item.query.filter_by(withdrawed=False).all()
    output = items_schema.dump(all_items)

    if form.validate_on_submit():
        return redirect(url_for("search", search_string=form.item_name.data, typ="not_withdrawed"))

    return render_template("all_items.html", title="All Items", items=output.data, form=form)

@app.route("/withdrawed_items", methods=["GET", "POST"])
@login_required
def withdrawed_items():
    form = SearchForm()

    items = Item.query.filter_by(withdrawed=True).all()
    output = items_schema.dump(items)

    if form.validate_on_submit():
        return redirect(url_for("search", search_string=form.item_name.data, typ="withdrawed"))

    return render_template("withdrawed_items.html", title="Withdrawed Items", items=output.data, form=form)

@app.route("/search", methods=["GET", "POST"])
def search():
    form = SearchForm()

    search_string = request.args["search_string"].lower()
    typ = request.args["typ"]

    if typ == "withdrawed":
        templ = "withdrawed_items.html"
        items = Item.query.filter_by(withdrawed=True).all()
    else:
        templ = "all_items.html"
        items = Item.query.filter_by(withdrawed=False).all()

    items = items_schema.dump(items).data
    items = [item for item in items if search_string in item["title"].lower()]

    if form.validate_on_submit():
        return redirect(url_for("search", search_string=form.item_name.data, typ=typ))

    return render_template(templ, title="Search Results", items=items, form=form)

@app.route("/add_picture", methods=["GET", "POST"])
@login_required
def add_picture():
    form = AddImageForm()
    image_name = ""

    if form.validate_on_submit():
        
        if form.picture.data:
            file = form.picture.data
            image_name = save_image_and_thumbnail(file)
            
        return redirect(url_for("add_item", img=image_name))

    return render_template("add_picture.html", title="Add Item", form=form)
    
@app.route("/add_item", methods=["GET", "POST"])
@login_required
def add_item():
    form = AddItemForm()
    image_name = request.args["img"]
    
    if image_name:
        image_path = os.path.join(os.getcwd(), "homestorage", "static", "images", image_name)
        model = Predictor(image_path)
        prediction = model.predict()

        if prediction == 0:
            prediction = "Batai"
        else:
            prediction = "Popieriai"

    else:
        image_name = "default.jpg"

    if request.method == "GET":
        form.item_name.data = prediction

    if form.validate_on_submit():
        title = form.item_name.data
        box = form.box_number.data

        if image_name:
            new_item = Item(title=title, box=box, image=image_name)
        else:
            new_item = Item(title=title, box=box)

        db.session.add(new_item)
        db.session.commit()

        flash(f"Item \"{title}\" has been succesfully added!", "success")

        return redirect(url_for('add_picture'))

    return render_template('add_item.html', title="Add Item", form=form, img=image_name, prediction=prediction)

@app.route("/withdraw_item", methods=["GET", "POST"])
@login_required
def withdraw_item():
    item_id = request.args["id"]

    item = Item.query.get(item_id)
    item.withdrawed = True
    db.session.commit()

    return redirect(url_for("items"))

@app.route("/return_item", methods=["GET", "POST"])
@login_required
def return_item():
    item_id = request.args["id"]

    item = Item.query.get(item_id)
    item.withdrawed = False
    db.session.commit()

    return redirect(url_for("withdrawed_items"))


@app.route("/delete_item", methods=["GET", "POST"])
@login_required
def delete_item():
    item_id = search_string = request.args["id"]
    Item.query.filter_by(id=item_id).delete()
    db.session.commit()

    return redirect(url_for("withdrawed_items"))

@app.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("main"))

    form = LoginForm()

    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()

        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=True)

            return redirect(url_for("main"))
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')

    return render_template("login.html", title='Login', form=form)

@app.route("/logout")
def logout():
    logout_user()

    return redirect(url_for("main"))