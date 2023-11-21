from lib.todo import *
from lib.todo_list import *

def test_todo_blank_task():
    todo = Todo("")
    assert todo.task == ""
    assert todo.complete == False

def test_todo_complete_blank_task():
    todo = Todo("")
    todo.mark_complete()
    assert todo.complete == True

def test_todolist_blank_list():
    todolist = TodoList()
    assert todolist.todolist == []

def test_todolist_add_string():
    todolist = TodoList()
    todolist.add("test string")
    assert todolist.todolist == ["test string"]

def test_integration_todolist_add():
    todolist = TodoList()
    todo = Todo("test task")
    todolist.add(todo)
    assert todolist.todolist == [todo]

def test_integration_todolist_return_incomplete():
    todolist = TodoList()
    todo = Todo("test task")
    todolist.add(todo)
    assert todolist.incomplete() == [todo]
    assert todolist.complete() == []

def test_integration_todolist_return_complete():
    todolist = TodoList()
    todo = Todo("test task")
    todolist.add(todo)
    todo.mark_complete()
    assert todolist.complete() == [todo]
    assert todolist.incomplete() == []

def test_integration_todolist_give_up():
    todolist = TodoList()
    todo = Todo("test task")
    todo2 = Todo("test task2")
    todo3 = Todo("test task3")
    todolist.add(todo)
    todolist.add(todo2)
    todolist.add(todo3)
    assert todolist.complete() == []
    todolist.give_up()
    assert todolist.complete() == [todo, todo2, todo3]