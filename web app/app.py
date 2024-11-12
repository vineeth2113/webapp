from flask import Flask, render_template
import csv
import os

app = Flask(__name__)

# Directory where your CSV files are stored
CSV_FOLDER = 'csv_files'  # Adjust to the folder containing example.csv and disease.csv

# Function to read a CSV file and return data as a list of dictionaries
def read_csv(file_path):
    data = []
    with open(file_path, newline='', encoding='utf-8') as csvfile:
        csvreader = csv.DictReader(csvfile)
        for row in csvreader:
            data.append(row)
    return data

@app.route('/')
def index():
    # Define the CSV files you want to read
    csv_files = ['example.csv', 'disease.csv']

    # Read data from each CSV file
    all_data = {}
    for file in csv_files:
        file_path = os.path.join(CSV_FOLDER, file)
        all_data[file] = read_csv(file_path)

    # Render the data to an HTML template
    return render_template('index.html', all_data=all_data)

if __name__ == '__main__':
    app.run(debug=True)
