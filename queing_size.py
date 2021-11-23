import matplotlib.pyplot as plt

queue_size = 0
queue_sizes = []
time_stamps = []

for line in open("test/tcp-example.tr"):
    if line[0] == '+':
        queue_size = queue_size + 1
        queue_sizes.append(queue_size)
        time_stamps.append(float(line[line.find(" ") + 1: (line.find(" ", line.find(" ") + 1))]))

    if line[0] == '-':
        queue_size = queue_size - 1
        queue_sizes.append(queue_size)
        time_stamps.append(float(line[line.find(" ") + 1: (line.find(" ", line.find(" ") + 1))]))

plt.plot(time_stamps,queue_sizes)
plt.title("Queing size vs Time")
plt.ylabel("Queing size")
plt.xlabel("Time")
plt.show()
