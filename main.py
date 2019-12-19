import wx

import accounting_gui as gui
import data_structures as db


def main():
    data = {
            'categories': [db.Categories(), gui.Categories],
            'subcategories': [db.SubCategories(), gui.SubCategories],
            'details': [db.Details(), gui.Details],
            'suppliers': [db.Suppliers(), gui.Suppliers],
            'accounts': [db.Accounts(), gui.Accounts],
            'subaccounts': [db.SubAccounts(), gui.SubAccounts],
            'transactions': [db.Transactions(), gui.Transactions],
            'rules': [db.Rules(), gui.Rules],
            'cards': [db.Cards(), gui.Cards],
            'contacts': [db.Contacts(), gui.Contacts]
    }
    app = wx.App()
    #    mainframe = gui.BaseWindow(data, parent=None, style=wx.DEFAULT_FRAME_STYLE)
    mainframe = gui.BaseWindow(parent=None)
    mainframe.Show()

    app.MainLoop()


if __name__ == '__main__':
    main()
