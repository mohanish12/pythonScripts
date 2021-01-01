class Name:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def find_printed_name(self):
        return self.first_name + " " + self.last_name

    def find_sortable_name(self):
        return self.last_name + "," + " " +  self.first_name[0]




test_name = Name("David", "Joyner")
print(test_name.first_name)
print(test_name.last_name)
print(test_name.find_printed_name())
print(test_name.find_sortable_name())
