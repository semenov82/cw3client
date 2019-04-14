import os
f = open('start.sh', 'w')
sessions = os.listdir('./sessions/')
for index in sessions:
    ind = index.replace('.session', '')
    i = 'python3 main.py -p {0} > ./log/{0}.log 2>&1 &'.format(ind)
    print(i)
    f.write(i + '\n')
f.close()
