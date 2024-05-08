from flask import Flask, render_template, request
import requests

API_KEY = '98da00d25670271167571d65b1b21b1a'

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/locate', methods=['POST'])
def locate():
    ip_address = request.form['ip_address']
    response = requests.get(f'http://api.ipstack.com/{ip_address}?access_key={API_KEY}')
    data = response.json()
    
    if 'error' in data:
        return data['error']['info']
    
    country = data['country_name']
    region = data['region_name']
    city = data['city']
    latitude = data['latitude']
    longitude = data['longitude']
    
    return render_template('location.html', 
                           ip_address=ip_address,
                           country=country,
                           region=region,
                           city=city,
                           latitude=latitude,
                           longitude=longitude)
    

if __name__ == '__main__':
    app.run(debug=True)
