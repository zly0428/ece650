import intersection as IS
import sys
import math
import numpy as np

class Vertex(object):

    def __init__(self, street, vertexPoint):
        self.street = street;
        self.vertexPoint = vertexPoint;

class Street(object):
	def __init__(self,streetName,streetPoints):
		self.streetName = streetName;
		self.streetPoints = streetPoints;
		# self.streetEdge = streetEdge;

class edge(object):
	def __init__(self,streetName,vertexPoint):
		self.streetName = streetName;
		self.vertexPoint = vertexPoint;

def a(str,list):
	return Street(str,list)

def c(streetList,str,list):
	for s in streetList:
		if s.streetName == str:
			s.streetPoints = list;

def r(streetList,str):
	for s in streetList:
		if s.streetName == str:
			streetList.remove(s);

def g():
	# 把所有点放在一个list里
	vertexPointSet = [];
	pointsAll = [];
	for s in streetList:
		p = s.streetPoints;
		for i in range(0,len(p)):
			pointsAll.append(p[i]);

	# 产生交点，放在vertexPointSet里
	for i,s in enumerate(streetList):
		if i == (len(streetList) -1):break;
		points = s.streetPoints;
		for i in range(0,len(points)-1):
			v = findVertex(points[i],points[i+1],streetList[i+1])
			for i in range(0,len(v)):
				vertexPointSet.append(v[i]);



def findVertex(A,B,street):
	vex = [];
	points = street.streetPoints
	for i in range(0,len(points)-1):
		if IS.is_intersected(A, B, points[i], points[i+1]):
			p = IS.findIntersectionPoint(A,B,C,D);
			vex.append(p);
	return vex


def getKs(streetList):
	ks = [];
	for s in streetList:
		points = s.streetPoints;
		plenth = len(points);
		for i in range(0,plenth-1):
			k = calK(points[i],points[i+1]);
			ks.append(k);
	return ks

def isConnected(A,B):
	return calDistance(A,B) 



def calDistance(A,B):
	return math.sqrt(np.square(A.x - B.x) + np.square(A.y - B.y))

def calK(A,B):
	if A.x == B.x:
		return 1000000;
	else:
		return (A.y - B.y)/(A.x - B.x)


def point_str2class(str):
	str = str[1:-1];
	a,b = str.split(',');
	x,y = float(a),float(b);
	return IS.Point(x,y);

def readInput(s):
	s_list = s.split(' ');
	command = s_list[0];
	str = s_list[1];
	pl = s_list[2:];
	pointList = [];
	for pointStr in pl:
		pointList.append(point_str2class(pointStr));


	return command,str,pointList

streetList = [];
# while True:
	
# 	s = input();
# 	command,str,pointList = readInput(s);
# 	if command == 'a':
# 		streetList.append(a(str,pointList));
# 	elif command == 'c':
# 		c(streetList,str,pointList);
# 	elif command == 'r':
# 		r(streetList,str);

# 	for s in streetList:
# 		print(s.streetName,s.streetPoints)

s1 = 'a "weber" (2,-1) (2,2) (5,5) (5,6) (3,8)'
s2 = 'a "king" (4,2) (4,8)'
s3 = 'a "daven" (1,4) (5,8)'
ss = [];
ss.append(s1);
ss.append(s2);
ss.append(s3);
for i in range(0,len(ss)):
	command,str,pointList = readInput(ss[i]);
	if command == 'a':
		streetList.append(a(str,pointList));
	elif command == 'c':
		c(streetList,str,pointList);
	elif command == 'r':
		r(streetList,str);

	for s in streetList:
		p = s.streetPoints
		print(p[0].p_print());
s = streetList[0];
print(s.streetName);
a = s.streetPoints;
for p in a:
	print(p.p_print())
# print(a.p_print())

# a = findVertex(A,B,streetList[1])

# vertexPointSet=[];
# for i,s in enumerate(streetList):
# 	if i == (len(streetList) -1):break;
# 	points = s.streetPoints;
# 	for i in range(0,len(points)-1):
# 		v = findVertex(points[i],points[i+1],streetList[i+1])
# 		for i in range(0,len(v)):
# 			vertexPointSet.append(v[i]);
## 1 test of intersection

# A = IS.Point(2,4)
# B = IS.Point(2,0)
# C = IS.Point(0,0)
# D = IS.Point(5,2)
# print(IS.is_intersected(A,B,C,D));
# if IS.is_intersected(A,B,C,D):
# 	xpp,ypp = IS.calculateIntersectionPoint(A,B,C,D)
# 	print(xpp,ypp)


## 2 test func of a()

# streetList = [];
# s = 'a "king" (1,2) (2,3) (3,4)';
# command,str,pointList = readInput(s);
# streetList.append(a(str,pointList));

# s = 'a "hello" (1,2) (2,3) (3,4) (0,0) (3,2)';
# command,str,pointList = readInput(s);
# streetList.append(a(str,pointList));

# for s in streetList:
# 	print(s.streetName)
# 	print(s.streetPoints)

## 3 test func of c()

# s = 'c "hello" (-1,-1) (-2,-2)';
# command,str,pointList = readInput(s);
# if command == 'c':
# 	c(streetList,str,pointList);

# for s in streetList:
# 	print(s.streetName)
# 	print(s.streetPoints)

## 4 test func of r()

# s = 'r "hello" (-1,-1) (-2,-2)';
# command,str,pointList = readInput(s);
# if command == 'r':
# 	r(streetList,str);

# for s in streetList:
# 	print(s.streetName)
# 	print(s.streetPoints)

	

