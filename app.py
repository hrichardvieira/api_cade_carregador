from flask_openapi3 import OpenAPI, Info, Tag
from flask_cors import CORS
from flask import redirect

from routes import register_routes

info = Info(title="Cadê o Carregador? API", version="0.0.1")
app = OpenAPI(__name__, info=info)
CORS(app)

home_tag = Tag(name="Documentação", description="Swagger, Redoc ou RapiDoc.")

@app.get('/', tags=[home_tag])
def home() :
    """Redireciona para /openapi.
    """
    return redirect('/openapi')

register_routes(app)
