# Even though Windows and macOS sometimes hide them, most files have file extensions, a suffix that starts with a period (.) at the end of their name.
# For instance, file names for GIFs end with .gif, and file names for JPEGs end with .jpg or .jpeg. When you double-click on a file to open it, your computer uses its file extension to determine which program to launch.

# Web browsers, by contrast, rely on media types, formerly known as MIME types, to determine how to display files that live on the web.
# When you download a file from a web server, that server sends an HTTP header, along with the file itself, indicating the file’s media type. For instance, the media type for a GIF is image/gif, and the media type for a JPEG is image/jpeg.
#  To determine the media type for a file, a web server typically looks at the file’s extension, mapping one to the other.

# See developer.mozilla.org/en-US/docs/Web/HTTP/Basics_of_HTTP/MIME_types/Common_types for common types.

# In a file called extensions.py, implement a program that prompts the user for the name of a file and then outputs that file’s media type if the file’s name ends, case-insensitively, in any of these suffixes:

# .gif
# .jpg
# .jpeg
# .png
# .pdf
# .txt
# .zip
# If the file’s name ends with some other suffix or has no suffix at all, output application/octet-stream instead, which is a common default.


# 1: use endswith() https://www.w3schools.com/python/ref_string_endswith.asp
# 2: create a dictionary

file_name = input("File name:").lower().strip()
last_4_characters = file_name[-4:] # [-4] choses the 4th character from the end, but [-4:] is the last 4 characters
last_5_characters = file_name[-5:] # this is for .jpeg; which is the only 5 characters file name

# Dictionary with
media_type_dictionary = { # dictionary with all the file names
      ".gif": "image/gif",
      ".jpg": "image/jpeg",
     ".jpeg" : "image/jpeg",
      ".png" : "image/png",
      ".pdf" : "application/pdf",
      ".txt" : "text/plain",
      ".zip" : "application/zip"
    }

# eg > .gif = 4 characters print the definition of ".gif" in the media_type_dictionary
if last_4_characters in media_type_dictionary:
    print(media_type_dictionary[last_4_characters])

# .jpeg is exception on the rule since it has 5 charachters
elif last_5_characters in media_type_dictionary:
    print(media_type_dictionary[last_5_characters])

# any other scenario the default output given by the exercize
else:
    print("application/octet-stream")


