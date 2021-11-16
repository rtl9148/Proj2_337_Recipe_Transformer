vegetarian_substitutes = {}

vegetarian_substitutes['chicken broth'] = 'vegetable broth'
vegetarian_substitutes['beef broth'] = 'vegetable broth'

##steak and steak cuts
#steak(tenderloin, sirloin, filet mignon, flank, skirt, t-bone )
vegetarian_substitutes['steak'] = 'tofu'
vegetarian_substitutes['tenderloin'] = 'tofu'
vegetarian_substitutes['sirloin'] = 'tofu'
vegetarian_substitutes['filet mignon'] = 'tofu'
vegetarian_substitutes['flank'] = 'tofu'
vegetarian_substitutes['t-bone'] = 'tofu'

##beef and beef types
##hamburger(burger), prime rib, brisket, buffalo, oxtail
vegetarian_substitutes['beef'] = 'tofu'
vegetarian_substitutes['hamburger'] = 'seitan' ##beans, portabello mushrooms
vegetarian_substitutes['hamburgers'] = 'seitan'
vegetarian_substitutes['burger'] = 'seitan'
vegetarian_substitutes['prime rib'] = 'seitan'
vegetarian_substitutes['ribs'] = 'seitan'
vegetarian_substitutes['rib'] = 'seitan'
vegetarian_substitutes['brisket'] = 'seitan'
vegetarian_substitutes['buffalo'] = 'seitan'
vegetarian_substitutes['oxtail'] = 'beans'
#meatloaf, meatballs
vegetarian_substitutes['meat'] = 'beans' 

##chicken and chicken types
##wings, breast, thigh, leg, drumsticks, nuggets, feet
vegetarian_substitutes['chicken'] = 'tofu' ##bird, pheasant
vegetarian_substitutes['chicken wings'] = 'tofu'
vegetarian_substitutes['wings'] = 'tofu'
vegetarian_substitutes['chicken thigh'] = 'tofu'
vegetarian_substitutes['chicken thighs'] = 'tofu'
vegetarian_substitutes['thighs'] = 'tofu'
vegetarian_substitutes['chicken leg'] = 'tofu'
vegetarian_substitutes['chicken legs'] = 'tofu'
vegetarian_substitutes['chicken drumstick'] = 'tofu'
vegetarian_substitutes['chicken drumsticks'] = 'tofu'
vegetarian_substitutes['chicken nuggets'] = 'tofu'
vegetarian_substitutes['chicken nugget'] = 'tofu'

##lunch meats/sliced meats
##salami, ham, chicken, turkey, bologna, pepperoni
vegetarian_substitutes['salami'] = 'seitan'
vegetarian_substitutes['ham'] = 'seitan'
##vegetarian_substitutes['chicken'] = 'tofu'
vegetarian_substitutes['turkey'] = 'seitan'
vegetarian_substitutes['bologna'] = 'seitan'
vegetarian_substitutes['pepperoni'] = 'mushroom'
##bacon, hot dog , sausage, brat, kielbasa, cutlet
vegetarian_substitutes['pork'] = 'tofu' ##jackfruit for pulled pork dishes
vegetarian_substitutes['bacon'] = 'tofu'
vegetarian_substitutes['hot dog'] = 'tofu'
vegetarian_substitutes['sausage'] = 'tofu'
vegetarian_substitutes['brat'] = 'tofu'
vegetarian_substitutes['kielbasa'] = 'tofu'
vegetarian_substitutes['cutlet'] = 'tofu'


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
            substitute(ingredient)
        ##if ingredient is in reducible_ingreidents:
            ##reduce amt


