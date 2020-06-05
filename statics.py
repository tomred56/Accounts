from datetime import datetime

NOW: datetime = datetime(datetime.today().year, datetime.today().month, datetime.today().day)
START_DATE: datetime = datetime(2019, 1, 1)
END_DATE: datetime = datetime(2050, 12, 31)

CX_DISCONNECTED = 0
CX_CONNECTED = 1
CX_FAILED = 2
TX_CLEAN = 0
TX_EDIT = 1
TX_ADD_PEER = 2
TX_ADD_CHILD = 4
TX_CHANGED = 8
TX_MOVING = 16
TX_EMPTY = 32
TX_UNUSED3 = 64
TX_UNUSED4 = 128
TX_RESET = 256

def main():
    pass


if __name__ == '__main__':
    main()
