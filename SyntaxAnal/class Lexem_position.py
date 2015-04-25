class Lexem_position(object):

	def __init__(self, name_or_lable = -1, mnem = -1, first_operand_start = -1, first_operand_count = -1, second_operand_start = -1, second_operand_count = -1):
		self.name_or_lable = name_or_lable
		self.mnem = mnem
		self.first_operand_start = first_operand_start
		self.first_operand_count = first_operand_count
		self.second_operand_start = second_operand_start
		self.second_operand_count = second_operand_count