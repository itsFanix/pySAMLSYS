from flask import Flask, render_template
from flask import Flask
from flask_saml2.sp  import ServiceProvider



class MyServiceProvider(ServiceProvider):
    def get_default_login_return_url(self):
        return super().get_default_login_return_url()
    
    def get_logout_return_url(self):
        return super().get_logout_return_url()


app = Flask(__name__)


sp = MyServiceProvider()



@app.route("/")
def home(): 
    return "Welcome Home"

@app.route('/dashboard')
def dashboard():
    return 'You ar logged in using SAML!'