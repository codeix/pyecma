from pyecma.semantics import EcmaSemantics
from pyecma.parser import EcmaParser

js = """


var i = 1+1+(2*4)+(3)*3+222*(((4)));
var j = 5;

j += 1;
j >>= 1;


var hello = "Hello";
hello += ' World';

var x = j + i;


var myfunc = function (){
    var j= 8*8;
    i = j;
}

function secfunc (arg){
    i=arg;
}

function echo (arg){
    return arg ;
}


function multi (arg1, arg2){
    return arg1 * arg2 ;
}

"""

def run():
    parser = EcmaParser()
    app=parser.parse(js, 'program', semantics=EcmaSemantics())
    app.echo('blup')
    import pdb; pdb.set_trace()
    app.i
    
    
    
    out=parser.parse('1+(2*4)+(3)*3+222*(((4)))', 'expression', semantics=EcmaSemantics())
    print(out())

