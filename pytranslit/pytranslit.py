# -*- coding: utf-8 -*-

#	A python module to tranliterate text based on transliteration system maps
#	Copyright (C) 2011  Petros Moisiadis <ernest0x@yahoo.gr>
#
#	This program is free software: you can redistribute it and/or modify
#	it under the terms of the GNU General Public License as published by
#	the Free Software Foundation, either version 3 of the License, or
#	(at your option) any later version.
#
#	This program is distributed in the hope that it will be useful,
#	but WITHOUT ANY WARRANTY; without even the implied warranty of
#	MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#	GNU General Public License for more details.
#
#	You should have received a copy of the GNU General Public License
#	along with this program.  If not, see <http://www.gnu.org/licenses/>
    
from copy import copy
from sys import argv

# Import transliteration maps
from transmaps import *


def short_keys(short_list=[], keys_list=[]):
	""" Returns a list that includes all keys from short_list that are found in keys_list,
sorted in the same order as in short_list """
	shorted_keys_list = []
	for key in short_list:
		if key in keys_list:
			shorted_keys_list.append(key)

	return shorted_keys_list


class Transliterator:
	system = ''

	def __init__(self, system):
		self.system = system

	def _matchrule(self, rules, orig_text, index):
		for rule in rules:
			if len(rule) == 1: # For simple, 'just replace' rules, just return replace
				return rule['replace']
			else:
				matched = True
				keys = short_keys(['before', 'after', 'position'], rule.keys())
				if 'before' in keys:
					if (index == 0) or (orig_text[index - 1] not in rule['before']):
						matched = False
				if 'after' in keys:
					if (index == len(orig_text) - 1) or (orig_text[index + 1] not in rule['after']):
						matched = False
				if 'position' in keys:
					position = rule['position']
					if position < 0:
						position = len(orig_text) + position
					if position != index:
						matched = False

				if matched:
					return rule['replace']

	def transliterate(self, text):
		try:
			text = text.decode('utf-8')
		except UnicodeEncodeError:
			pass

		text = list(text)
		orig_text = copy(text)

		for index in range(0, len(orig_text)):
			try:
				rules = TRANS_MAP[self.system][orig_text[index]]
				text[index] = self._matchrule(rules, orig_text, index)
			except KeyError:
				text[index] = orig_text[index]

		return ''.join(text)


if __name__ == '__main__':
	try:
		trans = Transliterator(argv[1])
		print(trans.transliterate(argv[2]))
	except IndexError:
		print('Usage: python ' + argv[0] + ' <system>' + ' <text>\n')
		print('Supported transliteration systems:')
		print(', '.join(TRANS_MAP.keys()))
