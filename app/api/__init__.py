from flask_restplus import Api

api = Api(version='1.0', title='group has role', description='simple group has role service code')
ns  = api.namespace('v0.1', 'group has role service')