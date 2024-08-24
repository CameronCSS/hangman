from flask import Flask, render_template, request, redirect, url_for, session
import random
import os

app = Flask(__name__, static_url_path='/static')

# Function to generate a random secret key
def generate_secret_key():
    return os.urandom(24)

app.secret_key = generate_secret_key()  # Generate a new key each time

words = [
    "python", "java", "javascript", "svelte", "ruby",
    "flask", "django", "typescript", "nodejs", "angular",
    "groovy", "haskell", "react", "harmony", "elixir",
    "swift", "kotlin", "scala", "perl", "rust",
    "apple", "banana", "cherry", "orange", "grapes",
    "peach", "plum", "mango", "melon", "lemon",
    "watermelon", "pineapple", "avocado", "tomato", "onion",
    "carrot", "potato", "broccoli", "spinach", "lettuce",
    "cucumber", "garlic", "pepper", "cabbage", "zucchini",
    "celery", "squash", "beetroot", "eggplant", "asparagus",
    "strawberry", "blueberry", "raspberry", "blackberry", "kiwifruit",
    "apricot", "pomegranate", "grapefruit", "fig", "date",
    "coconut", "cashew", "almond", "walnut", "hazelnut",
    "squirrel", "rabbit", "beetle", "butterfly", "flamingo",
    "giraffe", "elephant", "dolphin", "penguin", "parrot",
    "tiger", "lion", "giraffe", "zebra", "kangaroo",
    "penguin", "hippopotamus", "leopard", "whale", "octopus",
    "carpet", "blanket", "pillow", "sofa", "chair",
    "table", "lamp", "curtain", "rug", "mirror",
    "computer", "keyboard", "mouse", "monitor", "printer",
    "phone", "tablet", "camera", "headphones", "charger",
    "bottle", "cup", "plate", "fork", "spoon",
    "knife", "bowl", "tray", "napkin", "glass",
    "book", "notebook", "pen", "pencil", "eraser",
    "scissors", "ruler", "glue", "tape", "stapler"
]

def new_game():
    word = random.choice(words)
    return {
        'word': word,
        'word_display': ['_' for _ in word],
        'attempts': 8,
        'guessed_letters': []
    }

@app.route('/', methods=['GET', 'POST'])
def index():
    if 'game' not in session:
        session['game'] = new_game()

    game = session['game']
    message = ''  # Initialize message variable

    if request.method == 'POST':
        if 'guess' in request.form:
            guess = request.form['guess'].lower()
            if guess in game['guessed_letters']:
                message = f"You've already guessed '{guess}'"
            else:
                if guess in game['word']:
                    game['guessed_letters'].append(guess)
                    game['guessed_letters'].sort()  # Sort guessed letters alphabetically
                    for index, letter in enumerate(game['word']):
                        if letter == guess:
                            game['word_display'][index] = guess
                else:
                    game['guessed_letters'].append(guess)
                    game['guessed_letters'].sort()  # Sort guessed letters alphabetically
                    game['attempts'] -= 1

                if '_' not in game['word_display']:
                    success = f"Congratulations, you guessed '{game['word']}'"
                    session.pop('game', None)  # End game
                    return render_template('index.html', word=game['word'], word_display=game['word_display'], attempts=game['attempts'], guessed_letters=game['guessed_letters'], success=success, message='')
                elif game['attempts'] <= 0:
                    message = f"Game over! The word was '{game['word']}'"
                    session.pop('game', None)  # End game
                    return render_template('index.html', word=game['word'], word_display=game['word_display'], attempts=game['attempts'], guessed_letters=game['guessed_letters'], message=message)

            session['game'] = game
        elif 'reset' in request.form:
            session.pop('game', None)
            return redirect(url_for('index'))

    return render_template('index.html', word=game['word'], word_display=game['word_display'], attempts=game['attempts'], guessed_letters=game['guessed_letters'], message=message)


@app.route('/reset', methods=['POST'])
def reset():
    session.pop('game', None) # End game
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=80, debug=True)
