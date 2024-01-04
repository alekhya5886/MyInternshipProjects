def count_words(text):
    return len(text.split())

user_input = input("Enter the text you want to count: ")
word_count_result = count_words(user_input)
print(f"Number of words: {word_count_result}")
