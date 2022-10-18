INPUT_CODE_DELIMITER = '# ---end----'

def read_data(file_name):
    file = open(file_name)
    content = file.read()
    file.close()
    return content


def write_data(file_name, data):
    file = open(file_name, 'w')
    content = "\n".join(data)   
    file.write(content)
    file.close()    


def prepare_md_titles(data):
    title = description = None

    for line in data.split('\n'):
        if line.startswith('# title'):
            title = line.replace('# title ', '')
        elif line.startswith('# description'):
            description = line.replace('# description ', '')
    
    return title, description        
    

def prepare_md_format(title, description, source_code):
    md_link = '-'.join(title.lower().split())
    md_title = '+ [{}](#{})\n\n'.format(title, md_link)
    template = """## {}
    
    {}
    
    ```python
    {}
    ```""".format(title, description, source_code.lstrip())
    return md_title, template
    

def convert_data(data):
    titles, source_code = data.split(INPUT_CODE_DELIMITER)  
    title, description = prepare_md_titles(titles)
    format = prepare_md_format(title, description, source_code)  
    return format


def main():
    content = read_data('solution.py')
    format = convert_data(content)
    write_data('out.md', format)


if __name__ == "__main__":
    main()