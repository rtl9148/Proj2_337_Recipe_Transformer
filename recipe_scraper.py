



import re, json, os
from fractions import Fraction
import requests, spacy
from lxml import html

from transformation_vegetarian import vegetarian_substitutes_rev, vegetarian_substitutes, vegetarian_fallback_sentence, vegetarian_fallback_sentence_rev
from transformation_mexican import mexican_substitute, mexican_add, mexican_fallback_sentence
from healthy import to_healthy_substitution, to_healthy_modification, to_unhealthy_substitution, to_unhealthy_remove_modifier, healthy_fallback_sentence, unhealthy_fallback_sentence
from lactose_free import lactose_free_substitution, lactose_free_modifiers, lactose_free_fallback_sentence
from ingredient_list import ingredient_list

spacy_nlp = spacy.load("en_core_web_sm")


def normalize_keyword(keyword_in):
    word_tokens = spacy_nlp(keyword_in)
    return ' '.join([i.text for i in word_tokens[:-1]]+[word_tokens[-1].lemma_.lower()]).replace(' - ','-')

def normalize_keyword_tokens(word_tokens):
        return ' '.join([i.text for i in word_tokens[:-1]]+[word_tokens[-1].lemma_.lower()]).replace(' - ','-')
    
def original_keyword_tokens(word_tokens):
    return ' '.join([i.text for i in word_tokens]).replace(' - ','-')

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

unit_table = {"degree": ["degree", "C", "F"],
"hour": ["hr", "hour"], 
"minute": ["min", "minute"],
"second": ["sec", "second"],
'teaspoon': ['teaspoon', 'tsp.'],
'tablespoon': ['tablespoon', 'tbl.', 'tbs.', 'tbsp.'],
'fluid ounce': ['fluid ounce', 'fl oz'],
'gill': ['gill'],
'cup': ['cup'],
'pint': ['pint', 'pt', 'fl pt'],
'quart': ['quart', 'qt', 'fl qt'],
'gallon': ['gallon', 'gal'],
'ml': ['ml', 'milliliter', 'millilitre', 'cc', 'mL'],
'l': ['l', 'liter', 'litre', 'L'],
'dl': ['dl', 'deciliter', 'decilitre', 'dL'],
'pound': ['pound', 'lb', '#'],
'ounce': ['ounce', 'oz'],
'mg': ['mg', 'milligram', 'milligramme'],
'g': ['g', 'gram', 'gramme'],
'kg': ['kg', 'kilogram', 'kilogramme'],
'mm': ['mm', 'millimeter', 'millimetre'],
'cm': ['cm', 'centimeter', 'centimetre'],
'm': ['m', 'meter', 'metre'],
'inch': ['inch', 'in', '"'],
'pinch': ['pinch'],
}

non_convertible_unit = {'degree':True,
                        'hour': True,
                        'minute': True,
                        'second': True,}

rev_unit_table = {}
for key_i in unit_table:
    for word_i in unit_table[key_i]:
        assert not word_i in rev_unit_table
        rev_unit_table[word_i] = key_i

cooking_tools = ['knife', 'pan', 'skillet', 'spoon', 'scale', 'blender', 'bowl', 'whisk', 'grater', 
                 'shear', 'tong', 'towel', 'sponge', 'pot', 'stockpot', 'spatula', 'saucepan', 
                 'colander', 'peeler', 'ladle', 'scoop', 'sieve', 'scissor', 'funnel', 'food mill', 
                 'wooden spoon', 'pepper mill', 'slat shaker', 'oven glove', 'paper towel', 'chef\'s knife', 
                 'cutting board', 'can opener', 'measuring cup', 'measuring spoon', 'mixing bowl', 
                 'vegetable peeler', 'potato masher', 'salad spinner', 'citrus juicer', 'garlic press', 
                 'paring knife', 'bread knife', 'honing rod', 'sharpening rod', 'knife sharpener', 
                 'non-stick skillet', 'stainless steel skillet', 'sauté pan', 'small saucepan', 
                 'medium saucepan', 'large saucepan', 'cast iron skillet', 'cast-iron skillet', 
                 'grill pan', 'sheet pan', 'muffin pan', 'casserole dish', 'broiler pan', 'stirring spoon', 
                 'slotted spoon', 'oven mitt', 'trivet', 'splatter guard', 'thermometer', 'immersion blender', 
                 'kitchen scale', 'food storage containers', 'aluminum foil', 'parchment paper', 'ice cube tray', 'Dutch oven']

