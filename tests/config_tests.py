# import pytest
# from transitdata import tr
# import sqlalchemy as sa
# from transitdata import create_app
# from transitdata.config import TestingConfig
# from transitdata.models import Base


# @pytest.fixture
# def client():
#     db_fd, flaskr.app.config['DATABASE'] = tempfile.mkstemp()
#     flaskr.app.config['TESTING'] = True

#     with flaskr.app.test_client() as client:
#         with transitdata.app.app_context():
#             flaskr.init_db()
#         yield client

#     os.close(db_fd)
#     os.unlink(flaskr.app.config['DATABASE'])

# @pytest.yield_fixture
# def app():
#     engine = sa.create_engine(TestingConfig.SQLALCHEMY_DATABASE_URI)

#     def _app(config_class):
#         app = create_app(config_class)
#         app.test_request_context().push()

#         if config_class is TestingConfig:
#             # start with empty database
#             engine.drop_all()
#             # create tables
#             Base.metadata.create_all(engine)

#         return app

#     yield _app
#     engine.session.remove()
#     engine.drop_all()

    # if str(db.engine.url) == TestingConfig.SQLALCHEMY_DATABASE_URI:
    #     db.drop_all()

