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
			# constant_10 = Constants(counter, i, len_i, "10 constant")
			# Lexem_table.lexem_list.append(constant_10)
			print counter + '\t' + i + '\t' + str(len_i) + '\t' + "is 10 constant"
		elif (i[0].isdigit() and i[-1] == "B"):
			# constant_2 = Constants(counter, i, len_i, "2 constant")
			# Lexem_table.lexem_list.append(constant_2)
			print counter + '\t' + i + '\t' + str(len_i) + '\t' + "is 2 constant"
		elif (i[0].isdigit() and i[-1] == "H"):
			# constant_16 = Constants(counter, i, len_i, "16 constant")
			# Lexem_table.lexem_list.append(constant_16)
			print counter + '\t' + i + '\t' + str(len_i) + '\t' + "is 16 constant"
		elif ((i[0] == '\"' and i[-1] == '\"') or (i[0] == '\'' and i[-1] == '\'')):
			# constant_text = Constants(counter, i, len_i, "text constant")
			# Lexem_table.lexem_list.append(constant_text)
			print counter + '\t' + i + '\t' + str(len_i) + '\t' + "is text constant"

		elif (i in Lexer.register_8):
			# register_8 = Registers_8(counter, i, len_i, "8 register")
			# Lexem_table.lexem_list.append(register_8)
			print counter + '\t' + i + '\t' + str(len_i) + '\t' + "is 8 register"
		elif (i in Lexer.register_16):
			# register_16 = Registers_16(counter, i, len_i, "16 register")
			# Lexem_table.lexem_list.append(register_16)
			print counter + '\t' + i + '\t' + str(len_i) + '\t' + "is 16 register"
		elif (i in Lexer.segment_register):
			# register_segment = Segment_registers(counter, i, len_i, "segment register")
			# Lexem_table.lexem_list.append(register_segment)
			print counter + '\t' + i + '\t' + str(len_i) + '\t' + "is segment register"

		elif (i in Lexer.keyword):
			# keyword = Keywords(counter, i, len_i, "keyword")
			# Lexem_table.lexem_list.append(keyword)
			print counter + '\t' + i + '\t' + str(len_i) + '\t' + "is keyword"

		elif (i in Lexer.machine_command):
			# machine_command = Machine_commands(counter, i, len_i, "command")
			# Lexem_table.lexem_list.append(machine_command)
			print counter + '\t' + i + '\t' + str(len_i) + '\t' + "is command"

		elif (i[0].isalpha() and i[-1].isalpha() and len_i <= 8 or i[0] == "_") or (i[0].isalpha() and i[-1].isdigit() and len_i <= 8 or i[0] == "_"):
			# identifier = User_identifier(counter, i, str(int(len_i) - 2), "user identifier")
			# Lexem_table.lexem_list.append(identifier)
			print counter + '\t' + i + '\t' + str(len_i) + '\t' + "is identifier"
	@staticmethod
	def read_file():
		file = open("../Test.asm", "r")
		for line in file:
			my_list = (line.decode ('utf-8'))
			my_list = re.compile(ur"[\s]+", re.UNICODE).split(my_list)
			if len(my_list) > 0:
				print (" ".join(my_list))
				counter = 1
				for word in my_list:
					if len(word) > 0:
						current_word = ''
						for letter in word:
							if letter not in Lexer.delimiter:
								current_word += letter
							elif letter in Lexer.delimiter:
								if len(current_word) > 0:
									Lexer.search_and_print(current_word, str(counter))
									counter += 1
									current_word = ''
								Lexer.search_and_print(letter, str(counter))
								counter += 1
						Lexer.search_and_print(word, str(counter))
						counter += 1

				Processor(my_list)
		#print Processor.line_string
		#Processor.analyze()
		file.close()

Lexer().read_file()