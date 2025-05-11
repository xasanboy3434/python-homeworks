def create_acronym(phrase):
    words = phrase.split()
    acronym = ''.join(word[0].upper() for word in words if word)
    return acronym

# Misol:
input_phrase = input()
output_acronym = create_acronym(input_phrase)
print("Input:", input_phrase)
print("Output:", output_acronym)
