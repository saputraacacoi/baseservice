from app.tables import db
from app.tables import ma

class GroupHasRole(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    id_group = db.Column(db.Integer)  
    id_role = db.Column(db.Integer)

    def __serialize__(self):
        return{
            'id' : self.id,
            'id_group' : self.id_group,
            'id_role' : self.id_role,
        }

db.create_all()
class GroupHasRoleSchema(ma.Schema):
    class Meta:
        model = GroupHasRole
        fields = ['id','id_group','id_role']

grouphasrole_schema = GroupHasRoleSchema(many=True) 