from flask import Flask, request, render_template, session
import random

app = Flask(__name__)
app.config['DEBUG'] = True
app.secret_key = 'SIH*v-6u)c>q<;;h&);cRw,1E_CO8>'

def id_winner(computer, user):
  if (computer == 'rock' and user == 'scissors') or (computer == 'scissors' and user == 'paper') or (computer == 'paper' and user == 'rock'):
    return 'computer'
  elif (computer == 'paper' and user == 'scissors') or (computer == 'rock' and user == 'paper') or (computer == 'scissors' and user == 'rock'):
    return 'user'
  else:
    return 'tie'

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        session['selection'] = 
        # Call the id_winner() function.
        # Update the win totals.
        # Format a message to display on the webpage.
        pass
    else:
        options = ['rock', 'paper', 'scissors']
        comp_wins = 0
        user_wins = 0
        computer_choice = random.choice(options)
        message = ''

    return render_template('index.html', message = message)

if __name__ == '__main__':
    app.run()
