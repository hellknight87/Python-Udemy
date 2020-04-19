import requests
from io import BytesIO
from PIL import Image

r = requests.get("https://www.hipsthetic.com/wp-content/uploads/2016/01/running_my_fingers_down_ur_skin_i_can_feel_every_inch_of_u.png")

print("Status code:", r.status_code)

image = Image.open(BytesIO(r.content))

print(image.size, image.format, image.mode)
path = "./image." + image.format

try:
    image.save(path, image.format)
except IOError:
    print("Cannot save the image.")

