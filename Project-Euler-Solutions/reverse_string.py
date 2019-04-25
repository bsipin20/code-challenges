def reverse(string_):
    rev_string = ""
    for i in string_:
        rev_string = i + rev_string
    return rev_string


def reverse_using_stack_(string_):
    stack_of_reversed_letters = []
    for i in string_:
        stack_of_reversed_letters.append(i)

    rev_string = ""
    for j in range(0,len(stack_of_reversed_letters)):
        rev_string += stack_of_reversed_letters.pop()
    return(rev_string)
        


if __name__ == "__main__":
    print(reverse_using_stack_("Hello"))

