from requests_oauthlib.oauth2_session import OAuth2Session
import jwt


scope = ['https://it.nttdata.com/example']

oauth = OAuth2Session(
    'identificatore_client',
    redirect_uri='https://it.nttdata.com/redirect',
    scope=scope)

token = oauth.fetch_token('https://it.nttdata.com/token',
                          client_secret='password_esempio')

jwt.decode(token, options={"verify_signature":False})
