from enum import Enum

class Status(Enum):
    ACTIVE = 'Active'
    FINISHED = 'Finished'

class Task:
    
    def __init__(self, id, name = None, description = None, status = Status.ACTIVE):
        self.id = id
        self.name = name
        self.description = description
        self.status = status

    def get_id(self):
        return self.id

class Subtask(Task):
    
    def __init__(self, id, name, description, parent_id, status = Status.ACTIVE):
        super().__init__(id, name, description, status)
        self.parent_id = parent_id

class ComplexTask(Task):
    
    def __init__(self, id, name, description, subtasks = [], status = Status.ACTIVE):
        super().__init__(id, name, description, status)
        self.subtasks = subtasks

    
class TaskManager:

    id_series = 0

    def __init__(self):
        self.tasks = {}
        self.complex_tasks = {}
        self.subtasks = {}
        
    def get_and_increment_id(self):
        next_id_value = TaskManager.id_series
        TaskManager.id_series += 1 
        return next_id_value

    def create_task(self, name, description):
        current_id = self.get_and_increment_id()
        new_task = Task(current_id, name, description)
        self.tasks[current_id] = new_task
        return new_task
    
    def create_subtask(self, name, description, parent_id):
        current_id = self.get_and_increment_id()
        new_subtask = Subtask(current_id, name, description, parent_id)
        self.subtasks[current_id] = new_subtask
        parent_task = self.complex_tasks.get(parent_id)
        get_subtasks = parent_task.subtasks
        get_subtasks.append(current_id)
        return new_subtask
    
    def create_complex_task(self, name, description):
        current_id = self.get_and_increment_id()
        new_complex_task = ComplexTask(current_id, name, description)
        self.complex_tasks[current_id] = new_complex_task
        return new_complex_task

    def get_tasks(self):
        if len(self.tasks) == 0:
            return 'There are no tasks'
        else:
            return self.tasks

    def get_subtasks(self):
        if len(self.subtasks) == 0:
            return 'There are no subtasks'
        else:
            return self.subtasks
    
    def get_complex_tasks(self):
        if len(self.complex_tasks) == 0:
            return 'There are no complex tasks'
        else:
            return self.complex_tasks
    
    def get_tasks_by_id(self, id):
        if id not in self.tasks.keys():
            return 'No task with this id'    
        else:
            return self.tasks.get(id)

    def get_subtasks_by_id(self, id):
        if id not in self.subtasks.keys():
            return 'No subtask with this id'
        else:
            return self.subtasks.get(id)
    
    def get_complex_tasks_by_id(self, id):
        if id not in self.complex_tasks.keys():
            return 'No complex task with this id'
        else:
            return self.complex_tasks.get(id)

    def remove_tasks(self):
        self.tasks.clear()
    
    def remove_subtasks(self):
        for subtask in self.complex_tasks:
            del subtask
    
    def remove_complex_tasks(self):
        self.complex_tasks.clear()
        self.subtasks.clear()
    
    def remove_task_by_id(self, id):
        if id not in self.tasks.keys():
            return 'No task with this id'
        else:
            del self.tasks[id]
        
    def remove_subtask_by_id(self, id):
        if id not in self.subtasks.keys():
            return 'No subtask with this id'
        else:
            parent_id = self.subtasks[id].parent_id
            self.complex_tasks[parrent_id].subtasks.remove(id)
            del self.subtasks[id]
        
    def remove_complex_task_by_id(self, id):
        if id not in self.complex_tasks.keys():
            return 'No complex task with this id'
        else:
            subtasks_ids = self.complex_tasks[id].subtasks
            for i in subtasks_ids:
                self.remove_subtask_by_id(i)
            del self.complex_tasks[id]

    def update_status(self, task_id):
        if task_id in self.tasks:
            task = self.get_tasks_by_id(task_id)
            task.status = Status.FINISHED
        if task_id in self.subtasks:
            task = self.get_subtasks_by_id(task_id)
            task.status = Status.FINISHED
        if task_id in self.complex_tasks:
            task = self.complex_tasks(task_id)
            task.status = Status.FINISHED
        else:
            return 'No task with this id'
        
