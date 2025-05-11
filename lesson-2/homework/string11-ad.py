def extract_numbers(text):
    numbers = '1234567890'
    only_numbers = [char for char in text if char in numbers]
    return''.join(only_numbers)
text = input()
result = extract_numbers(text)
print('numbers:', result)