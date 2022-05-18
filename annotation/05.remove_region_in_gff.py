fNAME = "GCF_009829125.1_Isoseq_fPerMag1.pri_genomic_sorted.gff"
oNAME = "GCF_009829125.1_Isoseq_fPerMag1.pri_genomic_sorted_wo_region.gff"
fpin = open(fNAME,'r')
fpout = open(oNAME,'w')
for line in fpin:
    part = line.split("\t")
    if part[2]=="region":
        pass
    else:
        fpout.write(line)
fpin.close()
fpout.close()
