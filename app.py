from flask import Flask, render_template
import random

app = Flask(__name__)

def generate_name():
    consonants = "bcdfghjklmnpqrstvwxyz"
    vowels = "io"
    ending = "ng"

    name = random.choice(consonants + "ch")  # First letter is a consonant or 'ch'
    name += random.choice(vowels)  # Second letter is 'i' or 'o'
    name += ending  # Last two letters are 'ng'

    return name

@app.route('/')
def index():
    names = [generate_name() for _ in range(10)]
    return render_template('index.html', names=names)

if __name__ == '__main__':
    app.run()
