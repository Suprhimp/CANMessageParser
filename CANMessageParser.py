"""
CAN Message Parser
author : Suprhmip
date : 2021-09-14

Code for generate CAN headerfile from CAN message(excel file)

"""

import os

dataLoc = input("type the file location and file name!\n")
f = open(dataLoc,'r')
lines = f.readlines()

outputFile = open(os.path.dirname(dataLoc)+"/GenerateCANMessage.h",'w')

index = 0
SettingVal = ""
for line in lines:
    line = line.split(",")
    if index == 0:
        SettingVal = line[1]
        index +=1
        continue
    elif index == 1:
        index +=1
        continue
    

    MessageName = line[0]
    i=1
    signalName=[]
    signalType=[]
    signalSize=[]
    while True:
        try:
            if line[i] != "":
                signalName.append(line[i])
                signalType.append(line[i+1])
                signalSize.append(line[i+2])
                i+=3
            else:
                break
        except:
            break
    outputFile.write("//generated code by CANMessageParser\n\n")

    if SettingVal == "STM":
        outputFile.write("typedef union{\n")
        outputFile.write("\tuint8_t Txdata[8];\n")
        outputFile.write("\tuint8_t Rxdata[8];\n")
        outputFile.write("\tstruct{\n")
    
    else: 
        outputFile.write("typedef union{\n")
        outputFile.write("\tuint32_t Txdata[2];\n")
        outputFile.write("\tuint32_t Rxdata[2];\n")
        outputFile.write("\tstruct{\n")
    
    for i,name in enumerate(signalName):
        outputFile.write("\t\t"+signalType[i]+" "+name+" : "+signalSize[i].strip()+';\n')
    outputFile.write("\t}")
    if SettingVal == "STM":
        outputFile.write("__attribute__((aligned(1),packed))")
    outputFile.write(" B;\n\n")
    outputFile.write("}"+MessageName+"_t;\n\n")
