from flask import Flask, jsonify, request

# __name__ : Python var, gives each file a unique name
app = Flask(__name__)

stores = [
    {
        'name': 'My Wonderful Store',
        'items': [
            {
                'name': 'My Item',
                'price': 15.99
            }
        ]
    }
]

#  POST /store data: {name:}
@app.route('/store', methods=['POST'])
def create_store():
    request_data = request.get_json()
    new_store = {
        'name': request_data['name'],
        'items': []
    }
    stores.append(new_store)
    return jsonify(new_store)

# GET /store/<string:name>      'http://127.0.0.1:5000/store/some_name
@app.route('/store/<string:name>')
def get_store(name):
    found = list(filter(lambda x: x['name'] == name, stores))
    if not found:
        return jsonify({'message': 'store not found'})
    else:
        return jsonify(found[0])

# GET /store/
@app.route('/store/')
def get_stores():
    return jsonify({'stores': stores})

# POST /store/<string:name>/item {name:, price:}
@app.route('/store/<string:name>/item', methods=['POST'])
def create_item_in_store(name):
    found = list(filter(lambda x: x['name'] == name, stores))
    if not found:
        return jsonify({'message': 'store not found'})
    else:
        store = found[0]
        request_data = request.get_json()
        new_item = {
            'name': request_data['name'],
            'price': request_data['price']
        }
        store['items'].append(new_item)
        return jsonify(store)

# GET /store/<string:name>/item
@app.route('/store/<string:name>/item')
def get_item_in_store(name):
    found = list(filter(lambda x: x['name'] == name, stores))
    if not found:
        return jsonify({'message': 'store not found'})
    else:
        return jsonify({'items': found[0]['items']})

app.run(port=5000)
