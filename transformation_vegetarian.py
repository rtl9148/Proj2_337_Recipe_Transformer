##--------------------TRANSFORMATION FROM MEATS TO VEGETARIAN

# pacific snapper, parrotfish, patagonian toothfish, perch, rock cod, rockfish, sablefish, scallop, sea bass, sea cucumber, sea urchin, sea scallop, shark, shellfish, snail, snapper, sturgeon, swordfish, tilapia, tuna fish, yellowfin tuna, whitefish
### elk, fish stock, fish, flounder, fly-fish, goat, goose, lingcod, mackrel, monkfish, mussel, ostrich, emu, oyster, pacific cod, pacific sanddab,
##seitan for larger meats(brisket, )
vegetarian_substitutes = {
    "tofu" : ["chicken","chicken breast", "steak", "tenderloin", "sirloin", "filet mignon", "flank", "t-bone steak","beef",  "meatballs", "beef stew", "chorizo", "bison" \
                "buffalo wings", "chicken wings", "wings", "chicken thigh", "chicken thighs","thigh","thighs","chicken leg","chicken legs", "chicken drumstick","chicken drumsticks", "drumsticks", \
                "chicken nuggets", "nuggets", "pork", "bacon", "Bacon", "OSCAR MAYER Bacon", "hot dog", "italian sausage", "Italian Sausage", "sausage","brat","kielbasa","cutlet","duck","lamb","goat","falafel","liver","gyro","venison", \
                "bluefish","butter fish","cat fish","catfish","dogfish","salmon","cod", "black cod","atlantic cod","black cod","herring","mahi-mahi","perch","trout","sardine","bass", \
                "tuna", "albacore tuna", "bigeye tuna","bluefin tuna","dogtooth tuna","shrimp","crab", "crabmeat", "cray fish","lobster","clam","octopus","squid","eel", \
                "elk", "fish", "flounder", "fly-fish", "goose", "lingcod", "mackrel", "monkfish", "mussel", "ostrich", "emu", "oyster", "pacific cod", "pacific sanddab", 
                "pacific snapper", "parrotfish", "patagonian toothfish", "perch", "rock cod", "rockfish", "sablefish", "scallop", "sea bass", "sea cucumber", "sea urchin",\
                "sea scallop", "shark", "shellfish", "snail", "snapper", "sturgeon", "swordfish", "tilapia", "tuna fish", "yellowfin tuna", "whitefish", "white carp"],
    "seitan" : [ "ham", "turkey","hamburger", "hamburgers", "cheeseburger", "cheeseburgers", "burger", "prime rib", "ribs", "rib","brisket", "halibut" "fillets halibut"],
    "mushroom" : ["salami","pepperoni","bologna", "anchovy"],
    "vegetable broth" : ["chicken broth", "beef broth"],
    "vegetable stock" : ["chicken stock", "beef stock"],
    "vegetable shortening" : ["lard"],
    "shortening" : ["lard"],
    "soy sauce" : ["worcestershire sauce"]
}

##failed recipes
##https://www.allrecipes.com/recipe/217200/cheese-and-bacon-jalapeno-rellenos/
##https://www.allrecipes.com/recipe/217193/cheddar-bacon-mac-and-cheese/
##https://www.allrecipes.com/recipe/220080/sausage-stuffed-mushrooms/
##https://www.allrecipes.com/recipe/221180/famous-meatballs/
##https://www.allrecipes.com/recipe/23923/beef-tips/
##https://www.allrecipes.com/recipe/239824/grape-jelly-meatballs/
##https://www.allrecipes.com/recipe/245131/tamarind-sauce-fish-curry/
##https://www.allrecipes.com/recipe/25871/grilled-fish-steaks/
##https://www.allrecipes.com/recipe/267143/make-ahead-sweet-potato-and-chorizo-breakfast-burritos/


##this one might get replaced with "tofu tofu" (it has bison meatballs and we substitute bison with tofu and meatballs with tofu)
##https://www.allrecipes.com/recipe/285640/bison-meatballs-with-tomatoes-and-herbs/

vegetarian_substitutes_rev = {
    "chicken" : ["tofu"],
    "beef" : ["seitan"],
    "chicken broth" : ["vegetable broth", "vegetable stock"],
    "lard" : ["vegetable shortening", "shortening"]
}

##we don't need to add anything always to a vegetarian dish, IMO we should just remove all the 
##meats and be done
vegetarian_add = {

}

##we DO need to add meat to a vegetarian dish to make it not vegetarian, so for now add just bacon
##to everything
vegetarian_add_rev = {
    "bacon" : []

}
##gumbo? stew?
###ears, shoulder, eyes, arm, body, thigh[s], butt, breast, carcass?,


## https://www.allrecipes.com/recipe/221958/chef-johns-perfect-prime-rib/
ex_ingredients = [{'name':'Prime Rib','quantity': 4.0,'measurement':'pounds','tools': '','methods' : 'roast'}, \
                    {'name':'butter','quantity': 0.25,'measurement':'cup','tools': '','methods' : ''}, \
                    {'name':'black pepper','quantity':1.0,'measurement':'tablespoon','tools': 'measuring cup','methods' : ''}, \
                    {'name':'herbes de Provence','quantity':1.0,'measurement':'teaspoon','tools': 'measuring cup','methods' : ''}, \
                    {'name':'Salt','quantity':0.0,'measurement':'','tools': '','methods' : 'kosher'}]

## https://www.allrecipes.com/recipe/20963/oven-roasted-potatoes/
ex_ingredients2 = [{'name':'olive oil','quantity': .125, 'measurement':'cup','tools': 'measuring cup','methods' : ''}, \
                    {'name':'garlic','quantity': 1.0, 'measurement':'tablespoon','tools': 'knife','methods' : 'minced'}, \
                    {'name':'basil','quantity': 0.5, 'measurement':'teaspoon','tools': 'measuring cup','methods' : 'dried'}, \
                    {'name':'marjoram','quantity': 0.5, 'measurement':'teaspoon','tools': 'measuring cup','methods' : 'dried'}, \
                    {'name':'dill weed','quantity': 0.5, 'measurement':'teaspoon','tools': 'measuring cup','methods' : 'dried'}, \
                    {'name':'thyme','quantity': 0.5, 'measurement':'teaspoon','tools': 'measuring cup','methods' : 'dried'}, \
                    {'name':'oregano','quantity': 0.5, 'measurement':'teaspoon','tools': 'measuring cup','methods' : 'dried'}, \
                    {'name':'parsley','quantity': 0.5, 'measurement':'teaspoon','tools': 'measuring cup','methods' : 'dried'}, \
                    {'name':'red pepper flakes','quantity': 0.5, 'measurement':'teaspoon','tools': 'measuring cup','methods' : 'crushed'}, \
                    {'name':'salt','quantity': 0.5, 'measurement':'teaspoon','tools': 'measuring cup','methods' : ''}, \
                    {'name':'potatoes','quantity': 4, 'measurement':'count','tools': ['peeler', 'knife'],'methods' : ['peeled', 'cubed']}]

##second list of get rid of things
##Get rid of sugar, etc

##This function will take in a list of ingredients and tranform them to contain only 
##vegetarian products
def transform_vegetarian(ingredients) :
    if len(ingredients) < 2:
        ##only have to transform first one
        x = 1
    list_vegetarian_subs = vegetarian_substitutes.keys()
    for ing in ingredients :
        if ing['name'] in list_vegetarian_subs :
            ##substitute ingredient name
            substitute(ingredient)
        ##if ingredient is in reducible_ingreidents:
            ##reduce amt


