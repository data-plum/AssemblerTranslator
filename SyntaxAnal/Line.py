class Line(object):

	line_number = None
	offset = 0

	operation_code = None
	mrm = None
	sib = None
	adress = None
	operand = None
	change_segment_prefix = None
	adress_size_prefix = None
	operand_size_prefix = None



	def set_line_number(self):
		return Line.line_number

	def operation_code(self):
		return Line.operation_code != None

	def mrm(self):
		return Line.mrm != None

	def sib(self):
		return Line.sib != None

	def adress(self):
		return Line.adress != None

	def operand(self):
		return Line.operand != None

	def change_segment_prefix(self):
		return Line.change_segment_prefix != None

	def adress_size_prefix(self):
		return Line.adress_size_prefix != None

	def operand_size_prefix(self):
		return Line.operand_size_prefix != None

	def set_error(self):
		pass


	def generate_offset(self):
		return (1 if self.operation_code() else 0) + \
		(1 if self.mrm() else 0) +\
		(1 if self.sib() else 0) + \
		(Line.adress_size if self.adress() else 0) + \
		(Line.operand_size if self.operand() else 0) +\
		(1 if self.change_segment_prefix() else 0) + \
		(1 if self.adress_size_prefix() else 0) +\
		(1 if self.operand_size_prefix() else 0)

	def to_string(self):
		return line_number + "\t" + offset