import matplotlib.pyplot as plt 
fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
langs = ['Huy', 'Han', 'Hung']
Score = [9,8,7]

ax.plot(langs, Score)
plt.show()