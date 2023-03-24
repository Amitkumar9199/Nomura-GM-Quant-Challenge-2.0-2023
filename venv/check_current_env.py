import sys
import os
import difflib
import pandas as pd
import numpy as np

os.system('pip list > mainPkgs.txt')
with open('mainPkgs.txt','r') as f:
    d = f.readlines()
os.remove('mainPkgs.txt')

pkgs = {x.split()[0] : x.split()[1] for x in d[2:]}

argv = sys.argv
# argv = [1,2,3]
# argv[2] = r'C:\ProdGMQuantChallenge2023\NomuraQuant\virtual env\hello.txt'
# argv[1] = r'C:\ProdGMQuantChallenge2023\NomuraQuant\virtual env\requirements.txt'
req = set(list(pd.read_csv(argv[1], header=None)[0]))
current = set(list(pd.read_csv(argv[2], header=None)[0]))
newcurrent = set()

diff = list()
for pkg in current:
    if pkg.split('==')[0].replace('_','-') in pkgs:
        newcurrent.add(f"{pkg.split('==')[0].replace('_','-')}=={pkgs[pkg.split('==')[0].replace('_','-')]}")
    else:
        diff.append(pkg) 

diff = diff + list(newcurrent.difference(req))
delta = ', '.join(diff)

# exceptions = ['scikit_learn==1.2.2', 'pywinpty==2.0.10']

# updated_delta = [_ for _ in delta if _ not in exceptions]

if len(delta) == 0:
    print("Passed!, Current environment matches with the requirements")
else:
    print(f"Failed! You are using following packages which are incompatible with the requirements.txt: [{delta}], Please remove these, For any clarification please contact gmquantchallenge@nomura.com")
