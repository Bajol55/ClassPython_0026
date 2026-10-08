class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calculate_circumference(self):
        return 2 * (self.length + self.width)
 
     def calculate_area(self):
         return self.length * self.width
 
      def __str__(self):
          return f"rectangle, {self.length} cm long, and {self.width} cm wide"
   
    
    rect = Rectangle(3, 2)
    
    print(rect)
    print(f"Keliling: {rect.calculate_circumference()} cm")
    print(f"Luas: {rect.calculate_area()} cm²")