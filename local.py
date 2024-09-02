## RECURSO QUE LISTA PERSONAS ##
from flask import Flask, jsonify, request

app = Flask(__name__)

## PARA BUSCAR INFORMACION ##
@app.route("/users/<int:user_id>", methods=['GET'])
def get_user(user_id):
    data = request.get_json()
    user = {"user_id": data.get("user_id"), "email": data.get("email"), "password": data.get("password")}
    return jsonify(user), 200

## PARA INSERTAR INFORMACION ##
@app.route("/users", methods=['POST'])
def create_user():
    data = request.get_json()
    new_user = {"user_id": data.get("user_id"), "email": data.get("email"), "password": data.get("password")}
    return jsonify(new_user), 201

# Endpoint para actualizar un usuario
@app.route("/users/<int:user_id>", methods=['PUT'])
def update_user(user_id):
    data = request.get_json()
    # Aquí podrías incluir lógica para buscar el usuario por user_id y actualizarlo
    updated_user = {"user_id": user_id, "email": data.get("email"), "password": data.get("password")}
    return jsonify(updated_user), 200

# Endpoint para eliminar un usuario
@app.route("/users/<int:user_id>", methods=['DELETE'])
def delete_user(user_id):
    # Aquí podrías incluir lógica para eliminar el usuario por user_id
    return jsonify({"message": f"Usuario con ID {user_id} eliminado con éxito"}), 200
    

if __name__ == '_main_':
    app.run(debug=True)