from PIL import Image
from urllib.request import urlopen
from IPython.display import display

url = "https://python-pillow.github.io/assets/images/pillow-logo.png"
img = Image.open(urlopen(url))

display(img)
