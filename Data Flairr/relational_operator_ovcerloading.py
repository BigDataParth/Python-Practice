class mayclass:
    def __init__(self, a):
        self.a = a
    def __lt__(self, other):
        if isinstance(other, mayclass):
            return self.a < other.a
        return NotImplemented
    def __eq__(self, other):
        if isinstance(other, mayclass):
            return self.a == other.a
        return NotImplemented
    def __le__(self, other):
        if isinstance(other, mayclass):
            return self.a <= other.a
        return NotImplemented
    def __gt__(self, other):
        if isinstance(other, mayclass):
            return self.a > other.a
        return NotImplemented
    def __ge__(self, other):
        if isinstance(other, mayclass):
            return self.a >= other.a
        return NotImplemented
    
M1 = mayclass(10)
M2 = mayclass(20)
if M1 < M2:
    print("M1 is less than M2")
if M1 == M2:
    print("M1 is equal to M2")
if M1 <= M2:
    print("M1 is less than or equal to M2")
if M1 > M2:
    print("M1 is greater than M2")
if M1 >= M2:
    print("M1 is greater than or equal to M2")

#getters & Setters
class mayclass2:
    def setId(self, id):
        self.id = id
    def getId(self):
        return self.id
    def setName(self, name):
        self.name = name
    def getName(self):
        return self.name

M3 = mayclass2()
M3.setId(10)
M3.setName("Object 3")
print(M3.getId())
print(M3.getName())
