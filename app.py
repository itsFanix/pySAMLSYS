from flask import Flask, render_template, url_for
from flask import Flask
from flask_saml2.sp  import ServiceProvider
from flask_saml2.utils import certificate_from_file, private_key_from_file


class MyServiceProvider(ServiceProvider):

    def get_default_login_return_url(self):
        return url_for('index', _external=True)
    
    def get_logout_return_url(self):
         return url_for('index', _external=True)
    



sp = MyServiceProvider()


app = Flask(__name__)


app.secret_key = 'not a secret'
app.config['SERVER_NAME'] = 'http://localhost:8080'



app.config['SAML2_SP'] = {
    'certificate' :'',
    'private_key' : ''

}

app.config['SAML2_IDENTITY_PROVIDERS']  = [
    {
        'CLASS' : 'flask_smal2.sp.idphandler.IdPHandler',
        'OPTIONS' : {
            'display_name': 'KeyCloak',
            'entity_id' : 'http://localhost:8080/realms/TestRealm',
            'sso_url': '',
            'slo_url' : '',
            'certificate' : certificate_from_file('cert2.pem')

        } 
    }
]




@app.route("/")
def home(): 
    return "Welcome Home"

@app.route('/dashboard')
def dashboard():
    return 'You ar logged in using SAML!'