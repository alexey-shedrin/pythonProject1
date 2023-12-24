def find_big_letters(string):
    big_letters = [char for char in string if char.isupper()]
    return big_letters

input_string = input()
big_letters = find_big_letters(input_string)
print(big_letters)