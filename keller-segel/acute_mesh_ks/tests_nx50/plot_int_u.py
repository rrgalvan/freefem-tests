import matplotlib.pyplot as plt
import numpy as np
import sys

print(sys.argv)
if len(sys.argv)<2:
    print(f"Usage: {sys.argv[0]} <txt_data_file>")
    sys.exit(1)
filename = sys.argv[1]
m_float=np.loadtxt(filename)

plt.title(filename)
plt.plot(m_float,'bo')
plt.ylabel('Time iteration')
plt.xlabel('int_Th(u)')

output_file = filename.split('.')[0] + ".png"
print("Saving to file: " + output_file)

plt.savefig(output_file)
