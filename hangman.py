import random

def play_hangman():
    # 5 predefined words ki list
    words = ["python", "java", "code", "matrix", "student"]
    word = random.choice(words)
    
    guessed_letters = []
    incorrect_guesses = 0
    max_incorrect = 6

    print("🎯 Welcome to Hangman Game!")
    print(f"Aapko maximum {max_incorrect} galat guesses ki limit milti hai.")

    while incorrect_guesses < max_incorrect:
        # Current word ka status display karna (e.g., p _ t h _ n)
        display_word = ""
        for letter in word:
            if letter in guessed_letters:
                display_word += letter + " "
            else:
                display_word += "_ "
        
        print(f"\nWord: {display_word.strip()}")
        print(f"Bache hue galat chances: {max_incorrect - incorrect_guesses}")
        
        # User se input lena
        guess = input("Ek letter guess karein: ").lower().strip()
        
        # Validation
        if len(guess) != 1 or not guess.isalpha():
            print("⚠️ Please sirf ek valid English letter enter karein.")
            continue
            
        if guess in guessed_letters:
            print("⚠️ Aap yeh letter pehle hi guess kar chuke hain.")
            continue
            
        # List mein guessed letter add karna
        guessed_letters.append(guess)
        
        # Check karna ki letter word mein hai ya nahi
        if guess in word:
            print(f"✅ Sahi! '{guess}' word mein maujood hai.")
        else:
            incorrect_guesses += 1
            print(f"❌ Galat! '{guess}' word mein nahi hai.")
            
        # Check win condition: kya saare letters guess ho gaye?
        win = True
        for letter in word:
            if letter not in guessed_letters:
                win = False
                break
                
        if win:
            print(f"\n🎉 Badhaai ho! Aapne sahi word guess kar liya: {word}")
            break
            
    else:
        # Jab saare 6 incorrect guesses khatam ho jayein
        print(f"\n💀 Game Over! Aapke saare chances khatam ho gaye. Sahi word tha: {word}")

if __name__ == "__main__":
    play_hangman()