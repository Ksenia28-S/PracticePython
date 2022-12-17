import unittest

from converter import *

class TestConverter(unittest.TestCase):
 
    def test_prepare_md_titles(self):
        data = '# title Hello world\n# description Some description for out task'  
        title, description = prepare_md_titles(data)  
        self.assertEqual(title, 'Hello world')
        self.assertEqual(description, 'Some description for out task')
    
    
    def test_prepare_md_titles_with_empty_data(self):
        data = ''  
        title, description = prepare_md_titles(data)  
        self.assertEqual(title, None)
        self.assertEqual(description, None)
      
      
    def test_prepare_md_titles_with_extra_data(self):
        data = '# title Hello world\n# description Some description for out task\n# tag set, list'  
        title, description = prepare_md_titles(data)  
        self.assertEqual(title, 'Hello world')
        self.assertEqual(description, 'Some description for out task')  
        
        
    def test_prepare_md_link(self):   
        data = 'Some cool title'
        title = prepare_md_link(data)
        self.assertEqual(title, '+ [Some cool title](#some-cool-title)')
        
        
    def test_prepare_md_format(self):
        title = 'Some cool title'
        description =  'Some even cooler description'
        source_code = '  2 + 2 = 4'
        model_answer = '## Some cool title\n\nSome even cooler description\n\n``` python\n2 + 2 = 4\n```'
        self.assertEqual(prepare_md_format(title, description, source_code), model_answer)
        
        
    def test_prepare_new_md_content(self):
        new_md_link = '+ [New title](#new-title)'
        new_md_code = '## New title\n\nNew description\n\n``` python\n1 + 1 = 2\n```'
        old_md_content = '+ [Old name](#old-name)\n<!---md_file_delimeter>\n## Old name\nold code'
        model_answer = '+ [Old name](#old-name)\n+ [New title](#new-title)\n<!---md_file_delimeter>\n## Old name\nold code\n\n## New title\n\nNew description\n\n``` python\n1 + 1 = 2\n```'
        self.assertEqual(prepare_new_md_content(new_md_link, new_md_code, old_md_content), model_answer)
        
    def test_convert_data(self):
        data = '# title New title\n# description New desc\n# ---end----\nnew code'
        old_md_content = '+ [Old name](#old-name)\n<!---md_file_delimeter>\n## Old name\nold code'
        model_answer = '+ [Old name](#old-name)\n+ [New title](#new-title)\n<!---md_file_delimeter>\n## Old name\nold code\n\n## New title\n\nNew desc\n\n``` python\n-\nnew code\n```'
        self.assertEqual(convert_data(data, old_md_content), model_answer)

if __name__ == "__main__":
    unittest.main()
