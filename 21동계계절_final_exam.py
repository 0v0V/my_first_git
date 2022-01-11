### [ANSWER START]

class MyString():

    def __init__(self , in_val="*", second_val=None):
        if isinstance(in_val, str):
            self.val = in_val
            self.original = in_val
        elif isinstance(in_val, int):
            self.original = in_val
            self.val = str(in_val)
        elif isinstance(in_val, float):
            self.original = in_val
            self.val = str(in_val)
        elif isinstance(in_val, list):
            self.original = in_val
            self.val = "*"

    def __str__(self):
        return str(self.val)

    def set(self,in_val="*"):
        if isinstance(in_val, str):
            self.val = in_val
            self.original = in_val
        elif isinstance(in_val, int):
            self.original = in_val
            self.val = str(in_val)
        elif isinstance(in_val, float):
            self.original = in_val
            self.val = str(in_val)
        elif isinstance(in_val, list):
            self.original = in_val
            self.val = "*"
        return self.val
    
    def get(self):
        return self.val

    def get_original(self):
        return self.original

    def get_dictionary(self):
        return {self.val : self.original}

    def __add__(self, other):
        if isinstance(other, MyString):
            result = MyString(self.val + other.val)
            self.original = MyString()
            return result
        else:
            return MyString(self.original)
# STEP 6
    def __mul__(self, other):
        if isinstance(other, int):
            new_mystring = self.val * other
            new_original_str_mystring = self.val + '*' + str(other)
        else:
            new_mystring = self.val
            new_original_str_mystring = self.val
        return MyString(new_original_str_mystring, new_mystring)
"""
    def __mul__(self,other):
        if isinstance(other,int):
            result = MyString(self.val * other)
            other_val = f"*{other}"
            MyString(str(self.original)) + MyString(other_val)
        elif isinstance(other, str):
            result = MyString(self.original)
        return result
"""
   

### [ANSWER END]

#
# 시험 문제
# 
# 답안은 위의 [ANSWER START]와 [ANSWER END] 사이에 작성함
# 아래의 STEP 들을 수행하여 RESULTS의 결과를 출력하는 MyString 클래스를 개발함
# 수행 결과는 아래 RESULTS와 동일해야 함 (결과값, 대소문자, 철자, 빈공간 등 모든 정보가 동일해야 함)
#

''' STEP.1 : 20 points
'''

myStr = MyString()

varTmp = myStr.set('argv_str')
print('#A01:${}$==>>${}$'.format(varTmp, type(varTmp)))
print('#A02:${}$'.format(type(myStr)))
print('#A03:${}$==>>${}$'.format(myStr.get(), type(myStr.get())))
print('#A04:${}$==>>${}$'.format(myStr.get_original(), type(myStr.get_original())))

varTmp = myStr.set(1234)
print('#B01:${}$==>>${}$'.format(varTmp, type(varTmp)))
print('#B02:${}$'.format(type(myStr)))
print('#B03:${}$==>>${}$'.format(myStr.get(), type(myStr.get())))
print('#B04:${}$==>>${}$'.format(myStr.get_original(), type(myStr.get_original())))

varTmp = myStr.set(1234.5678)
print('#C01:${}$==>>${}$'.format(varTmp, type(varTmp)))
print('#C02:${}$'.format(type(myStr)))
print('#C03:${}$==>>${}$'.format(myStr.get(), type(myStr.get())))
print('#C04:${}$==>>${}$'.format(myStr.get_original(), type(myStr.get_original())))

varTmp = myStr.set([1,2,3,4])
print('#C01:${}$==>>${}$'.format(varTmp, type(varTmp)))
print('#C02:${}$'.format(type(myStr)))
print('#C03:${}$==>>${}$'.format(myStr.get(), type(myStr.get())))
print('#C04:${}$==>>${}$'.format(myStr.get_original(), type(myStr.get_original())))

varTmp = myStr.set()
print('#D01:${}$==>>${}$'.format(varTmp, type(varTmp)))
print('#D02:${}$'.format(type(myStr)))
print('#D03:${}$==>>${}$'.format(myStr.get(), type(myStr.get())))
print('#D04:${}$==>>${}$'.format(myStr.get_original(), type(myStr.get_original())))

