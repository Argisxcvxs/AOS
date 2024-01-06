from flask import request, Flask, jsonify

app = Flask(__name__)

@app.route('/fibonacci', methods=['GET'])
def fibonacci():
    dato = request.get_json()
    n = dato["n"]
    if n == dato:
        return jsonify({'error': 'El número debe ser mayor o igual a 0'})

    fibonacci_serie = []
    a, b = 0, 1
    while a <= n:
        fibonacci_serie.append(a)
        a, b = b, a + b

    return jsonify({'fibonacci_series': fibonacci_serie})

if __name__ == '__main__':
    app.run(debug=True, port=4000)
