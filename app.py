from flask import Flask, render_template, url_for
from flask import Flask
from flask_saml2.sp  import ServiceProvider
# from flask_saml2.utils import certificate_from_file, private_key_from_file


# class MyServiceProvider(ServiceProvider):

#     def get_default_login_return_url(self):
#         return url_for('index', _external=True)
    
#     def get_logout_return_url(self):
#          return url_for('index', _external=True)
    



#sp = MyServiceProvider()


app = Flask(__name__)


# app.secret_key = 'not a secret'
# app.config['SERVER_NAME'] = 'http://localhost:8080'



# app.config['SAML2_SP'] = {
#     'certificate' :certificate_from_file('keys\sp-certificate.pem'),
#     'private_key' : private_key_from_file('keys\sp-private-key.pem')

# }

# app.config['SAML2_IDENTITY_PROVIDERS']  = [
#     {
#         'CLASS' : 'flask_smal2.sp.idphandler.IdPHandler',
#         'OPTIONS' : {
#             'display_name': 'KeyCloak',
#             'entity_id' : 'http://localhost:8080/realms/TestRealm',
#             'sso_url': 'http://localhost:8080/realms/TestRealm/protocol/saml',
#             'slo_url' : 'http://localhost:8080/realms/TestRealm/protocol/saml',
#             'certificate' : certificate_from_file('keys\idp-certificate.pem')

#         } 
#     }
# ]




@app.route("/")
def index(): 
    return "Hello world"
    
    # if sp.is_user_logged_in():
    #     auth_data = sp.get_auth_data_in_session()

    #     message = f''' 
    #         <p> You are logged in as <strong>{auth_data.nameid}</strong>. 
    #         The Idp sent back the following attributes:<p> '''
        

    #     logout_url = url_for('flask_saml2_sp.logout')
    #     logout = f'< form action = "{logout_url}" method="POST"><input type ="submit" value="Log out'

    #     return message + logout
    
    # else:
    #     message = '<p> You are logged out.</p>'
    #     login_url = url_for('flask_saml2_sp.login')
    #     link = f'<p><a href="{login_url}"> Log in to continue</a></p>'

    #     return message + link
    

#blueprint
#app.register_blueprint(sp.create_blueprint(), url_prefix='/saml/')


#@app.route('/dashboard')
#@sp.login_required
#def dashboard():
#    return 'You ar logged in using SAML!'