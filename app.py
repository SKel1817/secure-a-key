from flask import Flask,render_template, send_from_directory
from flask import request
app = Flask(__name__)

@app.route("/")
def home():
    return render_template('home.html')

@app.route("/phising_mini_game")
def phising_mini_game():
    return render_template('phising_mini_game.html')

@app.route('/emails.json')
def emails():
    return send_from_directory('static', 'emails.json')

@app.route('/passwordBuilder')
def passwordBuilder():
    return render_template('passwordBuilder.html')

@app.route('/passwordTest')
def password_test():
    password = request.args.get('password', '')
    # Simulate cracking time based on password length and complexity
    cracking_time = simulate_cracking_time(password)
    return render_template('passwordTest.html', password=password, cracking_time=cracking_time)

def simulate_cracking_time(password):
    # This is a simplistic simulation; real cracking times depend on many factors
    length = len(password)
    complexity = len(set(list(password)))  # Unique characters for complexity estimation
    time_to_crack = (length * complexity) / 2  # Simplified formula for demonstration
    return max(1, time_to_crack)  # Ensure at least 1 second is shown for simplicity

if __name__ == '__main__':
    app.run()


