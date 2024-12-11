import numpy
from scipy import stats
speed = [99,86,87,88,111,86,103,87,94,78,77,85,86]
mean = numpy.mean(speed)
medain = numpy.median(speed(0))
print("Mode of given data is " % (stats.mode(speed)))
print (f"""Mean is: {mean},Median is : {medain}""")



