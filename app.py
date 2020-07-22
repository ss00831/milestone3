import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

if os.path.exists("env.py"):
    import env


app = Flask(__name__)
app.config["MONGO_DBNAME"] = os.getenv("MONGO_DBNAME")
app.config["MONGO_URI"] =  os.getenv("MONGO_URI")

mongo = PyMongo(app)


@app.route('/')
@app.route('/get_index')
def get_index():
    return render_template("index.html", 
                           recipes=mongo.db.recipes.find())


@app.route('/get_recipes')
def get_recipes():
    return render_template("recipes.html", 
                           recipes=mongo.db.recipes.find())


@app.route('/get_info')
def get_info():
    return render_template("aboutus.html", 
                           recipes=mongo.db.recipes.find())


@app.route('/add_recipe')
def add_recipe():
    return render_template("addrecipe.html", 
                           recipes=mongo.db.recipes.find())


@app.route('/insert_recipe', methods=['POST'])
def insert_recipe():
    recipes = mongo.db.recipes
    recipes.insert_one(
    {
        'recipe_name': request.form.get('recipe_name'),
        'nationality': request.form.get('nationality'),
        'portions': request.form.get('portions'),
        'ingredients': [],
        #request.form.get('ingredient_name_1')
        'instructions': [request.form.get('instructions_name_1'),request.form.get('instructions_name_2'),request.form.get('instructions_name_3')],
        'photo_url': request.form.get('photo_url'),
        'del_password': request.form.get('del_password')    
    })
    return redirect(url_for('get_recipes'))


@app.route('/get_singlerecipe/<recipe_id>')
def get_singlerecipe(recipe_id):
    the_recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})   
    return render_template("singlerecipe.html", recipe=the_recipe)


@app.route('/edit_recipe/<recipe_id>')
def edit_recipe(recipe_id):
    the_recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    return render_template("editrecipe.html", recipe=the_recipe)


@app.route('/update_recipe/<recipe_id>', methods=["POST"])
def update_recipe(recipe_id):
    recipes = mongo.db.recipes
    recipes.update({'_id': ObjectId(recipe_id)}, 
    {
        'recipe_name': request.form.get('recipe_name'),
        'nationality': request.form.get('nationality'),
        'portions': request.form.get('portions'),
        'ingredients': [request.form.get('ingredient_name_1'),request.form.get('ingredient_name_2'),request.form.get('ingredient_name_3')],
        'instructions': [request.form.get('instructions_name_1'),request.form.get('instructions_name_2'),request.form.get('instructions_name_3')],
        'photo_url': request.form.get('photo_url'),
        'del_password': request.form.get('del_password')
    })        
    return redirect(url_for('get_recipes'))


@app.route('/delete_recipe/<recipe_id>')
def delete_recipe(recipe_id):
    mongo.db.recipes.remove({'_id': ObjectId(recipe_id)})    
    return redirect(url_for('get_recipes'))
    

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)