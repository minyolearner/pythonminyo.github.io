class Flight:
    def __init__(self, capacity):
        self.capacity = capacity
        self.passengers = []
    def add_passenger(self, name):
        if not self.open_seats():
            return False # return false korle elhaney stop hoye jabe
        self.passengers.append(name)
        return True
    
    def open_seats(self):
        return (self.capacity - len(self.passengers))
    
flight_1 = Flight(5)

Peoples = ['Momo','Sana','Jihyo','Mina','Tyuzu','TT','Jennie','Nayeon','Yuna','Haerin']
for people in Peoples:
    Success = flight_1.add_passenger(people)
    if Success:
        print(f"{people} added to Flight")
    else:
        print(f"No More Seat Available For {people}")

