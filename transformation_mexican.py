
###Things that can be substituted
##tortilla, lime, 

###things that can be added


##substitutions

mexican_substitute = {
                        "oregano" : ["thyme", "marjoram"],
                        "cilantro" : ["coriander", "curry powder", "garam masala","caraway", "parsley","basil"], ##"lettuce","romaine lettuce", "cabbage"],
                        "cumin" : ["caraway seeds", "black cumin"],
                        "paprika" : ["cayenne pepper", "chili powder"],
                        "pinto beans" : ["black beans", "black eyed peas", "black-eyed peas", "garbanzo beans", "kidney beans", "lima beans"],
                        "brown rice" : ["white rice", "jasmine rice", "basmati rice" "wild rice", "rice"], 
                        "lime" : ["lemon"]
                        
}
                        
##list of additives
##mexican_add = [ "cilantro" , "pinto beans", "lime", 'salsa', 'garlic powder', 'onion'] ##onion needs to be chopped

 
 ##cilantro works with just about everything
 ##avocado works with any dish that has meat I guess
 ##jalapeno peppers can be added to anything that has meat(make the meat spicier yum!)
 ##lime can be added to any stews or soups
 ##cinnamon goes in anything that's like a dessert
mexican_add = { ##"cilantro" : [],
                "avocado" : ["chicken","chicken breast", "steak", "tenderloin", "sirloin", "filet mignon", "flank", "t-bone steak","beef", \
                            "buffalo wings", "chicken wings", "wings", "chicken thigh", "chicken thighs","thigh","thighs","chicken leg","chicken legs", "chicken drumstick","chicken drumsticks", "drumsticks", \
                            "chicken nuggets", "nuggets", "pork" ],
                "jalapeno peppers" : ["chicken","chicken breast", "steak", "tenderloin", "sirloin", "filet mignon", "flank", "t-bone steak","beef", \
                                    "buffalo wings", "chicken wings", "wings", "chicken thigh", "chicken thighs","thigh","thighs","chicken leg","chicken legs", "chicken drumstick","chicken drumsticks", "drumsticks", \
                                    "chicken nuggets", "nuggets", "pork"],
                "lime" : ["soup", "stew", "water"],
                "salsa" : ["avocado", ""],
                "cinnamon" : ["white sugar", "sugar", "brown sugar"] }
##modifiers

##microwave 1 pouch instant brown rice & serve alongside recipe

mexican_fallback = [
    "brown rice"
]

##--------------TRANSFORM BACK LISTS
mexican_substitute_rev = {
                        "bread" : ["tortillas"], ##corn or flour tortillas?? also could use lettuce instead of tortilla
                        "breakfast sausage" : ["chorizo", "chorizo sausage"],
                        "shredded pork" : ["carnita", "carnitas"],
                        "lemon" : ["lime"],
                        "black beans" : ["pinto beans"],
                        "white rice" : ["brown rice"],
                        
}

##serve 1 slice bread alongside dish(no preparation necessary)
#
mexican_fallback_rev = [
    "bread"
]

dict_vulgar_fraction_unicodes = {
    '\u00BC' : '1/4',
    '\u00BD' : '1/2',
    '\u00BE' : '3/4',
    '\u2150' : '1/7',
    '\u2151' : '1/9',
    '\u2152' : '1/10',
    '\u2153' : '1/3',
    '\u2154' : '2/3',
    '\u2155' : '1/5',
    '\u2156' : '2/5',
    '\u2157' : '3/5',
    '\u2158' : '4/5',
    '\u2159' : '1/6',
    '\u215A' : '5/6',
    '\u215B' : '1/8',
    '\u215C' : '3/8',
    '\u215D' : '5/8',
    '\u215E' : '7/8',
    '\u215F' : '1',
    '\u2189' : '0/3'
}
