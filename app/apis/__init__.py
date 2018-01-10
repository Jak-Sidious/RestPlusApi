from flask_restplus import Api

# from .models.cats import api as ns1


api = Api(
    title='My title',
    version='1.0',
    description='A description of sorts'
)


from .views.user import api as ns1
from .views.category import api as ns2
from .views.recipie import api as ns3
# api.add_namespace(ns1)
api.add_namespace(ns1)
api.add_namespace(ns2)
api.add_namespace(ns3)