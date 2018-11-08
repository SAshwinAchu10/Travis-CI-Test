# # project/server/user/views.py
# import json
#
# from flask import render_template, Blueprint, url_for, \
#     redirect, flash, request
# from flask_login import login_user, logout_user, login_required
# from flask import jsonify
# from project.server import bcrypt, db
# from project.server.models import Alpha
# from project.server.alpha.forms import AlphaForm
# from flask_cors import CORS
#
# alpha_blueprint = Blueprint('alpha', __name__,)
# CORS(alpha_blueprint)
#
# @alpha_blueprint.route('/alphaData', methods=['GET', 'POST'])
# def adddata():
#     if(request.method=='POST'):
#         form = AlphaForm(request.form)
#         if form.validate_on_submit():
#             alpha = Alpha(
#                 expert=form.expert.data,
#                 company=form.company.data,
#                 date=form.date.data,
#                 variable=form.variable.data,
#                 lowerbound=form.lowerbound.data,
#                 upperbound=form.upperbound.data,
#             )
#             result = json.dumps(request.form)
#             db.session.add(alpha)
#             db.session.commit()
#
#             return result
#
#         return form
#     elif(request.method=='GET'):
#         getData = Alpha.query.all()
#         contactsArr = []
#         for contact in getData:
#             contactsArr.append(contact.toDict())
#         return jsonify(contactsArr)
#
#
#
