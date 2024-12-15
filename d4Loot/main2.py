import matplotlib.pyplot as plt

place = ['helltide','IH','L boss']
score = [23,25,22]

plt.bar(place,score)

# plt.xlabel('แกน x')
# plt.ylabel('แกน y')
plt.title('SCORE WHERE TO FARM')
plt.savefig('static/output3.png')