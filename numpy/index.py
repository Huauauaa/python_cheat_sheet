import numpy as np

# a = np.arange(6)
# a2 = a[np.newaxis, :]
# print(a2.shape)

# t1 = np.loadtxt(
#     'data/index.csv',
#     encoding='unicode_escape',
#     dtype=str,
#     delimiter=",",
# )

table_num = np.loadtxt('data/num.csv', dtype=np.int64, delimiter=',')


print(table_num)
