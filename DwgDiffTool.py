import comtypes.client
from comtypes import COMError
from comtypes.client import CreateObject, GetModule, GetActiveObject
import sys

class DWGDiffer:
    def __init__(self): 
        try:
            self.acad = comtypes.client.GetActiveObject("AutoCAD.Application",dynamic=True)
        except Exception:
            self.acad = comtypes.client.CreateObject("AutoCAD.Application",dynamic=True)


    def DWGCompare(self, dwg1, dwg2):
        doc = self.acad.Documents.Open(dwg1)
        doc.SendCommand("-COMPARE %s\n" % dwg2)
        # doc.SendCommand("_COMPAREEXPORT F:/tmp/vs.dwg\n")
        # doc.SendCommand("_COMPARECLOSE\n")

if __name__ == "__main__":
    # dwg1 = "F:/tmp/Drawing1.dwg"
    # dwg2 = "F:/tmp/Drawing1_2.dwg"
    dwg1 = sys.argv[1]
    dwg2 = sys.argv[2]

    print("dwg1 = %s\ndwg2 = %s" % (dwg1, dwg2))

    differ = DWGDiffer()
    differ.DWGCompare(dwg1, dwg2)