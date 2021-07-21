# readhalopars
Use hash table to read MSI halo particles

## Install

``` sh
git clone https://github.com/POFK/readhalopars.git
cd readhalopars
python setup.py install
```

Before you use it, you should set `ulimit -s unlimited` in your terminal or `bashrc` first.


## Example
``` 
import numpy as np
from rhp.rhp import ReadGroupParticleClass

BaseDir = "/data/inspur_disk02/Simulations/Millennium/"
Gnum=[4386162,3831945,2162498,2117511,2117472,1838697,1838697] # number of particle 
rank = np.arange(len(Gnum)) # group rank
rgpc = ReadGroupParticleClass(BaseDir = BaseDir)
for i in range(len(Gnum)):
    pos, centre, mb = rgpc.readgroup(Gnum[i], rank[i])
    print(centre)
    print(mb)
```
Here the returned values `pos`, `centre`, `mb` indicate group particles position, group centre position and mostboundid. 
