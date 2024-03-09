from flask import Flask,render_template, send_from_directory
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
if __name__ == '__main__':
    app.run()


