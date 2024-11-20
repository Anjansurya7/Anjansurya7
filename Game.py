import random

def subject_guessing_game():
    # List of subjects with their hints
    subjects = {
        "Math": "This subject deals with numbers, calculations, and equations.",
        "Science": "This subject involves the study of nature, experiments, and the physical world.",
        "History": "This subject involves studying past events and civilizations.",
        "Geography": "This subject focuses on the study of the Earth, places, and how they are connected.",
        "English": "This subject involves reading, writing, and understanding the English language."
    }

    # Randomly choose a subject from the list
    subject, hint = random.choice(list(subjects.items()))

    print("Welcome to the Subject Guessing Game!")
    print("I will give you a hint, and you have to guess the subject.")

    # Provide the hint to the player
    print(f"Hint: {hint}")

    # Allow the player to guess
    attempts = 0
    while True:
        guess = input("Enter your guess: ").strip().title()  # Format input to match subject case
        attempts += 1
        
        if guess == subject:
            print(f"Congratulations! You've guessed the subject {subject} in {attempts} attempts.")
            break
        else:
            print("Incorrect guess. Try again!")

# Run the game
subject_guessing_game()

