import os, tempfile

class WebApiException(Exception):
    pass

def root_path():
    return os.path.dirname(os.path.dirname(os.path.realpath(__file__)))

def interpreter_path(interpreter):
    #return os.path.join(root_path(), 'interpreter', 'v' + interpreter, "gbs.py")
    return os.path.join(root_path(), 'language', 'gbs.py')

def run_program(interpreter, program, board, options):
    tempf = tempfile.NamedTemporaryFile(delete=False, suffix=".gbs")
    tempf.write(program)
    tempf.flush()
    tempf.close()     
    cmd = '%s %s %s %s' % (interpreter_path(interpreter), 
                                       tempf.name, 
                                       board, 
                                       options)  
    print cmd
    result = os.popen(cmd).read()
    os.unlink(tempf.name) 
    return result   


