import geocoder
from geopy.geocoders import Nominatim
import time

GENDER_CHOICE = (
        ('Male', 'Male'),
        ('Female', 'Female'),
)

CHEST_PAIN_CHOICE = (
      ('Typical Angina', 'Typical Angina'),
      ('Atypical Angina', 'Atypical Angina'),
      ('Non-Anginal Pain', 'Non-Anginal Pain'),
      ('Asymptomatic', 'Asymptomatic'),
)

TEST_CHOICES = (
        ('Basic Metabolic Panel', 'Basic Metabolic Panel'),
        ('Comprehensive Metabolic Panel', 'Comprehensive Metabolic Panel'),
        ('Lipid Panel', 'Lipid Panel'),
        ('Thyroid Panel', 'Thyroid Panel'),
)

TIME_SLOTS = [
    ['10AM - 11AM', '10AM - 11AM'],
    ['12PM - 1PM', '12PM - 1PM'],
    ['4PM - 5PM', '4PM - 5PM'],
    ['5PM - 6PM', '5PM - 6PM'],
    ['6:30PM - 7:30PM', '6:30PM - 7:30PM'],
]

chest_pain_type = {
      "Typical Angina" : "Substernal chest discomfort of characteristic quality and duration, Provoked by exertion or emotional stress, Relieved by rest and/ or GTN", 
                 "Atypical Angina" : "Meets two of above mentioned characteristics", 
                 "Non-Anginal Pain" : "Meets one or none of the characteristics"
}

heart_parameters_info = { 
    "Exercise Induced Angina" : "Pain that comes on with exercise, stress, or other things that make the heart work harder."
}

diabetes_parameters_info = {
    "BMI" : "It is defined as the body weight divided by the square of the body height."
}

liver_parameters_info = {
    "Bilirubin" : "It is the waste resulting from the breakdown of red blood cells that the liver filters out.",
    "Alkaline Phosphatase" : "It is an enzyme found in the body that is involved in several bodily processes.",
    "Alamine Aminotransferase" : "Another enzyme found in  the body.",
    "Albumin" : "Albumin is a protein made by your liver. Albumin helps keep fluid in your bloodstream so it doesn't leak into other tissues.",
}

def get_city():
    g = geocoder.ip('me')
    latlngArr = g.latlng
    Latitude = str(latlngArr[0])
    Longitude = str(latlngArr[1])
    geolocator = Nominatim(user_agent="geoapiExercises")
    location = geolocator.reverse(Latitude+","+Longitude)
    address = location.raw['address']
    city = address.get('city', '')
    return city

def slot_split(startTime, endTime) :
    allTimeSlots = [ "8 A.M", "8:30 A.M", "9 A.M", "9:30 A.M", "10 A.M", 
        "10:30 A.M", "11 A.M", "11:30 A.M", "12 P.M", "12:30 P.M", "1 P.M", 
        "1:30 P.M", "2 P.M", "2:30 P.M", "3 P.M", "3:30 P.M", "4 P.M", "4:30 P.M", 
        "5 P.M", "5:30 P.M", "6 P.M", "6:30 P.M", "7 P.M", "7:30 P.M", "8 P.M", 
        "8:30 P.M", "9 P.M", "9:30 P.M", "10 P.M", "10:30 P.M"
    ]

    startTime = str(startTime)
    endTime = str(endTime)

    startIndex = allTimeSlots.index(startTime)
    endIndex = allTimeSlots.index(endTime)

    result = []
    for i in range(startIndex, endIndex) :
        slot = allTimeSlots[i]
        result.append(slot)
    
    return result

def current_milli_time():
    return round(time.time())
