from Processor.line import Processor.line
from Useful_lexems import Useful_lexems

class Processor(object):

	def __init__(self, line_string):
		self.line_string = line_string

	line = Processor.line()
	#variables for line
	line_number = 0
	offset = 0
	#variable for errors
	segment_open = False
	close_program = False

	def analyze(self, string):
		pass

	def is_identifier(self, word):
		return (word[0].isalpha() and word[-1].isalpha() and len(word) <= 8 or word[0] == "_") or\
		(word[0].isalpha() and word[-1].isdigit() and len(word) <= 8 or word[0] == "_")
		

	def set_identifier(self):
		pass

	def parse_identifier(self, string):
		first_word = string[0]
		if len(first_word) > 8:
			Processor.line.set_error()
		#is lable
		elif string[1] = ":":
			Processor.line.set_error(first_word, "L NEAR", 0)
		#is variable
		else:
			nexxt = string[1]
			

	def parse_keyword(self):
		pass

	def parse_machine_command(self):
		pass
 
	def pars_string_to_Processor.line(self):
		for string in self.line_string:
			first_word = string[0]
			if (first_word[0] == ";"):
				continue
			elif ";" in string:
				if self.is_identifier(first_word):
					Processor.line = self.parse_identifier(string[:string.index(";")])
				elif (first_word in Useful_lexems.keyword):
					Processor.line = self.parse_keyword(string[:string.index(";")])
				elif (i in Useful_lexems.machine_command):
					Processor.line = self.parse_machine_command(string[:string.index(";")])
			elif self.is_identifier(first_word):
				Processor.line = self.parse_identifier(string)
			elif (first_word in Useful_lexems.keyword):
				Processor.line = self.parse_keyword(string)
			elif (i in Useful_lexems.machine_command):
				Processor.line = self.parse_machine_command(string)
			Processor.line.line_number = line_number + 1
			Processor.line.set_line_number()
			Processor.line.set_offset(offset)
			Processor.line.set_line(string)
			Processor.line.offset += Processor.line.generate_offset()
			if find_current_segment == None:
				Processor.line.offset = offset + 1
		return Processor.line