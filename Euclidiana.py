def distance(a,b):
    return (  (a[0]-b[0])**2 +(a[1]-b[1])**2)**0.5

def getDistance(p):
   limite=len(p)
   j=1
   distanceBox=[]
   for i in p:
       for j in p:
           if i==j:
               break
           distanceBox.append(distance(i,j))

   return distanceBox

def order(distanceBox):
   minorDistance=distanceBox[0]
   for i in distanceBox:
       for j in distanceBox:
        if minorDistance>j:
            minorDistance=j
   return minorDistance

def solution(p):
   distanceBox=getDistance(p)
   print(distanceBox)
   return order(distanceBox)

points=[
[19,-15], 
[4,9], 
[13,-7], 
[-3,-1], 
[-10,30]] 
a=solution(points)
print(a)