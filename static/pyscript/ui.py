from pyscript import document, when

from api import get_request_holidays

@when("click", ".search-cta")
async def click_go(e):

    location_input = document.getElementById("dest")
    location = location_input.value

    holidays = await get_request_holidays(location)
    print(holidays)






