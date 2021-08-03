from flask import Flask, request, render_template, session
import random

app = Flask(__name__)
app.config['DEBUG'] = True
app.secret_key = 'K>~EEAnH_x,Z{q.43;NmyQiNz1^Yr7'

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        still_guessing = True
        guess = int(request.form['guess'])
        if guess < session["magic_number"]:
            session['low_value']=guess
            message = f"Your guess of {guess} is too low"
        elif guess > session["magic_number"]:
            session['high_value'] = guess
            message = f"Your guess of {guess} is too high"
        elif guess == session["magic_number"]:
            message  = f"Congratulations! You guessed the number"
            still_guessing = False
        
    else:
        session['low_value'] = 1
        session['high_value'] = 50
        session["magic_number"] = random.randint(session['low_value'], session['high_value'])
        still_guessing = True

        message = ''

    return render_template('index.html', message = message, still_guessing = still_guessing)

if __name__ == '__main__':
    app.run()
