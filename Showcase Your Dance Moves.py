# Task1 Code Correction
# Below is a piece of Python code with incorrect indentation. Your task is to correct it.
weather = "sunny"

if weather == "sunny":
    print("Wear sunglasses!") # The code was a syntax error. Indemtation fixed
else:
    print("Take an umbrella!") # The indentation was not correct, fixed

# Task2
# Ask the user how they feel today. If they say "happy", print "That's great to hear!", 
# and if they say "sad", print "I hope your day gets better!". Ensure your if statement
# is properly indented. HINT: Use the input() function to ask the user how they feel!
# If you need a refresher, check this out here:
# https://www.w3schools.com/python/python_user_input.asp

mood = input("How are you feeling today? ")
if mood == "happy":
    print("That's great to hear!")
if mood == "sad":
    print("I hope your day gets better!")