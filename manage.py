# manage.py


import os
import unittest
import coverage
from flask import Flask
from flask_jwt_extended import JWTManager
from flask_restplus import Api
from flask_script import Manager, Server
from flask_migrate import Migrate, MigrateCommand


app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = 'super-secret'  # Change this!
jwt = JWTManager(app)
api = Api()

# This is where the duck typing magic comes in
jwt._set_error_handler_callbacks(api)

COV = coverage.coverage(
    branch=True,
    include='project/*',
    omit=[
        'project/tests/*',
        'project/server/config.py',
        'project/server/*/__init__.py'
    ]
)
COV.start()

from project.server import create_app, db, models
app = create_app()

migrate = Migrate(app, db)
manager = Manager(app)

# migrations
manager.add_command('db', MigrateCommand)

manager.add_command("runserver", Server(
    # use_debugger = True,
    # use_reloader = True,
    host = '127.0.0.1',
    port='5000') )

@manager.command
def test():
    """Runs the unit tests without test coverage."""
    tests = unittest.TestLoader().discover('project/tests', pattern='test*.py')
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        return 0
    return 1


@manager.command
def cov():
    """Runs the unit tests with coverage."""
    tests = unittest.TestLoader().discover('project/tests')
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        COV.stop()
        COV.save()
        print('Coverage Summary:')
        COV.report()
        basedir = os.path.abspath(os.path.dirname(__file__))
        covdir = os.path.join(basedir, 'tmp/coverage')
        COV.html_report(directory=covdir)
        print('HTML version: file://%s/index.html' % covdir)
        COV.erase()
        return 0
    return 1


@manager.command
def create_db():
    """Creates the db tables."""
    db.create_all()


@manager.command
def drop_db():
    """Drops the db tables."""
    db.drop_all()


if __name__ == '__main__':
    manager.run()