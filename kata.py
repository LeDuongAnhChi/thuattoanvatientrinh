import textwrap
import re
import sys

def delSpace(arr):
    sentence = re.sub(r"\s+", "", arr, flags=re.UNICODE)
    return sentence

def splitto6(XOR_48bits):
	"""split 48 bits into 6 bits each """
	list_of_6bits = textwrap.wrap(XOR_48bits,6)
	return list_of_6bits

def takeFirst(str):

	result = str[0] + str[-1]
	return result

def takeMid(str):
	result = str[1:5]
	return result

def bitoDe(bi):
	decimal = int(bi,2)
	return decimal

def detoBi(de):
	binary4bits = bin(de)[2:].zfill(4)
	return binary4bits

def permutation(str):
    # result3 =[]
    result4=""
    for i in range(len(str)):
        result1 = bitoDe(takeFirst(str[i]));
        result2 = bitoDe(takeMid(str[i]))
        sbox_value = sbox[result1][result2]
        resu = detoBi(sbox_value)
        # result3.append(resu)
        for j in range(len(resu)):
            result4 +=resu[j]

    return result4

def addtobit(a,c):
	# c =[]
    h = 0;
    d = [3, 7, 11, 15, 19, 23, 27]
    for i in range(len(a)):
        if len(c) == 0:
            c.insert(0, a[-1]);
            h = h + 1;
        if i in d:
            h = h + 1
            c.insert(h, a[i])
            h = h + 1
            c.insert(h, a[i + 1])
            h = h + 1
            c.insert(h, a[i])
            h = h + 1
        elif i == 31:
            c.insert(h, a[i]);
            h = h + 1
            c.insert(h, a[0])
        else:
            c.insert(h, a[i]);
            h = h + 1;


def tron1(a,k):
    result =""
    for i in range(len(a)):
        # num = int(a[i])^int(k[i])
        if a[i] == k[i]:
            result += '0'
        else:
            result += '1'

    return result

sbox= [
[14,4,13,1,2,15,11,8,3,10,6,12,5,9,0,7],
[0,15,7,4,14,2,13,1,10,6,12,11,9,5,3,8],
[4,1,14,8,13,6,2,11,15,12,9,7,3,10,5,0],
[15,12,8,2,4,9,1,7,5,11,3,14,10,0,6,13]
]


r ='1111 0000 1010 0101 1111 0000 1010 0101 0000 0000 1111 1111 1010 0101 0000 0000'
k ='1100 1000 1111 1111 0000 0000  1100 1000 1111 1111 0000 0000'
h ='1111 0000 1010 0101 1111 0000 1010 0101'




# print(r1)
# print(r1[38])
# print(r2)
# print(r2[1])

# def Thanos(arr,k):
#
#     arrLeft =arr[0:39]
#     arrRight = arr[40:]
#     k1=delSpace(k)
#     arrLeft1 =delSpace(arrLeft)
#     arrRight1 =delSpace(arrRight)
#
#     right =[]
#     tobit = addtobit(arrRight1,right)
#
#     result1 = tron1(right,k1)
#
#     result2 = splitto6(result1)
#     result3 = permutation(result2)
#     # print("result 2")
#     # print(result2)
#     result4 = tron1(result3,arrLeft1)
#     result5 =''.join([arrRight1,result4])
#     return result5


def longtivity(arr):
    result =[]
    for i in range(3,len(arr)-4,4):
        result.append(i);

    return result

def printList(arr):
    long = longtivity(arr);
    result =''
    for i in range(len(arr)):
        if i in long:
            result += arr[i]
            result += ' '
        else:
            result += arr[i]
    return result

def Thanos1(arr,k):

    arrLeft =arr[0:39]
    arrRight = arr[40:]
    # print("Left is: ")
    # print(arrLeft)
    # print("Right is: ")
    # print(arrRight)
    # print("Key is: ")
    # print(k)
    k1=delSpace(k)

    arrLeft1 =delSpace(arrLeft)
    arrRight1 =delSpace(arrRight)

    right =[]
    tobit = addtobit(arrRight1,right)
    # print("right to bit")
    # print(right)
    result1 = tron1(right,k1)
    # print("result 1 is: ")
    # print(printList(result1))

    result2 = splitto6(result1)
    # print("split to 6 bit")
    # print(result2)
    result3 = permutation(result2)
    # print("match with sbox")
    # print(printList(result3))
    # print("result 2")
    # print(result2)
    result4 = tron1(result3,arrLeft1)
    # print("match with left")
    # print(result4)
    result5 =''.join([arrRight1,result4])
    return result5

arr='1111 0000 1010 0101 1111 0000 1010 0101 0000 0000 1111 1111 1010 0101 0000 0000'
k='1100 1000 1111 1111 0000 0000  1100 1000 1111 1111 0000 0000'


cuoi = Thanos1(sys.argv[1],sys.argv[2])
print("output")
print(printList(cuoi))
# a1 = "00000000111111111010010100000000"
# c = []
# addtobit(a1,c)
# print(c)
# print(len(c))
# print(c[1]==a1[0])


sys.stdout.flush()
