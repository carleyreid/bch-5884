#!/usr/bin/env python3
#carleyreid

import sys
import math


#open and read pdb file
pdbname=sys.argv[1]
f=open(pdbname)
lines=f.readlines()
f.close()

#assign dictionary for atom masses (from PT)
records=[]
dictionarymass={"H":1.008,"C":12.011,"N":14.007,"O":15.999,"P":30.974,"S":32.06,"MG":24.305}

#define columns of pdb to information
for line in lines:
    atom=str(line[0:4])
    serialnumber=str(line[8:11])
    name=str(line[14:16])
    residue=str(line[18:20])
    chainID=str(line[22])
    residueseqnumber=int(line[24:26])
    x=float(line[33:38])
    y=float(line[40:46])
    z=float(line[49:54])
    occupancy=float(line[57:60])
    tempfactor=float(line[62:66])
    element=line[78].strip()
    mass=dictionarymass[element]
    records.append([atom,serialnumber,name,residue,chainID,residueseqnumber,x,y,z,occupancy,tempfactor,element,mass])


#I keep getting an "index out of range" error for line 22 but I've made sure everything is lined up with the pdb file
