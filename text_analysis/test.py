import matplotlib.pyplot as plt
import random
import pandas as pd
res= []
list = [i for i in range(1,36)]

for i in range(0,1000000):
    x = random.sample(list,5)
    res += x
df = pd.DataFrame(res)
count = df[0].value_counts()
plt.bar(count.index,count.values)
plt.show()
# plt.bar(range(len(Counter(res))), Counter(res))
# plt.show()


