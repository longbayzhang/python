
import pdb
################################################
def compare_num(a, b):
    return 1 <= a <= b <= 10

a = 3
b = 1
print compare_num(a, b)

################################################
def validate_null(str, list, dict):
    return str and list and dict

name = 'Tim'
langs = ['AS3', 'Lua', 'C']
info = {'name': 'Tim', 'sex': 'Male', 'age': 23}
print validate_null(name, langs, info)

################################################
def concat_str(strList):
    return ' '.join(strList)

strList = ["Python", "is", "good"]
print concat_str(strList)

################################################
def reverse_str(str):
    return str[::-1]

print reverse_str("abcdefg")

################################################
def operate_list(numList):
    from operator import mul
    print sum(numList)
    print max(numList)
    print min(numList)
    print reduce(mul, numList, 1)

numList = [1, 2, 3, 4, 5]
operate_list(numList)

################################################
def create_list():
    return [x * x for x in range(10) if x % 3 == 0]

print create_list()

################################################
def dict_default(dict1):
    dict1['workage'] = dict1.get('workage', 0) + 1
    return dict1

dict1 = {'name': 'Tim', 'age': 23}
print dict_default(dict1)

################################################
def for_else():
    for x in xrange(1, 5):
        pdb.set_trace()
        if x == 5:
            print 'find 5'
            break
    else:
        print 'can not find 5!'

for_else()

print list(xrange(1, 10))

################################################
def metadata_func(a):
    b = 2 if a > 2 else 1
    return b

a = 3
print metadata_func(a)

################################################
def enumerate_func(array):
    return dict((i, e) for i, e in enumerate(array, 0))

array = ['one', 'two', 'three', 'four', 'five']
print enumerate_func(array)

################################################
def zip_func(keys, values):
    return dict(zip(keys, values))

keys = ['Name', 'Sex', 'Age']
values = ['Tim', 'Male', 23]
print zip_func(keys, values)

################################################
def star_argv(*argv):
    return argv

print star_argv('c', 'java', 'python')

################################################
# if __name__ == '__main__':
#     main()