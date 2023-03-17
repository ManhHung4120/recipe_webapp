from flask import Blueprint,request, redirect,jsonify,make_response
from response.response_lib import *
from recipe.recipe_utils import getRecipeFromName, change_recipe_rating, userAddNewRecipe

recipe_blueprint = Blueprint("recipe_blueprint",__name__)

@recipe_blueprint.route("/recipe/name", methods = ["POST"])
def getRecipe():
    content = request.get_json(silent=True)
    recipe_name = content.get("recipe_name")
    if not recipe_name:
        raise MissingBody(MISSING_BODY_MSG %"recipe name")
    
    recipe, msg = getRecipeFromName(recipe_name)
    if msg:
        raise DatabaseError(msg)
    
    body = {
        "recipe_list":recipe,
        "msg":msg
    }
    return make_response(body, 200)
@recipe_blueprint.route("/recipe/rating", methods = ["POST"])
def getRecipeRating():
    content = request.get_json(silent=True)
    recipe_id = content.get("recipe_id")
    if not recipe_id:
        raise MissingBody(MISSING_BODY_MSG %"recipe_id")
    
    recipe, msg = change_recipe_rating(recipe_id)
    body = {
        "recipe_list":recipe,
        "msg":msg
    }
    return make_response(body, 200)


@recipe_blueprint.route("/recipe/add",methods = ["POST"])
def addNewRecipe():
    content = request.get_json(silent=True)
    recipe_name = content.get("recipe_name")
    if not recipe_name:
        raise MissingBody(MISSING_BODY_MSG %"recipe name")
    cuisine = content.get("cuisine")
    if not cuisine:
        raise MissingBody(MISSING_BODY_MSG %"cuisine")
    cook_time = content.get("cook_time")
    if not cook_time:
        raise MissingBody(MISSING_BODY_MSG %"cook time")
    creator_id = content.get("user_id")
    if not creator_id:
        raise MissingBody(MISSING_BODY_MSG %"creator id")
    description = content.get("description")
    recipe_id, msg = userAddNewRecipe(recipe_name, cuisine, cook_time, creator_id,description)
    if msg:
        raise DatabaseError(msg)
    return make_response(recipe_id,200)



    
@recipe_blueprint.errorhandler(MissingBody)
def missingbody(e):
    return jsonify(e.to_dict()), e.status_code

@recipe_blueprint.errorhandler(Unauthorized)
def unauthorized(e):
    return jsonify(e.to_dict()), e.status_code

@recipe_blueprint.errorhandler(DatabaseError)
def databaseError(e):
    return jsonify(e.to_dict()), e.status_code