class Identifier(object):

	def __init__(self):
		self.name = None
		self.ident_type = None
		self.offset = None
		self.length = None
		self.attribute = None
		self.value = None
		self.closed = None
		self.segment_register = None


	def identifier(self, name, ident_type, offset, value = None, attribute = None, length = None, closed = None):
		self.name = name
		self.ident_type = ident_type
		self.offset = offset
		self.value = value
		self.attribute = attribute
		self.length = length
		self.closed = closed