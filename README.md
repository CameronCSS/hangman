<a name="readme-top"></a>
# Flask Hangman Game
<br />
<div align="center">
  <a href="hangman.camcodes.dev">
    <img src="https://github.com/user-attachments/assets/de465150-2f4e-4cf7-a5b9-fdbb760f734f" alt="Logo" height="300">
  </a>
</div>


### Welcome to the Flask Hangman Game! 

This simple web application lets you play a classic game of Hangman using Flask, a popular web framework in Python. 
<br>
The game features a randomly selected word from a predefined list, and you have a limited number of attempts to guess the word correctly.


[CLICK HERE](hangman.camcodes.dev) to try Hangman!

## Features
* **Random Word Selection:** The game selects a word randomly from a predefined list of words.
* **Interactive Gameplay:** Guess letters and see them appear in the word if correct.
* **Attempt Tracking:** Keep track of your remaining attempts.
* **User Feedback:** Onscreen info about your guesses and game status.
* **Game Reset:** Easily restart the game at any time.



## Installation
To run this application locally, follow these steps:

* Clone the Repository:
  ```
  git clone https://github.com/CameronCSS/hangman.git
  ```

* Setup a Virtual Environment(optional:
  ```
  python -m venv newenv
  ```
  
* Install Dependencies:
  ```
  pip install flask
  ```

* Run the Application:
  ```
  python app.py
  ```

* Access the Application:
  ```
  Open your web browser and navigate to http://127.0.0.1:5000.
  ```

  <p align="right">(<a href="#readme-top">back to top</a>)</p>

## How It Works
#### Basic Python code is used for all the game logic
#### Local storage (in browser) is used to save current game information
#### Flask is doing everything else using flask routes.
<br>

**Routes:**
- /: Handles both GET and POST requests for playing the game and resetting.
- /reset: Handles the reset of the game session.

# Requirements
- Python 3.x
- Flask


<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>
