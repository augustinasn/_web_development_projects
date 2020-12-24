import glob
import os
import PIL
import uuid

from PIL import Image

def create_thumbnail(image: object) -> object:

   """[Function takes image object as an argument and resizes it (while keeping aspect ratio) to a width of 300px]
   
   Arguments:
       image {object} -- [an image file opened via PIL library]
   
   Returns:
       object -- [a resized image object]
   """ 
   
    width = 300
    wpercent = (width/float(image.size[0]))
    hsize = int((float(image.size[1])*float(wpercent)))

    img = image.resize((width, hsize), PIL.Image.ANTIALIAS)

    return img

def generate_filename() -> str:

    """[Functions creates a 14 character long alphanumeric string which is later used as a file name for a newly uploaded image]
    
    Returns:
        str -- [a unique name for an image file]
    """

    filename = str(uuid.uuid4().hex)[:15] + ".jpg"

    return filename

def save_image_and_thumbnail(file: object) -> str:

    """[Function takes in an image object as an argument, saves an original in the ./static/images location, a resized copy to the ./static/images/thumbnails directory]
    
    Returns:
        [str] -- [a unique name that was used for the file for further process]
    """

    filename = generate_filename()
    
    img = Image.open(file)
    img.save(os.path.join(os.getcwd(), "homestorage", "static", "images", filename))
    img = create_thumbnail(img)
    img.save(os.path.join(os.getcwd(), "homestorage", "static", "images", "thumbnails", filename))

    return filename