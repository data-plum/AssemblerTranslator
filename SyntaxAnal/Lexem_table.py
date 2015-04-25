from Lexem import Lexem

class Lexem_table(object):
	identifier_table = []

	def __init__(self, lexem_list):
		self.lexem_list = lexem_list
		if len(self.lexem_list) > 0:
		
	#def make_list_structure_of_sentense(self):
			for i in self.lexem_list:
				if i.lexem_type == "user identifier":
					if i.name not in Lexem_table.identifier_table:
						Lexem_table.identifier_table.append(i.name)
						print Lexem_table.identifier_table
					else:
						print "Syntax error. Identifier %s just is useable" % i.name