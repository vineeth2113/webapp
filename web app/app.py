from flask import Flask, render_template
import csv

app = Flask(__name__)

@app.route('/')
def index():
    data = []
    with open('example.csv', newline='') as csvfile:
        csvreader = csv.reader(csvfile)
        headers = next(csvreader)
        for row in csvreader:
            data.append(row)
    return render_template('index.html', headers=headers, data=data)

if __name__ == '__main__':
    app.run(debug=False,host='0.0.0.0')
