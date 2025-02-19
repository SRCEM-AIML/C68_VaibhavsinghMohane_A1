from flask import Flask, render_template # type: ignore

app = Flask(__name__)

recipes = {
    "1": {
        "name": "Spaghetti Carbonara",
        "ingredients": [
            "200g spaghetti",
            "100g pancetta",
            "2 large eggs",
            "50g grated Parmesan",
            "Black pepper"
        ],
        "procedure": "1. Cook spaghetti. 2. Fry pancetta. 3. Mix eggs and Parmesan. 4. Combine everything."
    },
    "2": {
        "name": "Chicken Tikka Masala",
        "ingredients": [
            "500g chicken breast",
            "200ml yogurt",
            "2 tbsp tikka masala paste",
            "1 onion",
            "1 can diced tomatoes"
        ],
        "procedure": "1. Marinate chicken in yogurt and spices. 2. Grill chicken. 3. Cook onions and add tomatoes. 4. Add chicken and simmer."
    },
    "3": {
        "name": "Vegetable Stir-Fry",
        "ingredients": [
            "1 bell pepper",
            "1 cup broccoli",
            "1 carrot",
            "2 tbsp soy sauce",
            "1 tbsp sesame oil"
        ],
        "procedure": "1. Chop vegetables. 2. Heat oil. 3. Stir-fry vegetables. 4. Add soy sauce."
    },
    "4": {
        "name": "Classic Pancakes",
        "ingredients": [
            "1 cup flour",
            "2 tbsp sugar",
            "1 egg",
            "1 cup milk",
            "1 tsp baking powder"
        ],
        "procedure": "1. Mix dry ingredients. 2. Add wet ingredients. 3. Cook on a hot pan."
    },
    "5": {
        "name": "Beef Tacos",
        "ingredients": [
            "500g ground beef",
            "1 packet taco seasoning",
            "4 taco shells",
            "Lettuce, cheese, salsa"
        ],
        "procedure": "1. Cook beef with seasoning. 2. Fill taco shells. 3. Add toppings."
    },
    "6": {
        "name": "Caesar Salad",
        "ingredients": [
            "Romaine lettuce",
            "Croutons",
            "Parmesan cheese",
            "Caesar dressing"
        ],
        "procedure": "1. Toss lettuce. 2. Add croutons and cheese. 3. Drizzle dressing."
    },
    "7": {
        "name": "Chocolate Brownies",
        "ingredients": [
            "100g butter",
            "200g dark chocolate",
            "2 eggs",
            "1 cup sugar",
            "1 cup flour"
        ],
        "procedure": "1. Melt butter and chocolate. 2. Mix eggs and sugar. 3. Add flour. 4. Bake."
    }
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/recipe/<recipe_id>')
def recipe(recipe_id):
    # Fetch the recipe based on the recipe_id
    recipe_data = recipes.get(recipe_id)
    if recipe_data:
        return render_template('recipe_page.html', recipe=recipe_data)
    else:
        return "Recipe not found", 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)