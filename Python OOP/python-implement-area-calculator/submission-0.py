import math

class AreaCalc:
    # TODO: Implement calculate method
    def calculate(self, length, width=None) -> int:
        if width == None:
            area = round(math.pi * length**2,2)
        else:
            area = length * width
        return area
    

    
# Don't modify the following code
calc = AreaCalc()
print(calc.calculate(5))    
print(calc.calculate(4, 6))
