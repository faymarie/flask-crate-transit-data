from transitdata import connection

# class (PostResource):
#     """
#     Resource for guestbook.posts
#     Supported methods: GET, PUT, DELETE
#     """


# class CrateResource(Resource):

#     __name__ = ''
#     __table__ = ''

#     def __init__(self):
#         super(CrateResource, self).__init__()
#         self.cursor = self.connection.cursor()

#     @property
#     def connection(self):
#         if not 'conn' in app_globals:
#             app_globals.conn = connect(app.config['CRATE_HOST'],
#                                        error_trace=True)
#         return app_globals.conn

#     def error(self, message, status=404):
#         return (dict(
#             error=message,
#             status=status,
#         ), status)

#     def refresh_table(self):
#         self.cursor.execute("REFRESH TABLE {}".format(self.__table__))

#     def convert(self, description, results):
#         cols = [c[0] for c in description]
#         return [dict(zip(cols, r)) for r in results]

#     def not_found(self, **kw):
#         keys = ', '.join(('{}="{}"'.format(k,v) for k,v in kw.items()))
#         return self.error('{} with {} not found'.format(self.__name__, keys), 404)

#     def argument_required(self, argument):
#         return self.error('Argument "{}" is required'.format(argument), 400)

# class TileResource(CrateResource):

#     __name__ = 'Tile'
#     __table__ = 'transit.tiles'

# class Post(PostResource):
#     """
#     Resource for guestbook.posts
#     Supported methods: GET, PUT, DELETE
#     """

#     def get(self, id):
#         self.cursor.execute("""
#             SELECT p.*, c.name as country, c.geometry as area
#             FROM guestbook.posts AS p, guestbook.countries AS c
#             WHERE within(p."user"['location'], c.geometry)
#               AND p.id = ?
#         """, (id,))
#         # convert response from Crate into
#         # json-serializable object array
#         response = self.convert(self.cursor.description,
#                                 self.cursor.fetchall())
#         if self.cursor.rowcount == 1:
#             return response[0], 200
#         else:
#             return self.not_found(id=id)

#     def put(self, id):
#         reqparse = reqparser.RequestParser()
#         reqparse.add_argument('text', type=str, location='json')
#         data = reqparse.parse_args()
#         if not data.text:
#             return self.argument_required('text')
#         self.cursor.execute("""
#             UPDATE {}
#             SET text = ?
#             WHERE id = ?
#         """.format(self.__table__), (data.text, id))
#         self.refresh_table()
#         return self.get(id)

# class PostList(PostResource):
#     """
#     Resource for guestbook.posts
#     Supported methods: POST, GET
#     """

#     def __init__(self):
#         super(PostList, self).__init__()

#     def get(self):
#         self.cursor.execute("""
#             SELECT p.*, c.name as country, c.geometry as area
#             FROM guestbook.posts AS p, guestbook.countries AS c
#             WHERE within(p."user"['location'], c.geometry)
#             ORDER BY p.created DESC
#         """)
#         # convert response from Crate into
#         # json-serializable object array
#         response = self.convert(self.cursor.description,
#                                 self.cursor.fetchall())
#         return (response, 200)