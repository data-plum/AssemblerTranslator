class Identifier(object):

	def __init__(self, name, ident_type, offset, value = None, attribute = None, length = None, closed = None, segment_register = None):
		self.name = name
		self.ident_type = ident_type
		self.offset = offset
		self.length = length
		self.attribute = attribute
		self.value = value
		self.closed = closed
		self.segment_register = segment_register


	def get_name(self):
		return self.name

	def get_ident_type(self):
		return self.ident_type

	def get_offset(self):
		return self.offset

	def get_length(self):
		return self.length

	def get_value(self):
		return self.value

	def get_attribute(self):
		return self.attribute

	def set_length(self, length):
		self.length = length

	def set_closed(self, closed):
		self.closed = closed

	def get_segment_register(self):
		return self.segment_register

	def set_segment_register(self, segment_register):
		self.segment_register = segment_register

	# def equals(self, o):
	# 	if self == o:
	# 		return True
	# 	elif (o == None or __name__ != o.__name__):
	# 		return False
	# 	else:
	# 		return True

	# def hash_code(self):
	# 	return 0 if self.name != None else name.hash_code() 
