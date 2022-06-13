#Software to operate simple json database

import requests
import json
import os
import sys

key_names = ["id", "brand", "model", "production_year", "convertible"]
key_widths = [10, 15, 10, 20, 15]
URL = "http://localhost:3000/cars"


def check_server(cid=None):

    if not cid:
        try:
            server = requests.head(URL)
        except requests.RequestException:
            return False
        else:
            return True
    else:
        try:
            server = requests.get(URL+f"/{cid}")
        except requests.RequestException:
            print("Server is not responding")
        else:
            if server.status_code == requests.codes.ok:
                return True
            else:
                return False


def print_menu():

    print("+" + "-"*35 + "+")
    print("|" + ' '*7 + "Vintage Cars Database" + ' '*7 + "|")
    print("+" + "-"*35 + "+")
    print("M E N U\n=======")
    print("1. List cars\n2. Add new car\n3. Delete car\n4. Update car\n0. Exit")
    

def read_user_choice():

    while True:
        choice = input("Enter your choice (0..4): ")
        try:
            choice = int(choice)
            if choice not in range(0,5):
                raise ValueError
            return choice
        except ValueError:
            print("Given value is invalid")


def print_header():

    for (n,w) in zip(key_names, key_widths):
        print(n.ljust(w), end="| ")
    print()


def print_car(car):

    for (n,w) in zip(key_names, key_widths):
        print(str(car[n]).ljust(w), end="| ")
    print()


def list_cars():

    try:
        server = requests.get(URL)
    except requests.RequestException:
        print("Connection error")
    if server.json() == []:
        print("*** Database is empty ***")
    else:
        print_header()
        data = server.json()
        for car in data:
            print_car(car)


def name_is_valid(name):

    if name == "":
        return False
    return True


def enter_id(fn=None):

    while True:
        id = input("Car ID (empty string to exit): ")
        try:
            if id == "":
                return None
            id = int(id)
            if id == 0:
                raise ValueError
        except ValueError:
            print("ID must consist of digits only and != 0")
        else:
            if fn:
                if not check_server(id):
                    print("Car with given ID doesn't exist")
                else:
                    return id
            else:
                if check_server(id):
                    print("Given ID is occupied")
                else:
                    return id
            

def enter_production_year():

    while True:
        year = input("Car production year (empty string to exit): ")
        try:
            if year == "":
                return None
            year = int(year)
            if year not in range(1900,2001):
                raise ValueError
        except ValueError:
            print("Production year must be in range (1900..2000)")
        else:
            return year


def enter_name(what):

    if what == "brand":
        brand = input("Car brand (empty string to exit): ")
        if name_is_valid(brand):
            return brand
        return None
    
    if what == "model":
        model = input("Car model (empty string to exit): ")
        if name_is_valid(model):
            return model
        return None


def enter_convertible():

    is_convertible = input("Is this car convertible? [y/n] (empty string to exit): ")
    while True:
        if is_convertible == "":
            return None
        if is_convertible == "y":
            return True
        if is_convertible == "n":
            return False
        print("Given value is invalid")
        is_convertible = input("Is this car convertible? [y/n] (empty string to exit): ")


def delete_car():

    try:
        server = requests.get(URL)
    except requests.RequestException:
        print("Connection error")
    if server.json() == []:
        print("There is nothing to delete")
        return None
    
    id = enter_id(delete_car.__name__)
    try:
        server = requests.delete(URL+f"/{id}")
        print("Success!")
    except requests.RequestException:
        print("Connection error")


def input_car_data(with_id):

    new_car_id = True
    if with_id:
        new_car_id = enter_id()
        if new_car_id is None:
            return None

    while True:
        new_car_brand = enter_name("brand")
        if new_car_brand is None:
            break
        new_car_model = enter_name("model")
        if new_car_model is None:
            break
        new_car_year = enter_production_year()
        if new_car_year is None:
            break
        new_car_is_convertible = enter_convertible()
        if new_car_is_convertible is None:
            break
        output_data = {'id': new_car_id, 
                        'brand': new_car_brand, 
                        'model': new_car_model,
                        'production_year': new_car_year,
                        'convertible': new_car_is_convertible}
        return output_data
    return None


def add_car():

    new_car_data = input_car_data(True)
    if new_car_data is not None:
        new_car_data = json.dumps(new_car_data)
        h_content = {"Content-Type": "application/json"}
        try:
            server = requests.post(URL, data=new_car_data, headers=h_content)
            print("Data successfully added to database")
        except requests.RequestException:
            print("Connection error")


def update_car():

    try:
        server = requests.get(URL)
    except requests.RequestException:
        print("Connection error")
    if server.json() == []:
        print("*** Database is empty ***")
        return None

    id = enter_id(update_car.__name__)
    updated_car_data = input_car_data(False)
    if updated_car_data is not None:
        updated_car_data = json.dumps(updated_car_data)
        h_content = {"Content-Type": "application/json"}
        try:
            server = requests.put(URL+f'/{id}', data=updated_car_data, headers=h_content)
            print("Data successfully modified")
        except requests.RequestException:
            print("Connection error")


while True:
    if not check_server():
        print("Server is not responding - quitting!")
        sys.exit(1)
    print_menu()
    choice = read_user_choice()
    if choice == 0:
        print("Bye!")
        sys.exit(0)
    elif choice == 1:
        os.system("cls")
        list_cars()
    elif choice == 2:
        os.system("cls")
        add_car()
    elif choice == 3:
        os.system("cls")
        delete_car()
    elif choice == 4:
        os.system("cls")
        update_car()



