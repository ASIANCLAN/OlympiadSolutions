#!/usr/bin/env python2.7
# encoding : utf-8
while True:
	try :
		a,b = [int(i) for i in raw_input().split(":")]
		horas = a*60 + b
		if horas <= 420:
			print "Atraso maximo: 0"
		else:
			print "Atraso maximo: %d" % (horas - 420)
	except EOFError:
		break