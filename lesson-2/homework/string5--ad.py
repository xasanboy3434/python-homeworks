def extract_vowels(text):
    vowels = 'aeiouAEIOU'
    only_vowels = [char for char in text if char not in vowels]
    return''.join(only_vowels)

text = input()
result = extract_vowels(text)
print('consanants:', result)

def extract_vowels(text):
    vowels ='aeiuoAEIUO'
    only_vowels = [ char for char in text if char in vowels]
    return''.join(only_vowels)

text = 'jxjcvkbjihuytdgxgrdtyguijokjhygtfrtgbhgjvsdtifyiotuiyrturtuyiuoj'
result = extract_vowels(text)
print('vowels:', result)
