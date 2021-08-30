from time import perf_counter_ns
import simples as sp
import mtrhead as mt

with open("data.csv") as file:
    data = [line.strip() for line in file]

data = list(map(int, data))
resutl1 = 0
result2 = 0
print('\n\nanalise de %d valores\n\n'%(len(data)))
for i in range(50):
    start1 = perf_counter_ns()
    primo_sp = sp.resolve_simples(data)
    finish1 = perf_counter_ns()

    start2 = perf_counter_ns()
    primo_mt = mt.resolve_trhread(data)
    finish2 = perf_counter_ns()

    resutl1 += (finish1-start1)/1000000
    result2 += (finish2-start2)/1000000
print('Tempo médio simples        > Tempo médio threads')
print(f'{resutl1/50}s     >    {result2/50} ms')
