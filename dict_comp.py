from string import ascii_uppercase, ascii_lowercase


dict_comp = {key: value for key, value in zip(ascii_lowercase, ascii_uppercase)}
print(dict_comp)
