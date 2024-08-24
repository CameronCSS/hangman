from flask import Flask, render_template, request, redirect, url_for
import random

app = Flask(__name__, static_url_path='/static')

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
    # Initialize game state
    game = new_game()

    if request.method == 'POST':
        # Load existing game state from URL parameters
        word = request.form.get('word', '')
        word_display = request.form.getlist('word_display')
        attempts = int(request.form.get('attempts', 8))
        guessed_letters = request.form.getlist('guessed_letters')

        # Handle new guess
        guess = request.form['guess'].lower()
        if guess in guessed_letters:
            message = f"You've already guessed '{guess}'"
        else:
            if guess in word:
                guessed_letters.append(guess)
                for index, letter in enumerate(word):
                    if letter == guess:
                        word_display[index] = guess
            else:
                guessed_letters.append(guess)
                attempts -= 1

            if '_' not in word_display:
                success = "Congratulations, you guessed the word!"
                return render_template('index.html', word=word, word_display=word_display, attempts=attempts, guessed_letters=guessed_letters, success=success)
            elif attempts <= 0:
                message = f"Game over! The word was '{word}'"
                return render_template('index.html', word=word, word_display=word_display, attempts=attempts, guessed_letters=guessed_letters, message=message)
        
        # Render template with updated state
        return render_template('index.html', word=word, word_display=word_display, attempts=attempts, guessed_letters=guessed_letters, message=message)
    
    # Render template for initial game state
    return render_template('index.html', word='', word_display=['_'*5], attempts=8, guessed_letters=[], message='')

@app.route('/reset', methods=['POST'])
def reset():
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=80, debug=True)
