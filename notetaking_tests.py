import unittest
from notetaking import NotesApplication

'''
	Note taking tests
'''

class NoteTakingTests(unittest.TestCase):
	

	def test_note_empty(self):
		#Test if note created is empty
		self.assertEqual(NotesApplication("Mike").create(), "Note content can't be empty")


	def test_note_list(self):
		#Test if note list function returns non for empty list
		mike = NotesApplication("Mike")
		mike.create()
		self.assertEqual(mike.list(), notes_list)

	def test_note_get(self):
		#Test if note id in get does not exists
		mike = NotesApplication("Mike")
		notes_list = mike.create("Remember to buy sugar")
		self.assertEqual(mike.get(8), "Note Doesn't exist")

	def test_note_delete(self):
		#Test if delete function can't delete note that doesn't exist
		mike = NotesApplication("Mike")
		notes_list = mike.create("Remember to buy sugar")
		self.assertEqual(mike.delete(4), "Note to be deleted doesn't exist")

	def test_note_edit(self):
		#Test if edit function can't edit a note that doesn't exist
		mike = NotesApplication("Mike")
		notes_list = mike.create("Remember to buy sugar")
		self.assertEqual(mike.edit(4, "Save all files to git"), "Note to be edited doesn't exist")

	def test_note_search(self):
		#Test if search returns not found when search text doesn't exist
		mike = NotesApplication("Mike")
		notes_list = mike.create("Remember to buy sugar")
		self.assertEqual(mike.search("Python"), "Sorry. Note not Found")		

	def test_object_is_instance(self):
		#test if an object is an instance of the class
		mike = NotesApplication('mike')
		with self.assertRaises(TypeError):
			isinstance(mike, NotesApplication)



if __name__ == '__main__':
	unittest.main()


