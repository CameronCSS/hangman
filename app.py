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
    "swift", "kotlin", "scala", "perl", "rust"
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
    if request.method == 'POST':
        guess = request.form['guess'].lower()
        if guess in game['guessed_letters']:
            return render_template('index.html', game=game, message=f"You've already guessed '{guess}'")
        
        if guess in game['word']:
            game['guessed_letters'].append(guess)
            for index, letter in enumerate(game['word']):
                if letter == guess:
                    game['word_display'][index] = guess
        else:
            game['guessed_letters'].append(guess)
            game['attempts'] -= 1

        if '_' not in game['word_display']:
            return render_template('index.html', game=game, success=f"Congratulations, you guessed '{game['word']}'")
        elif game['attempts'] <= 0:
            return render_template('index.html', game=game, message=f"Game over! The word was '{game['word']}'")
        
        session['game'] = game

    return render_template('index.html', game=session['game'])

@app.route('/reset', methods=['POST'])
def reset():
    session.pop('game', None)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=80, debug=True)
