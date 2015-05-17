from Line import Line
from Identifier import Identifier
from Useful_lexems import Useful_lexems

import re

class Processor(object):

	string_for_print = ''
	offset = 0
	nexxt = None
	is_segment_closed = True
	segment_value = None
	list_of_identifier = []

	def __init__(self, line_string):
		self.line_string = line_string
		self.line = Line()
		self.useful_lexems = Useful_lexems()
		self.offset = 0
		self.identifiers = []
		self.second = True

	def get_identifier_by_name(self, name):
		for i in self.identifiers:
			if i.self.name == name:
				return i
		return None

	def set_segment(self, name, typpe):
		self.identif = Identifier()
		self.identif = self.get_identifier_by_name(name)
		if not self.second and self.identif != None:
			self.identief.identifiers.append(self.identif(name, "ERROR", Processor.offset, length = 0, closed = False))
			return "Redefined identifier"
		elif not self.second:
			self.identif.identifiers.append(self.identif(name, typpe, Processor.offset, length = 0, closed = False))
		else:
			self.identif.closed = False
		return None 

	def set_identifier(self, name, typpe, value):
		if typpe == "SEGMENT":
			return self.set_segment(name, typpe)
		self.identif = Identifier()
		if self.identif == None:
			return "Define variable before SEGMENT opening"
		else:
			i = self.get_identifier_by_name(name)
			if i != None:
				self.identief.identifiers.append(self.identifier(name, "ERROR", Processor.offset, attribute = self.name))
			else:
				self.identief.identifiers.append(self.identifier(name, typpe, Processor.offset, attribute = self.name))
		return None

	def parse_int(self, string):
		if self.useful_lexems.is_constant(string) == 16:
			return hex(int(string[:-1], 16))
		elif self.useful_lexems.is_constant(string) == 10:
			if string[-1] == "D":
				return hex(int(string[:-1]))
			else:
				return hex(int(string))
		elif self.useful_lexems.is_constant(string) == 2:
			return hex(int(string[:-1], 2))
		else:
			return "Error"

	def check_constant(self, string):
		t = self.useful_lexems.is_constant(string)
		if t == 0:
			return "ERROR: Missed numeric constant"
		return None

	def parse_identifier(self, string):
		first_word = string[0]
		if string[1] == ":" and len(first_word) <= 8:
			new_identifier = Identifier(first_word, "L NEAR", Processor.offset, attribute = Processor.segment_value)
			Processor.list_of_identifier.append(new_identifier)

		if len(first_word) > 8:
			self.set_error("ERROR: identifier length more then 8 characters")
		#is variable
		elif first_word == "ORG":
			if self.useful_lexems.is_constant(string[1]) == 2:
				Processor.offset += int(string[1][:-1], 2)
			elif self.useful_lexems.is_constant(string[1]) == 16:
				Processor.offset += int(string[1][:-1], 16)
			else:
				Processor.offset = int(string[1])

			# Processor.string_for_print += hex(Processor.offset)

		else:
			Processor.nexxt = string[1]
			if Processor.nexxt == "DB":	
				#DB
				if not self.useful_lexems.is_text_constant(string[2]):
					self.line.operand_size = 1
					self.set_error(self.check_constant(string[2]))
					operand = self.parse_int(string[2])
					if operand == None:
						return None
					self.line.operand = operand
					Processor.string_for_print += str(operand[2:]) + "\t" if len(str(operand[2:])) >= 4 or len(str(operand[2:])) % 2 == 0 else "0" + str(operand[2:]) + "\t"
					# print str(operand[2:])
				else:
					text = string[2][1:-1]
					self.line.operand = 0
					#add to operand ASCII code all words which in text constant
					for word in text:
						operand = hex(ord(word))[2:]
						Processor.string_for_print += str(operand) + " "
					# self.line.operand =  len(u''.join([text]).encode('utf-8').strip().decode('utf-8')) 
					# Processor.string_for_print +=  str(operand) + "\t"
					self.line.operand_size = len(u''.join([text]).encode('utf-8').strip().decode('utf-8')) #len(text)
				# except:
				# 	self.set_error("Missed text constant")
			elif Processor.nexxt == "DW":
				#DW
				try:
					if not self.useful_lexems.is_text_constant(string[2]):
						self.line.operand_size = 2
						self.set_error(self.check_constant(string[2]))
						operand = self.parse_int(string[2])
						if operand == None:
							return None
						self.line.operand = operand
						Processor.string_for_print += str(operand[2:]) + "\t" if len(str(operand[2:])) >= 4 or len(str(operand[2:])) % 2 == 0 else "0" + str(operand[2:]) + "\t"
				except:
					self.set_error("ERROR: Incorrect constant value")
			elif Processor.nexxt == "DD":
				try:
					if not self.useful_lexems.is_text_constant(string[2]):
						self.line.operand_size = 4
						self.set_error(self.check_constant(string[2]))
						operand = self.parse_int(string[2])
						if operand == None:
							return None
						self.line.operand = operand
						Processor.string_for_print += str(operand[2:]) + "\t" if len(str(operand[2:])) >= 4 or len(str(operand[2:])) % 2 == 0 else "0" + str(operand[2:]) + "\t"
				except:
					self.set_error("Incorrect constant value")
			elif Processor.nexxt == "SEGMENT":
				Processor.offset = 0
				Processor.is_segment_closed = False
			elif Processor.nexxt == "ENDS":
				Processor.offset = 0
				Processor.is_segment_closed = True

	def parse_command(self, string):
		first_word = string[0]
		self.register_adress_mode = 0
		for i in self.useful_lexems.machine_command:
			if i["rule"] == "EMPTY" and i["name"] == first_word:
				Processor.offset += 1
				self.line.operation_code = i["code"]
				Processor.string_for_print += str(hex(i["code"])[2:]) + "\t" if len(str(i["code"])) >= 2 else "0" + str(i["code"]) + "\t"
				break
			elif i["rule"] == "ONLY_REG" and i["name"] == first_word:
				if string[1] in self.useful_lexems.registers:
					if self.get_register_position(string[1]) >= 8 and self.get_register_position(string[1]) <= 15:
						# Processor.offset += 1
						self.line.operand_size_prefix = 0x42
						Processor.string_for_print += str(self.line.operand_size_prefix) + "|" + " "	
					self.check_registers_adressing(string[1])
					if self.get_register_adressing_mode(string[1]) == 1:
						self.line.operation_code = hex(i["code"] + self.get_register_position(string[1]))
					else:
						self.line.operation_code = hex(i["code"])
						self.line.mrm = hex((3 << 6) | i["code"])
					Processor.string_for_print += str(self.line.operation_code[2:]) + "\t" if len(str(self.line.operation_code)) >= 2 else "0" + str(self.line.operation_code[2:]) + "\t"
					break
				elif string[1] in self.useful_lexems.segment_register:
					for j in self.useful_lexems.seg_reg:
						if string[1] == "FS":
							if i["name"] == "PUSH":
								self.line.operation_code = hex(0x0f)[2:]
								self.line.mrm = 0xa0
							elif i["name"] == "POP":
								self.line.operation_code = hex(0x0f)[2:]
								self.line.mrm = 0xa1
							Processor.string_for_print += str(self.line.operation_code) + " " + str(hex(self.line.mrm)[2:]) + \
							"\t" if len(str(self.line.operation_code)) >= 2 else "0" + str(self.line.operation_code) +  " " + \
							str(hex(self.line.mrm)[2:]) + "\t"
							break
						if string[1] == "GS":
							if i["name"] == "PUSH":
								self.line.operation_code = hex(0x0f)[2:]
								self.line.mrm = 0xa8
							elif i["name"] == "POP":
								self.line.operation_code = hex(0x0f)[2:]
								self.line.mrm = 0xa9
							Processor.string_for_print += str(self.line.operation_code) + " " + str(hex(self.line.mrm)[2:]) + \
							"\t" if len(str(self.line.operation_code)) >= 2 else "0" + str(self.line.operation_code) +  " " + \
							str(hex(self.line.mrm)[2:]) + "\t"
							break
						if string[1] == "CS" and i["name"] == "POP":
							self.set_error("ERROR: Illegal use of CS register")
							break
						elif j["name"] == string[1]:
							if i["name"] == "PUSH":
								self.line.operation_code = hex(j["code"] - 0x20)[2:]
							elif i["name"] == "POP":
								self.line.operation_code = hex(j["code"] - 0x1f)[2:]
							Processor.string_for_print += str(self.line.operation_code) + "\t" if len(str(self.line.operation_code)) >= 2 else "0" + str(self.line.operation_code) + "\t"
							break
				else:
					self.set_error("ERROR: Missed or incorrect register")

			elif i["rule"] == "MEM_REG" and i["name"] == first_word or i["rule"] == "MEM_IMM" and i["name"] == first_word:
				if string[-2] not in self.useful_lexems.registers:
					self.set_error("ERROR: Missed or incorrect register")
				elif len(string) == 3:
					self.set_error("ERROR: Missed part of command")
				
				data0 = string[-2]
				if not self.useful_lexems.is_identifier(string[1]):
					data1 = string[1:-2]
				self.generate_mrm(data0, data1, i["rule"])
				self.register_adress_mode = self.get_register_adressing_mode(data0)
				self.line.operation_code = i["code"] + self.get_register_adressing_mode(data0)
				if self.get_register_adressing_mode(data0) == 1:
					Processor.string_for_print += "66|" + " "
				Processor.string_for_print += hex(self.line.operation_code)[2:] + " " if len(hex(self.line.operation_code)[2:]) >= 2 else "0" + hex(self.line.operation_code)[2:] + " "
				Processor.string_for_print += hex(self.line.mrm)[2:] + "\t" if len(hex(self.line.mrm)[2:]) >= 2 else "0" + hex(self.line.mrm)[2:] + "\t"

			elif i["rule"] == "REG_MEM" and i["name"] == first_word:
				strings = []
				for e in string:
					res = re.findall(r'(?u)\w+', e)
					strings += res

				if strings[1] not in self.useful_lexems.registers:
					self.set_error("ERROR: Missed or incorrect register")
				elif len(strings) == 3:
					self.set_error("ERROR: Missed part of command")
				
				if len(string) == 4:
					data0 = string[1][:-1]
					if not self.useful_lexems.is_identifier(string[2]):
						data1 = string[2:-1]
				elif len(string) == 5:
					data0 = string[1][:-1]
					if not self.useful_lexems.is_identifier(string[2]):
						data1 = string[3:-1]

					for j in self.useful_lexems.seg_reg:
						if string[2][:-1] == "FS":
							Processor.string_for_print += "64:" + " "
							break
						elif string[2][:-1] == "GS":
							Processor.string_for_print += "65:" + " "
							break
						elif string[2][:-1] == j["name"]:
							Processor.string_for_print += hex(j["code"])[2:] + ":" + " "
				self.generate_mrm(data0, data1, i["rule"])
				self.register_adress_mode = self.get_register_adressing_mode(data0)
				self.line.operation_code = i["code"] + self.get_register_adressing_mode(data0)
				if self.get_register_adressing_mode(data0) == 1:
					Processor.string_for_print += "66|" + " "
				Processor.string_for_print += hex(self.line.operation_code)[2:] + " " if len(hex(self.line.operation_code)[2:]) >= 2 else "0" + hex(self.line.operation_code)[2:] + " "
				Processor.string_for_print += hex(self.line.mrm)[2:] + "\t" if len(hex(self.line.mrm)[2:]) >= 2 else "0" + hex(self.line.mrm)[2:] + "\t"

			elif i["rule"] == "REG_REG" and i["name"] == first_word:
				data1 = string[1][:-1]
				data0 = string[2]

				self.generate_mrm(data0, data1, i["rule"])
				self.line.operation_code += i["code"]
				if self.get_register_adressing_mode(data0) == 1 or self.get_register_adressing_mode(data1) == 1:
					Processor.string_for_print += "66|" + " "
					self.line.operation_code = i["code"] + 1
				else:
					self.line.operation_code = i["code"]
				Processor.string_for_print += hex(self.line.operation_code)[2:] + " " if len(hex(self.line.operation_code)[2:]) >= 2 else "0" + hex(self.line.operation_code)[2:] + " "
				Processor.string_for_print += hex(self.line.mrm)[2:] + "\t" if len(hex(self.line.mrm)[2:]) >= 2 else "0" + hex(self.line.mrm)[2:] + "\t"

			elif i["rule"] == "REG_IMM" and i["name"] == first_word:
				data1 = string[1][:-1]
				data0 = string[2]
				self.line.operation_code = i["code"]

				if self.useful_lexems.is_constant(data0) == 2:
					self.line.operand = int(data0[:-1], 2)
				elif self.useful_lexems.is_constant(data0) == 16:
					self.line.operand = int(data0[:-1], 16)
				else:
					self.line.operand = int(data0)
				
				if self.get_register_adressing_mode(data1) == 1:
					if self.line.operand == 1:
						Processor.string_for_print += "66|" + " "
						mrm = self.line.operation_code + self.get_register_position(data1)
						self.line.operation_code += self.get_register_adressing_mode(data1) + 16	
						Processor.string_for_print += hex(self.line.operation_code)[2:] + " " if len(hex(self.line.operation_code)[2:]) >= 2 else "0" + hex(self.line.operation_code)[2:] + " "	
						Processor.string_for_print += hex(mrm)[2:] + " " if len(hex(mrm)[2:]) >= 2 else "0" + hex(mrm)[2:] + " "
					else:
						Processor.string_for_print += "66|" + " "
						mrm = self.line.operation_code + self.get_register_position(data1)
						self.line.operation_code += self.get_register_adressing_mode(data1)	
						Processor.string_for_print += hex(self.line.operation_code)[2:] + " " if len(hex(self.line.operation_code)[2:]) >= 2 else "0" + hex(self.line.operation_code)[2:] + " "	
						Processor.string_for_print += hex(mrm)[2:] + " " if len(hex(mrm)[2:]) >= 2 else "0" + hex(mrm)[2:] + " "
						Processor.string_for_print += hex(self.line.operand)[2:] + "\t" if len(hex(self.line.operand)[2:]) % 2 == 0 else\
						"0" + hex(self.line.operand)[2:] + "\t"
				else:
					if self.line.operand == 1:
						mrm = self.line.operation_code + self.get_register_position(data1) - 8
						self.line.operation_code += 16
						Processor.string_for_print += hex(self.line.operation_code)[2:] + " " if len(hex(self.line.operation_code)[2:]) >= 2 else "0" + hex(self.line.operation_code)[2:] + " "
						Processor.string_for_print += hex(mrm)[2:] + " " if len(hex(mrm)[2:]) >= 2 else "0" + hex(mrm)[2:] + " "
					else:
						mrm = self.line.operation_code + self.get_register_position(data1) - 8
						Processor.string_for_print += hex(self.line.operation_code)[2:] + " " if len(hex(self.line.operation_code)[2:]) >= 2 else "0" + hex(self.line.operation_code)[2:] + " "
						Processor.string_for_print += hex(mrm)[2:] + " " if len(hex(mrm)[2:]) >= 2 else "0" + hex(mrm)[2:] + " "
						Processor.string_for_print += hex(self.line.operand)[2:] + "\t" if len(hex(self.line.operand)[2:]) % 2 == 0 else\
						"0" + hex(self.line.operand)[2:] + "\t"
			
			elif i["rule"] == "ONLY_LABEL" and i["name"] == first_word:
				if len(string) < 3 or not self.useful_lexems.is_identifier(string[1]):
					self.set_error("ERROR: expected identifier")
				example = self.find_identifier_by_name(string[1])
				print string[1]
				print "processor" + str(Processor.offset)
				print "example" + str(example)
				if example != None and Processor.offset > example.offset:
					Processor.string_for_print += hex(i["code"])[2:] + " "
					self.line.adress = 0xff - Processor.offset + example.offset - 1
					Processor.string_for_print += hex(self.line.adress)[2:]
				else:
					self.line.adress = i["code"]
					self.line.adress_size_prefix = 2
					Processor.string_for_print += "150" + "\t"
					self.line.operand_size = 4


	def find_identifier_by_name(self, name):
		for i in Processor.list_of_identifier:
			if i.name == name:
				return i
				break

	def generate_mrm(self, data0, data1, rule):
		mod = 0
		rm = 0
		reg = 0
		if rule != "EMPTY" and rule != "ONLY_REG" and rule != "ONLY_LABEL":
			first = data1
			second = data0

			if rule == "MEM_REG" or rule == "MEM_IMM" or rule == "REG_MEM":
				self.set_error(self.check_registers_adressing(second))
				reg = self.get_register_position(second) 	
				strings = []
				for e in data1:
					res = re.findall(r'(?u)\w+', e)
					strings += res

				self.line.adress_size_prefix = 0x67
				
				if len(strings) >= 2:
					if strings[1] in self.useful_lexems.adress_registers:
						rm = self.useful_lexems.adress_registers[strings[1]]
						reg = self.get_register_position(second) - 8 if self.get_register_adressing_mode(second) == 1 else\
							  self.get_register_position(second) - 16
						mod = 2
						Processor.string_for_print += hex(self.line.adress_size_prefix)[2:] + "|" + " "
					else:
						self.set_error("ERROR: must be index or base register")
				else:
					if strings[0] in self.useful_lexems.adress_registers:
						rm = self.useful_lexems.adress_registers[strings[0]] 
						reg = self.get_register_position(second) - 8
					else:
						self.set_error("ERROR: must be index or base register")
				if rule == "MEM_IMM":
					reg = 5

			elif rule == "REG_REG":
				mod = 3
				reg = self.get_register_position(first)
				rm = self.get_register_position(second)
				if data1 == "AX":
					rm -= 8

			elif rule == "REG_IMM":
				pass

		self.line.mrm = (mod << 6) | (reg << 3) | rm

	def generate_sib(self):
		pass


	def check_registers_adressing(self, reg):
		register_number = self.get_register_position(reg)
		if register_number <= 7:
			return self.set_error("ERROR: 32-bit data used")

	def get_register_adressing_mode(self, reg):
		register_number = -1
		if reg in self.useful_lexems.registers:
 			register_number = self.useful_lexems.registers.index(reg)
 		if register_number >= 8 and register_number <= 15:
 			return 1
 		return 0

 	def get_register_position(self, reg):
 		reg_pos = -1
 		if reg in self.useful_lexems.registers:
 			reg_pos = self.useful_lexems.registers.index(reg)
 		return reg_pos

	def is_segment(self, string):
		first_word = string[0]
		if self.useful_lexems.is_identifier(first_word):
			if len(first_word) > 8:
				self.set_error("ERROR: identifier length more then 8 characters")
			#is lable
			# elif string[1] == ":":
			# 	self.set_error(first_word, "L NEAR", 0)
			#is variable
			else:
				Processor.nexxt = string[1]
				if Processor.nexxt == "SEGMENT":
					Processor.segment_value = first_word
					Processor.offset = 0
					return True

	def is_ends(self, string):
		first_word = string[0]
		if self.useful_lexems.is_identifier(first_word):
			if len(first_word) > 8:
				self.set_error("ERROR: identifier length more then 8 characters")
			#is lable
			# elif string[1] == ":":
			# 	self.set_error(first_word, "L NEAR", 0)
			#is variable
			else:
				Processor.nexxt = string[1]
				if Processor.nexxt == "ENDS":
					Processor.segment_value = None
					Processor.offset = 0
					return False

	def parse_string_to_line(self):
		self.line.reset()
		string = self.line_string

		if self.is_segment(string):
			Processor.string_for_print += "0" * (4 - int(len(hex(Processor.offset)[2:]))) + str(Processor.offset) + "\t"
			# print "0" * (4 - int(len(str(Processor.offset)))) + str(Processor.offset) + "\t"
		elif self.is_ends(string):
			Processor.string_for_print += "0" * (4 - int(len(hex(Processor.offset)[2:]))) + str(Processor.offset) + "\t"
		elif len(hex(Processor.offset)[2:]) < 4:
			Processor.string_for_print += "0" * (4 - int(len(hex(Processor.offset)[2:]))) + hex(Processor.offset)[2:] + "\t"
			# print "0" * (4 - int(len(str(Processor.offset)))) + str(Processor.offset) + "\t",
		first_word = self.line_string[0]
		if (first_word[0] != ";"):
			if ";" in string:
				if self.useful_lexems.is_identifier(first_word):
					self.parse_identifier(string[:string.index(";")])
				elif (first_word in self.useful_lexems.machine_command["name"]):
					self.parse_command(string[:string.index(";")])
			elif first_word in self.useful_lexems.machine_commands:
				self.parse_command(string)
			elif self.useful_lexems.is_identifier(first_word):
				self.parse_identifier(string)
		self.line.line_number += 1

		Processor.offset += int(self.line.generate_offset()) 
		Processor.string_for_print += " ".join(string) + "\n"

		# Processor.offset += self.line.operand_size
		# self.line.offset = self.line.generate_offset()
		# self.line.my_line.append(string)
		# print self.line.to_string()
		# if find_current_segment == None:
		# 	self.line.offset = offset + 1
		return self.line

	def set_error(self, error):
		if error != None:
			Processor.string_for_print += error + 2 * "\t"

