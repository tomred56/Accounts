import wx

import accounting_gui as gui


def main():
    app = wx.App()
    mainframe = gui.BaseWindow(parent=None)
    mainframe.Show()

    app.MainLoop()


if __name__ == '__main__':
    main()
