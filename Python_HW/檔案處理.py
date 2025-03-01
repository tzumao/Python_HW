f=open("Cow.txt")
m,n=map(int,f.readline().split())
vertex_set=[set()for i in range(m)]
g=[0]*3
for i in range(m):
    x,y,z=map(float,f.readline().split())    
    g[0]+=x
    g[1]+=y
    g[2]+=z
print(g[0]/m,g[1]/m,g[2]/m)#done
for i in range(m):
    v1,v2,v3=map(int,f.readline().split())
    vertex_set[v1].add(v2)
    vertex_set[v1].add(v3)
    vertex_set[v2].add(v1)
    vertex_set[v2].add(v3)
    vertex_set[v3].add(v1)
    vertex_set[v3].add(v2)
maxnum=max(len(s) for s in vertex_set)
dist=[0]*(maxnum+1)
for i in range(m):
    dist[len(vertex_set[i])]+=1
print(dist)