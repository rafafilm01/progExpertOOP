#example of a class with methods that access the values defined in the constructor . change_position allows to make changes to the parameters 

class Rectangle:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    # Write your code here
    def change_position(self, x, y ):
        self.x = x
        self.y = y
    
    def get_position(self):
        return self.x , self.y
    
    def get_area (self):
        return self.width *self.height 
    
#example of a class with methods accessing existing list (defined in the constructor ) and making changes to it . Finally get_members method that sorts the existing list
## example of exception being raised  in order to prevent program crashing when an element that does not exist in the list is accessed    
    
class Group:
    def __init__(self, name, members=[]):
        self.name = name
        self.members = members

    # Write your code here
    def add(self, name):
        self.members.append(name)
        

    def delete(self, name):
        
        if name in  self.members :
            self.members.remove(name)
        else:
            raise Exception("Member not in group.")
        
    def get_members (self):
        return sorted(self.members)
        