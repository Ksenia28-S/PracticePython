import unittest
from Task_manager import *

class Test_Task_manager(unittest.TestCase):

    def setUp(self):
        
        self.manager = TaskManager()
    
    def test_create_usual_task(self):
        
        my_task = self.manager.create_task('Usual task name', 'Usual task description')
        self.assertEqual(my_task.name, 'Usual task name')
        self.assertEqual(my_task.description, 'Usual task description')
        self.assertEqual(my_task.status, Status.ACTIVE)
       
    def test_create_complex_task_and_subtasks(self):
        
        my_compl_task = self.manager.create_complex_task('Complex task name', 'Complex task description')
        my_subtask1 = self.manager.create_subtask('Subtask1 name', 'Subtask1 description', my_compl_task.get_id())
        my_subtask2 = self.manager.create_subtask('Subtask2 name', 'Subtask2 description', my_compl_task.get_id())
        
        self.assertEqual(my_compl_task.name, 'Complex task name')
        self.assertEqual(my_compl_task.description, 'Complex task description')
        self.assertEqual(my_subtask1.name, 'Subtask1 name')
        self.assertEqual(my_subtask1.description, 'Subtask1 description')
        self.assertEqual(my_compl_task.subtasks, [my_subtask1.get_id(), my_subtask2.get_id()])
        
    def test_get_various_types_of_tasks(self):
        
        my_task = self.manager.create_task('Usual task name', 'Usual task description')
        my_compl_task = self.manager.create_complex_task('Complex task name', 'Complex task description')
        my_subtask1 = self.manager.create_subtask('Subtask1 name', 'Subtask1 description', my_compl_task.get_id())
        my_subtask2 = self.manager.create_subtask('Subtask2 name', 'Subtask2 description', my_compl_task.get_id())
        
        self.assertEqual(self.manager.get_tasks(), {my_task.get_id(): self.manager.get_tasks_by_id(my_task.get_id())})
        self.assertEqual(self.manager.get_subtasks(), {my_subtask1.get_id(): self.manager.get_subtasks_by_id(my_subtask1.get_id()), my_subtask2.get_id(): self.manager.get_subtasks_by_id(my_subtask2.get_id())})
        self.assertEqual(self.manager.get_complex_tasks(), {my_compl_task.get_id(): self.manager. get_complex_tasks_by_id(my_compl_task.get_id())})
        
    def remove_various_tasks(self):
        
        my_task = self.manager.create_task('Usual task name', 'Usual task description')
        my_compl_task = self.manager.create_complex_task('Complex task name', 'Complex task description')
        my_subtask1 = self.manager.create_subtask('Subtask1 name', 'Subtask1 description', my_compl_task.get_id())
        my_subtask2 = self.manager.create_subtask('Subtask2 name', 'Subtask2 description', my_compl_task.get_id())
        
        self.manager.remove_tasks()
        self.assertEqual(self.manager.get_tasks(), 'There are no tasks')
        
        self.manager.remove_subtasks()
        self.assertEqual(self.manager.get_subtasks(), 'There are no subtasks')
        
        self.manager.remove_complex_tasks()
        self.assertEqual(self.manager.get_complex_tasks(), 'There are no complex tasks')
        
    def remove_various_tasks_by_id(self):
        
        my_task1 = self.manager.create_task('Usual task name1', 'Usual task description1')
        my_task2 = self.manager.create_task('Usual task name2', 'Usual task description2')
        my_compl_task = self.manager.create_complex_task('Complex task name', 'Complex task description')
        my_subtask1 = self.manager.create_subtask('Subtask1 name', 'Subtask1 description', my_compl_task.get_id())
        my_subtask2 = self.manager.create_subtask('Subtask2 name', 'Subtask2 description', my_compl_task.get_id())
        
        self.manager.remove_task_by_id(my_task1.get_id())
        self.assertEqual(self.manager.get_tasks(), {my_task2.get_id(): self.manager.get_tasks_by_id(my_task2.get_id())})
        
        self.assertEqual(self.manager.remove_task_by_id(20), 'No task with this id')
                
        self.manager.remove_subtask_by_id(my_subtask1.get_id())
        self.assertEqual(self.manager.get_subtasks(), {my_subtask2.get_id(): self.manager.get_subtasks_by_id(my_subtask2.get_id())})
        
        self.assertEqual(self.manager.remove_subtask_by_id(20), 'No subtask with this id')
        
        self.manager.remove_complex_task_by_id(my_compl_task.get_id())
        self.assertEqual(self.manager.get_complex_tasks(), 'There are no complex tasks') 
        
        self.assertEqual(self.manager.remove_complex_task_by_id(20), 'No complex task with this id')
        
    def test_update_status(self):
 
        my_task = self.manager.create_task('Usual task name', 'Usual task description')
        self.manager.update_status(my_task.get_id())
        self.assertEqual(my_task.status, Status.FINISHED)
                
        self.assertEqual(self.manager.update_status(20), 'No task with this id')


if __name__ == "__main__":
    unittest.main()