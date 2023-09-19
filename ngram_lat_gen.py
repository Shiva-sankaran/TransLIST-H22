import pandas as pd
import random
from tqdm import tqdm
# python flat_main_bigram.py --status test --test_model Trained_Translist_H22 --data_create no
r = 1 #fraction of lattice nodes per sentence

def create_lattice(sent):
    lattices = []
    chunks = sent.split()
    a = 0
    for chunk in chunks:
        l = len(chunk)
        for j in range(l):
            if j+1 < l : lattices.append((a+j,a+j+1,sent[a+j:a+j+2]))
            if j+2 < l : lattices.append((a+j,a+j+2,sent[a+j:a+j+3]))
            if j+3 < l : lattices.append((a+j,a+j+3,sent[a+j:a+j+4]))
        a = a + l + 1
    return lattices

df = pd.read_csv("H22-data/zero-shot_collection3_test.csv") #overall_test.csv
inp_sents = df['input'].tolist()
dcs_ids = df['UID'].tolist()
for i in tqdm(range(len(inp_sents))):
    sent = inp_sents[i]
    tuples = create_lattice(sent)
    if r < 1:
      tuples = random.sample(tuples,int(r*len(tuples)))
    dcs_id = dcs_ids[i]
    with open(f'H22_lattice_files/{dcs_id}.lat','w') as g:
        g.write('start,end,word\n')
        for t in tuples:
            g.write(f'{t[0]},{t[1]},{t[2]}\n')

## sent tarpaNo_bRMhaNo_balyo_vAtahRdroganASanaH
# lattice = [(0,1,'ta'),(0,2,'tar'),(0,3,'tarp'),(1,2,'ar'),(1,3,'arp'),(1,4,'arpa'),...]
