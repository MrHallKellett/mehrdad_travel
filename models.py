from datetime import date, datetime
from dataclasses import dataclass

@dataclass
class Holiday:  # make sure this matches the database
    id: str
    location: str
    departure_date: date
    duration: int
    outbound_plane_id: str
    return_plane_id: str
    
@dataclass
class Customer:
    forename: str
    surname: str
    id: str
    telephone: str
    

@dataclass
class Booking:
    customer: Customer
    holiday: Holiday

@dataclass
class Flight:
    airline: str
    flight_number: str
    departure_time: datetime
    duration: int

