from random import shuffle

state_dict = {
	"Alabama": "Montgomery",
	"Alaska": "Juneau",
	"Arizona": "Phoenix",
	"Arkansas": "Little Rock",
	"California": "Sacramento",
	"Colorado": "Denver"
}


class StateCapitalGame():
	def __init__(self, dictionary):
		self.dict_states = {}
		self.state = {"Correct": 0, "Incorrect": 0 }
		keys = list(dictionary.keys())
		shuffle(keys)
		for key in keys:
			self.dict_states.update({key: dictionary[key]})
		print("Welcome to the State Capital Game")
		print("more instructions go here")
		for key, value in self.dict_states.items():
			question = (("What is the capital of {}?").format(key))
			answer = input(question)
			if (answer == value):
				print('Great job bud!')
				self.state['Correct'] += 1
			else:
				print('Guuuurl you wrong')
				self.state['Incorrect'] += 1
				print("You got {} correct and {} wrong. Play again yo!").format(self.state['Correct'], self.state['Incorrect']) 	



	def __str__(self):
		return ("You got {} correct and {} wrong. Play again yo!").format(self.state['Correct'], self.state['Incorrect']) 	

dict_game = StateCapitalGame(state_dict)






# "Connecticut": "Hartford",
# "Delaware": "Dover",
# "Florida": "Tallahassee",
# "Georgia": "Atlanta",
# "Hawaii": "Honolulu",
# "Idaho": "Boise",
# "Illinois": "Springfield",
# "Indiana": "Indianapolis",
# Iowa - Des Moines
# Kansas - Topeka
# Kentucky - Frankfort
# Louisiana - Baton Rouge
# Maine - Augusta
# Maryland - Annapolis
# Massachusetts - Boston
# Michigan - Lansing
# Minnesota - St. Paul
# Mississippi - Jackson
# Missouri - Jefferson City
# Montana - Helena
# Nebraska - Lincoln
# Nevada - Carson City
# New Hampshire - Concord
# New Jersey - Trenton
# New Mexico - Santa Fe
# New York - Albany
# North Carolina - Raleigh
# North Dakota - Bismarck
# Ohio - Columbus
# Oklahoma - Oklahoma City
# Oregon - Salem
# Pennsylvania - Harrisburg
# Rhode Island - Providence
# South Carolina - Columbia
# South Dakota - Pierre
# Tennessee - Nashville
# Texas - Austin
# Utah - Salt Lake City
# Vermont - Montpelier
# Virginia - Richmond
# Washington - Olympia
# West Virginia - Charleston
# Wisconsin - Madison
# Wyoming - Cheyenne