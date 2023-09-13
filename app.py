#app.py

from flask import Flask, render_template, request
import random

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/play', methods=['POST'])
def play():
    player_choice = request.form['choice']
    choices = ['rock', 'paper', 'scissors']
    computer_choice = random.choice(choices)

    # Determine the winner
    if player_choice == computer_choice:
        result = "It's a tie!"
    elif (
        (player_choice == 'rock' and computer_choice == 'scissors') or
        (player_choice == 'paper' and computer_choice == 'rock') or
        (player_choice == 'scissors' and computer_choice == 'paper')
    ):
        result = "You win!"
    else:
        result = "You lose!"

    return render_template('result.html', player=player_choice, computer=computer_choice, result=result)

if __name__ == '__main__':
    app.run(debug=True)
