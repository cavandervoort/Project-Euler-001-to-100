# Problem 48
# Self powers

sumSeries = 0
mod = 10 ** 10
for n in range(1,1001):
    sumSeries += n ** n

sumSeriesStr = str(sumSeries)

print(sumSeriesStr[-10:])
