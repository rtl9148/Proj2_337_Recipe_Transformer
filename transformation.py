

#vegetarian_substitutes['milk'] = 'almond milk'
#vegetarian_substitutes['cheese'] = 'vegetarian cheese'
#vegetarian_substitutes['eggs'] = 'tofu scramble'

#vegetarian_substitutes['butter'] = 'vegetarian butter'
#vegetarian_substitutes['yogurt'] = 'vegetarian yogurt'
#vegetarian_substitutes['sour cream'] = 'vegetarian sour cream'
#vegetarian_substitutes['mayonnaise'] = 'vegetarian mayonnaise'
#vegetarian_substitutes['gelatin'] = 'agar flakes'
#vegetarian_substitutes['honey'] = 'sweetener'
#vegetarian_substitutes['sugar'] = 'beet sugar'
#vegetarian_substitutes['chocolate'] = 'non-dairy vegetarian chocolate bar'
#vegetarian_substitutes['ice cream'] = 'non-dairy vegetarian ice-cream'

vegetarian_substitutes = {}

vegetarian_substitutes['chicken broth'] = 'vegetable broth'
vegetarian_substitutes['beef broth'] = 'vegetable broth'

#steak(tenderloin, sirloin, filet mignon, flank, skirt, t-bone )
vegetarian_substitutes['steak'] = 'tofu'
##hamburger(burger), prime rib, brisket, buffalo, oxtail
vegetarian_substitutes['beef'] = 'tofu'
#meatloaf, meatballs
vegetarian_substitutes['meat'] = 'beans' 
##wings, breast, thigh, leg, feet, drumsticks, nuggets
vegetarian_substitutes['chicken'] = 'tofu' ##bird, pheasant

##lunch meats/sliced meats
##salami, ham, chicken, turkey, bologna, pepperoni

##bacon, hot dog , sausage, brat, kielbasa, cutlet
vegetarian_substitutes['pork'] = 'tofu' ##jackfruit for pulled pork dishes
vegetarian_substitutes['duck'] = 'tofu'
#falafel, gyro, venison, lamb
vegetarian_substitutes['goat'] = 'tofu'
vegetarian_substitutes['liver'] = 'tofu'
##

vegetarian_substitutes['turkey'] = 'tofu' ##bird
vegetarian_substitutes['ham'] = 'tofu'

##seitan for larger meats(brisket, )

##gumbo? stew?
###ears, shoulder, eyes, arm, body, thigh[s], butt, breast, carcass?,

##mexican stuff
##chorizo, masa(flour/dough), tortilla

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
            substitute(ingredient, )
        ##if ingredient is in reducible_ingreidents:
            ##reduce amt


