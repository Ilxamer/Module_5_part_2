import json


class Model:
	title = 'Programming Python'
	text = 'Python is an intepreted programming language'
	author = 'Mark Luts'

	def save(self):
		# keys = list(filter(lambda x: not x.startswith('_'), dir(Model)))
		dictionary = {keys: str(value) for keys, value in vars(Model).items()}

		with open('attribute_list.json','w') as file:
			json.dump(dictionary,file)


		

b = Model()
b.save()


		


