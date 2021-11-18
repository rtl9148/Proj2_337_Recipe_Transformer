
#Basic Lists
recipe_categories = ["Appetizer and Snacks", "BBQ & Grilling", "Bread Recipes", "Breakfast and Brunch", "Desserts", "Dinner Recipes", "Drinks", "Everyday Cooking", "Fruits, Vegetables, and Other Produce", "Holidays and Events", "Ingredients", "Lunch Recipes", "Main Dishes", "Meat and Poultry", "Pasta and Noodles", "Salad Recipes", "Seafood Recipes", "Side Dishes", "Soups, Stews, and Chili", "Trusted Brands", "U.S. Recipes", "World Cuisine"]
healthy_cooking_methods = ["Braising", "Broiling", "Grilling", "Poaching", "Sauteing", "Steaming"]

########### HEALTHY SUBSTITUTIONS AND MODIFICATIONS ########### 
to_healthy_substitution = {
    "whole-grain brown rice":  ["rice", "brown rice", "white rice", "long grain white rice", "uncooked instant rice", "instant rice", "wild rice", "uncooked white rice", "uncooked brown rice"],
    "skim milk":               ["milk", "whole milk", "heavy cream", "half-and-half", "evaporated milk", "2% milk", "heavy whipping cream", "buttermilk", "warm milk", "cold milk"],
    "light margarine":         ["butter", "shortening", "margarine", "salted butter", "unsalted butter", "butter or margarine", "butter OR margarine"],
    "dark chocolate chips":    ["chocolate chips", "milk chocolate chips", "chocolate morsels", "bittersweet chocolate chips"],
    "vegetable stock":         ["chicken broth", "chicken stock", "beef stock", "beef broth", "chicken base"],
    "ground turkey":           ["ground beef", "lean ground beef", "ground pork", "ground veal"],
    "whole-wheat flour":       ["all-purpose flour", "flour", "enriched flour"],
    "chicken sausage":         ["sausage", "pork sausage", "bulk pork sausage"],
    "extra-virgin olive oil:": ["olive oil", "canola oil", "vegetable oil", "canola", "oil"], 
    "dark chocolate":          ["chocolate", "milk chocolate", "semi-sweet chocolate"],
}

to_healthy_modification = {
    "reduced fat": ["cheese", "Cheddar", "Cheddar cheese", "shredded Cheddar", "shredded sharp Cheddar cheese", "American cheese", "Swiss cheese", "bacon", "turkey bacon", "mozzarella", "shredded mozzarella", "cheddar",],
    "fat free":    ["plain yogurt", "yogurt", "fruit yogurt", "sour cream"],
    "sugar free":  ["ketchup", "granola", "juice", "licorice", ],
    "low fat":     ["cream cheese", "cream cheese, softened", "mayonnaise", "mayo", "ice cream", ],
    "whole grain": ["pasta", "spaghetti", "fettucine", "penne", "rigatoni", "bowtie", "farfalle", "linguine", "angel's hair", "rotini", "elbows", "macaroni", "orzo", "oat", "oats",],
    "whole wheat": ["white bread", "croissant", "rolls" "brioche", "buns", "bagels", "thick slices bread", "ciabatta rolls", "French baguette", "baguette", "rye bread", "muffin"],
}

to_healthy_remove = ["salt", ]

########### UNHEALTHY SUBSTITUTIONS AND MODIFICATIONS ########### 
to_unhealthy_substitution = {
    "whole milk":           ["milk", "skim milk", "2% milk", "1% milk"],
    "milk chocolate chips": ["dark chocolate chips", "chocolate chips", "chocolate morsels", "semi-sweet chocolate chips", "semisweet chocolate chips", "bittersweet chocolate chips"],
    "beef broth":           ["vegetable stock", "chicken stock"],
    "vegetable oil":        ["canola oil", "olive oil", "extra-virgin olive oil", "avocado oil", "sesame oil", "coconut oil"],
    "ground beef":          ["ground chicken", "ground turkey", "lean ground beef", "lean ground chicken", "lean ground turkey"],
    "pork sausage":         ["chicken sausage", "turkey sausage", "lean sausage"],
    "salted butter":        ["unsalted butter", "butter substitute", "margarine", "light margarine"]
}

#List of modifiers to remove 
to_unhealthy_modification = ["reduced fat", "low fat", "fat free", "sugar free", "whole grain", "whole wheat", "low sodium", "zero calorie"]

to_unhealthy_add = []



