with open("input.txt") as f:
    lines = f.readlines()

order = [int(ele) for ele in lines[0].split(",")]
hashmap = [0 for _ in range(9)]
for i in range(len(order)):
    hashmap[order[i]] += 1

for i in range(256):
    temp = hashmap.pop(0)
    hashmap.append(temp)
    hashmap[6] += temp

print(sum(hashmap))
