from flask import request
def get_request_body():
    return request.get_json()

def generate_hash_password(plaintext):
    from app import bcrypt
    return bcrypt.generate_password_hash(plaintext,11).decode('UTF-8')

def is_boolean (var):
    if (isinstance(var, bool)):
        return True
    
    bool_chars = ["true", "false", "ok", "ko", "yes", "no"]
    return var is not None and any(c == "{}".format(var).lower() for c in bool_chars)

def is_not_empty (var):
    if (isinstance(var, bool)):
        return var
    elif (isinstance(var, int)):
        return not var == 0
    empty_chars = ["", "null", "nil", "false", "none"]
    return var is not None and not any(c == "{}".format(var).lower() for c in empty_chars)

def is_true (var):
    false_char = ["false", "ko", "no", "off"]
    return is_not_empty(var) and not any(c == "{}".format(var).lower() for c in false_char)

def is_false (var):
    return not is_true(var)

def is_empty (var):
    return not is_not_empty(var)

def is_disabled (var):
    return is_empty(var) or "changeit" == var
