from flask import Flask, jsonify
import math

app = Flask(__name__)

def calcular_factorial(n):
    if n < 0:
        return None
    return math.factorial(n)

def es_par_o_impar(n):
    return "par" if n % 2 == 0 else "impar"

@app.route('/numero/<numero>', methods=['GET'])
def procesar_numero(numero):
    try:
        numero = int(numero)
    except ValueError:
        return jsonify({"error": "El valor ingresado no es un numero válido"}), 400

    factorial = calcular_factorial(numero)

    if factorial is None:
        return jsonify({
            "error": "No se puede calcular el factorial de un numero negativo"
        }), 400

    respuesta = {
        "numero": numero,
        "factorial": factorial,
        "tipo": es_par_o_impar(numero)
    }

    return jsonify(respuesta)

@app.route('/', methods=['GET'])
def home():
    return jsonify({
        "mensaje": "Microservicio de cálculo de factorial",
        "uso": "Se debe usar /numero/<numero> para calcular factorial y determinar si es par o impar"
    })

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8000)
