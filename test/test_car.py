import unittest
from datetime import datetime

from WilloughhbyEngine import WilloughbyEngine
from CapuletEngine import CapuletEngine
from SternmanEngine import SternmanEngine
from NubbinBattery import NubbinBattery
from SpindlerBattery import SpindlerBattery
from CarFactory import CarFactory

class TestCarFactory(unittest.TestCase):
    def test_create_calliope(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)
        current_mileage = 0
        last_service_mileage = 0

        car_factory = CarFactory(last_service_date, today, current_mileage, last_service_mileage, False)
        car = car_factory.create_calliope()

        self.assertIsInstance(car.engine, CapuletEngine)
        self.assertIsInstance(car.battery, SpindlerBattery)
    
    def test_create_glissade(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)
        current_mileage = 0
        last_service_mileage = 0

        car_factory = CarFactory(last_service_date, today, current_mileage, last_service_mileage, False)
        car = car_factory.create_glissade()

        self.assertIsInstance(car.engine, WilloughbyEngine)
        self.assertIsInstance(car.battery, SpindlerBattery)
    
    def test_create_palindrome(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)
        warning_light_is_on = False

        car_factory = CarFactory(last_service_date, today, 0, 0, warning_light_is_on)
        car = car_factory.create_palindrome()

        self.assertIsInstance(car.engine, SternmanEngine)
        self.assertIsInstance(car.battery, NubbinBattery)
    
    def test_create_rorschach(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)
        current_mileage = 0
        last_service_mileage = 0

        car_factory = CarFactory(last_service_date, today, current_mileage, last_service_mileage, False)
        car = car_factory.create_rorschach()

        self.assertIsInstance(car.engine, WilloughbyEngine)
        self.assertIsInstance(car.battery, NubbinBattery)
    
    def test_create_thover(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)
        warning_light_is_on = False

        car_factory = CarFactory(last_service_date, today, 0, 0, warning_light_is_on)
        car = car_factory.create_thover()

        self.assertIsInstance(car.engine, CapuletEngine)
        self.assertIsInstance(car.battery, NubbinBattery)
    
if __name__ == '__main__':
    unittest.main()


