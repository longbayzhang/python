
from pecan import expose, request, response, abort
from mako.template import Template

class StudentController(object):
    def __init__(self, student):
        self.student = student

    @expose()
    def name(self):
        return self.student.name

class RootController(object):

    @expose()
    def english(self):
        return 'hello'

    @expose()
    def french(self):
        return 'bonjour'

    @expose()
    def _default(self):
        return 'I cannot say hello in that language'

    @expose()
    def login(self):
        assert request.path == '/login'
        username = request.POST.get('username')
        password = request.POST.get('password')
        response.status = 403
        # response.text = 'Bad Login!'
        return "username + ':' + password"

    @expose('json')
    def hellostatus(self):
        response.status = 203
        return {'foo': 'bar'}

    @expose('json')
    def helloabort(self):
        abort(404)


    # @expose()
    # def _lookup(self, primary_key, *remainder):
    #     student = dict(name='student')
    #     if student:
    #         return StudentController(student), remainder
    #     else:
    #         abort(404)