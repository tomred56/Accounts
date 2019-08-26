import shelve

import wx

import accounting_gui as gui
import data_structures as db

# SHELF = 'Accounting_DB'
SHELF = 'Test_DB'

database = shelve.open(SHELF, writeback=True)
institutions = db.Institutions(database)
accounts = db.Accounts(database)
transactions = db.Transactions(database)
record_type = (institutions, accounts, transactions)
app = wx.App(0)
frame = gui.FrameWithForms(None, record_type, title='Financial Account Manager')
frame.Show()
app.MainLoop()
database.close()
