class Useful_lexems(object):

	register_8 = ["AL", "CL", "DL", "BL", "AH", "CH", "DH", "BH"]
	register_16 = ["AX", "CX", "DX", "BX", "SP", "BP", "SI", "DI"]
	segment_register = ["DS", "FS", "ES", "CS", "SS", "GS"]
	
	#			   0      1      2      3      4      5      6      7    
	registers = ["EAX", "ECX", "EDX", "EBX", "ESP", "EBP", "ESI", "EDI",\
	#               8     9    10    11    12    13    14    15
				  "AX", "CX", "DX", "BX", "SP", "BP", "SI", "DI",\
	#			   16    17    18    19    20    21    22    23
				  "AL", "CL", "DL", "BL", "AH", "CH", "DH", "BH",\
	]

	adress_registers = {"BX": 7,
						"SI": 4,
						"DI": 5,
						"BP": 6
	}

	keyword = ["SEGMENT", "END", "ENDS", "ORG", "ASSUME", "DB", "DW", "DD"]
	machine_commands = ["STI", "PUSH", "POP", "TEST", "OR", "SUB", "ROR", "SHR", "JZ"]
	machine_command = [
	{"name": "STI", "code": 0xfb, "rule": "EMPTY"},
	{"name": "PUSH", "code": 0x48, "rule": "ONLY_REG"},
	{"name": "POP", "code": 0x50, "rule": "ONLY_REG"},
	{"name": "TEST", "code": 0x84, "rule": "REG_REG"},
	{"name": "OR", "code": 0x0a, "rule": "REG_MEM"},
	{"name": "SUB", "code": 0x28, "rule": "MEM_REG"},
	{"name": "ROR", "code": 0xc0, "rule": "REG_IMM"},
	{"name": "SHR", "code": 0xd2, "rule": "MEM_IMM"}, 
	{"name": "JZ", "code": 0x74, "rule": "ONLY_LABEL"}
	]

	seg_reg = [
	{"name": "DS", "code": 0x3e},
	# {"name": "FS", "code": 0x64},
	{"name": "ES", "code": 0x26},
	{"name": "CS", "code": 0x2e},
	{"name": "SS", "code": 0x36},
	# {"name": "GS", "code": 0x65},
	]
	delimiter = [',', ":", "[", "]"]
	lexem_list = []

	def is_identifier(self, word):
		return (word[0].isalpha() and word[-1].isalpha() or word[0] == "_") or\
		(word[0].isalpha() and word[-1].isdigit() or word[0] == "_")

	def is_text_constant(self, word):
		return (word[0] == '\"' and word[-1] == '\"') or (word[0] == '\'' and word[-1] == '\'')
	def is_constant(self, constant):
		if (constant[0].isdigit() and constant[-1].isdigit()) or (constant[0].isdigit() and constant[-1] == "D"):
			return 10
		elif (constant[0].isdigit() and constant[-1] == "B"):
			return 2
		elif (constant[0].isdigit() and constant[-1] == "H" or constant[0].isalpha and constant[-1] == "H"):
			return 16
		else:
			return 0