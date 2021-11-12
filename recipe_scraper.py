



import re, json, os
import requests
from lxml import html


class recipe_scraper():
    def __init__(self, recipe_url):
        self.webpage = requests.get(recipe_url)
        self.webxml = html.fromstring(self.webpage.content)
        
        self.unit_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'unit_table.json')
        with open(self.unit_file, 'r', encoding='utf-8') as open_file:
            self.unit_table = json.load(open_file)
        
        self.meta_key_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'meta_keys.txt')
        with open(self.meta_key_file, 'r', encoding='utf-8') as open_file:
            self.meta_keys = open_file.readline().split(' ')
        
        self.starting_check_pat = '(?:^|\s)'
        self.ending_check_pat = '(?:$|\s)'
        self.quant_with_unit_pat = '((?:(?:[0-9]+|[\u00BC\u00BD\u00BE])\s*\-\s*)?(?:[0-9]+|[\u00BC\u00BD\u00BE]))\s*('+'|'.join(['|'.join(i) for i in self.unit_table.values()])+')?(?:s|es)?'
        self.quant_item_pat = self.quant_with_unit_pat+self.ending_check_pat+'\s*((?:[A-Z]?[a-z\-0-9]+[\s,]+)*[A-Za-z\-0-9]+)'
        
        
    
    def get_meta_items(self):
        meta_items_table = {}
        recipe_meta_items = self.webxml.xpath('//div[@class="recipe-meta-item"]')
        for item_i in recipe_meta_items:
            meta_item_key = item_i.xpath('./div[@class="recipe-meta-item-header"]/text()')
            if len(meta_item_key) == 1:
                meta_item_key = re.findall('[a-z]+',meta_item_key[0].lower())
                if len(meta_item_key) == 1 and meta_item_key[0] in self.meta_keys:
                    meta_item_quant = item_i.xpath('./div[@class="recipe-meta-item-body"]/text()')
                    if len(meta_item_quant) == 1:
                        meta_item_quant = re.findall(self.quant_with_unit_pat+self.ending_check_pat, meta_item_quant[0].lower())
                        meta_items_table[meta_item_key[0]] = meta_item_quant
        return meta_items_table
    
    def get_ingredients(self):
        ingredient_list = []
        ingredient_items = self.webxml.xpath('//div[@class="recipe-shopper-wrapper"]//span[@class="ingredients-item-name"]/text()')
        for item_i in ingredient_items:
            ingredient_i = re.findall(self.quant_item_pat+self.ending_check_pat, item_i)
            if len(ingredient_i) == 1:
                ingredient_list.append(ingredient_i)
            else:
                print('An ingredient not parsed properly: {}'.format(item_i))
        return ingredient_list
    
    def get_directions(self):
        direction_list = self.webxml.xpath('//section[@class="component recipe-instructions recipeInstructions container"]//li[@class="subcontainer instructions-section-item"]//div[@class="paragraph"]//p/text()')
        return direction_list



if __name__ == '__main__':
    
    test_url = 'https://www.allrecipes.com/recipe/12682/apple-pie-by-grandma-ople/'
    test_scraper = recipe_scraper(test_url)
    meta_items_table = test_scraper.get_meta_items()
    print('Meta items:')
    for i in meta_items_table:
        print(i)
        print(meta_items_table[i])
    print()
    ingredient_list = test_scraper.get_ingredients()
    print('Ingredients:')
    for i in ingredient_list:
        print(i)
    print()
    direction_list = test_scraper.get_directions()
    print('Directions:')
    for i in direction_list:
        print(i)
