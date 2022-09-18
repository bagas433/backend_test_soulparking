from flask import Blueprint, request
from flask_inputs import Inputs
import jsonschema
import datetime
import time

todo = Blueprint('todo', __name__)
todoMaster = [] # TEMP DATABASE

######### GENERAL FUNCTION  ##################

# FOR VALIDATION
payload_schema = {
   'type'       : 'object',
   'properties' :{
       "title":{
           "type":"string"
       },
       "description":{
           "type":"string"
       }
   },
   "required"   :["title", "description"]
}
def validatePayload(payload):
    try:
        jsonschema.validate(instance=payload, schema=payload_schema)
    except jsonschema.ValidationError as e:
        return responseBuilder(e.message, [], 400)
    except jsonschema.SchemaError as e:
        return responseBuilder(e.message, [], 400)


def formattingDate(date):
    formatted = date.strftime("%d-%m-%Y %H:%M:%S")
    return formatted

def responseBuilder(message, data, status_code):
    response = {
        "message"   :message,
        "data"      :data,
    }
    return response, status_code


def checkExistTodoList(todo_id):
    todoListDetail = {}
    for key, value in enumerate(todoMaster):
        if value['id'] == todo_id:
            todoListDetail['data'] = todoMaster[0]
            todoListDetail['key'] = key
            return todoListDetail
    return False
###############################################################

@todo.route('', methods=['GET'])                                            
def index():
    return responseBuilder("Succesfully get all todo list", todoMaster, 200)

@todo.route('', methods=['POST'])
def createTodo():
    today = datetime.datetime.now()
    currentTimemillis = str(round(time.time() * 1000))        
    idTodoList = str(today.year) + str(currentTimemillis[-5:]) # SETUP PRIMARY KEY

    payload = request.get_json()
    validate = validatePayload(payload)
    if(validate):
        return validate


    data = {
        "id"            : idTodoList,
        "title"         : payload['title'],
        "description"   : payload['description'],
        "finished_at"   : None,
        "created_at"    : formattingDate(today),
        "updated_at"    : None,
        "deleted_at"    : None,
    }

    todoMaster.append(data)
    return responseBuilder("Succesfully add todo list", data, 201)

@todo.route('/<todo_id>', methods=['GET'])
def detailTodo(todo_id):
    detail = checkExistTodoList(todo_id)

    if(detail):
        return responseBuilder("Sucessfully get detail todo list", detail['data'], 200)
    else:
        return responseBuilder("todo list ID not found", [], 404)


@todo.route('/<todo_id>', methods=['PUT', 'PATCH'])
def updateTodo(todo_id):
    detail = checkExistTodoList(todo_id)
    today = datetime.datetime.now()

    if(detail):
        payload = request.get_json()
        validate = validatePayload(payload)
        if(validate):
            return validate

        keyArrayTodoMaster = detail['key']
        todoMaster[keyArrayTodoMaster]['title'] = payload['title']
        todoMaster[keyArrayTodoMaster]['description'] = payload['description']
        todoMaster[keyArrayTodoMaster]['updated_at'] = formattingDate(today)

        return responseBuilder("Sucessfully update todo list", todoMaster[keyArrayTodoMaster], 200)
    else:
        return responseBuilder("todolist ID not found", [], 404)

@todo.route('/<todo_id>', methods=['DELETE'])
def deleteTodo(todo_id):
    detail = checkExistTodoList(todo_id)
    today = datetime.datetime.now()

    if(detail):
        keyArrayTodoMaster = detail['key']
        todoMaster[keyArrayTodoMaster]['deleted_at'] = formattingDate(today)
        return responseBuilder("Sucessfully get delete todo list", detail['data'], 200)
    else:
        return responseBuilder("todo list ID not found", [], 404)

@todo.route('/<todo_id>/finish', methods=['POST'])
def finishTodo(todo_id):
    detail = checkExistTodoList(todo_id)
    today = datetime.datetime.now()

    if(detail):
        keyArrayTodoMaster = detail['key']
        todoMaster[keyArrayTodoMaster]['finished_at'] = formattingDate(today)
        return responseBuilder("Sucessfully finished todo list", detail['data'], 200)
    else:
        return responseBuilder("todo list ID not found", [], 404)