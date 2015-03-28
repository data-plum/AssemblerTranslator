#!/usr/bin/python
#-*- coding: utf-8 -*-
import re

class Lexer(object):
	registers = ["AX", "CX", "DX", "BX", "SP", "BP", "SI", "DI", "AL", "CL", "DL", "BL", "AH", "CH", "DH", "BH"]
	keywords = ["END", "SEGMENT", "ENDS", "ORG", "ASSUME", "DB", "DW", "DD"]
	machine_commands = ["STI", "PUSH", "POP", "TEST", "OR", "SUB", "RAR", "SHR", "JZ"]
	delimiters = [',', ":", "[", "]"]

	@staticmethod
	def search_and_print(i):
		len_i = len(i)
		if (i[0].isdigit() and i[-1].isdigit()) or (i[0].isdigit() and i[-1] == "D"):
			print i + '\t' + str(len_i) + '\t' + "is 10 constant"
		elif (i[0].isdigit() and i[-1] == "B"):
			print i + '\t' + str(len_i) + '\t' + "is 2 constant"
		elif (i[0].isdigit() and i[-1] == "H"):
			print i + '\t' + str(len_i) + '\t' + "is 16 constant"
		elif ((i[0] == '\"' and i[-1] == '\"') or (i[0] == '\'' and i[-1] == '\'')):
			print i + '\t' + str(len_i) + '\t' + "is text constant"
		elif (i in Lexer.registers):
			print i + '\t' + str(len_i) + '\t' + "is register"
		elif (i in Lexer.keywords):
			print i + '\t' + str(len_i) + '\t' + "is keyword"
		elif (i in Lexer.machine_commands):
			print i + '\t' + str(len_i) + '\t' + "is command"
		elif (i[0].isalpha() and i[-1].isalpha() and len_i <= 8 or i[0] == "_") or (i[0].isalpha() and i[-1].isdigit() and len_i <= 8 or i[0] == "_"):
			print i + '\t' + str(len_i) + '\t' + "is identifier"
	
	@staticmethod
	def read_file():
		file = open("../Test.asm", "r")
		for line in file:
			my_list = (line.decode ('utf-8'))
			my_list = re.compile(ur"[\s]+", re.UNICODE).split(my_list)
			if len(my_list) > 0:
				print (" ".join(my_list))
				for word in my_list:
					if len(word) > 0:
						current_word = ''
						for letter in word:
							if letter not in Lexer.delimiters:
								current_word += letter
							if letter in Lexer.delimiters:
								Lexer.search_and_print(current_word)
								current_word = ''
								Lexer.search_and_print(letter)
					Lexer.search_and_print(word)
						# for j in range(len(word)):
						# 	if word[j] in Lexer.delimiters:
						# 		if word[j] == "]":
						# 			Lexer.search_and_print(word[j-2:j])
						# 			print word[j] + '\t' + str(len(word[j])) + '\t' + "is one delimiter"
						# 		else:
						# 			Lexer.search_and_print(word[:j])
						# 			print word[j] + '\t' + str(len(word[j])) + '\t' + "is one delimiter"							
						# Lexer.search_and_print(word)	
				print
		file.close()

Lexer().read_file()

		        	

		        	