# Great-Circle-Distance-Formula
Great Circle Distance Formula to indicate the distance between the two GPS coordinates

## 1. Summary
Great Circle Distance refers to the distance between two points on the earth's surface (x1, y1), (x2, y2), when two points are considered to be made up of latitude and longitude, the following formula is established: ( * Both latitude and longitude must be replaced in radians from angle, distance results in miles, in km)

## 2. Formula
distance (Unit : miles) = arccos(sin(x1)*sin(x2) + cos(x1)*cos(x2)*cos(y2-y1))

## 3. Miles -> Km Formula
1 mile = 1.60934 km 
so, km_distance = distance * 1.60934

## 4. Suggestion
It would be good to change the above source code to JAVA P/L when determining the distance between the two GPS as a function inside the Android application. In addition, it can be easily implemented in other programming languages.
