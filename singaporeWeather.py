import requests
import json

city = "Singapore"
apikey = "2a60cb94620bef1cf52e542cf90df279"
lang = "kr"

api = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={apikey}&lang={lang}&units=metric"
# we input f in front of the address and change the variable names

print(api)

result = requests.get(api)
print(result.text)

data = json.loads(result.text)

#print(type(result.text))
# print(type(data))

print(data["name"], "의 날씨입니다.")
print("날씨는", data["weather"][0]["description"] , "입니다." )
print("날씨는", data["main"]["temp"], "입니다")
print("체감 온도는", data["main"]["feels_like"], "입니다.")
print("The lowest temperature is  ",data["main"]["temp_min"])
print("The highest temperature is ",data["main"]["temp_max"])
print("The humidity is:  ",data["main"]["humidity"])
print("The air pressure is ",data["main"]["pressure"])
print("The direction of wind is:  ",data["wind"]["deg"])
print("The velocity of the wind is: ",data["wind"]["speed"])

