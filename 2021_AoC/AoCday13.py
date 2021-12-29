import numpy as np

with open("/home/curt/Downloads/input13.txt", newline="\n") as f:
    raw_data = f.read()
    
with open("/home/curt/Downloads/input13.txt", newline="\n") as f:
    raw_data = f.read()
    
a,_,b = raw_data.partition('\n\n')
marks = [[int(s) for s in l.split(',')] for l in a.split("\n")]
instructions = [(l[11:12],int(l[13:])) for l in b[:-1].split("\n")]
x_max, y_max = [max(x) for x in zip(*marks)]
transperancy = np.zeros((y_max+2, x_max+4))
for x,y in marks:
    transperancy[y,x]=1

print(transperancy.shape)
print(instructions)



t = transperancy.copy()
for d, n in instructions[:]:
    if d == 'y':
        t_1 = t[:n, :]
        t_2 = t[n+1:, :]
        t_2 = t_2[::-1,::]
    elif d=='x':
        t_1 = t[:, :n]
        t_2 = t[:, n+1:]
        t_2 = t_2[::,::-1]
    print(t.shape, n, d, t_1.shape, t_2.shape)
    lgst = [max(n) for n in zip(*(t_1.shape, t_2.shape))]
    #t_1 = np.pad(t_1, ((0,(lgst[0]-t_1.shape[0])), (0,(lgst[1]-t_1.shape[1]))), mode='constant')
    #t_2 = np.pad(t_2, ((0,(lgst[0]-t_2.shape[0])), (0,(lgst[1]-t_2.shape[1]))), mode='constant')
    t = t_1+t_2
    print((t!=0).sum())

for l in t:
    for c in l:
        print(f'{"#" if c else "."}', end='')
    print()


