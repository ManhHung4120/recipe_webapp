from flask import Blueprint,request, redirect,jsonify,make_response
from user.user_util import getUserFromCredential
from response.response_lib import *
user_blueprint = Blueprint("user_blueprint",__name__)

@user_blueprint.route("/user/login", methods = ["POST"])
def userLogin():
    content = request.get_json(silent=True)
    username = content.get("username")
    if not username:
        raise MissingBody(MISSING_BODY_MSG %"username")
    password = content.get("password")
    if not password:
        raise MissingBody(MISSING_BODY_MSG %"password")
    user = getUserFromCredential(username,password)
    if not user:
        raise Unauthorized(WRONG_USERNAME_OR_PASSWORD)
    
    return make_response(user,200)
    
@user_blueprint.errorhandler(MissingBody)
def missingbody(e):
    return jsonify(e.to_dict()), e.status_code

@user_blueprint.errorhandler(Unauthorized)
def unauthorized(e):
    return jsonify(e.to_dict()), e.status_code