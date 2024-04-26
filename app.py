import csv
from flask import Flask, render_template, url_for

app = Flask(__name__)

# Define a route for listing the videos
@app.route('/')
def video_list():
    # Read data from the CSV file
    with open('data/data.csv', 'r') as file:
        reader = csv.reader(file)
        data = {row[0]: row[1] for row in reader}

    # Render the video list template with dynamic data
    return render_template('video_list.html', data=data)

# Define a route for dynamically created pages
@app.route('/generate_page/<page_url>')
def generate_page(page_url):
    # Read data from the CSV file
    with open('data/data.csv', 'r') as file:
        reader = csv.reader(file)
        data = {row[0]: row[1] for row in reader}

    # Get the URL for the given page_url
    source_url = data.get(page_url, '')

    # Render the HTML template with dynamic data
    return render_template('dynamic_page.html', page_url=page_url, source_url=source_url)

if __name__ == '__main__':
    app.run(debug=True)
