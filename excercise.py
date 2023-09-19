from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)


df = pd.read_csv('./dictionary.csv')
@app.route('/')
def home():
    return render_template('excerciseIndex.html')


@app.route('/api/v1/<phrase>')
def about(phrase):
    definition = df.loc[df['word']==phrase]['definition'].squeeze()
    return {'Word/Phrase': phrase, 'Definition': definition}


if __name__ == '__main__':
    app.run(debug=True)