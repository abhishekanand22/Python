from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


recipes = []

@app.route('/')
def index():
    return render_template('index.html', recipes=recipes)



@app.route('/add', methods=['GET', 'POST'])
def add_recipe():
    if request.method == 'POST':
        title = request.form['title']
        ingredients = request.form['ingredients']
        instructions = request.form['instructions']
        recipe = {
            'title': title,
            'ingredients': ingredients,
            'instructions': instructions
        }
        recipes.append(recipe)
        return redirect(url_for('index'))
    return render_template('add_recipe.html')



@app.route('/recipe/<int:recipe_id>')
def view_recipe(recipe_id):
    recipe = recipes[recipe_id]
    return render_template('view_recipe.html', recipe=recipe)



if __name__ == '__main__':
    app.run(debug=True)

