# project/server/auth/views.py


from flask import Blueprint, request, make_response, jsonify
from flask.views import MethodView

from project.server import bcrypt, db
from project.server.models import Expert
from flask_cors import CORS

expert_blueprint = Blueprint('expert', __name__)
CORS(expert_blueprint)

class ExpertPOSTAPI(MethodView):
    def post(self):

        post_data = request.get_json()
        try:
            expert = Expert(
                name=post_data.get('name'),
                nickname=post_data.get('nickname'),
            )
            db.session.add(expert)
            db.session.commit()
            responseObject = {
                'status': 'Success',
                'result': {
                    "name":expert.name,
                    "nickname":expert.nickname
                },
                'message':"Added successfully"
            }
            return make_response(jsonify(responseObject)), 200
        except Exception as e:
            responseObject = {
                'status': 'fail',
                'message': 'Some error occurred. Please try again.'
            }
            return make_response(jsonify(responseObject)), 401

class ExpertGETAPI(MethodView):
    def get(self):
        try:
            expert = Expert.query.all()
            contactsArr = []
            for contact in expert:
             contactsArr.append(contact.toDict())
            return jsonify(contactsArr)
        except Exception as e:
            responseObject = {
                'status': 'fail',
                'message': 'Some error occurred. Please try again.'
            }
            return make_response(jsonify(responseObject)), 401


@expert_blueprint.route('/alpha/expert/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def bucketlist_manipulation(id, **kwargs):
    gotData = Expert.query.filter_by(id=id).first()

    if request.method == "DELETE":
        if(gotData):
            db.session.delete(gotData)
            db.session.commit()
            response = {
                    'status': 'Success',
                    'result': {
                        "id":gotData.id,
                        "name":gotData.name,
                        "nickname":gotData.nickname,
                        "active": gotData.active
                    },
                    'message':"Removed successfully"
                }
            return make_response(jsonify(response)), 200
        else:
            return "Error while deleting"
    elif request.method == 'PUT':
        obj = request.get_json()
        if(obj):

            gotData.name = obj.get('name')
            gotData.nickname = obj.get('nickname')
            db.session.commit()

            response = {
                    'status': 'Success',
                    'result': {
                        "id":gotData.id,
                        "name":gotData.name,
                        "nickname":gotData.nickname,
                        "active": gotData.active
                    },
                    'message':"Updated successfully"
                }
            return make_response(jsonify(response)), 200
        else:
            return "Error while updating"
    else:
        if(gotData):
            response = {
                'status': 'Success',
                'result': {
                    "id": gotData.id,
                    "name": gotData.name,
                    "nickname": gotData.nickname,
                    "active": gotData.active
                },
                'message': "Retrieved successfully"
            }
            return make_response(jsonify(response)), 200
        else:
            return "Error while fetching data"

@expert_blueprint.route('/alpha/expert/status/<int:id>', methods=['PUT'])
def update(id, **kwargs):
    gotData = Expert.query.filter_by(id=id).first()

    if request.method == 'PUT':

        obj = request.get_json()
        if (obj):

            gotData.active = obj.get('active')
            db.session.add(gotData)
            db.session.commit()

            response = {
                'status': 'Success',
                'result': {
                    "id": gotData.id,
                    "name": gotData.name,
                    "nickname": gotData.nickname,
                    "active": gotData.active
                },
                'message': "Updated successfully"
            }
            return make_response(jsonify(response)), 200
        else:
            return "Error while updating"
    else:
        return "Error"


# define the API resources
expert_post_view = ExpertPOSTAPI.as_view('expert_post_api')
expert_get_view = ExpertGETAPI.as_view('expert_get_api')

expert_blueprint.add_url_rule(
    '/alpha/expert/createExpert',
    view_func=expert_post_view,
    methods=['POST']
)

expert_blueprint.add_url_rule(
    '/alpha/expert/getAllExpert',
    view_func=expert_get_view,
    methods=['GET']
)

