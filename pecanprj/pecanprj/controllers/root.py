import pecan
from pecan import expose, redirect

from webob.exc import status_map


# class RootController(object):
#
#     @expose(generic=True, template='index.html')
#     def index(self):
#         return dict()
#
#     @index.when(method='POST')
#     def index_post(self, q):
#         # redirect('https://pecan.readthedocs.io/en/latest/search.html?q=%s' % q)
#         return 'Hello World!'
#
#     @expose('error.html')
#     def error(self, status):
#         try:
#             status = int(status)
#         except ValueError:  # pragma: no cover
#             status = 500
#         message = getattr(status_map.get(status), 'explanation', '')
#         return dict(status=status, message=message)

class BooksController(object):
    @expose()
    def index(self):
        return "Welcome to book section."

    # /catalog/books/bestsellers
    @expose()
    def bestsellers(self):
        return "We have 5 books in the top 10."

class CatalogController(object):
    @expose()
    def index(self):
        return "Welcome to the catalog."

    # /catalog/books
    books = BooksController()

class RootController(object):
    @expose()
    def index(self):
        return "Welcome to store.example.com!"

    @expose()
    def hours(self):
        return "Open 24/7 on the web."

    @expose()
    def hello(self):
        return 'Hello World'

    @expose('html_template.html')
    def hellotemp(self):
        return {'msg': 'Hello!'}

    @expose('json')
    def hellojson(self):
        return {'msg': 'Hello!'}

    @expose('json')
    @expose('text_template.html', content_type='text/plain')
    @expose('html_template.html')
    def hellostack(self):
        return {'msg': 'Hello!'}

    @expose(route='some-path1')
    def some_path1(self):
        return dict()

    @expose(route='some-path2')
    def some_path2(self):
        return dict()

    # HTTP GET /
    @expose(generic=True, template='json')
    def index(self):
        return dict()

    # HTTP POST /
    @index.when(method='POST', template='json')
    def index_POST(self, **kw):
        uuid = 'uuid'
        return dict(uuid=uuid)

# /catalog
pecan.route(RootController, 'catalog', CatalogController())

# /some-path
pecan.route('some-path2', RootController.some_path2)