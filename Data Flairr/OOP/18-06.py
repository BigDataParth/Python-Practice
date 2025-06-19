class myclass:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"myclass object with name: {self.name}"

    def __repr__(self):
        return f"myclass({self.name!r})"
    
    def __add__(self,other):
        self.name *= other.name
        return self
    
    def __mul__(self, other):
        self.name *= other.name
        return self
# Example usage of the myclass
# class
# This will create two instances of myclass and add them together   
    def __len__(self):
        return len(self.name)
    def __floordiv__(self, other):
        return self.name // other.name
    def __truediv__(self, other):
        return self.name / other.name
    def __mod__(self, other):
        return self.name % other.name
    def __pow__(self, other):
        return self.name ** other.name
    
M1= myclass(500)
M2=myclass(600)
M3 = M1 + M2
print(M3)  # This will call the __str__ method