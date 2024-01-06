import numpy as np
from PIL import Image
import base64
from io import BytesIO
import io

def generate_shares(data, share=2):
    data = np.array(data, dtype='u1')

    # Generate image of the same size
    img1 = np.zeros(data.shape).astype("u1")
    img2 = np.zeros(data.shape).astype("u1")

    # Set a random factor
    for i in range(data.shape[0]):
        for j in range(data.shape[1]):
            for k in range(data.shape[2]):
                n = int(np.random.randint(data[i, j, k] + 1))
                img1[i, j, k] = n
                img2[i, j, k] = data[i, j, k] - n

    # Saving shares
    img1 = Image.fromarray(img1)
    img2 = Image.fromarray(img2)

    # Convert images to base64 strings
    img1_buffer = BytesIO()
    img1.save(img1_buffer, format="PNG")
    img1_str = "data:image/png;base64," + base64.b64encode(img1_buffer.getvalue()).decode("utf-8")

    img2_buffer = BytesIO()
    img2.save(img2_buffer, format="PNG")
    img2_str = "data:image/png;base64," + base64.b64encode(img2_buffer.getvalue()).decode("utf-8")

    return {
        'share1' : img1_str,
        'share2' : img2_str
    }


def compress_shares(img1_base64: str, img2_base64: str):
    # Decode base64 strings to bytes
    img1_bytes = base64.b64decode(img1_base64.split(',')[1])
    img2_bytes = base64.b64decode(img2_base64.split(',')[1])

    # Read images
    img1 = np.asarray(Image.open(io.BytesIO(img1_bytes))).astype('int16')
    img2 = np.asarray(Image.open(io.BytesIO(img2_bytes))).astype('int16')

    img = np.zeros(img1.shape)

    # Fit to range
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            for k in range(img.shape[2]):
                img[i, j, k] = img1[i, j, k] + img2[i, j, k]

    # Save compressed image
    img = img.astype(np.uint8)
    img_pil = Image.fromarray(img)
    
    # Convert compressed image to base64 string
    buffer = io.BytesIO()
    img_pil.save(buffer, format="PNG")
    img_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8')
    
    return img_base64
