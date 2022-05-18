import sys
import os
import glob
fNAME_only = "only_augustus.hints_supportedbyISOSEQ.gff"
fNAME = "augustus.hints.gff"
oNAME_pep = "augustus.hints.pep.fasta"
oNAME_partial_pep = "augustus.hints.pep.partial.fasta"
# list from bed
geneID_list = []
fpin = open(fNAME_only,'r')
for line in fpin:
    geneID = line.strip('\n').split("\t")[-1]
    geneID_list.append("g"+geneID)



# gff to pep

geneID_pepSeq_dic = {}
fpin= open(fNAME,'r')
fpout = open(oNAME_pep,'w')
iFlag_pep = 0
iCNT_pep = 0
for line in fpin:
    if line[0]=="#":
        if iFlag_pep == 1:
            if not "]" in line:
                pepSeq = line.strip('\n').split("# ")[1]
                tmpline+= pepSeq
            else:# "]" in line:
                pepSeq = line.strip('\n').split("# ")[1].split("]")[0]
                tmpline += pepSeq
                fpout.write(tmpline+"\n")
                geneID_pepSeq_dic.setdefault(geneID,tmpline)
                iFlag_pep = 0

        if len(line)>=10:
            if line[:10]=="# start ge":
                geneID = line.strip().split(" ")[-1]
                fpout.write(">"+geneID+"\n")

            if "[" in line:
                iFlag_pep = 1
                tmpline = ""
                if "]" in line:
                    pepSeq = line.strip('\n').split("[")[1].split("]")[0]
                    tmpline += pepSeq
                    fpout.write(tmpline+"\n")
                    geneID_pepSeq_dic.setdefault(geneID,tmpline)
                    iFlag_pep = 0
                else:
                    pepSeq = line.strip('\n').split("[")[1]
                    tmpline+= pepSeq

fpin.close()
fpout.close()
fpout = open(oNAME_partial_pep,'w')
for geneID in geneID_list:
    fpout_each = open("each/"+geneID+'.fasta','w')
    tmpline = ">"+geneID+'\n'+geneID_pepSeq_dic[geneID]+'\n'
    fpout.write(tmpline)
    fpout_each.write(tmpline)
    fpout_each.close()
fpout.close()

