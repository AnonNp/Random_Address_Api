import requests
from flask import Flask, jsonify, request, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/random-address', methods=['GET'])
def random_address():
    country_code = request.args.get('country', 'us')  # Default to 'us' if no country provided

    # Fetch data from randomuser.me API
    url = f"https://randomuser.me/api/?nat={country_code}"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        user = data['results'][0]
        
        # Extract address data from the API response
        name = user['name']['first'] + ' ' + user['name']['last']
        street = user['location']['street']['name']
        city = user['location']['city']
        state = user['location']['state']
        postal_code = user['location']['postcode']
        country = user['location']['country']

        return jsonify({
            'name': name,
            'street_address': street,
            'city': city,
            'state': state,
            'postal_code': postal_code,
            'country': country
        })
    else:
        return jsonify({'error': 'Could not fetch address data'}), 500

if __name__ == '__main__':
    app.run(debug=True)
