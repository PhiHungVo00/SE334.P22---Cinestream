from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.services.auth_service import login_service, logout_service, register_service

AUTH_BLUEPRINT = Blueprint('auth', __name__)

@AUTH_BLUEPRINT.route('/login', methods=['POST'])
def login():
    try:
        # Debug: In thông tin request
        print(f"Content-Type: {request.content_type}")
        print(f"Raw data: {request.data}")

        data = request.get_json()
        print(f"Parsed JSON: {data}")

        if not data:
            return jsonify({'message': 'No JSON data provided'}), 400

        username = data.get('username')
        password = data.get('password')

        print(f"Username: {username}")
        print(f"Password length: {len(password) if password else 0}")

        if not username or not password:
            return jsonify({'message': 'Username and password are required'}), 400

        result = login_service(username, password)
        print(f"Login successful: {result}")
        return jsonify(result), 200

    except ValueError as e:
        print(f"ValueError: {str(e)}")
        return jsonify({'message': str(e)}), 401
    except Exception as e:
        print(f"Unexpected error: {str(e)}")
        return jsonify({'message': f'Server error: {str(e)}'}), 500

@AUTH_BLUEPRINT.route('/logout', methods=['POST'])
@jwt_required()
def logout():
    return logout_service()

@AUTH_BLUEPRINT.route('/register', methods=['POST'])
def register():
    try:
        data = request.get_json()
        fields = ['username', 'password', 'name', 'phone', 'email']
        for field in fields:
            if field not in data:
                return jsonify({'message': f'{field} is required'}), 400

        username = data.get('username')
        password = data.get('password')
        name = data.get('name')
        phone = data.get('phone')
        email = data.get('email')

        if not all([username, password, name, phone, email]):
            return jsonify({'message': 'All fields are required'}), 400

        result = register_service(username, password, name, phone, email)
        return result
    except ValueError as e:
        return jsonify({'message': str(e)}), 400
    except Exception as e:
        print(f"Register error: {str(e)}")
        return jsonify({'message': f'Server error: {str(e)}'}), 500

# Route test
@AUTH_BLUEPRINT.route('/test', methods=['GET'])
def test():
    return jsonify({'message': 'Auth API is working'}), 200