cooking_tool_table = {i:True for i in cooking_tools}

cooking_methods = ['roasting', 'baking', 'broiling', 'frying', 'steaming', 'boiling', 'simmering', 'braising', 
                   'poaching', 'blanching', 'grilling', 'sauteing', 'searing', 'pressure cooking', 'slow cooking', 
                   'stewing', 'barbecuing', 'barding', 'broasting', 'microwaving']

cooking_method_table_normalized = {normalize_keyword(i):i for i in cooking_methods}
cooking_method_table = {i:cooking_method_table_normalized[i] for i in cooking_method_table_normalized}


cooking_methods_secondary = ['basting', 'browning', 'chopping', 'coddling', 'creaming', 'curdling', 'curing', 'deglazing',
                             'degreasing', 'dredging', 'canning', 'frosting', 'glazing', 'larding', 'low-temperature cooking', 
                             'mincing', 'pickling', 'proofing', 'rendering', 'ricing', 'seasoning', 'shrivelling', 'skimming', 'smoking', 
                             'smothering', 'souring', 'steeping', 'stir frying', 'stuffing', 'sugar panning', 'sweating', 
                             'Swissing', 'thickening', 'velveting']

cooking_method_secondary_table_normalized = {normalize_keyword(i):i for i in cooking_methods_secondary}
cooking_method_secondary_table = {i:cooking_method_secondary_table_normalized[i] for i in cooking_method_secondary_table_normalized}


meta_keys = ['prep', 'cook', 'total', 'servings', 'yield', 'additional']

trans_substitute_table = {'vegetarian':vegetarian_substitutes, 
                          'non-vegetarian': vegetarian_substitutes_rev,
                          'Mexican': mexican_substitute, 
                          'healthy': to_healthy_substitution,
                          'unhealthy': to_unhealthy_substitution,
                          'lactose-free':lactose_free_substitution,}
trans_modifier_table = {'healthy': to_healthy_modification,
                        'lactose-free': lactose_free_modifiers,}
trans_addition_table = {'Mexican': mexican_add,}

trans_removal_table = {'unhealthy': to_unhealthy_remove_modifier}

trans_fallback_table = {'vegetarian':vegetarian_fallback_sentence, 
                        'non-vegetarian': vegetarian_fallback_sentence_rev,
                        'Mexican': mexican_fallback_sentence, 
                        'healthy': healthy_fallback_sentence,
                        'unhealthy': unhealthy_fallback_sentence,
                        'lactose-free':lactose_free_fallback_sentence,}

trans_word_table = {}
operation_flag = 'sub'
cur_trans_table = trans_substitute_table
for trans_i in cur_trans_table:
    for change_i in cur_trans_table[trans_i]:
        for word_i in cur_trans_table[trans_i][change_i]:
            if word_i in trans_word_table:
                assert not trans_i in trans_word_table[word_i], str(trans_i)+' '+str(word_i)
                trans_word_table[word_i][trans_i] = (operation_flag, change_i)
            else:
                trans_word_table[word_i] = {trans_i: (operation_flag, change_i)}

operation_flag = 'mod'
cur_trans_table = trans_modifier_table
for trans_i in cur_trans_table:
    for change_i in cur_trans_table[trans_i]:
        for word_i in cur_trans_table[trans_i][change_i]:
            if word_i in trans_word_table:
                assert not trans_i in trans_word_table[word_i], str(trans_i)+' '+str(word_i)
                trans_word_table[word_i][trans_i] = (operation_flag, change_i)
            else:
                trans_word_table[word_i] = {trans_i: (operation_flag, change_i)}
            
operation_flag = 'add'
cur_trans_table = trans_addition_table
for trans_i in cur_trans_table:
    for change_i in cur_trans_table[trans_i]:
        for word_i in cur_trans_table[trans_i][change_i]:
            if word_i in trans_word_table:
                assert not trans_i in trans_word_table[word_i], str(trans_i)+' '+str(word_i)
                trans_word_table[word_i][trans_i] = (operation_flag, change_i)
            else:
                trans_word_table[word_i] = {trans_i: (operation_flag, change_i)}

