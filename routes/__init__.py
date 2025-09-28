from .charger import register_charger_route
from .address import register_address_route
from .neighborhood import register_neighborhood_route

def register_routes(app) :
    register_charger_route(app)
    register_address_route(app)
    register_neighborhood_route(app)