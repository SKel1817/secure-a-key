from flask import Flask,render_template, send_from_directory
from flask import request
from waitress import serve
import hashlib
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
    show_password = hash_password(password)
    crack_pass = crack_the_password(password, show_password)
    return render_template('passwordTest.html', password=password, cracking_time=cracking_time, show_password=show_password, crack_pass=crack_pass)

def simulate_cracking_time(password):
    # This is a simplistic simulation; real cracking times depend on many factors
    length = len(password)
    complexity = len(set(list(password)))  # Unique characters for complexity estimation
    time_to_crack = (length * complexity) / 2  # Simplified formula for demonstration
    return max(1, time_to_crack)  # Ensure at least 1 second is shown for simplicity


def hash_password(password):
    return hashlib.sha256(password.encode('utf-8')).hexdigest()


def crack_the_password(u_password, hashed_password):
    with open('passwords.txt', 'r') as f:
        common_password = f.read().splitlines()
    user_password = hashed_password
    for password in common_password:
        print("Trying password:", password)
        master_hashed_password = hashlib.sha256(password.encode('utf-8')).hexdigest()
        if master_hashed_password == user_password:
            return "password found, it is " + u_password
    return "password not found, Your password is safe!"   
    
@app.route('/twofactor')
def twofactor():
    return render_template('twofactor.html')

@app.route('/moreinfo')
def moreinfo():
    return render_template('moreinfo.html')

if __name__ == '__main__':
    serve(app, host='0.0.0.0', port=80)


