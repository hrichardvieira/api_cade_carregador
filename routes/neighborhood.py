from flask_openapi3 import Tag

from urllib.parse import unquote
from sqlalchemy.exc import IntegrityError

from model import Session
from model import Neighborhood

from schemas import ErrorSchema
from schemas import NeighborhoodSchema
from schemas.neighborhood import NeighborhoodViewSchema
from schemas.neighborhood import NeighborhoodFindSchema
from schemas.neighborhood import show_neighborhood

neighborhood_tag = Tag(name="Neighborhood", description="Adição e Visualização de Bairro.")

def register_neighborhood_route(app) :
    @app.post('/neighborhood', tags=[neighborhood_tag], responses={"200" : NeighborhoodViewSchema, "409" : ErrorSchema, "400" : ErrorSchema})
    def add_neighborhood(form: NeighborhoodSchema) :
        """Adiciona um novo bairro ao banco de dados

        Retorna as informa do bairro cadastrado.
        """
        new_register = Neighborhood(
            name = form.name,
            id_city = form.id_city
        )

        #logger.debug()

        try :
            session = Session()
            session.add(new_register)
            session.commit()
            #logger.debug()
            return show_neighborhood(new_register), 200
        
        except IntegrityError as integrityError :
            error_message = "Um bairro já foi cadastrado com esse nome!"
            #logger.warning()
            return {"message" : error_message}, 409
        
        except Exception as exception :
            print(exception)
            error_message = "Não foi possível salvar o bairro."
            #logger.warning()
            return {"message" : error_message}, 400

    @app.get('/neighborhood', tags=[neighborhood_tag], responses={"200" : NeighborhoodViewSchema, "404" : ErrorSchema})
    def get_neighborhood(query: NeighborhoodFindSchema) :
        """Faz a busca do bairro com base no nome do bairro
        Retorna o bairro cadastrado
        """

        neighborhood_name = query.name
        #logger.debug()

        session = Session()
        neighborhood = session.query(Neighborhood).filter(Neighborhood.name == neighborhood_name).first()

        if not neighborhood :
            error_message = "bairro não encontrado!"
            #logger.warning()
            return {"message" : error_message}, 404
        else :
            #logger.debug()
            return show_neighborhood(neighborhood), 200