''' STEP.2 : 10 points
'''

myStr = MyString('argv_str')
print('#E01:${}$'.format(type(myStr)))
print('#E02:${}$==>>${}$'.format(myStr.get(), type(myStr.get())))
print('#E03:${}$==>>${}$'.format(myStr.get_original(), type(myStr.get_original())))

myStr = MyString(1234)
print('#F01:${}$'.format(type(myStr)))
print('#F02:${}$==>>${}$'.format(myStr.get(), type(myStr.get())))
print('#F03:${}$==>>${}$'.format(myStr.get_original(), type(myStr.get_original())))

myStr = MyString(1234.5678)
print('#G01:${}$'.format(type(myStr)))
print('#G02:${}$==>>${}$'.format(myStr.get(), type(myStr.get())))
print('#G03:${}$==>>${}$'.format(myStr.get_original(), type(myStr.get_original())))

myStr = MyString([1,2,3,4])
print('#H01:${}$'.format(type(myStr)))
print('#H02:${}$==>>${}$'.format(myStr.get(), type(myStr.get())))
print('#H03:${}$==>>${}$'.format(myStr.get_original(), type(myStr.get_original())))

myStr = MyString()
print('#I01:${}$'.format(type(myStr)))
print('#I02:${}$==>>${}$'.format(myStr.get(), type(myStr.get())))
print('#I03:${}$==>>${}$'.format(myStr.get_original(), type(myStr.get_original())))

''' STEP.3 : 10 points
'''

myStr = MyString(1234)
print('#J01:${}$==>>${}$'.format(myStr, type(myStr)))
print('#J02:${}$==>>${}$'.format(myStr.get(), type(myStr.get())))
print('#J03:${}$==>>${}$'.format(myStr.get_original(), type(myStr.get_original())))

myStr = MyString('str#0')
print('#K01:${}$==>>${}$'.format(myStr, type(myStr)))
print('#K02:${}$==>>${}$'.format(myStr.get(), type(myStr.get())))
print('#K03:${}$==>>${}$'.format(myStr.get_original(), type(myStr.get_original())))

''' STEP.4 : 10 points
'''

myStr = MyString(1234)
print('#L01:${}$==>>${}$'.format(myStr.get_dictionary(), type(myStr.get_dictionary())))

myStr = MyString('str#0')
print('#M01:${}$==>>${}$'.format(myStr.get_dictionary(), type(myStr.get_dictionary())))


''' STEP.5 : 15 points
'''

myStr1 = MyString(1234)
myStr2 = MyString('str#0')
myStr3 = myStr1 + myStr2
print('#N01:${}$'.format(type(myStr3)))
print('#N02:${}$==>>${}$'.format(myStr3.get(), type(myStr3.get())))
print('#N03:${}$==>>${}$'.format(myStr3.get_original(), type(myStr3.get_original())))

myStr1 = MyString(1234)
myStr2 = 'str#0'
myStr3 = myStr1 + myStr2
print('#O01:${}$'.format(type(myStr3)))
print('#O02:${}$==>>${}$'.format(myStr3.get(), type(myStr3.get())))
print('#O03:${}$==>>${}$'.format(myStr3.get_original(), type(myStr3.get_original())))

''' STEP.6 : 15 points
'''

myStr1 = MyString(1234)
myStr2 = myStr1 * 3
print('#P01:${}$'.format(type(myStr2)))
print('#P02:${}$==>>${}$'.format(myStr2.get(), type(myStr2.get())))
print('#P03:${}$==>>${}$'.format(myStr2.get_original(), type(myStr2.get_original())))


myStr1 = MyString('01210')
myStr2 = myStr1 * 4
print('#Q01:${}$'.format(type(myStr2)))
print('#Q02:${}$==>>${}$'.format(myStr2.get(), type(myStr2.get())))
print('#Q03:${}$==>>${}$'.format(myStr2.get_original(), type(myStr2.get_original())))

