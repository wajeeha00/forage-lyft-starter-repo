from abc import ABC, abstractmethod
from engine import Engine
from battery import Battery 
from tire import Tire   

class Car():
    battery = Battery()
    engine = Engine()
    tire = Tire()

    def __init__(self, battery, engine, tire):
        self.battery = battery
        self.engine = engine
        self.tire = tire
    
    def needs_service(self):
        return self.battery.needs_service() or self.engine.needs_service() or self.tire.needs_service()
    
