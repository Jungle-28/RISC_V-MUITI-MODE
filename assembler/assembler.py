def read_file(file_path):
    """
    Reads the content of a file and returns it as a string.
    
    :param file_path: Path to the file to be read.
    :return: Content of the file as a string.
    """
    with open(file_path, 'r') as file:
        content = file.read()
    return content

def write_file(file_path, content):
    """
    Writes the given content to a file.
    
    :param file_path: Path to the file where content will be written.
    :param content: Content to write to the file.
    """
    with open(file_path, 'w') as file:
        file.write(content)

