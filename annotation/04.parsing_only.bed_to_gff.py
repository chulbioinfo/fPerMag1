fNAME_bed = "only_augustus.hints_supportedbyISOSEQ.bed"
fNAME_gff = "augustus.hints.gff"
fNAME_OrthoVen2 = "OrthoVen2_522.list"
oNAME_gff = "only_augustus.hints_supportedbyISOSEQ.bed.gff"

import os
import sys

# make list from bed
fpin = open(fNAME_bed,'r')
geneID_list = []
for line in fpin:
    geneID = "g"+line.strip().split("\t")[-1]
    geneID_list.append(geneID)
fpin.close()

# make dic from OrthoVen2
fpin = open(fNAME_OrthoVen2,'r')
gID_nInfo_dic = {}
for line in fpin:
    part = line.strip("\n").split("\t")
    gID = part[0]
    nInfo = part[1]
    gID_nInfo_dic[gID]=nInfo
fpin.close()

# scan list and write ann
fpin = open(fNAME_gff,'r')
fpout = open(oNAME_gff,'w')
iFlag_geneID = 0
for line in fpin:
    if line[0]=="#":
        if len(line)>=10:
            if line[:10]=="# start ge":
                geneID = line.strip().split(" ")[-1]
                if geneID in geneID_list:
                    iFlag_geneID = 1
            if line[:10]=="# end gene":
                iFlag_geneID = 0
    else:
        if iFlag_geneID == 1:
            part = line.strip().split("\t")
            gID = part[-1]
            if gID in gID_nInfo_dic.keys():
                tmpline = '\t'.join(part[:-1])+"\t"+gID_nInfo_dic[gID]+'\n'
                fpout.write(tmpline)
            else:
                fpout.write(line)
fpin.close()
fpout.close()
