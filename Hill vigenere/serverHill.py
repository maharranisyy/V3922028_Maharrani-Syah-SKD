from flask import Flask, render_template, request, jsonify
import numpy as np

app = Flask(__name__)

def preprocess_text(text):
    # Mengonversi teks ke huruf kapital dan menghapus karakter non-alfabet
    text = ''.join(filter(str.isalpha, text.upper()))
    return text

def matrix_to_numbers(matrix):
    return np.array([[ord(char) - ord('A') for char in row] for row in matrix])

def numbers_to_matrix(numbers):
    return np.array([[chr(num + ord('A')) for num in row] for row in numbers])

def encrypt(plaintext, key_matrix):
    plaintext = preprocess_text(plaintext)

    if len(plaintext) % len(key_matrix) != 0:
        plaintext += 'X' * (len(key_matrix) - len(plaintext) % len(key_matrix))

    plaintext_matrix = matrix_to_numbers([plaintext[i:i+len(key_matrix)] for i in range(0, len(plaintext), len(key_matrix))])
    encrypted_matrix = np.dot(plaintext_matrix, key_matrix) % 26

    ciphertext = numbers_to_matrix(encrypted_matrix).flatten()
    return ''.join(ciphertext)

def decrypt(ciphertext, key_matrix):
    ciphertext = preprocess_text(ciphertext)
    ciphertext_matrix = matrix_to_numbers([ciphertext[i:i+len(key_matrix)] for i in range(0, len(ciphertext), len(key_matrix))])

    key_matrix_inv = np.linalg.inv(key_matrix)
    key_matrix_inv = np.round(key_matrix_inv * np.linalg.det(key_matrix)).astype(int)
    key_matrix_inv = key_matrix_inv % 26

    decrypted_matrix = np.dot(ciphertext_matrix, key_matrix_inv) % 26

    decrypted_text = numbers_to_matrix(decrypted_matrix).flatten()
    return ''.join(decrypted_text)

# Matriks kunci Hill Cipher 3x3
key_matrix_3x3 = np.array([[6, 24, 1], [13, 16, 10], [20, 17, 15]])

@app.route('/')
def index():
    return render_template('hill.html')

@app.route('/encrypt', methods=['POST'])
def encrypt_route():
    data = request.get_json()
    plaintext = data['plaintext']
    ciphertext = encrypt(plaintext, key_matrix_3x3)
    return jsonify({'ciphertext': ciphertext})

@app.route('/decrypt', methods=['POST'])
def decrypt_route():
    data = request.get_json()
    ciphertext = data['ciphertext']
    decrypted_text = decrypt(ciphertext, key_matrix_3x3)
    return jsonify({'decryptedText': decrypted_text})

if __name__ == '__main__':
    app.run(debug=True)
