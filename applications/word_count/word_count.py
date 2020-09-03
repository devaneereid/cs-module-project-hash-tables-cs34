# import re module
import re

def word_count(s):
    # Your code here
    # set up empty dictionary
    dict = {}

    # re.sub() - it is the substitute function
    # set up regex - looking for letters\digits\whitespace
    # ^ is the start of string or start of line depending on multiline mode. When [^is inside the brackets], it means "not")
    regex = re.sub(r'[^\w\d\s\']',' ',s)

    for word in regex.split():
        # output keys must be lowercase.
        word = word.lower()
        if word in dict:
            dict[word] += 1
        else:
            dict[word] = 1

    return dict


if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))