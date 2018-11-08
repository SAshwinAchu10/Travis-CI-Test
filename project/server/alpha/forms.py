# # project/server/user/forms.py
#
#
# from flask_wtf import FlaskForm
# from wtforms import StringField, PasswordField , IntegerField, DateField
# from wtforms.validators import DataRequired,  Length, EqualTo
#
#
#
# class AlphaForm(FlaskForm):
#     expert = StringField(
#         'Expert',
#         validators=[
#             DataRequired(),
#             Length(min=2, max=40)
#         ]
#     )
#     company = StringField(
#         'Company',
#         validators=[
#             Length(min=2, max=40)
#         ]
#     )
#     date = DateField(
#         'Date'
#     )
#     variable = StringField(
#         'Variable',
#         validators=[
#             Length(min=2, max=40)
#         ]
#     )
#     lowerbound = IntegerField(
#         'Lower Bound'
#
#     )
#     upperbound = IntegerField(
#         'Upper Bound'
#     )
