import matplotlib.pyplot as plt

num_of_packets = 0
time = []
time_in_queue = []
index = 0

for line in open("test/tcp-example.tr"):
    if line[0] == '+':
        time_stamp = float(line[line.find(" ") + 1: (line.find(" ", line.find(" ") +1 ))])
        time.append(time_stamp)
        index += 1
        num_of_packets += 1

    if line[0] == '-':
        time_stamp = float(line[line.find(" ") + 1: (line.find(" ", line.find(" ") + 1))])
        time_in_queue.append(time_stamp-time[num_of_packets-index])
        index -= 1

plt.plot(time[0:len(time_in_queue)], time_in_queue)
plt.title("Queing Delay vs. Time")
plt.xlabel("Time")
plt.ylabel("Queing Delay")
plt.show()
