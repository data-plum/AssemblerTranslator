class Line(object):

	my_line = []

	def __init__(self):
		self.line_number = 0
		self.offset = 0

		self.operation_code = 0
		self.mrm = 0
		self.sib = 0
		self.adress = 0
		self.operand = 0
		self.change_segment_prefix = 0
		self.adress_size_prefix = 0
		self.operand_size_prefix = 0
		self.operand_size = 0
		self.adress_size = 0

	@staticmethod
	def add_to_file(line):
		f = open("../Listing.lst", "w")
		f.write(line)
		f.close()

	def generate_offset(self):
		return hex(int((1 if self.mrm != 0 else 0)) +\
		int((1 if self.sib != 0  else 0)) + \
		int((self.adress_size if self.adress != 0  else 0)) + \
		int(self.operand_size if self.operand != -1  else 0) +\
		int((1 if self.change_segment_prefix != 0  else 0)) + \
		int((1 if self.adress_size_prefix != 0  else 0)) +\
		int((1 if self.operand_size_prefix != 0  else 0)))[2:]


	def to_string(self):
		return self.generate_offset()  

	def reset(self):
		self.line_number = 0
		self.offset = 0

		self.operation_code = 0
		self.mrm = 0
		self.sib = 0
		self.adress = 0
		self.operand = -1
		self.change_segment_prefix = 0
		self.adress_size_prefix = 0
		self.operand_size_prefix = 0
		self.operand_size = 0