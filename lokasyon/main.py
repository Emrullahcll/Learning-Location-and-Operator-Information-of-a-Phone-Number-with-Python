import phonenumbers

number1 = '+526623952379'
number2 = '+905516587213'

from phonenumbers import geocoder
number = phonenumbers.parse(number2)
print(geocoder.description_for_number(number,'tr'))

from phonenumbers import carrier
number = phonenumbers.parse(number2)
print(carrier.name_for_number(number,'tr'))

from phonenumbers import timezone
number = phonenumbers.parse(number2)
print(timezone.time_zones_for_number(number,))