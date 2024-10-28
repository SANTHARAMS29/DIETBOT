from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Expanded nutritional data
nutrition_data = {
    'egg': {
        'protein': "Egg contains 6.5 grams of protein.",
        'vitamins': "Egg provides 2 mg of vitamins.",
        'minerals': "Egg contains 5 mg of minerals.",
        'calories': "Egg has about 78 calories."
    },
    'chicken': {
        'protein': "Chicken contains 31 grams of protein.",
        'vitamins': "Chicken provides 0 mg of vitamins.",
        'minerals': "Chicken contains 7 mg of minerals.",
        'calories': "Chicken has about 165 calories."
    },
    'apple': {
        'protein': "An apple contains 0.3 grams of protein.",
        'vitamins': "An apple provides 9 mg of vitamins.",
        'minerals': "An apple has 2 mg of minerals.",
        'calories': "An apple has about 95 calories."
    },
    'broccoli': {
        'protein': "Broccoli contains 2.8 grams of protein.",
        'vitamins': "Broccoli provides 89 mg of vitamins.",
        'minerals': "Broccoli has 33 mg of minerals.",
        'calories': "Broccoli has about 55 calories."
    },
    'salmon': {
        'protein': "Salmon contains 25 grams of protein.",
        'vitamins': "Salmon provides 4 mg of vitamins.",
        'minerals': "Salmon has 9 mg of minerals.",
        'calories': "Salmon has about 208 calories."
    },
    'almonds': {
        'protein': "Almonds contain 21 grams of protein.",
        'vitamins': "Almonds provide 0.6 mg of vitamins.",
        'minerals': "Almonds have 270 mg of minerals.",
        'calories': "Almonds have about 576 calories."
    },
    'banana': {
        'protein': "A banana contains 1.3 grams of protein.",
        'vitamins': "A banana provides 10 mg of vitamins.",
        'minerals': "A banana has 27 mg of minerals.",
        'calories': "A banana has about 105 calories."
    },
    'spinach': {
        'protein': "Spinach contains 2.9 grams of protein.",
        'vitamins': "Spinach provides 28 mg of vitamins.",
        'minerals': "Spinach has 79 mg of minerals.",
        'calories': "Spinach has about 23 calories."
    },
    'beef': {
        'protein': "Beef contains 26 grams of protein.",
        'vitamins': "Beef provides 0 mg of vitamins.",
        'minerals': "Beef has 6 mg of minerals.",
        'calories': "Beef has about 250 calories."
    },
    'carrot': {
        'protein': "A carrot contains 0.9 grams of protein.",
        'vitamins': "A carrot provides 5.9 mg of vitamins.",
        'minerals': "A carrot has 27 mg of minerals.",
        'calories': "A carrot has about 41 calories."
    },
    'oats': {
        'protein': "Oats contain 13 grams of protein.",
        'vitamins': "Oats provide 0.6 mg of vitamins.",
        'minerals': "Oats have 54 mg of minerals.",
        'calories': "Oats have about 389 calories."
    },
    'milk': {
        'protein': "Milk contains 3.3 grams of protein.",
        'vitamins': "Milk provides 0.5 mg of vitamins.",
        'minerals': "Milk has 120 mg of minerals.",
        'calories': "Milk has about 42 calories."
    },
    'yogurt': {
        'protein': "Yogurt contains 10 grams of protein.",
        'vitamins': "Yogurt provides 1.2 mg of vitamins.",
        'minerals': "Yogurt has 180 mg of minerals.",
        'calories': "Yogurt has about 59 calories."
    },
    'lentils': {
        'protein': "Lentils contain 9 grams of protein.",
        'vitamins': "Lentils provide 0 mg of vitamins.",
        'minerals': "Lentils have 25 mg of minerals.",
        'calories': "Lentils have about 116 calories."
    },
    'peanut butter': {
        'protein': "Peanut butter contains 25 grams of protein.",
        'vitamins': "Peanut butter provides 13 mg of vitamins.",
        'minerals': "Peanut butter has 200 mg of minerals.",
        'calories': "Peanut butter has about 588 calories."
    },
    'cheese': {
        'protein': "Cheese contains 25 grams of protein.",
        'vitamins': "Cheese provides 1 mg of vitamins.",
        'minerals': "Cheese has 100 mg of minerals.",
        'calories': "Cheese has about 402 calories."
    },
    'potato': {
        'protein': "Potato contains 2 grams of protein.",
        'vitamins': "Potato provides 19 mg of vitamins.",
        'minerals': "Potato has 12 mg of minerals.",
        'calories': "Potato has about 77 calories."
    },
    'rice': {
        'protein': "Rice contains 2.7 grams of protein.",
        'vitamins': "Rice provides 0 mg of vitamins.",
        'minerals': "Rice has 10 mg of minerals.",
        'calories': "Rice has about 130 calories."
    },
    'tofu': {
        'protein': "Tofu contains 8 grams of protein.",
        'vitamins': "Tofu provides 0 mg of vitamins.",
        'minerals': "Tofu has 20 mg of minerals.",
        'calories': "Tofu has about 76 calories."
    },
    'orange': {
        'protein': "An orange contains 1.2 grams of protein.",
        'vitamins': "An orange provides 70 mg of vitamins.",
        'minerals': "An orange has 18 mg of minerals.",
        'calories': "An orange has about 62 calories."
    },
    'pork': {
        'protein': "Pork contains 27 grams of protein.",
        'vitamins': "Pork provides 0 mg of vitamins.",
        'minerals': "Pork has 4 mg of minerals.",
        'calories': "Pork has about 242 calories."
    },
    'avocado': {
        'protein': "Avocado contains 2 grams of protein.",
        'vitamins': "Avocado provides 10 mg of vitamins.",
        'minerals': "Avocado has 7 mg of minerals.",
        'calories': "Avocado has about 160 calories."
    },
    'tomato': {
        'protein': "A tomato contains 0.9 grams of protein.",
        'vitamins': "A tomato provides 12 mg of vitamins.",
        'minerals': "A tomato has 5 mg of minerals.",
        'calories': "A tomato has about 18 calories."
    },
    'walnuts': {
        'protein': "Walnuts contain 15 grams of protein.",
        'vitamins': "Walnuts provide 0.6 mg of vitamins.",
        'minerals': "Walnuts have 270 mg of minerals.",
        'calories': "Walnuts have about 654 calories."
    },
    'turkey': {
        'protein': "Turkey contains 29 grams of protein.",
        'vitamins': "Turkey provides 0 mg of vitamins.",
        'minerals': "Turkey has 8 mg of minerals.",
        'calories': "Turkey has about 189 calories."
    },
    'quinoa': {
        'protein': "Quinoa contains 4.4 grams of protein.",
        'vitamins': "Quinoa provides 0 mg of vitamins.",
        'minerals': "Quinoa has 20 mg of minerals.",
        'calories': "Quinoa has about 120 calories."
    },
    'mushrooms': {
        'protein': "Mushrooms contain 3.1 grams of protein.",
        'vitamins': "Mushrooms provide 0.4 mg of vitamins.",
        'minerals': "Mushrooms have 12 mg of minerals.",
        'calories': "Mushrooms have about 22 calories."
    },
    'shrimp': {
        'protein': "Shrimp contains 20 grams of protein.",
        'vitamins': "Shrimp provides 0 mg of vitamins.",
        'minerals': "Shrimp has 2 mg of minerals.",
        'calories': "Shrimp has about 99 calories."
    },
    'blueberries': {
        'protein': "Blueberries contain 0.7 grams of protein.",
        'vitamins': "Blueberries provide 9.7 mg of vitamins.",
        'minerals': "Blueberries have 6 mg of minerals.",
        'calories': "Blueberries have about 57 calories."
    },
    'peas': {
        'protein': "Peas contain 5 grams of protein.",
        'vitamins': "Peas provide 22 mg of vitamins.",
        'minerals': "Peas have 33 mg of minerals.",
        'calories': "Peas have about 81 calories."
    },
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_response', methods=['POST'])
def get_response():
    user_message = request.json['message']
    
    # Normalize input
    user_message = user_message.lower()
    
    # Define nutrient keywords
    nutrient_keywords = ['protein', 'vitamins', 'minerals', 'calories']
    
    # Extract food item and nutrient
    food_item = None
    nutrient = None
    
    # Check for food item in message
    for item in nutrition_data.keys():
        if item in user_message:
            food_item = item
            break
    
    # Check for nutrient in message
    for keyword in nutrient_keywords:
        if keyword in user_message:
            nutrient = keyword
            break
    
    # Formulate response
    if food_item:
        if nutrient:
            bot_response = nutrition_data[food_item][nutrient]
        else:
            bot_response = "Please specify a nutrient (protein, vitamins, minerals, calories)."
    else:
        bot_response = "I'm sorry, I didn't understand that. Please ask about a specific food item."
    
    return jsonify({'response': bot_response})

if __name__ == '__main__':
    ++app.run(debug=True)