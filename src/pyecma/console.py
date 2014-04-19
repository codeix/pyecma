from pyecma.semantics import EcmaSemantics
from pyecma.parser import EcmaParser

js = r"""

function abs(value){
    if (value < 0)
        return value * -1;
    return value;
}

function ggt(e, f) {
    while (abs(e - f) > 0) {
        if ( e < f )
             f = f - e;
        else
             e = e - f;
    }
    return e;
}


var iftest= 'iftest';

if (1*0) {
    iftest += ' True';
}else{
    iftest += ' False';
}



var c = 1==1;
var cc = 1==(1==0);

var i = 1;
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

function self(){
    return self;
}

function multi (arg1, arg2){
    return arg1 * arg2 ;
}

var myecho = echo('it\'s works :-)');

function factorial (fac){
  if(fac > 1)
      return fac * factorial(fac-1);
  else
    return fac;
}

function dofactorial(counter){
    var result = 1;
    do {
        result *= counter;
        counter -= 1;
    } while (counter > 0);
    return result;
}

var br = 9;
while (br){
    if (br<5)
        break;
    br -= 1;
}

var builtin = parseInt('3');
"""




def run():
    parser = EcmaParser()
    app=parser.parse(js, 'program', semantics=EcmaSemantics())
    app.dofactorial(3)
    import pdb; pdb.set_trace()
    
    
    
    out=parser.parse('1+(2*4)+(3)*3+222*(((4)))', 'expression', semantics=EcmaSemantics())
    print(out())

