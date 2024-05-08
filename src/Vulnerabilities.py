from requests_oauthlib.oauth2_session import OAuth2Session
import jwt

# Inizializza lo scope
scope = ['https://it.nttdata.com/example']

# Inizializza una sessione OAuth 2
oauth = OAuth2Session(
    'identificatore_client',
    redirect_uri='https://it.nttdata.com/redirect',
    scope=scope)

# Inizializza il token di autenticazione
token = oauth.fetch_token('https://it.nttdata.com/token',
                          client_secret='password_esempio')

# Decodifica il token di autenticazione
jwt.decode(token, options={"verify_signature":False})
