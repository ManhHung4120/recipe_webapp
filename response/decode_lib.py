import base64
def encode_base64(image):
    image_encode = base64.b64encode(image.read())
    return image_encode

def decode_base64(encode_string):
    image = base64.b64decode(encode_string)
    
    return image