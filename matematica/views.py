# -*- coding: utf-8 -*-

#maryklayne
# from __future__ import unicode_literals
# from django.utils.encoding import python_2_unicode_compatible
from django.shortcuts import render
from django.http.response import HttpResponse
import json
import re
from sympy import *

def home(request):
    return render(request, 'index.html')




def funcao1(request):
	x = Symbol('x')
	campo1 = request.POST["funcao"]
	
	if verificaSQRT(campo1):
		campo1 = sympify(traducao(campo1))
		

	funcaoUnicode = str(campo1)

	#IntersecXptMaxAndMin
	intx = intersecX(campo1)

	#IntersecY
	inty = intersecY(campo1)

	#converter de unicode para sympify
	campo1 = sympify(campo1)

	#Pontos Crítico
	pontCritico = pontosCritico(campo1)

	#Maximo e Minimo
	maxEmin = ptMaxAndMin(campo1, pontCritico)

	#Pont wde Inflexao
	pontInflx = pontInflexao(campo1)

	#Assintota Horizontal
	av1 = asssintotaH(campo1)

	#Assintota Vertical
	av2 = assintotaV(funcaoUnicode)
    #
	# print 'Assintota Horizontal ',av1
	# print 'Assintota Vertical ',av2

	# print 'dfdsf ', maxEmin
	# print ('IntersecX ' , str(intx))
	# print ('IntersecY ', str(inty))
	# print 'ptnCritico ', str(pontCritico)[2:-2]
	# print 'min ',str(maxEmin[0])[2:-2]
	# print 'max ',str(maxEmin[1])[2:-2]
	# print 'pontInfl ',str(pontInflx)[2:-2]
	print 'assintV', str(av2)[2:-2]
	print 'assintH', str(av1)

	lista = [str(intx), str(inty), str(pontCritico)[1:-1], str(maxEmin[0])[1:-1], str(maxEmin[1])[1:-1],str(pontInflx)[1:-1],str(av1),str(av2)[2:-2]]

	for lista[i] in lista:
		if verificaSQRT(i):
			lista[i] = traducaoInversa(lista[i])


	dados = json.dumps({'IntersecX':lista[0], 'IntersecY':lista[1],
			'ptnCritico':lista[2], 'min':lista[3],
			'max':lista[4], 'pontInfl':lista[5],
			'ah':lista[6], 'av':lista[7],})

	return HttpResponse(dados, content_type='application/json') #retornar lista

#Cálculo dos pontos de intersecção da funcao com o eixo x
def intersecX(funcao):
	x = Symbol('x')
	retorno = []
	try:
		raizes = solve(funcao, x)

	except:
		raizes = []

	if raizes:
		for i in raizes:
			pontos = (i, sympify(funcao).subs(x, i))
			retorno.append(pontos)
		retorno = str(retorno)[1:-1]
	else:
		retorno.append('nao possui intX')

	return retorno

def verificaSQRT(funcao):
	f = str(funcao)
	if ("raiz" in f) or ("seno" inf f):
		return true
	else:
		return false
		

def traducao(funcao):
	funcao.replace("raiz", "sqrt")
	funcao.replace("seno","sin")
	return funcao


def traducaoInversa(funcao):
	funcao.replace("sqrt", "raiz")
	funcao.replace("sin", "seno")
	return funcao



#Cálculo dos pontos de intersecção da funcao com o eixo y
def intersecY(funcao):
	x = Symbol('x')
	resolv = sympify(funcao).subs(x,0)
	resolv = '(0, ' + str(resolv) + ')'
	return resolv

#Cálculo da derivada de uma função
def calcDerivada(funcao):
	x = Symbol('x')
	return funcao.diff(x)

#Cálculo das raízes da derivada ou seja, iguala f'(x) a 0
def raizesDerivada(dx):
	x = Symbol('x')
	try:
		return solve(dx, x)
	except:
		return []

#Cálculo dos pontos críticos
def pontosCritico(f):
	x = Symbol('x')
	retorno = []
	dx  = calcDerivada(f) #1ª derivada

	raizes = raizesDerivada(dx) #raizes da 1ª derivada

	if raizes: #Se tiver raizes, então tem pontos críticos
		i = 0
		while i < len(raizes):
			pontos = (raizes[i], f.subs(x, raizes[i])) #tupla de coordenada do ponto (x,y)
			retorno.append(pontos)
			i=i+1
	else: #Se não tiver pontos críticos
		retorno.append('nao possui')
	return retorno

#Cálculo dos pontos máximos e mínimos da função
def ptMaxAndMin(funcao, listaDePontosCriticos): #todos mínimos e máximos são pontos críticos
	x = Symbol('x')
	resMin = []
	resMax = []

	if listaDePontosCriticos[0]!='nao possui pontCritico':
		for i in listaDePontosCriticos:
			print 'este ',i[0]
			if i[0] > 0: #Se  a coordenada x do ponto crítico for maior que 0, então é mínimo
				resMin.append(i)
			elif i[0] < 0: #Se  a coordenada x do ponto crítico for menos que 0, então é máximo
				resMax.append(i)
			else: #Se  a coordenada x do ponto crítico for igual a 0, então é sela
				'o ponto é sela'

	if not resMin:
		resMin.append('nao possui')
	if not resMax:
		resMax.append('nao possui')

	return  (resMin,resMax)

def pontInflexao(funcao):
	x = Symbol('x')
	retorno = []
	dx2 = calcDerivada(calcDerivada(funcao)) #2ª derivada
	raizes = raizesDerivada(dx2) #raizes da 1ª derivada
	# print raizes
	if raizes:
		i = 0
		while i < len(raizes):
			pontos = (raizes[i], funcao.subs(x, raizes[i]))
			retorno.append(pontos)
			i=i+1
	else:
		retorno = ['nao possui']
	return retorno

def denominador(fracao):
	x = Symbol('x')
	try:
		den = denom(fracao)
		return solve(den, x)
	except:
		return 'sem denominador'


def assintotaV(st):
	x = Symbol('x')
	try:
		assintotas = []
		expressions1 = sympify(st)
		sym, = expressions1.free_symbols
		expressions1 = expressions1.subs(sym,x)
		fracao = cancel(together(expressions1))
		xis = denominador(fracao)

		if len(xis) != 0:
			for i in xis:
				limE = limit(expressions1,x,i,'-')
				limD = limit(expressions1,x,i,'+')
				if ((limE == oo) and (limD == -oo) or (limE == -oo) and (limD == oo)):
					soma = 'x=' + str(i)
					assintotas.append(soma)
		if len(assintotas)==0:
			return 'nao existe'
		return assintotas
	except:
		return 'nao existe'

def asssintotaH(funcao):
	x = Symbol('x')
	f = sympify(funcao)
	sym, = f.free_symbols
	f = f.subs(sym,x)
	try:
		lim1 = limit(f,x,oo)
		lim2 = limit(f,x,-oo)

		if (lim1 == lim2):
			return 'y='+str(lim1)
		else:
			return 'nao existe'
	except:
		'erro limite'






