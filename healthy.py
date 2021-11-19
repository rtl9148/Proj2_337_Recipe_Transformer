

########### HEALTHY SUBSTITUTIONS AND MODIFICATIONS ########### 
to_healthy_substitution = {
    "whole-grain brown rice":  ["rice", "brown rice", "white rice", "long grain white rice", "uncooked instant rice", "instant rice", "wild rice", "uncooked white rice", "uncooked brown rice"],
    "skim milk":               ["milk", "whole milk", "heavy cream", "half-and-half", "evaporated milk", "2% milk", "heavy whipping cream", "buttermilk", "warm milk", "cold milk"],
    "light margarine":         ["butter", "shortening", "margarine", "salted butter", "unsalted butter", "butter or margarine", "butter OR margarine"],
    "dark chocolate chips":    ["chocolate chips", "milk chocolate chips", "chocolate morsels", "bittersweet chocolate chips", "BAKER'S Semi-Sweet Baking Chocolate, melted",],
    "vegetable stock":         ["chicken broth", "chicken stock", "beef stock", "beef broth", "chicken base"],
    "ground turkey":           ["ground beef", "lean ground beef", "ground pork", "ground veal"],
    "whole-wheat flour":       ["all-purpose flour", "flour", "enriched flour"],
    "chicken sausage":         ["sausage", "pork sausage", "bulk pork sausage"],
    "extra-virgin olive oil:": ["olive oil", "canola oil", "vegetable oil", "canola", "oil"], 
    "dark chocolate":          ["chocolate", "milk chocolate", "semi-sweet chocolate"],
    "maple syrup":             ["corn syrup", "high fructose corn syrup", "light corn syrup",],
}

to_healthy_modification = {
    "reduced fat": ["cheese", "Cheddar", "Cheddar cheese", "shredded Cheddar", "shredded sharp Cheddar cheese", "American cheese", "Swiss cheese", \
                    "bacon", "turkey bacon", "mozzarella", "shredded mozzarella", "cheddar", "feta", "feta cheese", "crumbled feta",],
    "fat free":    ["plain yogurt", "yogurt", "fruit yogurt", "sour cream", "greek yogurt"],
    "sugar free":  ["ketchup", "granola", "juice", "licorice", "can peach pie filling", "peach pie filling", "barbecue sauce", "barbeque sauce", "whole cranberry sauce"], 
    "low fat":     ["cream cheese", "cream cheese, softened", "mayonnaise", "mayo", "ice cream", "PHILADELPHIA Cream Cheese, softened", \
                    "package PHILADELPHIA Cream Cheese, softened"],
    "whole grain": ["pasta", "spaghetti", "fettucine", "penne", "rigatoni", "bowtie", "farfalle", "linguine", "angel's hair", "rotini", "elbows", \
                    "macaroni", "orzo", "oat", "oats",],
    "whole wheat": ["white bread", "croissant", "rolls" "brioche", "buns", "bagels", "thick slices bread", "ciabatta rolls", "French baguette", \
                    "baguette", "rye bread", "muffin", "French bread"],
    "low sodium":  ["fish sauce", "soy sauce", "balsamic vinaigrette", "miso paste", "pimento-stuffed green olives", "can chopped tomatoes in puree", \
                    "creamy salad dressing", "cole slaw dressing", "jar sauerkraut with liquid", "beef bouillon", "cubes beef bouillon", "sauerkraut with liquid" \
                    "condensed cream of mushroom soup", "can condensed cream of mushroom soup", "Italian-style salad dressing", "Bavarian-style sauerkraut, undrained", "balsamic vinaigrette salad dressing, or to taste", "condensed cream of celery soup", "dry brown gravy mix", "bottle soy sauce", "creamy salad dressing"],
    "lean":        ["ham", "cooked ham", "chuck roast", "pork tenderloin", "rump roast", "thick cut pork chops", "pork loin roast", "pork chops", "ham hock", "chopped ham", "skinless chicken thighs", "cooked ham, crumbled"],
}

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
to_unhealthy_remove_modifier = ["reduced fat", "low fat", "fat free", "sugar free", "whole grain", "whole wheat", "low sodium", "zero calorie"]

to_unhealthy_add = []



