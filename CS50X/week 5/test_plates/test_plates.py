
# In a file called plates.py, reimplement Vanity Plates from Problem Set 2, restructuring your code per the below, wherein is_valid still expects a str as input and returns True if that str meets all requirements and False if it does not,
# but main is only called if the value of __name__ is "__main__":

# def main():
#     ...


# def is_valid(s):
#     ...


# if __name__ == "__main__":
#     main()


# Then, in a file called test_plates.py, implement four or more functions that collectively test your implementation of is_valid thoroughly, each of whose names should begin with test_ so that you can execute your tests with:

# Rule 1: Len(plate) between 2 and 6 x
# Rule 2: Numbers must be at the end of each word
# Rule 3: First number used cannot be 0 x
# Rule 4: " ", "." or punctuation marks allowed > only allow A-Z and 0-9 x
# Rule 5: All letters must be UPPERCASE. x


from plates import is_valid


def test_len():
    assert is_valid("a") == False
    assert is_valid("aaaa123") == False
    assert is_valid ("aa") == True
    assert is_valid("aaaa12") == True

def test_order():
    assert is_valid("1a") == False
    assert is_valid("abc1d2") == False
    assert is_valid("aa1") == True
    assert is_valid("abcd12") == True

def test_zero():
    assert is_valid("abcd01") == False
    assert is_valid("abcd10") == True

def test_punctuation():
    assert is_valid("abcd!") ==  False


