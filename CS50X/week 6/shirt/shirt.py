# After finishing CS50 itself, students on campus at Harvard traditionally receive their very own I took CS50 t-shirt. No need to buy one online, but like to try one on virtually?

# In a file called shirt.py, implement a program that expects exactly two command-line arguments:

# in sys.argv[1], the name (or path) of a JPEG or PNG to read (i.e., open) as input
# in sys.argv[2], the name (or path) of a JPEG or PNG to write (i.e., save) as output
# The program should then overlay shirt.png (which has a transparent background) on the input after resizing and cropping the input to be the same size, saving the result as its output.

# Open the input with Image.open,
# per pillow.readthedocs.io/en/stable/reference/Image.html
# #PIL.Image.open, resize and crop the input with ImageOps.fit, per pillow.readthedocs.io/en/stable/reference/ImageOps.html#PIL.ImageOps.fit, using default values for method, bleed, and centering, overlay the shirt with Image.paste,
# # per pillow.readthedocs.io/en/stable/reference/Image.html#PIL.Image.Image.paste, and save the result with Image.save, per pillow.readthedocs.io/en/stable/reference/Image.html#PIL.Image.Image.save.

# The program should instead exit via sys.exit:

# if the user does not specify exactly two command-line arguments,
# if the input’s and output’s names do not end in .jpg, .jpeg, or .png, case-insensitively,
# if the input’s name does not have the same extension as the output’s name, or
# if the specified input does not exist.
# Assume that the input will be a photo of someone posing in just the right way, like these demos, so that, when they’re resized and cropped, the shirt appears to fit perfectly.

# If you’d like to run your program on a photo of yourself, first drag the photo over to VS Code’s file explorer, into the same folder as shirt.py. No need to submit any photos with your code.
# But, if you would like, you’re welcome (but not expected) to share a photo of yourself wearing your virtual shirt in any of CS50’s communities!


#TODO 1: 2 command lines, sys.argv[1] = name of file to read, sys.argv[2] = name of file to write
#TODO 2: open sys.argv[1] with Image.open
#TODO 3: resize and crop with ImageOps.fit , using default values for method, bleed, and centering, overlay the shirt with Image.paste . Write this all to sys.argv[2]
#TODO 4: The program should instead exit via sys.exit:

# if the user does not specify exactly two command-line arguments,
# if the input’s and output’s names do not end in .jpg, .jpeg, or .png, case-insensitively,
# if the input’s name does not have the same extension as the output’s name, or
# if the specified input does not exist.

import sys
from PIL import Image, ImageOps

def main():
    file_before, file_after = check_arguments() # see if sys.argv follows the rules
    overlay_shirt(file_before, file_after)

def check_arguments(): # checks if command-line arguments are according to rules

    if len(sys.argv) < 3: # name file ,file before, file after
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

    file_before = sys.argv[1]
    file_after = sys.argv[2]

    if not file_before.lower().endswith((".jpg", ".jpeg", ".png")):
    # Double (()) creates a tuple inside .endswith().
    # This way .endswith() understands it only needs to match *one* of
    # .jpg, .jpeg, or .png. Without the tuple, it would expect all three
    # separately → error.
        sys.exit(f"Could not read {file_before}")

    if not file_after.lower().endswith((".jpg", ".jpeg", ".png")):
        sys.exit(F"Could not read {file_after}")

    return file_before, file_after

def overlay_shirt(file_before, file_after): # opens the before file rewrites it to a new file

    shirt = Image.open("shirt.png")

    with Image.open(file_before) as before_img:
        # step 1: Resize and crop the input photo to the same size as shirt.png
        # .size is an attribute of an imagw object that gives: width, height
        # PIL.ImageOps.fit(image: Image, size: tuple[int, int], method: int = Resampling.BICUBIC, bleed: float = 0.0, centering: tuple[float, float] = (0.5, 0.5)) → Image[source]
        # .imagesops.fit scales the photo and then crops the center so the result exactly matches shirt.size (600*600)
        # Both shirt.png and the before images are aleady centered to match eachother. This means we only need to resize/crop to the same size. The shirt will automatically overlay in the correct position.
        # The background of shirt.png is transparant.
        # so we can simply stack them on top of eachother
        resized_image = ImageOps.fit(before_img, shirt.size)

        # Step 2: Overlay the shirt on top of the resized photo
        # .paste() draws one image onto another
        # the first argument ( shirt) decides which image to draw
        # The mask argument decides which pixels and where those are drawn

        # In this case we use mask=shirt
        # Pillow looks at the shirt's alpha channel ( Alpha channel are the transparant pixels of an image)
        # The only pixels that cover the before_image are the pixels that are not transparant.
        # The transparant pixels are shown as transparant, which means that the before_image is shown
        # If we don't use the correct mask, Pillow could show the transparant pixels as non transparant, for example black or white
        # That is very important in this scenario, because CS50 already centered the shirt exactly the same as the example images
        # By only having the transparant pixels shown as transparant the shirt will automatically overlay the before_image correctly,
        # If we use another mask, we could change how pillow would print the transparant pixels, or change what part of the shirt to be printed etc.
        resized_image.paste(shirt, mask=shirt)

        #Step 3: we need to save the final image to the output file
        resized_image.save(file_after)





main()




