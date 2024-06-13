from flask_keycloak import Keycloak

keycloak = Keycloak(app)

@app.route('/login')
def login():
    return keycloak.login()

@app.route('/callback')
def callback():
    user = keycloak.callback()  # Authentication
    if user:
        return redirect('/todo')  # Redirect to To-Do page after successful login
    else:
        return 'Login failed', 401

def current_user():
    # Retrieve user information from session
    return session.get('user')

def has_pro_license(user):
    return user.get('is_pro', False)  # Default to False for non-pro users
