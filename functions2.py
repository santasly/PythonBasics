def Calc_average(list):

    total=sum(list)
    count=len(list)
    average=total/count
    return average

list = [10, 12, 45, 42, 32, 45, 78]
answer= Calc_average(list)
print("the average is ", answer)

