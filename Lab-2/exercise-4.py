
user_input = input("Enter a word or short sentence: ")

vowels = "aeiouAEIOU"
vowel_count = 0
space_count = 0

for char in user_input:
    if char in vowels:
        vowel_count += 1
    elif char == " ":
        space_count += 1

total_characters = len(user_input)

# Display analysis
print("\n--- Text Analysis ---")
print(f"Total Characters: {total_characters}")
print(f"Vowel Count:      {vowel_count}")
print(f"Space Count:      {space_count}")