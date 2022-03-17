import statistics

def calculate_area(x,y):
    z = statistics.NormalDist(x,y)
    prob = z.cdf(y) - z.cdf(x)
    print(prob)

calculate_area(15000,25000)

def calc_var_95(x,y):
    mid = (x+y)/2
    print(mid)

calc_var_95(15000,25000)
