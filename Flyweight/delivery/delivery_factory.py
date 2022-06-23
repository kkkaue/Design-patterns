from delivery_flyweight_interface import DeliveryFlyweight
from delivery_types import DeliveryLocationData
from delivery_location import DeliveryLocation

class DeliveryFactory:
    locations = {str : DeliveryLocation}

    def createId(self, street = DeliveryLocationData.street, city = DeliveryLocationData.city) -> str:
        values = street + "_" +  city
        values_str = str(values)
        values_str = values_str.replace(" ", "")
        return values_str.lower()

    def makeLocation(self, street = DeliveryLocationData.street, city = DeliveryLocationData.city) -> DeliveryFlyweight:
        key = self.createId(street, city)
        if key in self.locations:
            return self.locations[key]
        self.locations[key] = DeliveryLocation(street, city)
        return self.locations[key]

    def getLocations(self) -> locations:
        return self.locations
