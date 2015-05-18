#!/usr/bin/python
#-*- coding: utf-8 -*-
import re
from Lexem_table import Lexem_table
from Processor import Processor

class Lexer(object):

	register_8 = ["AL", "CL", "DL", "BL", "AH", "CH", "DH", "BH"]
	register_16 = ["AX", "CX", "DX", "BX", "BP", "SI", "DI", "SP"]
	segment_register = ["DS", "FS", "ES", "CS", "SS", "GS"]
	keyword = ["END", "SEGMENT", "ENDS", "ORG", "ASSUME", "DB", "DW", "DD"]
	machine_command = ["STI", "PUSH", "POP", "TEST", "OR", "SUB", "RAR", "SHR", "JZ"]
	delimiter = [',', ":", "[", "]"]
	lexem_list = []


	@staticmethod
	def search_and_print(i, counter):
		len_i = len(i)
		if (i in Lexer.delimiter):
			print counter + '\t' + i + '\t' + str(len_i) + '\t' + "one delimiter"

		elif (i[0].isdigit() and i[-1].isdigit()) or (i[0].isdigit() and i[-1] == "D"):
			print counter + '\t' + i + '\t' + str(len_i) + '\t' + "is 10 constant"
		elif (i[0].isdigit() and i[-1] == "B"):
			print counter + '\t' + i + '\t' + str(len_i) + '\t' + "is 2 constant"
		elif (i[0].isdigit() and i[-1] == "H"):
			print counter + '\t' + i + '\t' + str(len_i) + '\t' + "is 16 constant"
		elif ((i[0] == '\"' and i[-1] == '\"') or (i[0] == '\'' and i[-1] == '\'')):
			print counter + '\t' + i + '\t' + str(len_i) + '\t' + "is text constant"

		elif (i in Lexer.register_8):
			print counter + '\t' + i + '\t' + str(len_i) + '\t' + "is 8 register"
		elif (i in Lexer.register_16):
			print counter + '\t' + i + '\t' + str(len_i) + '\t' + "is 16 register"
		elif (i in Lexer.segment_register):
			print counter + '\t' + i + '\t' + str(len_i) + '\t' + "is segment register"

		elif (i in Lexer.keyword):
			print counter + '\t' + i + '\t' + str(len_i) + '\t' + "is keyword"

		elif (i in Lexer.machine_command):
			print counter + '\t' + i + '\t' + str(len_i) + '\t' + "is command"

		elif (i[0].isalpha() and i[-1].isalpha() and len_i <= 8 or i[0] == "_") or (i[0].isalpha() and i[-1].isdigit() and len_i <= 8 or i[0] == "_"):
			print counter + '\t' + i + '\t' + str(len_i) + '\t' + "is identifier"

	@staticmethod
	def read_file():
		file = open("../Asm/Test.asm", "r")
		for line in file:
			my_list = (line.decode ('utf-8'))
			my_list = re.compile(ur"[\s]+", re.UNICODE).split(my_list)
			if len(my_list) > 0:
				# print (" ".join(my_list))
				# counter = 1
				# for word in my_list:
				# 	if len(word) > 0:
				# 		current_word = ''
				# 		for letter in word:
				# 			if letter not in Lexer.delimiter:
				# 				current_word += letter
				# 			elif letter in Lexer.delimiter:
				# 				if len(current_word) > 0:
				# 					Lexer.search_and_print(current_word, str(counter))
				# 					counter += 1
				# 					current_word = ''
				# 				Lexer.search_and_print(letter, str(counter))
				# 				counter += 1
				# 		Lexer.search_and_print(word, str(counter))
				# 		counter += 1
				if len(my_list[0]) > 0:
					tesla_loshara = Processor(my_list)
					tesla_loshara.parse_string_to_line()
		print tesla_loshara.string_for_print.upper()
		#Processor.analyze()
		file.close()

Lexer().read_file()