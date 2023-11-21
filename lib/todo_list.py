class TodoList:
    def __init__(self):
        self.todolist = []
        pass

    def add(self, todo):
        # Parameters:
        #   todo: an instance of Todo
        # Returns:
        #   Nothing
        # Side-effects:
        #   Adds the todo to the list of todos
        self.todolist.append(todo)
        pass

    def incomplete(self):
        # Returns:
        #   A list of Todo instances representing the todos that are not complete
        return [x for x in self.todolist if x.complete == False]

    def complete(self):
        # Returns:
        #   A list of Todo instances representing the todos that are complete
        return [x for x in self.todolist if x.complete == True]

    def give_up(self):
        # Returns:
        #   Nothing
        # Side-effects:
        #   Marks all todos as complete
        for task in self.todolist:
            task.mark_complete()
        pass