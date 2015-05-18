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