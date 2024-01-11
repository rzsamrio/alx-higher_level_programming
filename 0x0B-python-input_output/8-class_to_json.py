#!/usr/bin/python3
""" Converts a data structure to JSON format """


def class_to_json(obj):
	""" Function thst converts """
	import json
	return json.dumps(obj.__dict__)
