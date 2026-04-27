from pyscript import document, when, display
from api import get_request_holidays, post_request_booking
from dto import parse_booking, parse_guest


@when("change", "#trip")
def select_holiday(e):
    # get the rest of the form elements out of the DOM (getElementById)
    # un-disable all of them
    form = document.getElementsByClassName("booking")[0]
    inputs = form.querySelectorAll("input, button, select")


    for input_ in inputs:
        input_.disabled = False



def create_booking() -> dict:
    # get the the stuff from the fields - variables
    customer_name = document.getElementById("cust-name").value
    telephone = document.getElementById("cust-tel").value
    guest_name = document.getElementById("guest1").value
    allergies = [allergy.name for allergy in \
                 document.querySelectorAll('input[type="checkbox"]') \
                 if allergy.checked]
    meal = document.getElementById("meal").value

    
    holiday_id = document.getElementById("trip").value

    # come back to multiple guests later

    guest = parse_guest(guest_name, allergies, meal)

    guests = [guest]

    booking = parse_booking(customer_name, telephone,
                            holiday_id, guests)

    

    return booking

    

    

  
@when("click", "#book_holiday")
async def click_book_holiday(e):    
    '''Triggers a request to add the new booking to the database'''
    booking = create_booking()
    feedback = await post_request_booking(booking)
    display(feedback)


def click_add_another_guest():
    '''Duplicates the customer form for another guest'''

def save_for_later():
    '''Save the partially completed form using a cookie'''
 

@when("click", ".search-cta")
async def click_go(e):
    '''Triggers a request to the database to find holidays matching
    the location the user enters'''
    location_input = document.getElementById("dest")
    location = location_input.value
    holidays = await get_request_holidays(location)    
    load_holidays_to_select_trip_dropdown(holidays)


def load_holidays_to_select_trip_dropdown(holidays):
    select_trip_dd = document.getElementById("trip")
    select_trip_dd.disabled = False

    for holiday in holidays:
        print(holiday)

        duration = holiday["duration"]
        location = holiday["location"]
        date = holiday["departure_date"]

        holiday_option = document.createElement("option")
        holiday_option.innerHTML = f"Go to {location} on {date} for {duration} days"

        holiday_option.value = holiday["id"]

        select_trip_dd.appendChild(holiday_option)

        











