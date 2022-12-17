import numpy as np

class var():
    x=[[1],[2],[3],[4],[5]]
    y=[[1],[2],[3],[4],[5]]

def mean_x():
    return np.mean(var.x)


def mean_y():
    return np.mean(var.y)


def x_y_mean_sum():
    arr_x_y_sum_res=[]
    for itr in range(0,len(var.x)):
        arr_x_y_sum_res.append((var.x[itr]-mean_x())*(var.y[itr]-mean_y()))

    return sum(arr_x_y_sum_res)


def square_x_min_meanx():
    sum_ = 0
    for x_item in var.x:
        sum_ = sum_ + ((x_item - mean_x())**2)

    return sum_


def b1():
    b1=x_y_mean_sum()/square_x_min_meanx()

    return b1


def b0():
    result=mean_y()- b1()*mean_x()
    return result


def predict(x):
    y=b0()+b1()*x
    return y

if __name__=="__main__":
    x=predict(x=8)
    print(x)
