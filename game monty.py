import random

def choose_movie():
    movies = [
        "dilwale dulhania le jayenge", "sholay", "lagaan", "pk", "dangal",
        "three idiots", "chennai express", "kabhi khushi kabhie gham",
        "bajrangi bhaijaan", "padmaavat", "om shanti om", "dhoom",
        "kuch kuch hota hai", "kal ho naa ho", "zindagi na milegi dobara"
    ]
    return random.choice(movies)

def display_movie(movie, guessed_letters):
    return ' '.join(letter if letter in guessed_letters or not letter.isalpha() else '_' for letter in movie)

def bollywood_hangman():
    print("🎬 Welcome to Bollywood Hangman! 🎥")
    movie = choose_movie()
    movie_letters = set(letter.lower() for letter in movie if letter.isalpha())
    alphabet = set('abcdefghijklmnopqrstuvwxyz')
    guessed_letters = set()

    lives = 7
    bollywood_phrases = [
        "Action!", "Lights, Camera, Action!", "Cut!", "That's a wrap!",
        "Interval.", "Climax scene!", "The End.", "It's a flop!"
    ]

    while movie_letters and lives > 0:
        print("\n🎭 You have", lives, "chances left.")
        print("Letters used:", ' '.join(sorted(guessed_letters)))

        movie_display = display_movie(movie, guessed_letters)
        print("\nMovie title:", movie_display)

        guess = input("Guess a letter: ").lower().strip()
        if len(guess) != 1:
            print("🚫 Please enter a single letter.")
            continue

        if guess in alphabet - guessed_letters:
            guessed_letters.add(guess)
            if guess in movie_letters:
                movie_letters.remove(guess)
                print("👏 Great shot!")
            else:
                lives -= 1
                print(f"😕 Oops! {bollywood_phrases[min(7-lives, len(bollywood_phrases)-1)]}")
        elif guess in guessed_letters:
            print("🔁 You've already tried that letter. Choose another!")
        else:
            print("🚫 Invalid character. Please try again.")

    if lives == 0:
        print(f"\n💔 Game Over! The movie was: {movie}")
    else:
        print(f"\n🎉 Congratulations! You guessed the movie: {movie}")
    
    print("\n🎬 Thanks for playing Bollywood Hangman! 🎥")

if __name__ == "__main__":
    bollywood_hangman()