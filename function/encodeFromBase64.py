


from function.lsb_stegno import lsb_encode
from function.n_share import generate_shares



def encodeFromBase64(base64Str : str):
    """encode data from base64 string convert from image"""
    result = generate_shares(lsb_encode(base64_data=base64Str , data='visual crypography'))
    return result
    