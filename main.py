import os

line = "Your download is 99% complete and has been for 40 minutes. The last 1% is on a server that fell asleep in 2019."

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(line)
print("chars:", len(line))
