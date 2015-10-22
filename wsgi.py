#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
def application(environ, start_response):
	data = 'Hello world \n'
	data = data + 'REQUEST_METHOD : ' + environ['REQUEST_METHOD'] + '\n'
	if environ['REQUEST_METHOD'] == 'POST':
		try:
			data += 'CONTENT_TYPE : ' + environ['CONTENT_TYPE'] + '\n'
			data += 'CONTENT_LENGTH : ' + environ['CONTENT_LENGTH'] + '\n'
			data += 'wsgi.input : ' + environ['wsgi.input'].read(int(environ['CONTENT_LENGTH'])) + '\n'
		except KeyError:
			data += 'CONTENT_TYPE : ' + '\n'
			data += 'CONTENT_LENGTH : ' + '\n'
			data += 'wsgi.input : ' + str(environ['wsgi.input']) + '\n'
	start_response('200', [
		("Content-Type","text"),
		("Content-Length",str(len(data)))
	])
	return iter([data])

