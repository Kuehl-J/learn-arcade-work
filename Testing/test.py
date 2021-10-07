class Character:
    """
    This is a video game character
    """
    def __init__(self):
        """ Create my character"""
        x = 0
        self.name = ""
        self.outfit = ""
        self.max_hit_points = 0
        self.current_hit_points = 0
        self.armor_amount = 0
        self.max_speed = 0

class Address:
    """
    Set up address fields
    """
    def __init__(self):
        self.name = ""
        self.line1 = ""
        self.line2 = ""
        self.city = ""
        self.state = ""
        self.zip = ""

def main():
    home_address = Address()
    home_address.name = "John Smith"
    home_address.line1 = "701 N C St"
    home_address.line2 = "Carver Science Building"
    home_address.city = "Indianola"
    home_address.state = "IA"
    home_address.zip = "50125"

def print_address(address):
    #If there is a line1 in the adddress, print it
    if len(address.line1) > 0:
        print(address.line1)
    #If ther is a line2 in the address, print it
    if len(address)



class Dog
    def __init__(self, name):
        """Constructor"""

        self.name = new_name
        print("A dog has been born!")

def main():
    #This creates the dog
    my_dog = Dog("Spot")
    print(f"The dog's name is:) {my_dog.name}"

    my_other_dog = Dog("Sam")
    print(f"The dog's name is:) {my_other_dog}")

main()







class Person:
        def __init__(self):

            self.name; str = "A"

mary = Person()
mary.name = 22



@dataclass
class Address:
    name: str = ""
    line1: str = ""
    line2: str = ""
    city: str = ""
    state: str = ""
    zip_code: str = ""