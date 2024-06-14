import sys
import numpy as np

from time import *
from glm import ivec2, ivec3

from gdpc import __url__, Editor, Block, geometry
from gdpc.exceptions import InterfaceConnectionError, BuildAreaNotSetError

editor = Editor(buffering=True)
"""
try:
    editor.checkConnection()
except InterfaceConnectionError:
    print(
        f"Error: Could not connect to the GDMC HTTP interface at {editor.host}!\n"
        "To use GDPC, you need to use a \"backend\" that provides the GDMC HTTP interface.\n"
        "For example, by running Minecraft with the GDMC HTTP mod installed.\n"
        f"See {__url__}/README.md for more information."
    )
    sys.exit(1)
"""
def build_copy(x1,y1,z1,x2,y2,z2,filename):#�����copy    
    file=open(filename,'w')#file������
    
    file.write("from gdpc import Editor, Block\n\n")#file��import
    file.write("editor=Editor(buffering=True)\n\n")
    
    file.write(f"def {filename}(x,y,z):\n")#�v���ζ��x
    
    editor.placeBlock((1000,150,1000),Block("minecraft:air"))#air block�ζ��x
    air=editor.getBlock((1000,150,1000))
    
    xxx=-1;yyy=-1;zzz=-1;
    
    if x1<x2 and z1<z2:     #block���i���z��
        for xx in range(x1,x2+1):
            xxx=xxx+1
            yyy=-1
            for yy in range(y1,y2+1):
                yyy=yyy+1
                zzz=-1
                for zz in range(z1,z2+1):
                    zzz=zzz+1
                    block=editor.getBlock((xx,yy,zz))
                    #if block!=air:  #air block��oҕ
                    file.write(f"    editor.placeBlock((x+{xxx},y+{yyy},z+{zzz}),Block(\"{block}\"))\n")
                    print(f"{block}")
    elif x1<x2 and z1>z2:
        for xx in range(x1,x2+1):
            xxx=xxx+1
            yyy=-1
            for yy in range(y1,y2+1):
                yyy=yyy+1
                zzz=-1
                for zz in range(z2,z1+1):
                    zzz=zzz+1
                    block=editor.getBlock((xx,yy,zz))                   
                    #if block!=air:
                    file.write(f"    editor.placeBlock((x+{xxx},y+{yyy},z+{zzz}),Block(\"{block}\"))\n")
                    print(f"{block}")
    elif x1>x2 and z1<z2:
        for xx in range(x2,x1+1):
            xxx=xxx+1
            yyy=-1
            for yy in range(y1,y2+1):
                yyy=yyy+1
                zzz=-1
                for zz in range(z1,z2+1):
                    zzz=zzz+1
                    block=editor.getBlock((xx,yy,zz))
                   # if block!=air:
                    file.write(f"    editor.placeBlock((x+{xxx},y+{yyy},z+{zzz}),Block(\"{block}\"))\n")
                    print(f"{block}")
    elif x1>x2 and z1>z2:
        for xx in range(x2,x1+1):
            xxx=xxx+1
            yyy=-1
            for yy in range(y1,y2+1):
                yyy=yyy+1
                zzz=-1
                for zz in range(z2,z1+1):
                    zzz=zzz+1
                    block=editor.getBlock((xx,yy,zz))
                    #if block!=air:
                    file.write(f"    editor.placeBlock((x+{xxx},y+{yyy},z+{zzz}),Block(\"{block}\"))\n")
                    print(f"{block}")


begin_time = time()
build_copy(92,37,290,93,47,289,"bamboo")#y1<y2, �����ǥե�������(.py��Ҫ��ʤ�)�����ˤ�׷��
end_time = time()
print("run time:", end_time-begin_time)#�r�g��ʾ
