from flask import make_response
MISSING_BODY_MSG = "No %s is provided"
WRONG_USERNAME_OR_PASSWORD = "The username or password you entered is incorrect"
class MissingBody(Exception):
    status_code = 400
    
    def __init__(self, message, status_code = None):
        super().__init__()
        self.message = message
        if status_code is not None:
            self.status_code = status_code
    
    def to_dict(self):
        error = {}
        error["message"] = self.message
        error["status_code"] = self.status_code
        return error
    
class Unauthorized(Exception):
    status_code = 401
    
    def __init__(self, message, status_code = None):
        super().__init__()
        self.message = message
        if status_code is not None:
            self.status_code = status_code
    
    def to_dict(self):
        error = {}
        error["message"] = self.message
        error["status_code"] = self.status_code
        return error
    
class DatabaseError(Exception):
    status_code = 502
    
    def __init__(self, message, status_code = None):
        super().__init__()
        self.message = message
        if status_code is not None:
            self.status_code = status_code
    
    def to_dict(self):
        error = {}
        error["message"] = self.message
        error["status_code"] = self.status_code
        return error

    


    
    