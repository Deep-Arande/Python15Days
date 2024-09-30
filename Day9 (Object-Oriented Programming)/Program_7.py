#  Write a program that uses a Person class to keep track of 
# a person's name, age, and addres

class Person:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Address: {self.address}")

    def update_name(self, new_name):
        self.name = new_name

    def update_age(self, new_age):
        self.age = new_age

    def update_address(self, new_address):
        self.address = new_address

# Example usage
if __name__ == "__main__":
    # Create a new person
    person = Person("John Doe", 30, "123 Main St, Springfield")
    
    # Display person information
    print("Original Info:")
    person.display_info()
    
    # Modify the person's details
    person.update_name("Jane Smith")
    person.update_age(28)
    person.update_address("456 Oak Avenue, Springfield")
    
    # Display updated information
    print("\nUpdated Info:")
    person.display_info()
