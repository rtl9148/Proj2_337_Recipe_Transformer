
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


##--------------TRANSFORM BACK LISTS
mexican_substitute_rev = {
                        "bread" : ["tortillas"], ##corn or flour tortillas?? also could use lettuce instead of tortilla
                        "breakfast sausage" : ["chorizo", "chorizo sausage"],
                        "shredded pork" : ["carnita", "carnitas"],
                        "lemon" : ["lime"],
                        "black beans" : ["pinto beans"],
                        "white rice" : ["brown rice"],
                        
}
