from car import Car
from engine import Engine
from battery import Battery
from SternmanEngine import SternmanEngine
from WilloughhbyEngine import WilloughbyEngine
from CapuletEngine import CapuletEngine
from SpindlerBattery import SpindlerBattery
from NubbinBattery import NubbinBattery




class CarFactory():
    def __init__(self, last_service_date,current_date,current_mileage,last_service_mileage,warning_light_on):
        self.last_service_date = last_service_date
        self.current_date = current_date
        self.current_mileage = current_mileage
        self.last_service_mileage = last_service_mileage
        self.warning_light_on = warning_light_on


    def create_calliope(self):
        engine = CapuletEngine(self.last_service_mileage,self.current_mileage)
        battery = SpindlerBattery(self.last_service_date,self.current_date)
        return Car(battery,engine)
    
    def create_glissade(self):
        engine = WilloughbyEngine(self.last_service_mileage,self.current_mileage)
        battery = SpindlerBattery(self.last_service_date,self.current_date)
        return Car(battery,engine)
    
    def create_palindrome(self):
        engine = SternmanEngine(self.warning_light_on,)
        battery = NubbinBattery(self.last_service_date,self.current_date)
        return Car(battery,engine)
    def create_rorschach(self):
        engine = WilloughbyEngine(self.last_service_mileage,self.current_mileage)
        battery = NubbinBattery(self.last_service_date,self.current_date)
        return Car(battery,engine)
    def create_thover(self):
        engine = CapuletEngine(self.warning_light_on,)
        battery = NubbinBattery(self.last_service_date,self.current_date)
        return Car(battery,engine)
    