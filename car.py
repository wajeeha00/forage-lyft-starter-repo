from abc import ABC, abstractmethod
from engine import Engine
from battery import Battery 

class Car():
    battery = Battery()
    engine = Engine()

    def __init__(self, battery, engine):
        self.battery = battery
        self.engine = engine
    
    def needs_service(self):
        return self.battery.needs_service() or self.engine.needs_service()
    
    

# class Car(ABC):
#     def __init__(self, last_service_date):
#         self.last_service_date = last_service_date

#     @abstractmethod
#     def needs_service(self):
#         pass