operation_flag = 'rem'
cur_trans_table = trans_addition_table
for trans_i in cur_trans_table:
    for word_i in cur_trans_table[trans_i]:
        if word_i in trans_word_table:
            assert not trans_i in trans_word_table[word_i], str(trans_i)+' '+str(word_i)
            trans_word_table[word_i][trans_i] = (operation_flag, '')
        else:
            trans_word_table[word_i] = {trans_i: (operation_flag, '')}

commond_set = {
               '1':'vegetarian',
               '2':'non-vegetarian',
               '3':'Mexican',
               '4':'healthy',
               '5':'unhealthy',
               '6':'lactose-free',
               '7':'doubled',
               '8':'halved',
               }           

def check_url(url_in):
    return re.search('https://www.allrecipes.com/recipe/[0-9]+/', url_in)

def recipe_ui():
    next_input = ''
    while next_input != 'quit':
        next_input = input('Please input a URL from a recipe from Allrecipe.com\nOr type \'quit\' to quit\n')
        if check_url(next_input):
            cur_scraper = None
            try:
                cur_scraper = recipe_scraper(next_input)
            except:
                print('Failed to process the recipe! Please try again!')
                
            if cur_scraper:
                input_prompt = 'Please type a command to make the transformation:\n'
                for command_i in commond_set:
                    input_prompt += 'Type \''+ command_i + '\': '+ commond_set[command_i]+'\n'
                input_prompt += 'Otherwise, type \'quit\' to quit or \'back\' to change recipe\n'
                
                parsed_output = {'ingredient':[],'direction':[]}
                while next_input != 'quit' and next_input != 'back':
                    next_input = input(input_prompt)
                    if next_input in commond_set:
                        cur_ingredient_str_list_input = parsed_output['ingredient']
                        cur_direction_str_list_input = parsed_output['direction']
                        output_str, parsed_output = cur_scraper.transform_recipe(commond_set[next_input], ingredient_str_list_input=cur_ingredient_str_list_input, direction_str_list_input=cur_direction_str_list_input)
                        print(output_str)
                    elif next_input != 'quit' and next_input != 'back':
                        print('Invalid command! Please try again!\n')
        
        elif next_input != 'quit':
            print('Invalid url! Please use a url of the form https://www.allrecipes.com/recipe/...')
            
        

