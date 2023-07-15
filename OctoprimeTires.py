from tire import Tire

class OctoprimeTires(Tire):
    def __init__(self,my_array):
        self.my_array = my_array
        
    def needs_service(self):
        #sum of values in array is greater than or equal to 3
        sum = 0
        for i in range(len(self.my_array)):
            sum += self.my_array[i]
        if sum >= 3:
            return True
        else:
            return False