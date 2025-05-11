text = input("Enter a string: ")
vowels = "aeiouAEIOU"
symbol = "*"
text_replace = ''.join(symbol if char in vowels else char for char in text)
print("The new string is:", text_replace)