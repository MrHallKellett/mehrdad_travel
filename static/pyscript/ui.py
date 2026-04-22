from pyscript import document, when

from api import get_request_holidays

from models import Booking


@when("select", "#trip")
def select_holiday(e):    
    # get the rest of the form elements out of the DOM (getElementById)

    # un-disable all of them

    # store which holiday was clicked
    holiday = e.target.innerHTML # text of the dropdown option - (we need to think)

    




    

@when("click", ".search-cta")
async def click_go(e):

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

        select_trip_dd.appendChild(holiday_option)











