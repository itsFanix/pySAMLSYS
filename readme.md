

# Library I try to use in this project
1. Python-saml : Wheel Error
2. Flask-saml2: It is no longer maintained, which leads to dependency issues



# Keycloack client Settings
1. Client ID
    A unique identifier for the client in the keycloack realm
    Flask app(SP) will reference this ID during SAML communication

2. Client Protocol
     Protocol used for the client 
        *openid-connect* or *saml*

3. Access settings
    - Root URL :  base URL your the application; it helps Keycloak build URLs for redirects
    - Home URL :  Default URL to use when the auth server needs to redirect or link back to client
    - Valid redirect URIs:  Sepicifies the allowable URLs for redirecting back to your application after authentication (Relative path or Wildcard "*")
    - Valid post logout redirect URIs:  Specifies where to redirect the user after log out
  
4. Web Orignins
5.  SAML capabilities
    - Name ID format: The format for the NameID sent in SAML responses (email, username)
      - NameID is a fundemental element in SAML assertions. It represents the principal (user) in the context of the SP. UserId shared between IDP and SP. FNIDFormat when Enabled the IDP enforces the specified NamedID format in all SAML assertions sent to the client. When Disanled: NameID is dertermined dynamically or defaults to the SP's requested format
    

    Keycloak generate a certificat for  each client. To download that certificate, you have 3 choice for format:
      - JKS : Java keystore
      - PKCS12 : 
      - BCFKS : 
    I download a pkcs keystore file . From that file I was able to get the key but not the certificate because newer versions of OpenSSL don't handle older encryption algorithms. HAd to try different approach.
    I just copy and paste certificate from keycloak

