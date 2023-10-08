Program:
def summation(test_tup):
    test= list(test_tup)
    count= 0
    for i in test:
            count += 1
    return count
test_tup = {5,20,7,3,6}
print("sum of digits is : ",summation(test_tup))

output:
sum of digits is :  5
