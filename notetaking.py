class  NotesApplication(object):

	notes_list = []

	def __init__(self, author):

		self.author = author
		self.notes_list = NotesApplication.notes_list

	def create(self, note_content=None):

		note_content = str(note_content)

		if note_content != 'None':
			self.notes_list.append({'content': note_content, 'author':self.author})
			return self.notes_list

		else:
			return "Note content can't be empty"

	def list(self):
		for note in self.notes_list:
			return "Note ID: [%s]\n %s\n By Author[%s]" %(self.notes_list.indexOf(note), note['content'], note['author'])

	def get(self, note_id):
		try:
			return self.notes_list[note_id]
		except:
			return "Note Doesn't exist"

	def search(self, search_text):

		for text in self.notes_list:
			if text.find(search_text) > -1:
				return ('Showing results for %s \n Note ID [%s] \n %s \n By Author [%s]'
				 %(search_text, self.notes_list.indexOf(text), text, self.author))

			return 'Sorry. Note not Found'

	def delete(self, notes_id):
		try:
			deleted_note = notes_list.pop([notes_id])
			return deleted_note

		except:
			return "Note to be deleted doesn't exist"

	def edit(self, notes_id, new_content):
		try:
			notes_list.insert(notes_id, new_content)
			return notes_list
		except:
			return "Note to be edited doesn't exist"


s = NotesApplication("Mike")
print (s.create("I rememeber"))
print 