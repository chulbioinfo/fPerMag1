fNAME = "GCF_009829125.1_fPerMag1.pri_genomic.gff"
oNAME = "GCF_009829125.1_fPerMag1.pri_genomic_wo_region.gff"
fpin = open(fNAME,'r')
fpout = open(oNAME,'w')
for line in fpin:
    if not line[0]=="#":
        part = line.split("\t")
        if part[2]=="region":
            pass
        else:
            fpout.write(line)
fpin.close()
fpout.close()
