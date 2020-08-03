import os
from flask import Flask, render_template, redirect, url_for, request, flash
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
if os.path.exists("env.py"):
    import env

app = Flask(__name__)

"""
- Setting variables for MongoDB.
- import env.py
- The variables are also on Heroku config vars.
"""
app.config["MONGO_DBNAME"] = os.getenv("MONGO_DBNAME")
app.config["MONGO_URI"] = os.getenv("MONGO_URI")
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")

mongo = PyMongo(app)

"""
1. index.html : /get_index
"""


@app.route('/')
@app.route('/get_index')
def get_index():
    return render_template("index.html",
                           recipes=mongo.db.recipes.find())


"""
2. recipes.html : /get_recipes
- Show all recipes in the recipes collection.
"""


@app.route('/get_recipes')
def get_recipes():
    return render_template("recipes.html",
                           recipes=mongo.db.recipes.find())


"""
3. aboutus.html : /get_info
- Show the short noodle story and message form.
"""


@app.route('/get_info')
def get_info():
    return render_template("aboutus.html")


"""
4. addrecipe.html : /add_recipe
- Show add recipe form.
"""


@app.route('/add_recipe')
def add_recipe():
    return render_template("addrecipe.html",
                           recipes=mongo.db.recipes.find(),
                           difficulty=mongo.db.difficulty.find())


"""
5. Send the input data to /add_recipe
- Get input data from the input form and save on the recipes collection

* Check if a given key already exists in a dictionary
  : https://stackoverflow.com/questions/1602934
  /check-if-a-given-key-already-exists-in-a-dictionary
* How to append existing array in existing collection in mongodb
  : https://stackoverflow.com/questions/31956696
  /how-to-append-existing-array-in-existing-collection-in-mongodb-using-java-with-n
"""


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
            'difficulty': request.form.get('difficulty'),
            'ingredients': ingredient,
            'instructions': instruction,
            'photo_url': request.form.get('photo_url'),
            'del_password': request.form.get('del_password')
        })
    return redirect(url_for('get_recipes'))


"""
6. get_singlerecipe.html/<recipe_id> : /get_singlerecipe/<recipe_id>
- Show the selected recipe.
"""


@app.route('/get_singlerecipe/<recipe_id>')
def get_singlerecipe(recipe_id):
    the_recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    return render_template("singlerecipe.html", recipe=the_recipe)


"""
7. editrecipe.html : /editrecipe
- Show the input data on the edit recipe form.
- Get from the input data and show the data on the page.
"""


@app.route('/edit_recipe/<recipe_id>')
def edit_recipe(recipe_id):
    the_recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    all_difficulty = mongo.db.difficulty.find()
    len_ingredient = range(0, len(the_recipe['ingredients']))
    len_instruction = range(0, len(the_recipe['instructions']))
    return render_template("editrecipe.html",
                           recipe=the_recipe,
                           recipe_id=the_recipe['_id'],
                           difficulty=all_difficulty,
                           len_ingredient=len_ingredient,
                           len_instruction=len_instruction)


"""
8. Send the changed data to /edit_recipe
- Get the changed data from the input form and save on the recipes collection

* Check if a given key already exists in a dictionary
  : https://stackoverflow.com/questions/1602934
  /check-if-a-given-key-already-exists-in-a-dictionary
* How to append existing array in existing collection in mongodb
  : https://stackoverflow.com/questions/31956696
  /how-to-append-existing-array-in-existing-collection-in-mongodb-using-java-with-n

- Users can't edit the deletion password.
The value of Password field will be the same as the saved data in add_recipe.
"""


@app.route('/update_recipe/<recipe_id>', methods=["POST"])
def update_recipe(recipe_id):
    recipes = mongo.db.recipes
    del_recipe_id = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
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
        'difficulty': request.form.get('difficulty'),
        'ingredients': ingredient,
        'instructions': instruction,
        'photo_url': request.form.get('photo_url'),
        'del_password': del_recipe_id['del_password']
    })
    return redirect(url_for('get_recipes'))


"""
9. singlerecipe.html/<recipe_id> : /delete_recipe/<recipe_id>
- The delete form exists as a modal form in singlerecipe.html.
- To compare the "del_password" data in the recipes collection and
  input data on the field of "input_password".
 * If the two values are the same, the recipe is removed.
 * If the two values are not the same, the recipe can not be removed
  and shows deletefail.html page.
"""


@app.route('/delete_recipe/<recipe_id>', methods=['POST'])
def delete_recipe(recipe_id):
    del_recipe_id = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    input_password = request.values.get("input_password")
    if del_recipe_id["del_password"] == input_password:
        mongo.db.recipes.delete_one({'_id': ObjectId(recipe_id)})
        return redirect(url_for('get_recipes'))
    else:
        error = 'Delete fail. Try again.'
        return render_template("deletefail.html", error=error)

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
