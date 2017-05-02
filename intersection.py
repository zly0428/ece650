import math
import numpy as np
import sys
# 点
class Point(object):

    def __init__(self, x, y):
        self.x, self.y = x, y

    def __repr__(self):
        return "(%d,%d)"%(self.x,self.y)
    def p_print(self):
        return "(%d,%d)"%(self.x,self.y)

# 向量
class Vector(object):

    def __init__(self, start_point, end_point):
        self.start_point, self.end_point = start_point, end_point
        self.x = end_point.x - start_point.x
        self.y = end_point.y - start_point.y

ZERO = 1e-9

def negative(vector):
    """取反"""
    return Vector(vector.end_point, vector.start_point)

def vector_product(vectorA, vectorB):
    '''计算 x_1 * y_2 - x_2 * y_1'''
    return vectorA.x * vectorB.y - vectorB.x * vectorA.y

def is_intersected(A, B, C, D):
    '''A, B, C, D 为 Point 类型'''
    AC = Vector(A, C)
    AD = Vector(A, D)
    BC = Vector(B, C)
    BD = Vector(B, D)
    CA = negative(AC)
    CB = negative(BC)
    DA = negative(AD)
    DB = negative(BD)
    # print(vector_product(AC, AD) * vector_product(BC, BD))
    # print(vector_product(CA, CB) * vector_product(DA, DB))
    if ((vector_product(AC, AD) * vector_product(BC, BD) != 0) \
        or (vector_product(CA, CB) * vector_product(DA, DB) != 0)):
    	return (vector_product(AC, AD) * vector_product(BC, BD) <= ZERO) \
        	and (vector_product(CA, CB) * vector_product(DA, DB) <= ZERO)
    else:
    	s1 = math.sqrt(np.square(A.x-B.x)+np.square(A.y-B.y));
    	s2 = math.sqrt(np.square(C.x-D.x)+np.square(C.y-D.y));
    	s3 = math.sqrt(np.square(A.x-D.x)+np.square(A.y-D.y));
    	# print(s1,s2,s3)
    	return s1+s2 >= s3

def findIntersectionPoint(A,B,C,D):
    k1,b1 = findKandB(A,B);
    k2,b2 = findKandB(C,D);
    xp = (b2-b1)/(k1-k2);
    yp = k1*xp + b1;
    intersectionPoint = Point(xp,yp);
    return intersectionPoint

def findKandB(A,B):
	k = (A.y-B.y)/(A.x-B.x);
	b = B.y - B.x*k;
	return k,b

def calculateIntersectionPoint(A,B,C,D):
	if A.x == B.x:
		if C.y == D.y:
			xp,yp = A.x,C.y;
		else:
			k,b = findKandB(C,D);
			xp = A.x;
			yp = k*xp + b
	elif A.y == B.y:
		if C.x == D.x:
			xp,yp = C.x,A.y;
		else:
			k,b = findKandB(C,D);
			xp = C.x;
			yp = k*xp + b
	else:
		xp,yp = findIntersectionPoint(A,B,C,D);
	return xp,yp


# if __name__ == __main__:
#     main()
##########        

# def a():
# 	print('hello world!')

# # a();

# while True:
# 	try:
# 		s = input()
# 	except:
# 		break
		
		
