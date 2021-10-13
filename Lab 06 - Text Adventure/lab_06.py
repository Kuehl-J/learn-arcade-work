class Room:
    """
    This is the 0 room/entrance to dungeon
    """
    def __init__(self, description, north, east, south, west):
        self.description = description
        self.north = north
        self.east = east
        self.south = south
        self.west = west

def main():
    room_list = []
    room = Room("You are in the entrance of a dark cave, you have been told there lies great treasures"
                "to those who are brave enough to enter. You walk in with a lit torch and your trusted sword"
                " You see a tunnel about 5 feet wide to the east.", None, 1, None, None)
    room_list.append(room)
    room = Room("You have entered the corridor. You travel east for 10 feet before coming across a suspicious"
                " room.", None, 2, None, 0)
    room_list.append(room)
    room = Room("You see the pendulum swing out and slam into the southern wall causing part of it to crumble"
                "in a peculiar way. The room is roughly 10ft by 10ft. There is a hallway to the east.",
                None, 3, 16, 1)
    room_list.append(room)
    room = Room("You walk through a 20ft long hallway, you see your path begins to open up.",
                None, 4, None, 2)
    room_list.append(room)
    room = Room("You walk into the large room and find that your path is being blocked"
                "by an angry goblin holding a serrated knife. You notice he is wearing"
                "a necklace that says 'Boblin', huh.", None, 5, 11, 3)
    room_list.append(room)
    room = Room("This goblin sized hole is barely big enough for you to fit through. You crawl through for"
                "15ft before making a sharp turn.", None, None, 6, 4)
    room_list.append(room)
    room = Room("You make the tight squeeze to turn the corner and follow the path further.", None, 8, 7, 5)
    room_list.append(room)
    room = Room("The small pathway opens into a 10 ft by 10 ft room. Sitting on a table you see a large"
                "golden treasure chest.", 6, None, 9, None)
    room_list.append(room)
    room = Room("You barely noticed this path in the darkness, you follow it along until you see an "
                "intersection. Will you go north or south?", None, None, 9, 6)
    room_list.append(room)
    room = Room("You find yourself entering another hallway, similar to the one you were previously in.",
                7, None, 10, None)
    room_list.append(room)
    room = Room()




main()