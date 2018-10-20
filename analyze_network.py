import networkx as nx
import matplotlib.pyplot as plt
import networkx.drawing as nd
import random
from scipy import stats

wedges_file = 'net.wedges'

G = nx.read_weighted_edgelist(wedges_file,'%',None,None,int)

print('orginal nodes # =', G.number_of_nodes())
print('orginal edges # =', G.number_of_edges())

percent = 10
#onn = G.number_of_nodes()
nnn = int(G.number_of_nodes()*percent/100);

H = nx.Graph();

n = random.choice(list(G.nodes))
nbr = random.choice(list(G[n].keys()))
while H.number_of_nodes() < nnn:
    H.add_weighted_edges_from([(n, nbr, G[n][nbr]['weight'])])
    n = random.choice(list(H.nodes))
    nbr = random.choice(list(G[n].keys()))

'''
nd = {}
for i in range(nnn):    
    n = random.randint(1, onn)
    while n in nd:
        n = random.randint(1, onn)
    nd[n] = n
l = list(nd.keys())    



#print(G.adj)
for n in l:
    for nbr in G[n]:
        if nbr in l:
            #print (n, ' ', nbr, ' ', G[n][nbr]['weight'])
            #print ( G.edges[G.nodes(n)][nbr]['weight'] )
            H.add_weighted_edges_from([(n, nbr, G[n][nbr]['weight'])])
            #print(G.edges(n))
    #for e in G.edges(n):
'''
        
print('tested nodes # =', H.number_of_nodes())
print('tested edges # =', H.number_of_edges())

#Degree
samp1 = []
samp2 = []

dG = nx.degree(G)
dH = nx.degree(H)

for i in dG:
    samp1.append(i[0])
for i in dH:
    samp2.append(i[0])

sd = stats.ks_2samp(samp1, samp2)

print('degree KS test result:\t\t statistic=',sd[0],' pvalue=', sd[1])

#Betweennes
samp1 = []
samp2 = []

bcG = nx.betweenness_centrality(G)
bcH = nx.betweenness_centrality(H)

samp1 = list(bcG.values())
samp2 = list(bcH.values())

sb = stats.ks_2samp(samp1, samp2)

print('betweenness KS test result:\t statistic=',sb[0],' pvalue=', sb[1])

#Closeness
samp1 = []
samp2 = []

ccG = nx.closeness_centrality(G)
ccH = nx.closeness_centrality(H)

samp1 = list(ccG.values())
samp2 = list(ccH.values())

sb = stats.ks_2samp(samp1, samp2)

print('closeness KS test result:\t statistic=',sb[0],' pvalue=', sb[1])

#PageRank
samp1 = []
samp2 = []

prG = nx.pagerank(G)
prH = nx.pagerank(H)

samp1 = list(prG.values())
samp2 = list(prH.values())

spr = stats.ks_2samp(samp1, samp2)

print('pagerank KS test result:\t statistic=',spr[0],' pvalue=', spr[1])

'''
plt.subplot(121)
nx.draw(G, with_labels=True)
plt.subplot(122)
nx.draw(H, with_labels=True)
plt.show()
'''
