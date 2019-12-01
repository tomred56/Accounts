import wx

import accounting_gui as gui
import data_structures as db


def main():
    data = {
            'categories': db.Categories(),
            'subcategories': db.SubCategories(),
            'details': db.Details(),
            'suppliers': db.Suppliers(),
            'accounts': db.Accounts(),
            'subaccounts': db.SubAccounts(),
            'transactions': db.Transactions(),
            'rules': db.Rules(),
            'cards': db.Cards(),
            'contacts': db.Contacts()
    }
    app = wx.App()
    mainframe = gui.BaseWindow(data, parent=None, style=wx.DEFAULT_FRAME_STYLE)
    mainframe.Show()
    
    app.MainLoop()


if __name__ == '__main__':
    main()
