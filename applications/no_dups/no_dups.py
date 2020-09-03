def no_dups(s):
    # Your code here
    dict = {}
    dup_list = s.split()

    new_list = []

    for i in dup_list:
        if i not in dict:
            new_list.append(i)
            dict[i] = 0

    return " ".join(new_list)


if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))