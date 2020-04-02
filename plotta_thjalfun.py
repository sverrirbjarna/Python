import sys
import matplotlib.pyplot as plt

lines = []
for line in open('results1k'):
    if "avg" in line:
        lines.append(line)

iterations = []
avg_loss = []
rate = []

print('Retrieving data and plotting training loss graph...')
for i in range(len(lines)):
    lineParts = lines[i].split(',')
    #print(lineParts)
    iterations.append(int(lineParts[0].split(':')[0]))
    avg_loss.append(float(lineParts[1].split()[0]))
    rate.append(float(lineParts[2].split()[0]))

fig = plt.figure()
for i in range(0, len(lines)):
    plt.plot(iterations[i:i+2], avg_loss[i:i+2], 'r.-')


plt.xlabel('Batch Number')
plt.ylabel('Avg Loss')
fig.savefig('training_loss_plot.png', dpi=1000)

fig = plt.figure()
for i in range(0, len(lines)):
    plt.plot(iterations[i:i+2], rate[i:i+2], 'b.-')


plt.xlabel('Batch Number')
plt.ylabel('Learning rate')
fig.savefig('training_rate_plot.png', dpi=1000)

print('Done! Plot saved as training_loss_plot.png')