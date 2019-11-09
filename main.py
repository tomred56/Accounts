import wx

import accounting_gui as gui
import data_structures as db

categories = db.Categories()
sub_categories = db.SubCategories()
details = db.Details()
companies = db.Companies()
accounts = db.Accounts()
transactions = db.Transactions()
rules = db.Rules()
cards = db.Cards()
contacts = db.Contacts()
# record_type = (institutions, accounts, transactions)
app = wx.App(0)
frame0 = gui.FrameForCategory(None, categories, sub_categories, details)
frame0.Show()
# frame1 = gui.FrameWithForms(None, record_type, title='Financial Account Manager')
# frame1.Show()
app.MainLoop()
