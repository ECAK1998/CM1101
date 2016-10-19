>>> from items import *
from encounter import *

class room():
	"""The base class for all rooms"""
	def __init__(self, name, description, exits, items, encounter, NPCs):
		self.name = name
		self.description = description
		self.exits = exits
		self.items = items
		self.encounter = encounter
		self.NPCs = NPCs
				
room_reception = room("Reception", 
"""You find yourself in the Cardiff School of Computer Science and
Informatics reception. The receptionist, Matt Strangis,looks to be playing an old school text-based adventure
game on his computer. Matt tells you your smarthphone can always bring you straight back here 

You feel safe here

There are corridors leading to the North,South, East and west. their is also a staircase which goes to T 2.09 

West leads to the parking lot where you can get to the western extension and central building.

South goes to the admin room where you can get your student id.

East goes to your personal tutors room.
North goes to the canteen.
""",
{"south": "Admins", "east": "Tutor", "west": "Parking","north":"Canteen","staircase":"T 2.09"}, [item_biscuits, item_handbook], "", "")
 
room_admins = room("MJ and Simon's room",
"""You are leaning agains the door of the systems managers'
room. Inside you notice Matt "MJ" John and Simon Jones. They
ignore you. To the north is the reception.
You try your best to get their attention it is unsuccessful""",
{"north": "Reception","Smarthphone":"Reception"}, [item_id], "", "")

room_tutor = room("your personal tutor's office",
"""You are in your personal tutor's office. they intently
stare at their huge monitor, Defeated they carry on with their work.
On the desk you notice a cup of coffee and an empty
pack of biscuits and an orange key.

The reception is to the west.""",
{"west": "Reception","Smarthphone":"Reception"},[], "", "")

room_parking = room("the parking lot",
"""You are standing in the Queen's Buildings parking lot.
You can go north to the west extension and from their the south building

Southeast to the closest starbucks

West to the Central building
.""",
{"Southeast": "coffeshop", "East": "Reception","West":"central","North";"WX 3.07","Smarthphone":"Reception"}, [], "", "")

room_Coffeshop = room("Starbucks", 
"""
You are in the starbucks, on the table closest to the door you notice a blue key a weary lecturer must have forgotten it"
If you go west you can return to the Queen's Buildings.""",
                      
{"west": "Parking","Smarthphone":"Reception"}, [item_pen,item_key_B], "", "")

room_T2.09 = room("lecture theater",
"""this is the lecture hall where you wont be exhausted by the time you get to it,
its a fairly cramed room when everyones here today it looks empty, the lectures sits in the swivel chair exhausted after losing to you in a dance battle.
you can get back to reception via the staircase
""",

{"staircase":"Reception","Smarthphone":"Reception"}[],"","")

room_WX3.07 = room ("WX 3.07",
""" The western extension the small lecture room where you faced the guest speaker,
they enticed you with the description sherlock and you thought may have something to do with robert downey jr or benedict cumberbatch
so you defeted them with your impressive skanking skills you found the indigo key here """

{"west":"S 2.22", "South":"Parking","Smarthphone":"Reception"}[]"","")

room_S2.22 = room ("S 2.22",
"""the rarley ventured south building, one does not simply walk into south building
another lecturer sits defeated on the floor, you found the violet key here"""

{"east":"WX 3.07","Smarthphone":"Reception"}[]"","")

room_central = room ("central",
"""the central building this building has the staircase from hell,
but taking the lift takes just as long so you should probably just walk"""

{"staircase": "C 2.04-5","East":"Parking","Smarthphone":"Reception"}[]"","")

room_C2.04-5 = room ("C 2.04-5",
""" the main lab for computer science you've spent a lot of hours here,
the lecturer here was a hardy and steadfast in their defence of their key
you found the green key here 
"""
{"staircase down": "central","staircase up":"N 4.07","Smarthphone":"Reception"}[]"","")
 
room_N4.07 = room  ("N 4.07","""here stood the final lecturer,
the final challenge, the only thing which stood between you and a summer of relative freedom
walk through the fire exit doors to complete your journey
"""

{"forward":"Roof","Smarthphone":"Reception"}[]"","")

room_Roof = room ("rooftop","""you've done it, youve beaten them all,
achived your final grade, you have become the very best,
You get the title of edm death machine,
Now you get to enjoy the rare picturesque day, you sly fox"""

rooms = {
    "Reception": room_reception,
    "Canteen": room_canteen
    "Admins": room_admins,
    "Tutor": room_tutor,
    "T 2.09" room_T2.09,
    "Parking": room_parking,
    "Starbucks": room_coffeshop,
    "WX 3.07": room_WX3.07,
    "S 2.22": room_S2.22,
    "central": room_central
    "C 2.04-5": room_C2.04-5
    "N 4.07": room_N4.07,
    "Roof": room_Roof
}