myStr1 = MyString(1234)
myStr2 = myStr1 * '3'
print('#R01:${}$'.format(type(myStr2)))
print('#R02:${}$==>>${}$'.format(myStr2.get(), type(myStr2.get())))
print('#R03:${}$==>>${}$'.format(myStr2.get_original(), type(myStr2.get_original())))

myStr1 = MyString('01210')
myStr2 = myStr1 * '4'
print('#S01:${}$'.format(type(myStr2)))
print('#S02:${}$==>>${}$'.format(myStr2.get(), type(myStr2.get())))
print('#S03:${}$==>>${}$'.format(myStr2.get_original(), type(myStr2.get_original())))

''' RESULTS

#A01:$argv_str$==>>$<class 'str'>$
#A02:$<class '__main__.MyString'>$
#A03:$argv_str$==>>$<class 'str'>$
#A04:$argv_str$==>>$<class 'str'>$
#B01:$1234$==>>$<class 'str'>$
#B02:$<class '__main__.MyString'>$
#B03:$1234$==>>$<class 'str'>$
#B04:$1234$==>>$<class 'int'>$
#C01:$1234.5678$==>>$<class 'str'>$
#C02:$<class '__main__.MyString'>$
#C03:$1234.5678$==>>$<class 'str'>$
#C04:$1234.5678$==>>$<class 'float'>$
#C01:$*$==>>$<class 'str'>$
#C02:$<class '__main__.MyString'>$
#C03:$*$==>>$<class 'str'>$
#C04:$[1, 2, 3, 4]$==>>$<class 'list'>$
#D01:$*$==>>$<class 'str'>$
#D02:$<class '__main__.MyString'>$
#D03:$*$==>>$<class 'str'>$
#D04:$*$==>>$<class 'str'>$
#E01:$<class '__main__.MyString'>$
#E02:$argv_str$==>>$<class 'str'>$
#E03:$argv_str$==>>$<class 'str'>$
#F01:$<class '__main__.MyString'>$
#F02:$1234$==>>$<class 'str'>$
#F03:$1234$==>>$<class 'int'>$
#G01:$<class '__main__.MyString'>$
#G02:$1234.5678$==>>$<class 'str'>$
#G03:$1234.5678$==>>$<class 'float'>$
#H01:$<class '__main__.MyString'>$
#H02:$*$==>>$<class 'str'>$
#H03:$[1, 2, 3, 4]$==>>$<class 'list'>$
#I01:$<class '__main__.MyString'>$
#I02:$*$==>>$<class 'str'>$
#I03:$*$==>>$<class 'str'>$
#J01:$1234$==>>$<class '__main__.MyString'>$
#J02:$1234$==>>$<class 'str'>$
#J03:$1234$==>>$<class 'int'>$
#K01:$str#0$==>>$<class '__main__.MyString'>$
#K02:$str#0$==>>$<class 'str'>$
#K03:$str#0$==>>$<class 'str'>$
#L01:${'1234': 1234}$==>>$<class 'dict'>$
#M01:${'str#0': 'str#0'}$==>>$<class 'dict'>$
#N01:$<class '__main__.MyString'>$
#N02:$1234str#0$==>>$<class 'str'>$
#N03:$1234str#0$==>>$<class 'str'>$
#O01:$<class '__main__.MyString'>$
#O02:$1234$==>>$<class 'str'>$
#O03:$1234$==>>$<class 'int'>$
#P01:$<class '__main__.MyString'>$
#P02:$123412341234$==>>$<class 'str'>$
#P03:$1234*3$==>>$<class 'str'>$
#Q01:$<class '__main__.MyString'>$
#Q02:$01210012100121001210$==>>$<class 'str'>$
#Q03:$01210*4$==>>$<class 'str'>$
#R01:$<class '__main__.MyString'>$
#R02:$1234$==>>$<class 'str'>$
#R03:$1234$==>>$<class 'int'>$
#S01:$<class '__main__.MyString'>$
#S02:$01210$==>>$<class 'str'>$
#S03:$01210$==>>$<class 'str'>$
'''