from image.image_utils import getImageFromImageId
from models import User
from sqlalchemy.exc import SQLAlchemyError

from response.static_lib import DEFAULT_PROFILE_PICTURE


def getUserFromCredential(username,password):
    user = User.query.filter_by(username = username, password=password).first()
    user_obj = {}
    if user:
        user_obj ={
            "user_id":user.user_id,
            "username":user.username,
            "first_name":user.first_name,
            "last_name":user.last_name,
            "date_of_birth":user.date_of_birth,
            "image_id":user.image_id
        }
    return user_obj

def getUserFromUserId(user_id):
    try:
        user = User.query.filter_by(user_id = user_id).first()
    except SQLAlchemyError as e:
        error = f"Failed to query user: {e.__class__.__name__}"
        return "",error
    if user:
        user_objs = {
            "user_id":user.user_id,
            "username":user.username,
            "first_name":user.first_name,
            "last_name":user.last_name,
            "date_of_birth":user.date_of_birth,
            "image_id":user.image_id if user.image_id else "default"
        }
    profile_picture, msg = getImageFromImageId(user_objs.get("image_id"))
    if not profile_picture:
        profile_picture = DEFAULT_PROFILE_PICTURE
    user_objs["profile_image"] = profile_picture

    return user_objs, ""
        
        
        