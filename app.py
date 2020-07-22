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
    
    ingredient_dict = [ingredient for ingredient in request.form.keys() 
                       if "ingredient_name_" in ingredient]
    instruction_dict = [instruction for instruction in request.form.keys() 
                       if "instructions_name_" in instruction]
    ingredient = []
    instruction = []
    for ingre in ingredient_dict:
        ingredient.append(request.form[ingre])
    for instr in instruction_dict:
        instruction.append(request.form[instr])
    recipes.insert_one( 
    {
        'recipe_name': request.form.get('recipe_name'),
        'nationality': request.form.get('nationality'),
        'portions': request.form.get('portions'),
        'ingredients': ingredient,
        'instructions': instruction,
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
    len_ingredient = range(0, len(the_recipe['ingredients']))
    len_instruction = range(0, len(the_recipe['instructions']))
    return render_template("editrecipe.html", 
                           recipe=the_recipe, 
                           recipe_id=the_recipe['_id'],
                           len_ingredient=len_ingredient,
                           len_instruction=len_instruction)


@app.route('/update_recipe/<recipe_id>', methods=["POST"])
def update_recipe(recipe_id):
    recipes = mongo.db.recipes
    ingredient_dict = [ingredient for ingredient in request.form.keys() 
                       if "ingredient_name_" in ingredient]
    instruction_dict = [instruction for instruction in request.form.keys()
                       if "instructions_name_" in instruction]
    ingredient = []
    instruction = []
    for ingre in ingredient_dict:
        ingredient.append(request.form[ingre])
    for instr in instruction_dict:
        instruction.append(request.form[instr])
    recipes.update({'_id': ObjectId(recipe_id)}, 
    {
        'recipe_name': request.form.get('recipe_name'),
        'nationality': request.form.get('nationality'),
        'portions': request.form.get('portions'),
        'ingredients': ingredient,
        'instructions': instruction,
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