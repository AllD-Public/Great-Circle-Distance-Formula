import math

lat1 = float(input('첫 번째 GPS 좌표의 위도를 입력하세요 : '))
lat1 = math.radians(lat1)
lon1 = float(input('첫 번째 GPS 좌표의 경도를 입력하세요 : '))

lat2 = float(input('두 번째 GPS 좌표의 위도를 입력하세요 : '))
lat2 = math.radians(lat2)
lon2 = float(input('두 번째 GPS 좌표의 경도를 입력하세요 : '))

c = math.radians(lon2 - lon1)

dist = 69.1 * (180 / math.pi) * math.acos(math.sin(lat1) * math.sin(lat2) + math.cos(lat1) * math.cos(lat2) * math.cos(c))

print('두 GPS 좌표 사이의 거리는', dist * 1.60934, '(km) 입니다.')
