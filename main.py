from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

stations = pd.read_csv('./data/stations.txt', skiprows=17)

@app.route('/')
def home():
    return render_template('index.html', data=stations.to_html())


@app.route('/api/v1/<station>/<date>')
def about(station, date):
    filename = './data/TG_STAID' + str(station).zfill(6) +'.txt'
    df = pd.read_csv(filename, skiprows=20, parse_dates=['    DATE'])
    temp=df.loc[df['    DATE']==date]['   TG'].squeeze()/10
    return {'Station': station, 'Date': date, 'Temperature': temp}

@app.route('/api/v1/<station>/')
def data_by_stationId(station):
    filename = './data/TG_STAID' + str(station).zfill(6) +'.txt'
    df = pd.read_csv(filename, skiprows=20, parse_dates=['    DATE'])
    temp=df.to_dict(orient='records')
    return {'Station': station, 'Temperature': temp}

@app.route('/api/v1/yearly/<station>/<year>')
def data_by_year(station, year):
    filename = './data/TG_STAID' + str(station).zfill(6) +'.txt'
    df = pd.read_csv(filename, skiprows=20)
    df['    DATE']= df['    DATE'].astype(str)
    data = df[df['    DATE'].str.startswith(str(year))].to_dict(orient='records')
    return data


if __name__ == '__main__':
    app.run(debug=True)