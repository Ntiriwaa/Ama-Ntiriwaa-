#list of carName and its salePrice
carName ={
    "Tesla":250,
    "Jeep":300,
    "Hyundai":450,
    "Chevrolet":180,
    "Kia":950,
    "Toyota":450,
    "Honda":700,
    "Ford":700,
    "BMW":339,
    "Mercedes-Benz":760,
    "Ferrari":660,
    "Porshe":990,
    "Bentley":554,
    "Subaru":668,
    "Jaguar":654,
    "Mazda":865,
    "Nissan":437,
    "Bugatti":332,
    "Acura":556,
    "Astorn Martin":778,
    "Volkswagen":875,
    "Volvo":667,
    "Mclaren":990,
    "Lincoln":624,
    "Genesis":889,
    "Lotus":990,
    "Diamler":941,
    "Peugot":999,
    "Mini":554,
    "Fiat":225,
    "Pontiac":556}
carBrand =input("input carName").strip()
#check if carBrand in carName
if carBrand in carName:
    print("carName available")
#if carName in carBrand get its price
    carPrice=carName[carBrand]
    print(f"the price of {carBrand} is $ {carPrice}.")
else:
#if carName not in carBrand
    print("sorry,carName unavailable")      
    
    
    
    
    