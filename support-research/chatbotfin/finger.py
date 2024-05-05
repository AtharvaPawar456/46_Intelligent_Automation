from flask import Flask, render_template, request, jsonify, session
from fido2 import cbor
from fido2.client import ClientData
from fido2.ctap2 import AttestationObject, AuthenticatorData
from fido2.server import Fido2Server, RelyingParty
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from base64 import urlsafe_b64encode, urlsafe_b64decode
import os

app = Flask(__name__)
app.secret_key = os.urandom(32)

# Change these values to fit your application
ORIGIN = 'http://localhost:5000'
RP_NAME = 'YourApp'
RP_ID = 'localhost'

# Initialize FIDO2 server
rp = RelyingParty(RP_ID, RP_NAME, urlsafe_b64decode(os.urandom(32)))
fido2_server = Fido2Server(rp)

# Mock user database
registered_credentials = {}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['POST'])
def register():
    username = request.form['username']
    user_id = username.encode('utf-8')
    challenge = os.urandom(32)

    attestation_options, state = fido2_server.register_begin(
        {
            'id': user_id,
            'name': username,
            'displayName': username
        },
        user_verification='discouraged',
        authenticator_attachment='platform'
    )

    session['state'] = state
    session['username'] = username

    return jsonify(attestation_options)

@app.route('/register/complete', methods=['POST'])
def register_complete():
    attestation_response = request.json
    state = session['state']
    username = session['username']

    # Complete registration
    attestation_object = AttestationObject(attestation_response['attestationObject'])
    client_data = ClientData(attestation_response['clientDataJSON'])

    authenticator_data = fido2_server.register_complete(
        state,
        attestation_object,
        client_data
    )

    credential_id = urlsafe_b64encode(authenticator_data.credential_data.credential_id).decode('utf-8')
    registered_credentials[username] = credential_id

    return jsonify({'success': True})

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    user_id = username.encode('utf-8')
    challenge = os.urandom(32)

    credential_id = registered_credentials.get(username)
    if not credential_id:
        return jsonify({'error': 'User not registered'})

    assertion_options, state = fido2_server.authenticate_begin(
        {
            'id': user_id,
            'name': username,
            'displayName': username
        },
        credentials=[{'type': 'public-key', 'id': urlsafe_b64decode(credential_id)}],
        user_verification='discouraged'
    )

    session['state'] = state
    session['username'] = username

    return jsonify(assertion_options)

@app.route('/login/complete', methods=['POST'])
def login_complete():
    assertion_response = request.json
    state = session['state']
    username = session['username']

    credential_id = registered_credentials.get(username)
    if not credential_id:
        return jsonify({'error': 'User not registered'})

    credential_id = urlsafe_b64decode(credential_id)
    credential = {'type': 'public-key', 'id': credential_id}
    assertion_response = {'credentialId': assertion_response['credentialId'], 'authenticatorData': assertion_response['authenticatorData'], 'clientDataJSON': assertion_response['clientDataJSON'], 'signature': assertion_response['signature'], 'userHandle': b''}

    try:
        fido2_server.authenticate_complete(state, credential, assertion_response, rp_id=RP_ID)
        return jsonify({'success': True})
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
