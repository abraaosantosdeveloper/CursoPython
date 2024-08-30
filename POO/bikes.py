class Bike:
    def __init__(self, color, model, year, price,):
        self.color = color
        self.model = model
        self.year = year
        self.price = price
        
orbea = Bike("Red", "Orbea", 2019, 7000)

print(f'''
    Color: {orbea.color}
    Model: {orbea.model}
    Year: {orbea.year}
    Price(USD): US$ {orbea.price}
    
    ''')

