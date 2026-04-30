from typing import Tuple
from random import randint
import sqlite3

# test

from models import *


class DatabaseError(Exception):
    pass

class Database:
    def __enter__(self):
        self.__conn = sqlite3.connect("./db/holidays.db")
        self.__cursor = self.__conn.cursor()
        return self

    def __exit__(self, *args):
        
        self.__conn.close()
    
    def add_new_customer(self, forename: str, surname: str, telephone: str):
        id_ = forename[0] + surname[:2].upper() + str(randint(111, 999))
        self.__cursor.execute(f"INSERT INTO Customer VALUES ('{id_}', '{forename}', '{surname}', '{telephone}')")
        self.__conn.commit()

    def get_all_customers(self) -> Tuple[Tuple]:    
        records = self.__cursor.execute("SELECT * FROM Customer").fetchall()
        return records
    
    def get_holidays_by_location(self, location: str) -> Tuple[Holiday]:
        records = self.__cursor.execute("SELECT * FROM Holiday WHERE Location = ?", (location,)).fetchall()

        return [Holiday(*record) for record in records]

        
    def get_holiday_by_id(self, holiday_id) -> Holiday | None:
        record = self.__cursor.execute("SELECT * FROM Holiday WHERE HolidayID = ?", (holiday_id,)).fetchone()

        return Holiday(*record)
    
    def create_new_customer(self, forename: str, surname: str, telephone: str) -> Customer:
        '''work out the new customer's ID
        write the new customer to the database
        return the new customer as a Customer object'''
    
    def get_customer_by_names(self, forename: str, surname: str) -> Customer | None:        
        '''look in the database to find a customer
        if it exists, return the customer as a Customer
        if it doesn't, return None'''

    def get_allergen_by_name(self, allergen_name) -> Allergen | None:
        '''look in the database to find an allergen
        if it exists, return the Allergen object
        if it doesn't return None'''

    def create_new_guest(self, guest_name: str, allergies: list[Allergen], food: Food) -> Guest:
        '''write a new guest to the database (primary key will be made automatically)
        return the new guest as a Guest'''
    
    def create_new_booking(self, customer_id: str, holiday_id: str) -> Booking:
        '''write a new booking to the database
        return the new booking as a Booking'''

    def get_food_choice_by_name(self, food_choice: str) -> Food:
        pass

    def process_booking(self, form_data) -> tuple[Customer, Booking, list[Guest]]:
        '''Validates that the data received from the front end is acceptable
        returns models if valid'''
        
        #extract data from post request body
        holiday_id = form_data.get("holiday_id")  
        forename = form_data.get("forename")
        surname = form_data.get("surname")
        telephone = form_data.get("telephone")
        guests = form_data.get("guests")

        if holiday_id is None:
            raise AttributeError("holiday_id was not found in post request data")

        if not isinstance(holiday_id, str):
            raise TypeError("holiday_id was not a string")
        
        holiday = self.get_holiday_by_id(holiday_id)

        # if it isn't - error
        if not holiday:
            raise DatabaseError(f"holiday_id {holiday_id} not found in database")
        

        # check if the customer's forename/surname exists, and is in the database?
        if not forename:
            raise AttributeError("forename was not found in post request data")
                
        if not isinstance(forename, str):
            raise TypeError("forename was not a string")
                
        if not surname:
            raise AttributeError("surname was not found in post request data")
        
        if not isinstance(surname, str):
            raise TypeError("surname was not a string")


        # if it is - make a Customer object
        customer = self.get_customer_by_names(forename, surname)

        ## probably should do something regarding phone numbers
        # what if the phone number doesn't match? come back later

        if customer is None:
            customer = self.create_new_customer(forename, surname, telephone)


        booking = self.create_new_booking(customer.id, holiday.id)

        # check if guest data present
        if not guests:
            raise AttributeError("guest data missing from post request")
        
        if not isinstance(guests, list):
            raise TypeError("guests was not a list")

        for guest in guests:

            # to do - client will deal with missing data / duplicates
            # assume everything OK re: guest names if we got to this point

            meal = guest.get("meal")            
            allergies = guest.get("allergies")
            name = guest.get("name")

            if not meal:
                raise AttributeError(f"guest {name}'s meal missing from post request data")
            
            if not allergies:
                raise AttributeError(f"guest {name}'s allergies missing from post request data")


        return holiday, customer, booking, guests, allergies


if __name__ == "__main__":

    # tests
    print(db.get_holidays("New York"))
    

    # should see martin davies

