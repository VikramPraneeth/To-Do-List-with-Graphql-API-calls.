from flask import Flask, request, jsonify
from flask_graphql import GraphQLView
from graphql_schema import schema

import os
from flask_keycloak import Keycloak

app = Flask(__name__)
app.config.from_envfile('.env')

# Initialize Keycloak
keycloak = Keycloak(app, config=dict(server_url=app.config['KEYCLOAK_SERVER_URL'],
                                     realm_name=app.config['KEYCLOAK_REALM'],
                                     client_id=app.config['KEYCLOAK_CLIENT_ID'],
                                     client_secret=app.config['KEYCLOAK_CLIENT_SECRET'],
                                     ssl_required=False,  # Adjust based on your setup
                                     browser_flow=True))  # Use browser flow for login

# Protect GraphQL endpoint with Keycloak
app.add_url_rule('/graphql', view_func=GraphQLView.as_view('graphql', schema=schema, graphiql=True, context=lambda: {'keycloak': keycloak}))

@app.route('/login')
def login():
    return keycloak.openid_connect.authorize()  # Redirect to Keycloak login

@app.route('/callback')
def callback():
    user = keycloak.openid_connect.userinfo()  # Access user info after login
    return f'<h1>Welcome, {user["preferred_username"]}!</h1>'

if __name__ == '__main__':
    app.run(debug=True)
