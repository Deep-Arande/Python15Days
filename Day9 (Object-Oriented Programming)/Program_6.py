# Given a JSON file with customer data, create a Customer
# class to store and manipulate the data
import json


def dump_data(customers):

    up_data = dict({'customers': [c.to_dict() for c in customers]}) #convert data into dict and append

    with open("customer.json", "w") as j_file:
        json.dump(up_data, j_file, indent=4)


def load_customer():

    customers = list()

    with open("customer.json", "r") as j_file:
        data = json.load(j_file)

    for row in data['customers']:
        cu = customer(row['id'], row['name'], row['email'], row['phone'])
        customers.append(cu)
    return customers


class customer:
    id = str()
    name = str()
    email = str()
    ph_num = str()

    def __init__(self, id, name, email, num):
        self.id = id
        self.name = name
        self.email = email
        self.ph_num = num

    def __str__(self):

        return f"name={self.name}\nemail={self.email}\nphone number={self.ph_num}"

    def data_modify(self, data, attribute):

        if attribute == 'name':
            self.name = data
        elif attribute == 'id':
            self.id = data
        elif attribute == 'email':
            self.email = data
        elif attribute == 'ph_num':
            self.ph_num = data
        else:
            print("Wrong attribute")
            return
        
        

    def to_dict(self):  # function to return data in dict formate to store in json

        data = dict({
            'id': self.id,
            'name': self.name,
            'email': self.email,
            'phone': self.ph_num
        })
        return data


# extract json data

customers_data = load_customer()

print("Data before modification")

for c in customers_data:
    print(f"{c}\n")
    


customers_data[0].data_modify("Deep","name")

dump_data(customers_data)

print("Data after modification")

for c in customers_data:
    print(f"{c}\n")