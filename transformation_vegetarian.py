##--------------------TRANSFORMATION FROM MEATS TO VEGETARIAN

# pacific snapper, parrotfish, patagonian toothfish, perch, rock cod, rockfish, sablefish, scallop, sea bass, sea cucumber, sea urchin, sea scallop, shark, shellfish, snail, snapper, sturgeon, swordfish, tilapia, tuna fish, yellowfin tuna, whitefish
### elk, fish stock, fish, flounder, fly-fish, goat, goose, lingcod, mackrel, monkfish, mussel, ostrich, emu, oyster, pacific cod, pacific sanddab,
##seitan for larger meats(brisket, )
vegetarian_substitutes = {
    "tofu" : ["chicken","chicken breast", "steak", "tenderloin", "sirloin", "filet mignon", "flank", "t-bone steak","beef",  "meatballs", "beef stew", "chorizo", "bison" \
                "buffalo wings", "chicken wings", "wings", "chicken thigh", "chicken thighs","thigh","thighs","chicken leg","chicken legs", "chicken drumstick","chicken drumsticks", "drumsticks", \
                "chicken nuggets", "nuggets", "pork", "bacon", "Bacon", "OSCAR MAYER Bacon", "hot dog", "italian sausage", "Italian Sausage", "sausage","brat","kielbasa","cutlet","duck","lamb","goat","falafel","liver","gyro","venison", \
                "bluefish","butter fish","cat fish","catfish","dogfish","salmon","cod", "atlantic cod","black cod","herring","mahi-mahi","perch","trout","sardine","bass", \
                "tuna", "albacore tuna", "bigeye tuna","bluefin tuna","dogtooth tuna","shrimp","crab", "crabmeat", "cray fish","lobster","clam","octopus","squid","eel", \
                "elk", "fish", "flounder", "fly-fish", "goose", "lingcod", "mackrel", "monkfish", "mussel", "ostrich", "emu", "oyster", "pacific cod", "pacific sanddab", 
                "pacific snapper", "parrotfish", "patagonian toothfish", "rock cod", "rockfish", "sablefish", "scallop", "sea bass", "sea cucumber", "sea urchin",\
                "sea scallop", "shark", "shellfish", "snail", "snapper", "sturgeon", "swordfish", "tilapia", "tuna fish", "yellowfin tuna", "whitefish", "white carp"],
    "seitan" : [ "ham", "turkey","hamburger", "hamburgers", "cheeseburger", "cheeseburgers", "burger", "prime rib", "ribs", "rib","brisket", "halibut" "fillets halibut"],
    "mushroom" : ["salami","pepperoni","bologna", "anchovy"],
    "vegetable broth" : ["chicken broth", "beef broth"],
    "vegetable stock" : ["chicken stock", "beef stock"],
    "vegetable shortening" : ["lard"],
    "soy sauce" : ["worcestershire sauce"]
}

##vegetarian fallback
vegetarian_fallback_sentence = ['steam 14 ounce broccoli floret in pot for ~10 mins and serve',
                                'steam 14 ounce cauliflour in pot for ~10 mins and serve',
                                'cut up 1 zucchini, steam in pot for ~10 mins and serve']

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

vegetarian_fallback_sentence_rev = ['cut up chicken breast into bits and saute, serve alongside meal',
                                    'cut up steak into bits and saute, serve alongside meal ']



