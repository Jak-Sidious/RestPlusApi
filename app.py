from flask import Flask
from flask_restplus import Resource, Api, fields
from werkzeug.contrib.fixers import ProxyFix
from apis import api

app = Flask(__name__)
api.init_app(app)

app.run(debug=True)

# ready to go implementation without utilising namespaces
# app.wsgi_app = ProxyFix(app.wsgi_app)
# api = Api(app, version='1.0', title='TodoMVC API',
#     description='A simple ToDoMVC API',
# )

# ns = api.namespace('todos', description='TODO operations')

# todo = api.model('Todo', {
#     'id': fields.Integer(readOnly=True, description='The task unique identifier'),
#     'task': fields.String(required=True, description='The task details')
# })

# class TodoDAO(object):
#     def __init__(self):
#         self.counter = 0
#         self.todos = []

#     def get(self, id):
#         for todo in self.todos:
#             if todo['id'] == id:
#                 return todo
#             api.abort(404, "Todo {} doesn't exist".format(id))

#     def create(self, data):
#         todo = data
#         todo['id'] = self.counter = self.counter + 1
#         self.todos.append(todo)
#         return todo

#     def update(self, id, data):
#         todo = self.get(id)
#         todo.update(data)
#         return todo

#     def delete(self, id):
#         todo = self.get(id)
#         self.todos.remove(todo)

# DAO = TodoDAO()
# DAO.create({'task': 'Build an API'})
# DAO.create({'task': '?????'})
# DAO.create({'task': 'profit!'})

# @ns.route('/')
# class ToDoList(Resource):
#     '''Shows a list of all todos, and lets you post to add new tasks'''
#     @ns.doc('list_todos')
#     @ns.marshal_list_with(todo)
#     def get(self):
#         '''List all tasks'''
#         return DAO.todos

#     @ns.doc('create_todo')
#     @ns.expect(todo)
#     @ns.marshal_with(todo, code=201)
#     def post(self):
#         '''Create a new task'''
#         return DAO.create(api.payload), 201

#     @ns.route('/<int:id>')
#     @ns.response(404, 'Todo not found')
#     @ns.param('id', 'The task identifier')
#     class Todo(Resource):
#         '''Show a single todo item and lets you delete them'''
#         @ns.doc('get_todo')
#         @ns.marshal_with(todo)
#         def get(self, id):
#             '''Fetch a given resource'''
#             return DAO.get(id)

#         @ns.doc('delete_todo')
#         @ns.response(204, 'Todo deleted')
#         def delete(self, id):
#             '''Delete a task given its identifier'''
#             DAO.delete(id)
#             return '', 204

#         @ns.expect(todo)
#         @ns.marshal_with(todo)
#         def put(self, id):
#             '''Update a task given its identifier'''
#             return DAO.update(id, api.payload)

# if __name__ == '__main__':
#     app.run(debug=True)

#basic
# @api.route('/hello')
# class HelloWorld(Resource):
#     def get(self):
#         return {'hello': 'world'}

# if __name__ == '__main__':
#     app.run(debug=True)

# more extensive example
# todos = {}

# @api.route('/<string:todo_id>')
# class ToDoSimole(Resource):
#     def get(self, todo_id):
#         return {todo_id: todos[todo_id]}

#     def put(self, todo_id):
#         todos[todo_id] = request.form['data']
#         return {todo_id: todos[todo_id]}

# if __name__ == '__main__':
#     app.run(debug=True)