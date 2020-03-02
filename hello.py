from PIL import Image
import hyperLinks as hl

import requests
import shutil
import urllib3

# im = Image.open("il_fullxfull.977078474_51xi.jpg")
im = Image.open(requests.get(hl.p1, stream=True).raw)

print(im.format, im.size, im.mode)
im.show()

# This is the image url.
image_url = hl.p3

# Open the url image, set stream to True, this will return the stream content.
resp = requests.get(image_url, stream=True)

# Open a local file with wb ( write binary ) permission.
local_file = open('local_image2.jpg', 'wb')
# Set decode_content value to True, otherwise the downloaded image file's size will be zero.
resp.raw.decode_content = True
# Copy the response stream raw data to local image file.
shutil.copyfileobj(resp.raw, local_file)
# Remove the image url response object.
del resp
