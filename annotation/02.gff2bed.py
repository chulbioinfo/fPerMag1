import sys
import os
import glob
fNAME= "GCF_009829125.1_Isoseq_fPerMag1.pri_genomic_sorted_wo_region.gff"
flist = glob.glob("./*.gff")
#for fNAME in flist:
if 1==1:
    iCNT_gene = 0
    fpin = open(fNAME,'r')
    oNAME = os.path.basename(fNAME).split(".gff")[0]+".bed"
    fpout = open(oNAME,'w')
    for line in fpin:
        if not line[0]=="#":
            part = line.strip("\n").split("\t")
            nChrom = part[0]
            nSource = part[1]
            nType = part[2]
            nStart = part[3]
            nEnd = part[4]
            if nType == "gene":
                iCNT_gene += 1
                tmpline = nChrom +"\t"+ nStart+"\t"+ nEnd +'\t'+str(iCNT_gene)+"\n"
                fpout.write(tmpline)
    fpin.close()
    fpout.close()
