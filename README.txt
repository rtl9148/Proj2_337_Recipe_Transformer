GitHub Repo: https://github.com/rtl9148/Proj2_337_Recipe_Transformer

## SETUP

Run the following command:

python -m pip install requests

pip install lxml

pip install -U spacy

python -m spacy download en_core_web_sm

## RUNNING THE CODE

The interface is defined by the function recipe_ui() in recipe_scraper.py and it uses the main class recipe_scraper() in the same file. Run recipe_scraper.py by "python recipe_scraper.py" will run the recipe interface by default.

recipe_scraper.py relies on 5 files: healthy.py, ingredient_list.py, lactose_free.py, transformation_mexican.py, transformation_vegetarian.py