class recipe_scraper():
    def __init__(self, recipe_url):
        self.webpage = requests.get(recipe_url)
        self.webxml = html.fromstring(self.webpage.content)
        
        self.keyword_limit = 3
        self.ingredient_list = []
        
    def check_number(self, str_in):
        found_number = re.search('([1-9]/[1-9][0-9]*|[1-9][0-9]*|[\u00BC\u00BD\u00BE\u2150-\u215F])', str_in)
        found_number = found_number[1] if found_number else ''
        return found_number
    
    def convert_number(self, str_in):
        if '/' in str_in:
            return Fraction(str_in)
        elif str_in in dict_vulgar_fraction_unicodes:
            return  Fraction(dict_vulgar_fraction_unicodes[str_in])
        elif str_in.isnumeric():
            return int(str_in)
        elif re.search('[0-9]+\.[0-9]+', str_in):
            return float(str_in)
        else:
            return ''
    
    def check_keyword(self, str_in, keyword_table):
        found_keyword = re.search('(?:^|\s)('+'|'.join(keyword_table)+')(?:$|\s)', str_in)
        found_keyword = rev_unit_table[found_keyword[1]] if found_keyword else ''
        
    def check_ingredient(self, word_in, check_word):
        len_diff = abs(len(word_in) - len(check_word))
        matched = False
        longer = False
        if len(word_in) <= len(check_word):
            matched = word_in == check_word[len_diff:]
        else:
            matched = word_in[len_diff:] == check_word
            longer = True
        return (matched, longer)
    
    def check_ingredient_list(self, ingredient_in, cur_ingredients, to_update = True):
        found_ingredient = False
        to_replace = ''
        for check_i in cur_ingredients:
            check_result = self.check_ingredient(check_i, ingredient_in)
            if check_result[0]:
                found_ingredient = True
                if check_result[1]:
                    to_replace = check_i
                break
        if to_replace and to_update:
            cur_ingredients.remove(to_replace)
            cur_ingredients.append(ingredient_in)
        return found_ingredient
                       
    def combine_list(self, list_1, list_2):
        for str_i in list_2:
            if not str_i in list_1:
                list_1.append(str_i)
        return list_1
        
            
    def transform_recipe(self, trans_choice, ingredient_str_list_input = [], direction_str_list_input = []):
        
        parsed_output = {'ingredient':[],'direction':[]}
        ingredient_tracking = []
        cooking_tool_tracking = []
        cooking_method_tracking = []
        cooking_method_sec_tracking = []
        change_record_tracking = {'rem':{},'mod':{},'add':{},'sub':{}}
        
        ingredient_str_list = ingredient_str_list_input if ingredient_str_list_input else self.get_ingredients()
        for str_i in ingredient_str_list:
            parsed_list, found_ingredient, found_cooking_tool, found_cooking_method, found_cooking_method_sec, change_record = self.transform_str(str_i, trans_choice, found_ingredient = ingredient_tracking)
            ingredient_tracking = found_ingredient
            cooking_tool_tracking = self.combine_list(cooking_tool_tracking, found_cooking_tool)
            cooking_method_tracking = self.combine_list(cooking_method_tracking, found_cooking_method)
            cooking_method_sec_tracking = self.combine_list(cooking_method_sec_tracking, found_cooking_method_sec)
            for key_i in change_record_tracking:
                change_record_tracking[key_i].update(change_record[key_i])
            parsed_output['ingredient'].append(' '.join(parsed_list))
            
        
        direction_str_list = direction_str_list_input if direction_str_list_input else self.get_directions()
        for str_i in direction_str_list:
            parsed_list, found_ingredient, found_cooking_tool, found_cooking_method, found_cooking_method_sec, change_record = self.transform_str(str_i, trans_choice, found_ingredient=ingredient_tracking,  to_update_ingredient=False, num_default=False)
            cooking_tool_tracking = self.combine_list(cooking_tool_tracking, found_cooking_tool)
            cooking_method_tracking = self.combine_list(cooking_method_tracking, found_cooking_method)
            cooking_method_sec_tracking = self.combine_list(cooking_method_sec_tracking, found_cooking_method_sec)
            for key_i in change_record_tracking:
                change_record_tracking[key_i].update(change_record[key_i])
            parsed_output['direction'].append(' '.join(parsed_list))
            
        output_str = ''
        output_str += '\n\n==============================================================================\n\n\n'
        output_str += 'Cooking tools:\n'
        output_str += ', '.join(cooking_tool_tracking)+'\n'
        output_str += 'Cooking methods:\n'
        output_str += ', '.join(cooking_method_tracking)+'\n'
        output_str += 'Secondary cooking methods:\n'
        output_str += ', '.join(cooking_method_sec_tracking)+'\n\n'
        
        output_str += '\nIngredients:\n\n'
        cur_ind = 1
        for str_i in parsed_output['ingredient']:
            output_str += 'Ingredient-'+str(cur_ind)+': '+str_i+'\n\n'
            cur_ind += 1
        output_str += '\nDirections:\n\n'
        cur_ind = 1
        for str_i in parsed_output['direction']:
            output_str += 'Step-'+str(cur_ind)+': '+str_i+'\n\n'
            cur_ind += 1
            
        added_fall_back = ''
        if not any(change_record_tracking[i] for i in change_record_tracking) and trans_choice in trans_fallback_table:
            choose_ind = len(output_str)%len(trans_fallback_table[trans_choice])
            output_str += 'Step-'+str(cur_ind)+': '+trans_fallback_table[trans_choice][choose_ind]+'\n'
            added_fall_back = trans_fallback_table[trans_choice][choose_ind]
            
        output_str += '\n==============================================================================\n\n\n'
        output_str += '\n\n\n***Changes for the transformation:\n'
        if added_fall_back:
            output_str += 'Uses the fall back plan: '+added_fall_back+'\n'
        else:
            if trans_choice == 'doubled':
                output_str += 'Doubled the ingredients\n'
            elif trans_choice == 'halved':
                output_str += 'Halved the ingredients\n'
            else:
                if change_record_tracking['rem']:
                    for key_i in change_record_tracking['rem']:
                        output_str += "Removed "+key_i+'\n'
                if change_record_tracking['sub']:
                    for key_i in change_record_tracking['sub']:
                        output_str += "Replaced "+key_i+' by '+change_record_tracking['sub'][key_i]+'\n'
                if change_record_tracking['add']:
                    for key_i in change_record_tracking['sub']:
                        output_str += "Added "+change_record_tracking['sub'][key_i]+' to '+key_i+'\n'
                if change_record_tracking['mod']:
                    for key_i in change_record_tracking['mod']:
                        output_str += "Added "+change_record_tracking['mod'][key_i]+' to '+key_i+'\n'
        
        output_str = output_str.replace(' .', '.').replace(' ,',',')
        return output_str, parsed_output
        
            
        
        
    def transform_str(self, str_in, trans_choice, found_ingredient = [], to_update_ingredient=True, num_default=True):
        token_list = spacy_nlp(str_in)
        found_cooking_tool = []
        found_cooking_method = []
        found_cooking_method_sec = []
        change_record = {'rem':{},'mod':{},'add':{},'sub':{}}
        
        parsed_list = []
        
        start_ind = 0
        cur_ind = 0
        while start_ind < len(token_list):
            found_word = False
            found_num = self.check_number(token_list[cur_ind].text)
            if found_num:
                to_convert = num_default
                if cur_ind + 1 < len(token_list) and token_list[cur_ind + 1].lemma_ in rev_unit_table:
                    num_unit = rev_unit_table[token_list[cur_ind + 1].lemma_]
                    if num_unit in non_convertible_unit:
                        to_convert = False
                    else:
                        to_convert = True
                if to_convert:
                    converted_num = self.convert_number(found_num)
                    if converted_num:
                        if trans_choice == 'doubled':
                            found_num = str(2*converted_num)
                        elif trans_choice == 'halved':
                            found_num = str(converted_num/2) if converted_num//2==0 else str(converted_num//2)
                parsed_list.append(found_num)
                start_ind += 1
                cur_ind = start_ind
            else:
                cur_ind = start_ind + min(self.keyword_limit, len(token_list) - start_ind)
                while cur_ind > start_ind:
                    cur_word_tokens = token_list[start_ind:cur_ind]
                    cur_normal_word = normalize_keyword_tokens(cur_word_tokens)
                    cur_original_word = original_keyword_tokens(cur_word_tokens)
                    if cur_normal_word in trans_word_table:
                        #transformation
                        word_operation = trans_word_table[cur_normal_word]
                        if trans_choice in word_operation:
                            found_word = True
                            word_trans = trans_word_table[cur_normal_word][trans_choice]
                            if word_trans[0] != 'rem':
                                self.check_ingredient_list(cur_normal_word, found_ingredient, to_update = to_update_ingredient)
                                if word_trans[0] == 'mod':
                                    word_change = word_trans[1]+' '+cur_original_word
                                    parsed_list.append(word_change)
                                elif word_trans[0] == 'add':
                                    word_change = cur_original_word + ' (add '+word_trans[1]+')'
                                    parsed_list.append(word_change)
                                else:
                                    word_trans[0] == 'sub'
                                    word_change = word_trans[1]
                                    parsed_list.append(word_trans[1])
                            else:
                                word_change = ''
                            change_record[word_trans[0]][cur_normal_word] = word_trans[1]
                    if cur_normal_word in rev_unit_table and not found_word:
                        found_word = True
                        parsed_list.append(cur_original_word)
                    if cur_normal_word in cooking_method_table:
                        found_cooking_method.append(cur_normal_word)
                    elif cur_normal_word in cooking_method_table_normalized:
                        found_cooking_method.append(cooking_method_table_normalized[cur_normal_word])
                    elif cur_normal_word in cooking_method_secondary_table:
                        found_cooking_method_sec.append(cur_normal_word)
                    elif cur_normal_word in cooking_method_secondary_table_normalized:
                        found_cooking_method_sec.append(cooking_method_secondary_table_normalized[cur_normal_word])
                    elif cur_normal_word in cooking_tool_table:
                        found_cooking_tool.append(cur_normal_word)
                    if found_word:
                        start_ind = cur_ind
                        break
                    cur_ind -= 1
                if not found_word:
                    parsed_list.append(token_list[start_ind].text)
                    start_ind += 1
                    cur_ind = start_ind
                
        return parsed_list, found_ingredient, found_cooking_tool, found_cooking_method, found_cooking_method_sec, change_record
        
    
    def get_meta_items(self):
        meta_items_table = {}
        recipe_meta_items = self.webxml.xpath('//div[@class="recipe-meta-item"]')
        for item_i in recipe_meta_items:
            meta_item_key = item_i.xpath('./div[@class="recipe-meta-item-header"]/text()')
            if len(meta_item_key) == 1:
                meta_item_key = re.findall('[a-z]+',meta_item_key[0].lower())
                if len(meta_item_key) == 1 and meta_item_key[0] in meta_keys:
                    meta_item_quant = item_i.xpath('./div[@class="recipe-meta-item-body"]/text()')
                    if len(meta_item_quant) == 1:
                        meta_item_quant = re.findall(self.quant_with_unit_pat+self.ending_check_pat, meta_item_quant[0].lower())
                        meta_items_table[meta_item_key[0]] = meta_item_quant
        return meta_items_table
    
    def get_ingredients(self):
        ingredient_items = [str(i) for i in self.webxml.xpath('//div[@class="recipe-shopper-wrapper"]//span[@class="ingredients-item-name"]/text()')]
        return ingredient_items
    
    def get_directions(self):
        direction_list = [str(i) for i in self.webxml.xpath('//section[@class="component recipe-instructions recipeInstructions container"]//li[@class="subcontainer instructions-section-item"]//div[@class="paragraph"]//p/text()')]
        return direction_list
    
    



