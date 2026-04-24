from pyodide.http import pyfetch


async def post_request_booking(booking):
    pass

async def get_request_holidays(location):

    location = location.replace(" ", "%20")

    response = await pyfetch(f"/api/holidays?location={location}")   
    data = await response.json()
    
    return data
