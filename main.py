import requests
import os
import time
from flask import Flask, render_template, request
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.environ.get('API_KEY')

app = Flask(__name__)


def find_timezone(location):
    if not API_KEY:
        return "not found (404 error)"

    #get latitude and longitude of user's input
    geocode_url = f"https://maps.googleapis.com/maps/api/geocode/"\
                f"json?address={location}&key={API_KEY}'"
    response = requests.get(geocode_url)

    if response.status_code == 200:
        lat = response.json()['results'][0]['geometry']['location']['lat']
        lng = response.json()['results'][0]['geometry']['location']['lng']

        #get timezone of location
        timestamp = int(time.time())  #get the current timestamp required for URL:
        timezone_url = 'https://maps.googleapis.com/maps/'\
                    f'api/timezone/json?location={lat}'\
                    f'%2C{lng}&timestamp={timestamp}&key={API_KEY}'
        time_response = requests.get(timezone_url)

        if time_response.status_code == 200:
            timezone = time_response.json()["timeZoneName"]
            return timezone
    return "Invalid input"

@app.route('/', methods=['GET', 'POST'])
def index():
    location = None
    timezone = None
    if request.method == 'POST':
        location = request.form['location']
        timezone = find_timezone(location)
    return render_template('index.html', timezone=timezone, location=location.title())


if __name__ == '__main__':
    app.run(debug=True)
