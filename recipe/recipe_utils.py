from models import Recipe
from repo import db
from sqlalchemy import text
from sqlalchemy.exc import SQLAlchemyError

from user.user_util import getUserFromUserId


def getRecipeFromName(recipe_name):
    try:
        recipes = Recipe.query.filter(Recipe.recipe_name.ilike(f"%{recipe_name}%")).all()
    except SQLAlchemyError as e:
        return [], f"Failed to query recipe: {e.__class__.__name__}"
    recipe_objects = []
    for recipe in recipes:
        objs = {
            "recipe_name":recipe.recipe_name,
            "recipe_id":recipe.recipe_id,
            "description":recipe.description,
            "cuisine":recipe.cuisine,
            "cook_time":recipe.cook_time,     
            "rating":recipe.rating,
            "user_id":recipe.user_id      
        }
        if objs.get("user_id"):
            user = getUserFromUserId(objs.get("user_id"))
            objs["creator"] = user
        recipe_objects.append(objs)
    return recipe_objects,""

def change_recipe_rating(recipe_id):
    try:
        db.session.execute(text("call update_recipe_rating(:param)"),{"param":recipe_id})
        db.session.commit()
    except SQLAlchemyError as e:
        db.session.rollback()
        error = str(e.orig)
        return "",error
    
    return recipe_id,""

def userAddNewRecipe(recipe_name, cuisine, cook_time, creator_id, description):
    recipe_obj = Recipe(recipe_name = recipe_name, cuisine = cuisine, cook_time = cook_time, creator_id = creator_id, description = description)
    db.session.add(recipe_obj)
    db.session.commit()
    return "ok",""




        