# When texting or tweeting, it’s not uncommon to shorten words to save time or space, as by omitting vowels, much like Twitter was originally called twttr. In a file called twttr.py,
# implement a program that prompts the user for a str of text and then outputs that same text but with all vowels (A, E, I, O, and U) omitted, whether inputted in uppercase or lowercase.


def main():
    word = input("Input: ")
    result = shorten(word)
    print(f"Output: {result}")

def shorten(word):
    # The letters to remove
    to_remove = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
    output = ""

    for letter in word:
        if letter not in to_remove:
            output += letter

    return output



if __name__ == "__main__":
    main()




