#!/usr/bin/env python3
'''
New Flask view that handles all routes for the session authentication
'''
from api.v1.views import app_views
from flask import request, jsonify
from models.user import User
import os

User = User()

@app_views.route('/auth_session/login', methods=['POST'], strict_slashes=False)
def auth_session():
    '''
    Creates POST route that logins session
    '''
    email = request.form.get('email')
    password = request.form.get('password')
    if not email:
        return jsonify({ "error": "email missing" }), 400
    if not password:
        return jsonify({ "error": "password missing" }), 400

    attribute = {"email": email}
    user_list = User.search(attribute)

    if len(user_list) == 0:
        return jsonify({ "error": "no user found for this email" }), 404

    if user_list[0].is_valid_password(password):
        from api.v1.app import auth
        session_id = auth.create_session(user_list[0].id)
        session_name = os.getenv('SESSION_NAME')
        dict_representation = jsonify(user_list[0].to_json())
        dict_representation.set_cookie(session_name, session_id)
        return dict_representation
    return jsonify({ "error": "wrong password" }), 401
