# It turns out that (most) YouTube videos can be embedded in other websites, just like the above. For instance, if you visit https://youtu.be/xvFZjo5PgG0 on a laptop or desktop, click Share, and then click Embed,
# you’ll see HTML (the language in which web pages are written) like the below, which you could then copy into your own website’s source code, wherein iframe is an HTML “element,” and src is one of several HTML “attributes” therein, the value of which,
# between quotes, is https://www.youtube.com/embed/xvFZjo5PgG0.

# <iframe width="560" height="315" src="https://www.youtube.com/embed/xvFZjo5PgG0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
# Because some HTML attributes are optional, you could instead minimally embed just the below.

# <iframe src="https://www.youtube.com/embed/xvFZjo5PgG0"></iframe>
# Suppose that you’d like to extract the URLs of YouTube videos that are embedded in pages (e.g., https://www.youtube.com/embed/xvFZjo5PgG0), converting them back to shorter, shareable youtu.be URLs (e.g., https://youtu.be/xvFZjo5PgG0)
# where they can be watched on YouTube itself.

# In a file called watch.py, implement a function called parse that expects a str of HTML as input, extracts any YouTube URL that’s the value of a src attribute of an iframe element therein,
# and returns its shorter, shareable youtu.be equivalent as a str. Expect that any such URL will be in one of the formats below. Assume that the value of src will be surrounded by double quotes. And assume that the input will contain no more than one such URL.
# If the input does not contain any such URL at all, return None.

# http://youtube.com/embed/xvFZjo5PgG0
# https://youtube.com/embed/xvFZjo5PgG0
# https://www.youtube.com/embed/xvFZjo5PgG0
# Structure watch.py as follows, wherein you’re welcome to modify main and/or implement other functions as you see fit, but you may not import any other libraries. You’re welcome, but not required, to use re and/or sys.

import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    match = re.search(r'<iframe[^>]*src="http.*youtube\.com/embed/([^"]+)"', s)
    # explenation of the re.search code step by step:
    # 1: we always start with "<iframe " , since that's the start of the youtube URL within HTMLO
    # 2: [^>] > This means any character except for ">", because ">" would close iframe
    # 3: when we add * this means 0 or more character. After iframe we can immediatelily expect "src", or there can be characters in between, doesn't matter
    # 4: so [^>]* means , 0 or more characters except for "> "
    # 5: src="http , this is how the Youtube url starts, so has to exactly match
    # 6: ".*" means 0 or more characters except newline , because the url can start with https:// or with http:// , it doesnt matter which
    # 7: since "." means any character except new line, and we need: youtube.com/embed/ , we replace "." with "\.", this tells python to read "." as a dot, and not as "any character except newline".
    # 8: [^"]+ means, any character except '"', but we need 1 or more, since it's the ID of the youtube video it needs at least 1 character
    # 9: ([^"]+) > we added () around '[^"]+', because this is the ID we need later and by adding a "capture group" we can find it later on using the group function.

    # if no match found we return nothing
    if not match:
        return None

    else:
        # .group() or .group(0) will return the entire line of:r'<iframe[^>]*src="http.*youtube\.com/embed/([^"]+)"'
        #.group(1) will return the first capture group , which is the first part between (), in this case: ([^"]+)
        return f"https://youtu.be/{match.group(1)}"

...


if __name__ == "__main__":
    main()
