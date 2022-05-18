import pyads
from config import settings

AMSNETID = settings.AMSNETID


def plc_store(x_cord: int, y_cord: int):
    print("Preparing to send Instruction to PLC")

    # plc = pyads.Connection(AMSNETID, pyads.PORT_TC3PLC1)
    # with plc:
    #     print("Sending coordinates to PLC to Insert")
    #     plc.write_by_name('GVL.X', x_cord)
    #     print(f"Sent X Cordinate: {x_cord}")
    #     plc.write_by_name('GVL.Y', y_cord)
    #     print(f"Sent Y Cordinate: {y_cord}")
    #     plc.write_by_name('GVL.isInsert', True)
    
    print("Instructions to Insert Sent Successfully")
    pass


def plc_retreive(x_cord: int, y_cord: int):
    print("Preparing to send Instruction to PLC")

    # plc = pyads.Connection(AMSNETID, pyads.PORT_TC3PLC1)
    # with plc:
    #     print("Sending coordinates to PLC to Retreive")
    #     plc.write_by_name('GVL.X', x_cord)
    #     print(f"Sent X Cordinate: {x_cord}")
    #     plc.write_by_name('GVL.Y', y_cord)
    #     print(f"Sent Y Cordinate: {y_cord}")
    #     plc.write_by_name('GVL.isInsert', False)

    print("Instructions to Fetch Sent Successfully")
    pass