if __name__ == '__main__':
    
    recipe_ui()
    
# =============================================================================
#     print(len(trans_word_table))
#     print(cooking_tool_table)
#     print(cooking_method_table_normalized)
#     print(cooking_method_secondary_table_normalized)
# =============================================================================
    
    
# =============================================================================
#     print(len(cooking_methods_secondary))
#     cooking_methods_check = []
#     for i in cooking_methods_check:
#         for j in cooking_methods:
#             if i[:5] == j[:5]:
#                 print(i,j)
# =============================================================================
# =============================================================================
#     for ind1 in range(len(cooking_tools)):
#         for ind2 in range(len(cooking_tools)):
#             if cooking_tools[ind1] == cooking_tools[ind2] and ind1!=ind2:
#                 print(cooking_tools[ind1])
# =============================================================================

# =============================================================================
#     test_url = 'https://www.allrecipes.com/recipe/12682/apple-pie-by-grandma-ople/'
#     test_url = 'https://www.allrecipes.com/recipe/43655/perfect-turkey/'
#     test_scraper = recipe_scraper(test_url)
#     test_scraper.transform_recipe('doubled')
# =============================================================================
# =============================================================================
#     meta_items_table = test_scraper.get_meta_items()
#     print('Meta items:')
# # =============================================================================
# #     for i in meta_items_table:
# #         print(i)
# #         print(meta_items_table[i])
# #     print()
# # =============================================================================
#     ingredient_list = test_scraper.get_ingredients()
#     print('Ingredients:')
#     for i in ingredient_list:
#         parsed_list, found_ingredient, found_cooking_tool, found_cooking_method, found_cooking_method_sec, change_record = test_scraper.transform_str(i, 'vegetarian')
#         print(parsed_list)
#         print(found_ingredient)
#         print(found_cooking_tool)
#         print(found_cooking_method)
#         print(found_cooking_method_sec)
#         print(change_record)
#         
#     print()
#     direction_list = test_scraper.get_directions()
#     print('Directions:')
#     for i in direction_list:
#         parsed_list, found_ingredient, found_cooking_tool, found_cooking_method, found_cooking_method_sec, change_record = test_scraper.transform_str(i, 'vegetarian')
#         print(parsed_list)
#         print(found_ingredient)
#         print(found_cooking_tool)
#         print(found_cooking_method)
#         print(found_cooking_method_sec)
#         print(change_record)
# =============================================================================
