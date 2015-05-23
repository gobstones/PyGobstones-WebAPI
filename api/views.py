from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
import os
import tempfile
from utils import run_program

@csrf_exempt
def index(request, interpreter='gbs'):
    """ 
        POST Parameters:
            - program, a Gobstones/XGobstones program.
            - board, an initial board for Gobstones/XGobstones interpreter.
            - options, a list of options to setup the interpreter.
    """
        
    program = request.POST.get('program', '')
    board = request.POST.get('board', '')    
    options = request.POST.get('options', '')
    
    result = run_program(interpreter, program, board, options + " --output-type json --silent")
    return HttpResponse(repr(result))
    


