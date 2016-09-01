from sympy import *
import re

x = Symbol('x')
y = Symbol('y')
z = Symbol('z')

#	if (tipo==1){ alert("numerador");}
#	if (tipo==2){ alert("numerador raiz");}
#	if (tipo==3){ alert("numerador e denominador");}
#	if (tipo==4){ alert("numerador raiz e denominador");}
#	if (tipo==5){ alert("numerador raiz e denominador raiz");}
#	if (tipo==6){ alert("numerador e denominador raiz");}


def calcTipo(funcao):
	math = re.search(r'/')
	return type(math)
