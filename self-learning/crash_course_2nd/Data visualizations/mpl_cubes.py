import matplotlib.pyplot as plt

y_val = range(1, 101)
x_val = [y ** 3 for y in y_val]

fig, ax = plt.subplots()

ax.scatter(y_val, x_val, linewidth=3, c=y_val, cmap=plt.cm.Reds)

plt.show()
