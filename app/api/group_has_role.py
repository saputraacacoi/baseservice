from flask import jsonify, request, Blueprint
from app.api import api, ns
from flask_restplus import Resource, fields
from app.tables.models import GroupHasRole, GroupHasRoleSchema, db

grouphasrole_fields = api.model('GroupHasrole', {
    'id_group': fields.Integer,
    'id_role': fields.Integer
})


@ns.route('/grouphasrole')
class ListGrouphasRole(Resource):

    def get(self):
        """Returns list of Group Has Role."""

