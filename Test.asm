DATA1 SEGMENT
VB DB 101B
СРІМЇ DB 'ПРИВЄТ'
DATA1 ENDS

DATA2 SEGMENT
VW DW 407D
VD DD 56FDAH
DATA2 ENDS

ASSUME CS:  CODE, DS: DATA1
CODE SEGMENT
ORG 100H
_START:
STI

PUSH ES
POP AX
PUSH BX
POP CX

POINT:

TEST DI, SI
TEST AX, DX
TEST BL, CL

OR BL, FS: VB[DI]
JZ POINT

SUB AX[SI], BX

RAR AH, 01B
RAR BX, 10
RAR CX, A1H

JZ EXIT

SHR VB[SI], CL

OR AX, VD[SI]

EXIT:
CODE ENDS

END _START

CODE ENDS


