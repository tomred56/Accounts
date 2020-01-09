# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Oct 26 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.adv
import wx.dataview
import wx.grid
import wx.lib.masked
import wx.xrc

ID_EXIT = 1000


###########################################################################
## Class MainFrame
###########################################################################

class MainFrame(wx.Frame):
    
    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=u"Manage My Accounts", pos=wx.DefaultPosition,
                          size=wx.Size(-1, -1), style=wx.DEFAULT_FRAME_STYLE | wx.BORDER_THEME | wx.TAB_TRAVERSAL)
        
        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)
        self.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_WINDOWTEXT))
        self.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_MENU))
        
        self.main_menu = wx.MenuBar(0)
        self.file_menu = wx.Menu()
        self.exit = wx.MenuItem(self.file_menu, ID_EXIT, u"Exit" + u"\t" + u"alt-x", wx.EmptyString, wx.ITEM_NORMAL)
        self.file_menu.Append(self.exit)
        
        self.main_menu.Append(self.file_menu, u"File")
        
        self.tables_menu = wx.Menu()
        self.suppliers = wx.MenuItem(self.tables_menu, wx.ID_ANY, u"Suppliers", wx.EmptyString, wx.ITEM_RADIO)
        self.tables_menu.Append(self.suppliers)
        
        self.contacts = wx.MenuItem(self.tables_menu, wx.ID_ANY, u"Contacts", wx.EmptyString, wx.ITEM_RADIO)
        self.tables_menu.Append(self.contacts)
        
        self.accounts = wx.MenuItem(self.tables_menu, wx.ID_ANY, u"Accounts", wx.EmptyString, wx.ITEM_RADIO)
        self.tables_menu.Append(self.accounts)
        
        self.subaccounts = wx.MenuItem(self.tables_menu, wx.ID_ANY, u"SubAccounts", wx.EmptyString, wx.ITEM_RADIO)
        self.tables_menu.Append(self.subaccounts)
        
        self.transactions = wx.MenuItem(self.tables_menu, wx.ID_ANY, u"Transactions", wx.EmptyString, wx.ITEM_RADIO)
        self.tables_menu.Append(self.transactions)
        
        self.rules = wx.MenuItem(self.tables_menu, wx.ID_ANY, u"Rules", wx.EmptyString, wx.ITEM_RADIO)
        self.tables_menu.Append(self.rules)
        
        self.cards = wx.MenuItem(self.tables_menu, wx.ID_ANY, u"Cards", wx.EmptyString, wx.ITEM_RADIO)
        self.tables_menu.Append(self.cards)
        
        self.categories = wx.MenuItem(self.tables_menu, wx.ID_ANY, u"Categories", wx.EmptyString, wx.ITEM_RADIO)
        self.tables_menu.Append(self.categories)
        
        self.subcategories = wx.MenuItem(self.tables_menu, wx.ID_ANY, u"SubCategories", wx.EmptyString, wx.ITEM_RADIO)
        self.tables_menu.Append(self.subcategories)
        
        self.details = wx.MenuItem(self.tables_menu, wx.ID_ANY, u"Details", wx.EmptyString, wx.ITEM_RADIO)
        self.tables_menu.Append(self.details)
        
        self.main_menu.Append(self.tables_menu, u"Tables")
        
        self.SetMenuBar(self.main_menu)
        
        self.main_sizer = wx.BoxSizer(wx.VERTICAL)
        
        self.p_summary = wx.StaticText(self, wx.ID_ANY, u"Summary", wx.DefaultPosition, wx.DefaultSize,
                                       wx.ALIGN_LEFT | wx.BORDER_SIMPLE)
        self.p_summary.Wrap(-1)
        
        self.p_summary.SetFont(
            wx.Font(11, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial"))
        self.p_summary.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_WINDOWTEXT))
        self.p_summary.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_ACTIVECAPTION))
        
        self.main_sizer.Add(self.p_summary, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL | wx.EXPAND, 5)
        
        self.summary = wx.BoxSizer(wx.VERTICAL)
        
        self.main_sizer.Add(self.summary, 0, wx.ALIGN_LEFT, 5)
        
        self.p_header = wx.StaticText(self, wx.ID_ANY, u"Table: ", wx.DefaultPosition, wx.DefaultSize,
                                      wx.ALIGN_LEFT | wx.BORDER_SIMPLE)
        self.p_header.Wrap(-1)
        
        self.p_header.SetFont(
            wx.Font(11, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial"))
        self.p_header.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_ACTIVECAPTION))
        
        self.main_sizer.Add(self.p_header, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL | wx.EXPAND, 5)
        
        self.p_notebook = wx.Notebook(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0)
        self.tab_accounts = wx.Panel(self.p_notebook, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        self.bSizer_top1 = wx.BoxSizer(wx.VERTICAL)
        
        rows1 = wx.BoxSizer(wx.VERTICAL)
        
        self.m_grid11 = wx.grid.Grid(self.tab_accounts, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0)
        
        # Grid
        self.m_grid11.CreateGrid(0, 0)
        self.m_grid11.EnableEditing(False)
        self.m_grid11.EnableGridLines(True)
        self.m_grid11.EnableDragGridSize(False)
        self.m_grid11.SetMargins(0, 0)
        
        # Columns
        self.m_grid11.AutoSizeColumns()
        self.m_grid11.EnableDragColMove(False)
        self.m_grid11.EnableDragColSize(True)
        self.m_grid11.SetColLabelSize(0)
        self.m_grid11.SetColLabelAlignment(wx.ALIGN_CENTER, wx.ALIGN_CENTER)
        
        # Rows
        self.m_grid11.AutoSizeRows()
        self.m_grid11.EnableDragRowSize(True)
        self.m_grid11.SetRowLabelSize(0)
        self.m_grid11.SetRowLabelAlignment(wx.ALIGN_CENTER, wx.ALIGN_CENTER)
        
        # Label Appearance
        
        # Cell Defaults
        self.m_grid11.SetDefaultCellAlignment(wx.ALIGN_LEFT, wx.ALIGN_TOP)
        rows1.Add(self.m_grid11, 0, wx.ALL, 5)
        
        self.bSizer_top1.Add(rows1, 1, wx.EXPAND, 5)
        
        fgSizer21 = wx.FlexGridSizer(0, 2, 0, 0)
        fgSizer21.AddGrowableCol(1)
        fgSizer21.SetFlexibleDirection(wx.HORIZONTAL)
        fgSizer21.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_NONE)
        
        self.m_staticText61 = wx.StaticText(self.tab_accounts, wx.ID_ANY, u"Financial Institution", wx.DefaultPosition,
                                            wx.DefaultSize, 0)
        self.m_staticText61.Wrap(-1)
        
        fgSizer21.Add(self.m_staticText61, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_LEFT | wx.ALL, 5)
        
        p_parentChoices = [u"Unknown"]
        self.p_parent = wx.ComboBox(self.tab_accounts, wx.ID_ANY, u"Combo!", wx.DefaultPosition, wx.DefaultSize,
                                    p_parentChoices, wx.CB_DROPDOWN | wx.CB_READONLY, wx.DefaultValidator, u"parent")
        self.p_parent.SetSelection(0)
        fgSizer21.Add(self.p_parent, 1, wx.ALL | wx.EXPAND, 5)
        
        self.m_staticText12 = wx.StaticText(self.tab_accounts, wx.ID_ANY, u"Account Name", wx.DefaultPosition,
                                            wx.DefaultSize, 0)
        self.m_staticText12.Wrap(-1)
        
        fgSizer21.Add(self.m_staticText12, 0, wx.ALL | wx.EXPAND, 5)
        
        self.p_name1 = wx.TextCtrl(self.tab_accounts, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(-1, -1), 0)
        self.p_name1.SetMaxLength(80)
        fgSizer21.Add(self.p_name1, 1, wx.ALL | wx.EXPAND, 5)
        
        self.m_staticText111 = wx.StaticText(self.tab_accounts, wx.ID_ANY, u"Account Description", wx.DefaultPosition,
                                             wx.DefaultSize, 0)
        self.m_staticText111.Wrap(-1)
        
        fgSizer21.Add(self.m_staticText111, 0, wx.ALL | wx.EXPAND, 5)
        
        self.p_description = wx.TextCtrl(self.tab_accounts, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                         wx.Size(-1, -1), 0)
        self.p_description.SetMaxLength(80)
        fgSizer21.Add(self.p_description, 1, wx.ALL | wx.EXPAND, 5)
        
        self.bSizer_top1.Add(fgSizer21, 0, wx.EXPAND | wx.LEFT | wx.RIGHT, 5)
        
        self.m_staticline511 = wx.StaticLine(self.tab_accounts, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                             wx.LI_HORIZONTAL)
        self.bSizer_top1.Add(self.m_staticline511, 0, wx.EXPAND, 5)
        
        bSizer_panels1 = wx.BoxSizer(wx.HORIZONTAL)
        
        fgSizer141 = wx.FlexGridSizer(0, 2, 0, 0)
        fgSizer141.AddGrowableCol(1)
        fgSizer141.SetFlexibleDirection(wx.BOTH)
        fgSizer141.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_NONE)
        
        self.m_staticText551 = wx.StaticText(self.tab_accounts, wx.ID_ANY, u"Sort Code", wx.DefaultPosition,
                                             wx.DefaultSize, wx.ALIGN_LEFT)
        self.m_staticText551.Wrap(-1)
        
        fgSizer141.Add(self.m_staticText551, 0, wx.ALL | wx.EXPAND, 5)
        
        self.p_sort_code = wx.lib.masked.TextCtrl(self, wx.ID_ANY, u"00-00-00", wx.DefaultPosition, wx.DefaultSize, 0,
                                                  mask=u"##-##-##")
        self.p_sort_code.SetMaxLength(8)
        
        self.p_sort_code.SetFont(
            wx.Font(wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL,
                    False, wx.EmptyString))
        self.p_sort_code.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_WINDOW))
        
        fgSizer141.Add(self.p_sort_code, 0, wx.ALL, 5)
        
        self.m_staticText701 = wx.StaticText(self.tab_accounts, wx.ID_ANY, u"Account Number", wx.DefaultPosition,
                                             wx.DefaultSize, 0)
        self.m_staticText701.Wrap(-1)
        
        fgSizer141.Add(self.m_staticText701, 0, wx.ALL, 5)
        
        self.p_account_no = wx.TextCtrl(self.tab_accounts, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                        wx.DefaultSize, 0)
        self.p_account_no.SetMaxLength(8)
        fgSizer141.Add(self.p_account_no, 1, wx.ALL, 5)
        
        self.m_staticText74 = wx.StaticText(self.tab_accounts, wx.ID_ANY, u"Initial Value", wx.DefaultPosition,
                                            wx.DefaultSize, 0)
        self.m_staticText74.Wrap(-1)
        
        fgSizer141.Add(self.m_staticText74, 0, wx.ALL, 5)
        
        self.p_initial = wx.SpinCtrlDouble(self.tab_accounts, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                           wx.DefaultSize, wx.ALIGN_RIGHT | wx.SP_ARROW_KEYS, -1e+06, 1e+06, 0, 0.01)
        self.p_initial.SetDigits(2)
        fgSizer141.Add(self.p_initial, 0, wx.ALL, 5)
        
        bSizer_panels1.Add(fgSizer141, 0, wx.ALL, 5)
        
        self.m_staticline321 = wx.StaticLine(self.tab_accounts, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                             wx.LI_VERTICAL)
        bSizer_panels1.Add(self.m_staticline321, 0, wx.EXPAND | wx.LEFT | wx.RIGHT, 5)
        
        bSizer491 = wx.BoxSizer(wx.VERTICAL)
        
        fgSizer311 = wx.FlexGridSizer(0, 2, 0, 0)
        fgSizer311.AddGrowableCol(1)
        fgSizer311.SetFlexibleDirection(wx.BOTH)
        fgSizer311.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_ALL)
        
        self.m_staticText71 = wx.StaticText(self.tab_accounts, wx.ID_ANY, u"Account Holder", wx.DefaultPosition,
                                            wx.DefaultSize, 0)
        self.m_staticText71.Wrap(-1)
        
        fgSizer311.Add(self.m_staticText71, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)
        
        p_holderChoices = [u"Dermot", u"Fenella", u"Joint", u"Other"]
        self.p_holder = wx.ComboBox(self.tab_accounts, wx.ID_ANY, u"Dermot", wx.DefaultPosition, wx.DefaultSize,
                                    p_holderChoices, wx.CB_DROPDOWN | wx.CB_READONLY)
        self.p_holder.SetSelection(0)
        fgSizer311.Add(self.p_holder, 1, wx.ALL | wx.EXPAND, 5)
        
        self.m_staticText731 = wx.StaticText(self.tab_accounts, wx.ID_ANY, u"Account Type", wx.DefaultPosition,
                                             wx.DefaultSize, 0)
        self.m_staticText731.Wrap(-1)
        
        fgSizer311.Add(self.m_staticText731, 0, wx.ALL, 5)
        
        p_typeChoices = [u"Current", u"Savings", u"ISA", u"Credit Card", u"Loan", u"Mortgage", u"Cash", u"Shares",
                         u"Current", u"Insurance"]
        self.p_type = wx.ComboBox(self.tab_accounts, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize,
                                  p_typeChoices, wx.CB_DROPDOWN | wx.CB_READONLY)
        self.p_type.SetSelection(10)
        fgSizer311.Add(self.p_type, 0, wx.ALL | wx.EXPAND, 5)
        
        bSizer491.Add(fgSizer311, 0, wx.ALL, 5)
        
        bSizer491.Add((0, 0), 1, wx.EXPAND, 5)
        
        fgSizer231 = wx.FlexGridSizer(0, 3, 0, 0)
        fgSizer231.AddGrowableCol(1)
        fgSizer231.AddGrowableCol(2)
        fgSizer231.SetFlexibleDirection(wx.HORIZONTAL)
        fgSizer231.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_NONE)
        
        self.m_staticText511 = wx.StaticText(self.tab_accounts, wx.ID_ANY, u"Dates Active", wx.DefaultPosition,
                                             wx.DefaultSize, 0)
        self.m_staticText511.Wrap(-1)
        
        fgSizer231.Add(self.m_staticText511, 0, wx.ALIGN_CENTER | wx.ALL, 5)
        
        self.p_start_date1 = wx.adv.DatePickerCtrl(self.tab_accounts, wx.ID_ANY, wx.DefaultDateTime, wx.DefaultPosition,
                                                   wx.DefaultSize,
                                                   wx.adv.DP_DEFAULT | wx.adv.DP_DROPDOWN | wx.BORDER_SIMPLE)
        fgSizer231.Add(self.p_start_date1, 0, wx.ALIGN_BOTTOM | wx.ALL, 10)
        
        self.p_end_date1 = wx.adv.DatePickerCtrl(self.tab_accounts, wx.ID_ANY, wx.DefaultDateTime, wx.DefaultPosition,
                                                 wx.DefaultSize,
                                                 wx.adv.DP_DEFAULT | wx.adv.DP_DROPDOWN | wx.BORDER_SIMPLE)
        fgSizer231.Add(self.p_end_date1, 0, wx.ALIGN_BOTTOM | wx.ALL, 10)
        
        bSizer491.Add(fgSizer231, 0, wx.ALIGN_BOTTOM, 5)
        
        bSizer_panels1.Add(bSizer491, 0, wx.EXPAND, 5)
        
        self.bSizer_top1.Add(bSizer_panels1, 0, wx.EXPAND, 5)
        
        self.m_staticline52 = wx.StaticLine(self.tab_accounts, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                            wx.LI_HORIZONTAL)
        self.bSizer_top1.Add(self.m_staticline52, 0, wx.EXPAND, 5)
        
        self.p_message2 = wx.TextCtrl(self.tab_accounts, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize,
                                      wx.TE_MULTILINE | wx.TE_READONLY)
        self.p_message2.Hide()
        
        self.bSizer_top1.Add(self.p_message2, 1, wx.ALL | wx.EXPAND, 5)
        
        self.tab_accounts.SetSizer(self.bSizer_top1)
        self.tab_accounts.Layout()
        self.bSizer_top1.Fit(self.tab_accounts)
        self.p_notebook.AddPage(self.tab_accounts, u"Accounts", True)
        self.tab_suppliers = wx.Panel(self.p_notebook, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL,
                                      u"suppliers")
        bSizer_top = wx.BoxSizer(wx.VERTICAL)
        
        rows = wx.BoxSizer(wx.VERTICAL)
        
        self.m_grid1 = wx.grid.Grid(self.tab_suppliers, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0)
        
        # Grid
        self.m_grid1.CreateGrid(0, 0)
        self.m_grid1.EnableEditing(False)
        self.m_grid1.EnableGridLines(True)
        self.m_grid1.EnableDragGridSize(False)
        self.m_grid1.SetMargins(0, 0)
        
        # Columns
        self.m_grid1.AutoSizeColumns()
        self.m_grid1.EnableDragColMove(False)
        self.m_grid1.EnableDragColSize(True)
        self.m_grid1.SetColLabelSize(0)
        self.m_grid1.SetColLabelAlignment(wx.ALIGN_CENTER, wx.ALIGN_CENTER)
        
        # Rows
        self.m_grid1.AutoSizeRows()
        self.m_grid1.EnableDragRowSize(True)
        self.m_grid1.SetRowLabelSize(0)
        self.m_grid1.SetRowLabelAlignment(wx.ALIGN_CENTER, wx.ALIGN_CENTER)
        
        # Label Appearance
        
        # Cell Defaults
        self.m_grid1.SetDefaultCellAlignment(wx.ALIGN_LEFT, wx.ALIGN_TOP)
        rows.Add(self.m_grid1, 0, wx.ALL, 5)
        
        bSizer_top.Add(rows, 0, wx.EXPAND, 0)
        
        single = wx.BoxSizer(wx.VERTICAL)
        
        fgSizer2 = wx.FlexGridSizer(0, 2, 0, 0)
        fgSizer2.AddGrowableCol(1)
        fgSizer2.SetFlexibleDirection(wx.HORIZONTAL)
        fgSizer2.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_NONE)
        
        self.m_staticText1 = wx.StaticText(self.tab_suppliers, wx.ID_ANY, u"Supplier Name", wx.DefaultPosition,
                                           wx.DefaultSize, 0)
        self.m_staticText1.Wrap(-1)
        
        fgSizer2.Add(self.m_staticText1, 0, wx.ALL | wx.EXPAND, 5)
        
        self.p_name = wx.TextCtrl(self.tab_suppliers, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(-1, -1), 0)
        self.p_name.SetMaxLength(80)
        fgSizer2.Add(self.p_name, 1, wx.ALL | wx.EXPAND, 5)
        
        self.m_staticText11 = wx.StaticText(self.tab_suppliers, wx.ID_ANY, u"Web Address", wx.DefaultPosition,
                                            wx.DefaultSize, 0)
        self.m_staticText11.Wrap(-1)
        
        fgSizer2.Add(self.m_staticText11, 0, wx.ALL | wx.EXPAND, 5)
        
        self.p_web = wx.TextCtrl(self.tab_suppliers, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(-1, -1),
                                 wx.TE_AUTO_URL | wx.TE_RICH2)
        self.p_web.SetMaxLength(80)
        fgSizer2.Add(self.p_web, 1, wx.ALL | wx.EXPAND, 5)
        
        single.Add(fgSizer2, 0, wx.EXPAND | wx.LEFT | wx.RIGHT, 5)
        
        self.m_staticline51 = wx.StaticLine(self.tab_suppliers, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                            wx.LI_HORIZONTAL)
        single.Add(self.m_staticline51, 0, wx.EXPAND | wx.ALL, 5)
        
        bSizer_panels = wx.BoxSizer(wx.HORIZONTAL)
        
        fgSizer14 = wx.FlexGridSizer(0, 2, 0, 0)
        fgSizer14.AddGrowableCol(1)
        fgSizer14.AddGrowableRow(0)
        fgSizer14.SetFlexibleDirection(wx.BOTH)
        fgSizer14.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_NONE)
        
        self.m_staticText73 = wx.StaticText(self.tab_suppliers, wx.ID_ANY, u"Address", wx.DefaultPosition,
                                            wx.DefaultSize, 0)
        self.m_staticText73.Wrap(-1)
        
        fgSizer14.Add(self.m_staticText73, 0, wx.ALL, 5)
        
        self.p_address = wx.TextCtrl(self.tab_suppliers, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize,
                                     wx.TE_MULTILINE)
        self.p_address.SetMinSize(wx.Size(-1, 75))
        
        fgSizer14.Add(self.p_address, 1, wx.ALL | wx.EXPAND, 5)
        
        self.m_staticText55 = wx.StaticText(self.tab_suppliers, wx.ID_ANY, u"Phone", wx.DefaultPosition, wx.DefaultSize,
                                            wx.ALIGN_LEFT)
        self.m_staticText55.Wrap(-1)
        
        fgSizer14.Add(self.m_staticText55, 1, wx.ALL | wx.EXPAND, 5)
        
        self.p_phone = wx.TextCtrl(self.tab_suppliers, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        fgSizer14.Add(self.p_phone, 1, wx.ALL | wx.EXPAND, 5)
        
        self.m_staticText70 = wx.StaticText(self.tab_suppliers, wx.ID_ANY, u"e-mail", wx.DefaultPosition,
                                            wx.DefaultSize, 0)
        self.m_staticText70.Wrap(-1)
        
        fgSizer14.Add(self.m_staticText70, 0, wx.ALL, 5)
        
        self.p_email = wx.TextCtrl(self.tab_suppliers, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        fgSizer14.Add(self.p_email, 1, wx.ALL | wx.EXPAND, 5)
        
        bSizer_panels.Add(fgSizer14, 0, wx.ALL | wx.EXPAND, 5)
        
        self.m_staticline32 = wx.StaticLine(self.tab_suppliers, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                            wx.LI_VERTICAL)
        bSizer_panels.Add(self.m_staticline32, 0, wx.EXPAND | wx.LEFT | wx.RIGHT, 5)
        
        bSizer49 = wx.BoxSizer(wx.VERTICAL)
        
        self.p_is_financial = wx.CheckBox(self.tab_suppliers, wx.ID_ANY, u"Financial Institution?", wx.DefaultPosition,
                                          wx.DefaultSize, 0)
        bSizer49.Add(self.p_is_financial, 0, wx.ALL, 5)
        
        fgSizer31 = wx.FlexGridSizer(0, 2, 0, 0)
        fgSizer31.AddGrowableCol(1)
        fgSizer31.SetFlexibleDirection(wx.BOTH)
        fgSizer31.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_ALL)
        
        self.m_staticText112 = wx.StaticText(self.tab_suppliers, wx.ID_ANY, u"Online Access", wx.DefaultPosition,
                                             wx.DefaultSize, 0)
        self.m_staticText112.Wrap(-1)
        
        fgSizer31.Add(self.m_staticText112, 0, wx.ALIGN_CENTER_VERTICAL, 5)
        
        self.p_online = wx.TextCtrl(self.tab_suppliers, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(-1, -1),
                                    wx.TE_AUTO_URL | wx.TE_RICH2)
        self.p_online.SetMaxLength(80)
        fgSizer31.Add(self.p_online, 0, wx.ALL | wx.EXPAND, 5)
        
        bSizer49.Add(fgSizer31, 1, wx.ALL | wx.EXPAND, 5)
        
        bSizer49.Add((0, 0), 1, wx.EXPAND, 5)
        
        fgSizer23 = wx.FlexGridSizer(0, 3, 0, 0)
        fgSizer23.AddGrowableCol(1)
        fgSizer23.AddGrowableCol(2)
        fgSizer23.SetFlexibleDirection(wx.HORIZONTAL)
        fgSizer23.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_NONE)
        
        self.m_staticText51 = wx.StaticText(self.tab_suppliers, wx.ID_ANY, u"Dates Active", wx.DefaultPosition,
                                            wx.DefaultSize, 0)
        self.m_staticText51.Wrap(-1)
        
        fgSizer23.Add(self.m_staticText51, 0, wx.ALIGN_CENTER | wx.ALL, 5)
        
        self.p_start_date = wx.adv.DatePickerCtrl(self.tab_suppliers, wx.ID_ANY, wx.DefaultDateTime, wx.DefaultPosition,
                                                  wx.DefaultSize,
                                                  wx.adv.DP_DEFAULT | wx.adv.DP_DROPDOWN | wx.BORDER_SIMPLE)
        fgSizer23.Add(self.p_start_date, 0, wx.ALIGN_BOTTOM | wx.ALL, 10)
        
        self.p_end_date = wx.adv.DatePickerCtrl(self.tab_suppliers, wx.ID_ANY, wx.DefaultDateTime, wx.DefaultPosition,
                                                wx.DefaultSize,
                                                wx.adv.DP_DEFAULT | wx.adv.DP_DROPDOWN | wx.BORDER_SIMPLE)
        fgSizer23.Add(self.p_end_date, 0, wx.ALIGN_BOTTOM | wx.ALL, 10)
        
        bSizer49.Add(fgSizer23, 0, wx.ALIGN_BOTTOM, 5)
        
        self.m_staticline5 = wx.StaticLine(self.tab_suppliers, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                           wx.LI_HORIZONTAL)
        bSizer49.Add(self.m_staticline5, 0, wx.EXPAND, 5)
        
        bSizer_panels.Add(bSizer49, 1, wx.EXPAND, 5)
        
        single.Add(bSizer_panels, 0, wx.EXPAND, 5)
        
        bSizer_top.Add(single, 1, wx.EXPAND, 5)
        
        self.tab_suppliers.SetSizer(bSizer_top)
        self.tab_suppliers.Layout()
        bSizer_top.Fit(self.tab_suppliers)
        self.p_notebook.AddPage(self.tab_suppliers, u"Suppliers", False)
        self.tab_taxonomy = wx.Panel(self.p_notebook, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL,
                                     u"taxonomy")
        self.bSizer_top = wx.BoxSizer(wx.VERTICAL)
        
        bSizer82 = wx.BoxSizer(wx.HORIZONTAL)
        
        self.tree_taxonomy = wx.dataview.DataViewTreeCtrl(self.tab_taxonomy, wx.ID_ANY, wx.DefaultPosition,
                                                          wx.DefaultSize, 0)
        bSizer82.Add(self.tree_taxonomy, 0, wx.ALL | wx.EXPAND, 5)
        
        bSizer81 = wx.BoxSizer(wx.VERTICAL)
        
        fgSizer211 = wx.FlexGridSizer(1, 2, 0, 0)
        fgSizer211.AddGrowableCol(1)
        fgSizer211.SetFlexibleDirection(wx.HORIZONTAL)
        fgSizer211.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_NONE)
        
        self.m_staticText113 = wx.StaticText(self.tab_taxonomy, wx.ID_ANY, u"Description", wx.DefaultPosition,
                                             wx.DefaultSize, 0)
        self.m_staticText113.Wrap(-1)
        
        fgSizer211.Add(self.m_staticText113, 0, wx.ALL | wx.EXPAND, 5)
        
        self.p_name2 = wx.TextCtrl(self.tab_taxonomy, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(-1, -1), 0)
        self.p_name2.SetMaxLength(80)
        fgSizer211.Add(self.p_name2, 1, wx.ALL | wx.EXPAND, 5)
        
        bSizer81.Add(fgSizer211, 0, wx.EXPAND | wx.LEFT | wx.RIGHT | wx.TOP, 5)
        
        self.m_staticline53 = wx.StaticLine(self.tab_taxonomy, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                            wx.LI_HORIZONTAL)
        bSizer81.Add(self.m_staticline53, 0, wx.EXPAND, 5)
        
        bSizer_panels11 = wx.BoxSizer(wx.HORIZONTAL)
        
        gSizer_left1 = wx.GridSizer(5, 2, 10, 10)
        
        gSizer_left1.Add((0, 0), 1, wx.EXPAND, 5)
        
        bSizer_panels11.Add(gSizer_left1, 1, wx.EXPAND, 5)
        
        self.m_staticline7 = wx.StaticLine(self.tab_taxonomy, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                           wx.LI_VERTICAL)
        bSizer_panels11.Add(self.m_staticline7, 0, wx.EXPAND | wx.LEFT | wx.RIGHT, 5)
        
        bSizer492 = wx.BoxSizer(wx.VERTICAL)
        
        bSizer492.Add((0, 0), 1, wx.EXPAND, 5)
        
        fgSizer232 = wx.FlexGridSizer(0, 3, 0, 0)
        fgSizer232.AddGrowableCol(1)
        fgSizer232.AddGrowableCol(2)
        fgSizer232.SetFlexibleDirection(wx.HORIZONTAL)
        fgSizer232.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_NONE)
        
        self.m_staticText512 = wx.StaticText(self.tab_taxonomy, wx.ID_ANY, u"Dates Active", wx.DefaultPosition,
                                             wx.DefaultSize, 0)
        self.m_staticText512.Wrap(-1)
        
        fgSizer232.Add(self.m_staticText512, 0, wx.ALIGN_CENTER | wx.ALL, 5)
        
        self.p_start_date2 = wx.adv.DatePickerCtrl(self.tab_taxonomy, wx.ID_ANY, wx.DefaultDateTime, wx.DefaultPosition,
                                                   wx.DefaultSize,
                                                   wx.adv.DP_DEFAULT | wx.adv.DP_DROPDOWN | wx.BORDER_SIMPLE)
        fgSizer232.Add(self.p_start_date2, 0, wx.ALIGN_BOTTOM | wx.ALL, 10)
        
        self.p_end_date2 = wx.adv.DatePickerCtrl(self.tab_taxonomy, wx.ID_ANY, wx.DefaultDateTime, wx.DefaultPosition,
                                                 wx.DefaultSize,
                                                 wx.adv.DP_DEFAULT | wx.adv.DP_DROPDOWN | wx.BORDER_SIMPLE)
        fgSizer232.Add(self.p_end_date2, 0, wx.ALIGN_BOTTOM | wx.ALL, 10)
        
        bSizer492.Add(fgSizer232, 0, wx.ALIGN_BOTTOM, 5)
        
        bSizer_panels11.Add(bSizer492, 1, wx.EXPAND, 5)
        
        bSizer81.Add(bSizer_panels11, 0, wx.EXPAND, 5)
        
        self.m_staticline6 = wx.StaticLine(self.tab_taxonomy, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                           wx.LI_HORIZONTAL)
        bSizer81.Add(self.m_staticline6, 0, wx.EXPAND, 5)
        
        bSizer82.Add(bSizer81, 1, wx.EXPAND, 5)
        
        self.bSizer_top.Add(bSizer82, 1, wx.EXPAND, 5)
        
        self.tab_taxonomy.SetSizer(self.bSizer_top)
        self.tab_taxonomy.Layout()
        self.bSizer_top.Fit(self.tab_taxonomy)
        self.p_notebook.AddPage(self.tab_taxonomy, u"Taxonomy", False)
        self.m_panel4 = wx.Panel(self.p_notebook, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        bSizer79 = wx.BoxSizer(wx.VERTICAL)
        
        self.p_taxonomy = wx.dataview.DataViewTreeCtrl(self.m_panel4, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer79.Add(self.p_taxonomy, 0, wx.ALL, 5)
        
        self.m_panel4.SetSizer(bSizer79)
        self.m_panel4.Layout()
        bSizer79.Fit(self.m_panel4)
        self.p_notebook.AddPage(self.m_panel4, u"a page", False)
        self.m_panel5 = wx.Panel(self.p_notebook, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        self.p_notebook.AddPage(self.m_panel5, u"a page", False)
        self.m_panel6 = wx.Panel(self.p_notebook, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        self.p_notebook.AddPage(self.m_panel6, u"a page", False)
        self.m_panel7 = wx.Panel(self.p_notebook, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        self.p_notebook.AddPage(self.m_panel7, u"a page", False)
        self.m_panel8 = wx.Panel(self.p_notebook, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        self.p_notebook.AddPage(self.m_panel8, u"a page", False)
        self.m_panel9 = wx.Panel(self.p_notebook, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        self.p_notebook.AddPage(self.m_panel9, u"a page", False)
        self.m_panel10 = wx.Panel(self.p_notebook, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        self.p_notebook.AddPage(self.m_panel10, u"a page", False)
        
        self.main_sizer.Add(self.p_notebook, 1, wx.EXPAND | wx.ALL, 5)
        
        self.main_single = wx.BoxSizer(wx.VERTICAL)
        
        self.single = wx.BoxSizer(wx.VERTICAL)
        
        self.main_single.Add(self.single, 1, wx.EXPAND, 5)
        
        self.main_sizer.Add(self.main_single, 1, wx.ALL | wx.EXPAND, 5)
        
        self.p_message = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize,
                                     wx.TE_MULTILINE | wx.TE_READONLY | wx.BORDER_THEME | wx.FULL_REPAINT_ON_RESIZE)
        self.p_message.Hide()
        
        self.main_sizer.Add(self.p_message, 0, wx.ALIGN_TOP | wx.ALL | wx.EXPAND, 5)
        
        self.buttons_sizer = wx.BoxSizer(wx.HORIZONTAL)
        
        self.buttons_sizer.Add((0, 0), 1, wx.EXPAND, 5)
        
        self.b_new = wx.Button(self, wx.ID_ANY, u"New", wx.DefaultPosition, wx.DefaultSize, 0 | wx.BORDER_RAISED)
        self.b_new.SetToolTip(u"Add a New Row")
        
        self.buttons_sizer.Add(self.b_new, 0,
                               wx.ALIGN_BOTTOM | wx.ALIGN_RIGHT | wx.ALL | wx.RESERVE_SPACE_EVEN_IF_HIDDEN, 5)
        
        self.b_edit = wx.Button(self, wx.ID_ANY, u"Edit", wx.DefaultPosition, wx.DefaultSize, 0 | wx.BORDER_RAISED)
        self.b_edit.Enable(False)
        self.b_edit.SetToolTip(u"Edit Currently Selected Row")
        
        self.buttons_sizer.Add(self.b_edit, 0,
                               wx.ALIGN_BOTTOM | wx.ALIGN_RIGHT | wx.ALL | wx.RESERVE_SPACE_EVEN_IF_HIDDEN, 5)
        
        self.b_reset = wx.Button(self, wx.ID_ANY, u"Reset", wx.DefaultPosition, wx.DefaultSize, 0 | wx.BORDER_RAISED)
        self.b_reset.Enable(False)
        self.b_reset.SetToolTip(u"Reset Original Values")
        
        self.buttons_sizer.Add(self.b_reset, 0,
                               wx.ALIGN_BOTTOM | wx.ALIGN_RIGHT | wx.ALL | wx.RESERVE_SPACE_EVEN_IF_HIDDEN, 5)
        
        self.b_apply = wx.Button(self, wx.ID_ANY, u"Apply", wx.DefaultPosition, wx.DefaultSize, 0 | wx.BORDER_RAISED)
        self.b_apply.Enable(False)
        self.b_apply.SetToolTip(u"Save Changes")
        
        self.buttons_sizer.Add(self.b_apply, 0,
                               wx.ALIGN_BOTTOM | wx.ALIGN_RIGHT | wx.ALL | wx.RESERVE_SPACE_EVEN_IF_HIDDEN, 5)
        
        self.b_cancel = wx.Button(self, wx.ID_ANY, u"Cancel", wx.DefaultPosition, wx.DefaultSize, 0 | wx.BORDER_RAISED)
        self.b_cancel.Enable(False)
        self.b_cancel.SetToolTip(u"Cancel Changes Without Saving")
        
        self.buttons_sizer.Add(self.b_cancel, 0,
                               wx.ALIGN_BOTTOM | wx.ALIGN_RIGHT | wx.ALL | wx.RESERVE_SPACE_EVEN_IF_HIDDEN, 5)
        
        self.b_quit = wx.Button(self, wx.ID_ANY, u"Quit", wx.DefaultPosition, wx.DefaultSize, 0 | wx.BORDER_RAISED)
        self.b_quit.SetToolTip(u"Close App")
        
        self.buttons_sizer.Add(self.b_quit, 0,
                               wx.ALIGN_BOTTOM | wx.ALIGN_RIGHT | wx.ALL | wx.RESERVE_SPACE_EVEN_IF_HIDDEN, 5)
        
        self.main_sizer.Add(self.buttons_sizer, 0, wx.ALIGN_BOTTOM | wx.EXPAND, 5)
        
        self.SetSizer(self.main_sizer)
        self.Layout()
        self.main_sizer.Fit(self)
        self.status_bar = self.CreateStatusBar(3, wx.STB_DEFAULT_STYLE, wx.ID_ANY)
        
        self.Centre(wx.BOTH)
        
        # Connect Events
        self.Bind(wx.EVT_MENU, self.on_quit_button, id=self.exit.GetId())
        self.Bind(wx.EVT_MENU, self.on_table_selected, id=self.suppliers.GetId())
        self.Bind(wx.EVT_MENU, self.on_table_selected, id=self.contacts.GetId())
        self.Bind(wx.EVT_MENU, self.on_table_selected, id=self.accounts.GetId())
        self.Bind(wx.EVT_MENU, self.on_table_selected, id=self.subaccounts.GetId())
        self.Bind(wx.EVT_MENU, self.on_table_selected, id=self.transactions.GetId())
        self.Bind(wx.EVT_MENU, self.on_table_selected, id=self.rules.GetId())
        self.Bind(wx.EVT_MENU, self.on_table_selected, id=self.cards.GetId())
        self.Bind(wx.EVT_MENU, self.on_table_selected, id=self.categories.GetId())
        self.Bind(wx.EVT_MENU, self.on_table_selected, id=self.subcategories.GetId())
        self.Bind(wx.EVT_MENU, self.on_table_selected, id=self.details.GetId())
        self.p_notebook.Bind(wx.EVT_NOTEBOOK_PAGE_CHANGED, self.on_new_page)
        self.p_notebook.Bind(wx.EVT_NOTEBOOK_PAGE_CHANGING, self.on_changing_page)
        self.p_parent.Bind(wx.EVT_COMBOBOX, self._on_lookup)
        self.p_holder.Bind(wx.EVT_COMBOBOX, self.on_grandparent)
        self.p_start_date1.Bind(wx.adv.EVT_DATE_CHANGED, self.on_start_date)
        self.p_end_date1.Bind(wx.adv.EVT_DATE_CHANGED, self.on_end_date)
        self.p_start_date.Bind(wx.adv.EVT_DATE_CHANGED, self.on_start_date)
        self.p_end_date.Bind(wx.adv.EVT_DATE_CHANGED, self.on_end_date)
        self.p_name2.Bind(wx.EVT_TEXT, self.on_text)
        self.p_start_date2.Bind(wx.adv.EVT_DATE_CHANGED, self.on_start_date)
        self.p_end_date2.Bind(wx.adv.EVT_DATE_CHANGED, self.on_end_date)
        self.b_new.Bind(wx.EVT_BUTTON, self.on_new_button)
        self.b_edit.Bind(wx.EVT_BUTTON, self.on_edit_button)
        self.b_reset.Bind(wx.EVT_BUTTON, self.on_reset_button)
        self.b_apply.Bind(wx.EVT_BUTTON, self.on_apply_button)
        self.b_cancel.Bind(wx.EVT_BUTTON, self.on_cancel_button)
        self.b_quit.Bind(wx.EVT_BUTTON, self.on_quit_button)
    
    def __del__(self):
        pass
    
    # Virtual event handlers, overide them in your derived class
    def on_quit_button(self, event):
        event.Skip()
    
    def on_table_selected(self, event):
        event.Skip()
    
    def on_new_page(self, event):
        event.Skip()
    
    def on_changing_page(self, event):
        event.Skip()
    
    def _on_lookup(self, event):
        event.Skip()
    
    def on_grandparent(self, event):
        event.Skip()
    
    def on_start_date(self, event):
        event.Skip()
    
    def on_end_date(self, event):
        event.Skip()
    
    def on_text(self, event):
        event.Skip()
    
    def on_new_button(self, event):
        event.Skip()
    
    def on_edit_button(self, event):
        event.Skip()
    
    def on_reset_button(self, event):
        event.Skip()
    
    def on_apply_button(self, event):
        event.Skip()
    
    def on_cancel_button(self, event):
        event.Skip()


###########################################################################
## Class SupplierEdit
###########################################################################

class SupplierEdit(wx.Panel):
    
    def __init__(self, parent, id=wx.ID_ANY, pos=wx.DefaultPosition, size=wx.Size(-1, -1),
                 style=wx.BORDER_THEME | wx.TAB_TRAVERSAL, name=u"suppliers"):
        wx.Panel.__init__(self, parent, id=id, pos=pos, size=size, style=style, name=name)
        
        self.SetFont(
            wx.Font(wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL,
                    False, wx.EmptyString))
        self.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_WINDOW))
        
        self.bSizer_top = wx.BoxSizer(wx.VERTICAL)
        
        fgSizer2 = wx.FlexGridSizer(0, 2, 0, 0)
        fgSizer2.AddGrowableCol(1)
        fgSizer2.SetFlexibleDirection(wx.HORIZONTAL)
        fgSizer2.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_NONE)
        
        self.m_staticText1 = wx.StaticText(self, wx.ID_ANY, u"Supplier Name", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText1.Wrap(-1)
        
        fgSizer2.Add(self.m_staticText1, 0, wx.ALL | wx.EXPAND, 5)
        
        self.p_name = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(-1, -1), 0)
        self.p_name.SetMaxLength(80)
        fgSizer2.Add(self.p_name, 1, wx.ALL | wx.EXPAND, 5)
        
        self.m_staticText11 = wx.StaticText(self, wx.ID_ANY, u"Web Address", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText11.Wrap(-1)
        
        fgSizer2.Add(self.m_staticText11, 0, wx.ALL | wx.EXPAND, 5)
        
        self.p_web = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(-1, -1),
                                 wx.TE_AUTO_URL | wx.TE_RICH2)
        self.p_web.SetMaxLength(80)
        fgSizer2.Add(self.p_web, 1, wx.ALL | wx.EXPAND, 5)
        
        self.bSizer_top.Add(fgSizer2, 0, wx.EXPAND | wx.LEFT | wx.RIGHT, 5)
        
        self.m_staticline51 = wx.StaticLine(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL)
        self.bSizer_top.Add(self.m_staticline51, 0, wx.EXPAND, 5)
        
        bSizer_panels = wx.BoxSizer(wx.HORIZONTAL)
        
        fgSizer14 = wx.FlexGridSizer(0, 2, 0, 0)
        fgSizer14.AddGrowableCol(1)
        fgSizer14.AddGrowableRow(0)
        fgSizer14.SetFlexibleDirection(wx.BOTH)
        fgSizer14.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_NONE)
        
        self.m_staticText73 = wx.StaticText(self, wx.ID_ANY, u"Address", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText73.Wrap(-1)
        
        fgSizer14.Add(self.m_staticText73, 0, wx.ALL, 5)
        
        self.p_address = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize,
                                     wx.TE_MULTILINE)
        self.p_address.SetMinSize(wx.Size(-1, 75))
        
        fgSizer14.Add(self.p_address, 1, wx.ALL | wx.EXPAND, 5)
        
        self.m_staticText55 = wx.StaticText(self, wx.ID_ANY, u"Phone", wx.DefaultPosition, wx.DefaultSize,
                                            wx.ALIGN_LEFT)
        self.m_staticText55.Wrap(-1)
        
        fgSizer14.Add(self.m_staticText55, 1, wx.ALL | wx.EXPAND, 5)
        
        self.p_phone = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        fgSizer14.Add(self.p_phone, 1, wx.ALL | wx.EXPAND, 5)
        
        self.m_staticText70 = wx.StaticText(self, wx.ID_ANY, u"e-mail", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText70.Wrap(-1)
        
        fgSizer14.Add(self.m_staticText70, 0, wx.ALL, 5)
        
        self.p_email = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        fgSizer14.Add(self.p_email, 1, wx.ALL | wx.EXPAND, 5)
        
        bSizer_panels.Add(fgSizer14, 0, wx.ALL | wx.EXPAND, 5)
        
        self.m_staticline32 = wx.StaticLine(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_VERTICAL)
        bSizer_panels.Add(self.m_staticline32, 0, wx.EXPAND | wx.LEFT | wx.RIGHT, 5)
        
        bSizer49 = wx.BoxSizer(wx.VERTICAL)
        
        fgSizer31 = wx.FlexGridSizer(0, 2, 0, 0)
        fgSizer31.AddGrowableCol(1)
        fgSizer31.SetFlexibleDirection(wx.BOTH)
        fgSizer31.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_ALL)
        
        self.p_is_financial = wx.CheckBox(self, wx.ID_ANY, u"Financial Institution?", wx.DefaultPosition,
                                          wx.DefaultSize, 0)
        fgSizer31.Add(self.p_is_financial, 0, wx.ALL, 5)
        
        bSizer49.Add(fgSizer31, 1, wx.ALL | wx.EXPAND, 5)
        
        bSizer49.Add((0, 0), 1, wx.EXPAND, 5)
        
        fgSizer23 = wx.FlexGridSizer(0, 3, 0, 0)
        fgSizer23.AddGrowableCol(1)
        fgSizer23.AddGrowableCol(2)
        fgSizer23.SetFlexibleDirection(wx.HORIZONTAL)
        fgSizer23.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_NONE)
        
        self.m_staticText51 = wx.StaticText(self, wx.ID_ANY, u"Dates Active", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText51.Wrap(-1)
        
        fgSizer23.Add(self.m_staticText51, 0, wx.ALIGN_CENTER | wx.ALL, 5)
        
        self.p_start_date = wx.adv.DatePickerCtrl(self, wx.ID_ANY, wx.DefaultDateTime, wx.DefaultPosition,
                                                  wx.DefaultSize,
                                                  wx.adv.DP_DEFAULT | wx.adv.DP_DROPDOWN | wx.BORDER_SIMPLE)
        fgSizer23.Add(self.p_start_date, 0, wx.ALIGN_BOTTOM | wx.ALL, 10)
        
        self.p_end_date = wx.adv.DatePickerCtrl(self, wx.ID_ANY, wx.DefaultDateTime, wx.DefaultPosition, wx.DefaultSize,
                                                wx.adv.DP_DEFAULT | wx.adv.DP_DROPDOWN | wx.BORDER_SIMPLE)
        fgSizer23.Add(self.p_end_date, 0, wx.ALIGN_BOTTOM | wx.ALL, 10)
        
        bSizer49.Add(fgSizer23, 0, wx.ALIGN_BOTTOM, 5)
        
        self.m_staticline5 = wx.StaticLine(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL)
        bSizer49.Add(self.m_staticline5, 0, wx.EXPAND, 5)
        
        bSizer_panels.Add(bSizer49, 0, wx.EXPAND, 5)
        
        self.bSizer_top.Add(bSizer_panels, 0, wx.EXPAND, 5)
        
        self.p_message = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize,
                                     wx.TE_MULTILINE | wx.TE_READONLY)
        self.p_message.Hide()
        
        self.bSizer_top.Add(self.p_message, 1, wx.ALL | wx.EXPAND, 5)
        
        self.SetSizer(self.bSizer_top)
        self.Layout()
        self.bSizer_top.Fit(self)
        
        # Connect Events
        self.p_start_date.Bind(wx.adv.EVT_DATE_CHANGED, self.on_start_date)
        self.p_end_date.Bind(wx.adv.EVT_DATE_CHANGED, self.on_end_date)
    
    def __del__(self):
        pass
    
    # Virtual event handlers, overide them in your derived class
    def on_start_date(self, event):
        event.Skip()
    
    def on_end_date(self, event):
        event.Skip()


###########################################################################
## Class AccountEdit
###########################################################################

class AccountEdit(wx.Panel):
    
    def __init__(self, parent, id=wx.ID_ANY, pos=wx.DefaultPosition, size=wx.Size(-1, -1),
                 style=wx.BORDER_THEME | wx.TAB_TRAVERSAL, name=u"accounts"):
        wx.Panel.__init__(self, parent, id=id, pos=pos, size=size, style=style, name=name)
        
        self.bSizer_top = wx.BoxSizer(wx.VERTICAL)
        
        fgSizer2 = wx.FlexGridSizer(0, 2, 0, 0)
        fgSizer2.AddGrowableCol(1)
        fgSizer2.SetFlexibleDirection(wx.HORIZONTAL)
        fgSizer2.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_NONE)
        
        self.m_staticText61 = wx.StaticText(self, wx.ID_ANY, u"Financial Institution", wx.DefaultPosition,
                                            wx.DefaultSize, 0)
        self.m_staticText61.Wrap(-1)
        
        fgSizer2.Add(self.m_staticText61, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_LEFT | wx.ALL, 5)
        
        p_parentChoices = [u"Unknown"]
        self.p_parent = wx.ComboBox(self, wx.ID_ANY, u"Combo!", wx.DefaultPosition, wx.DefaultSize, p_parentChoices,
                                    wx.CB_DROPDOWN | wx.CB_READONLY, wx.DefaultValidator, u"parent")
        self.p_parent.SetSelection(0)
        fgSizer2.Add(self.p_parent, 1, wx.ALL | wx.EXPAND, 5)
        
        self.m_staticText1 = wx.StaticText(self, wx.ID_ANY, u"Account Name", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText1.Wrap(-1)
        
        fgSizer2.Add(self.m_staticText1, 0, wx.ALL | wx.EXPAND, 5)
        
        self.p_name = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(-1, -1), 0)
        self.p_name.SetMaxLength(80)
        fgSizer2.Add(self.p_name, 1, wx.ALL | wx.EXPAND, 5)
        
        self.m_staticText11 = wx.StaticText(self, wx.ID_ANY, u"Account Description", wx.DefaultPosition, wx.DefaultSize,
                                            0)
        self.m_staticText11.Wrap(-1)
        
        fgSizer2.Add(self.m_staticText11, 0, wx.ALL | wx.EXPAND, 5)
        
        self.p_description = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(-1, -1), 0)
        self.p_description.SetMaxLength(80)
        fgSizer2.Add(self.p_description, 1, wx.ALL | wx.EXPAND, 5)
        
        self.bSizer_top.Add(fgSizer2, 0, wx.EXPAND | wx.LEFT | wx.RIGHT, 5)
        
        self.m_staticline51 = wx.StaticLine(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL)
        self.bSizer_top.Add(self.m_staticline51, 0, wx.EXPAND, 5)
        
        bSizer_panels = wx.BoxSizer(wx.HORIZONTAL)
        
        fgSizer14 = wx.FlexGridSizer(0, 2, 0, 0)
        fgSizer14.AddGrowableCol(1)
        fgSizer14.SetFlexibleDirection(wx.BOTH)
        fgSizer14.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_NONE)
        
        self.m_staticText55 = wx.StaticText(self, wx.ID_ANY, u"Sort Code", wx.DefaultPosition, wx.DefaultSize,
                                            wx.ALIGN_LEFT)
        self.m_staticText55.Wrap(-1)
        
        fgSizer14.Add(self.m_staticText55, 0, wx.ALL | wx.EXPAND, 5)
        
        self.p_sort_code = wx.lib.masked.TextCtrl(self, wx.ID_ANY, u"00-00-00", wx.DefaultPosition, wx.DefaultSize, 0,
                                                  mask=u"##-##-##")
        self.p_sort_code.SetMaxLength(8)
        
        self.p_sort_code.SetFont(
            wx.Font(wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL,
                    False, wx.EmptyString))
        self.p_sort_code.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_WINDOW))
        
        fgSizer14.Add(self.p_sort_code, 0, wx.ALL, 5)
        
        self.m_staticText70 = wx.StaticText(self, wx.ID_ANY, u"Account Number", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText70.Wrap(-1)
        
        fgSizer14.Add(self.m_staticText70, 0, wx.ALL, 5)
        
        self.p_account_no = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        self.p_account_no.SetMaxLength(8)
        fgSizer14.Add(self.p_account_no, 1, wx.ALL, 5)
        
        self.m_staticText74 = wx.StaticText(self, wx.ID_ANY, u"Initial Value", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText74.Wrap(-1)
        
        fgSizer14.Add(self.m_staticText74, 0, wx.ALL, 5)
        
        self.p_initial = wx.SpinCtrlDouble(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize,
                                           wx.ALIGN_RIGHT | wx.SP_ARROW_KEYS, -1e+06, 1e+06, 0, 0.01)
        self.p_initial.SetDigits(2)
        fgSizer14.Add(self.p_initial, 0, wx.ALL, 5)
        
        bSizer_panels.Add(fgSizer14, 0, wx.ALL, 5)
        
        self.m_staticline32 = wx.StaticLine(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_VERTICAL)
        bSizer_panels.Add(self.m_staticline32, 0, wx.EXPAND | wx.LEFT | wx.RIGHT, 5)
        
        bSizer49 = wx.BoxSizer(wx.VERTICAL)
        
        fgSizer31 = wx.FlexGridSizer(0, 2, 0, 0)
        fgSizer31.AddGrowableCol(1)
        fgSizer31.SetFlexibleDirection(wx.BOTH)
        fgSizer31.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_ALL)
        
        self.m_staticText71 = wx.StaticText(self, wx.ID_ANY, u"Account Holder", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText71.Wrap(-1)
        
        fgSizer31.Add(self.m_staticText71, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)
        
        p_holderChoices = [u"Dermot", u"Fenella", u"Joint", u"Other"]
        self.p_holder = wx.ComboBox(self, wx.ID_ANY, u"Dermot", wx.DefaultPosition, wx.DefaultSize, p_holderChoices,
                                    wx.CB_DROPDOWN | wx.CB_READONLY)
        self.p_holder.SetSelection(0)
        fgSizer31.Add(self.p_holder, 1, wx.ALL | wx.EXPAND, 5)
        
        self.m_staticText73 = wx.StaticText(self, wx.ID_ANY, u"Account Type", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText73.Wrap(-1)
        
        fgSizer31.Add(self.m_staticText73, 0, wx.ALL, 5)
        
        p_typeChoices = [u"Current", u"Savings", u"ISA", u"Credit Card", u"Loan", u"Mortgage", u"Cash", u"Shares",
                         u"Current", u"Insurance"]
        self.p_type = wx.ComboBox(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, p_typeChoices,
                                  wx.CB_DROPDOWN | wx.CB_READONLY)
        self.p_type.SetSelection(10)
        fgSizer31.Add(self.p_type, 0, wx.ALL | wx.EXPAND, 5)
        
        bSizer49.Add(fgSizer31, 0, wx.ALL, 5)
        
        bSizer49.Add((0, 0), 1, wx.EXPAND, 5)
        
        fgSizer23 = wx.FlexGridSizer(0, 3, 0, 0)
        fgSizer23.AddGrowableCol(1)
        fgSizer23.AddGrowableCol(2)
        fgSizer23.SetFlexibleDirection(wx.HORIZONTAL)
        fgSizer23.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_NONE)
        
        self.m_staticText51 = wx.StaticText(self, wx.ID_ANY, u"Dates Active", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText51.Wrap(-1)
        
        fgSizer23.Add(self.m_staticText51, 0, wx.ALIGN_CENTER | wx.ALL, 5)
        
        self.p_start_date = wx.adv.DatePickerCtrl(self, wx.ID_ANY, wx.DefaultDateTime, wx.DefaultPosition,
                                                  wx.DefaultSize,
                                                  wx.adv.DP_DEFAULT | wx.adv.DP_DROPDOWN | wx.BORDER_SIMPLE)
        fgSizer23.Add(self.p_start_date, 0, wx.ALIGN_BOTTOM | wx.ALL, 10)
        
        self.p_end_date = wx.adv.DatePickerCtrl(self, wx.ID_ANY, wx.DefaultDateTime, wx.DefaultPosition, wx.DefaultSize,
                                                wx.adv.DP_DEFAULT | wx.adv.DP_DROPDOWN | wx.BORDER_SIMPLE)
        fgSizer23.Add(self.p_end_date, 0, wx.ALIGN_BOTTOM | wx.ALL, 10)
        
        bSizer49.Add(fgSizer23, 0, wx.ALIGN_BOTTOM, 5)
        
        bSizer_panels.Add(bSizer49, 0, wx.EXPAND, 5)
        
        self.bSizer_top.Add(bSizer_panels, 0, wx.EXPAND, 5)
        
        self.m_staticline5 = wx.StaticLine(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL)
        self.bSizer_top.Add(self.m_staticline5, 0, wx.EXPAND, 5)
        
        self.p_message = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize,
                                     wx.TE_MULTILINE | wx.TE_READONLY)
        self.p_message.Hide()
        
        self.bSizer_top.Add(self.p_message, 1, wx.ALL | wx.EXPAND, 5)
        
        self.SetSizer(self.bSizer_top)
        self.Layout()
        self.bSizer_top.Fit(self)
        
        # Connect Events
        self.p_parent.Bind(wx.EVT_COMBOBOX, self._on_lookup)
        self.p_holder.Bind(wx.EVT_COMBOBOX, self.on_grandparent)
        self.p_start_date.Bind(wx.adv.EVT_DATE_CHANGED, self.on_start_date)
        self.p_end_date.Bind(wx.adv.EVT_DATE_CHANGED, self.on_end_date)
    
    def __del__(self):
        pass
    
    # Virtual event handlers, overide them in your derived class
    def _on_lookup(self, event):
        event.Skip()
    
    def on_grandparent(self, event):
        event.Skip()
    
    def on_start_date(self, event):
        event.Skip()
    
    def on_end_date(self, event):
        event.Skip()


###########################################################################
## Class CategoryEdit
###########################################################################

class CategoryEdit(wx.Panel):
    
    def __init__(self, parent, id=wx.ID_ANY, pos=wx.DefaultPosition, size=wx.Size(-1, -1),
                 style=wx.BORDER_THEME | wx.TAB_TRAVERSAL, name=u"categories"):
        wx.Panel.__init__(self, parent, id=id, pos=pos, size=size, style=style, name=name)
        
        self.bSizer_top = wx.BoxSizer(wx.VERTICAL)
        
        fgSizer21 = wx.FlexGridSizer(1, 2, 0, 0)
        fgSizer21.AddGrowableCol(1)
        fgSizer21.SetFlexibleDirection(wx.HORIZONTAL)
        fgSizer21.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_NONE)
        
        self.m_staticText11 = wx.StaticText(self, wx.ID_ANY, u"Description", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText11.Wrap(-1)
        
        fgSizer21.Add(self.m_staticText11, 0, wx.ALL | wx.EXPAND, 5)
        
        self.p_name = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(-1, -1), 0)
        self.p_name.SetMaxLength(80)
        fgSizer21.Add(self.p_name, 1, wx.ALL | wx.EXPAND, 5)
        
        self.bSizer_top.Add(fgSizer21, 0, wx.EXPAND | wx.LEFT | wx.RIGHT | wx.TOP, 5)
        
        self.m_staticline5 = wx.StaticLine(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL)
        self.bSizer_top.Add(self.m_staticline5, 0, wx.EXPAND, 5)
        
        bSizer_panels1 = wx.BoxSizer(wx.HORIZONTAL)
        
        gSizer_left1 = wx.GridSizer(5, 2, 10, 10)
        
        gSizer_left1.Add((0, 0), 1, wx.EXPAND, 5)
        
        bSizer_panels1.Add(gSizer_left1, 1, wx.EXPAND, 5)
        
        self.m_staticline7 = wx.StaticLine(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_VERTICAL)
        bSizer_panels1.Add(self.m_staticline7, 0, wx.EXPAND | wx.LEFT | wx.RIGHT, 5)
        
        bSizer49 = wx.BoxSizer(wx.VERTICAL)
        
        bSizer49.Add((0, 0), 1, wx.EXPAND, 5)
        
        fgSizer23 = wx.FlexGridSizer(0, 3, 0, 0)
        fgSizer23.AddGrowableCol(1)
        fgSizer23.AddGrowableCol(2)
        fgSizer23.SetFlexibleDirection(wx.HORIZONTAL)
        fgSizer23.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_NONE)
        
        self.m_staticText51 = wx.StaticText(self, wx.ID_ANY, u"Dates Active", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText51.Wrap(-1)
        
        fgSizer23.Add(self.m_staticText51, 0, wx.ALIGN_CENTER | wx.ALL, 5)
        
        self.p_start_date = wx.adv.DatePickerCtrl(self, wx.ID_ANY, wx.DefaultDateTime, wx.DefaultPosition,
                                                  wx.DefaultSize,
                                                  wx.adv.DP_DEFAULT | wx.adv.DP_DROPDOWN | wx.BORDER_SIMPLE)
        fgSizer23.Add(self.p_start_date, 0, wx.ALIGN_BOTTOM | wx.ALL, 10)
        
        self.p_end_date = wx.adv.DatePickerCtrl(self, wx.ID_ANY, wx.DefaultDateTime, wx.DefaultPosition, wx.DefaultSize,
                                                wx.adv.DP_DEFAULT | wx.adv.DP_DROPDOWN | wx.BORDER_SIMPLE)
        fgSizer23.Add(self.p_end_date, 0, wx.ALIGN_BOTTOM | wx.ALL, 10)
        
        bSizer49.Add(fgSizer23, 0, wx.ALIGN_BOTTOM, 5)
        
        bSizer_panels1.Add(bSizer49, 1, wx.EXPAND, 5)
        
        self.bSizer_top.Add(bSizer_panels1, 0, wx.EXPAND, 5)
        
        self.m_staticline6 = wx.StaticLine(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL)
        self.bSizer_top.Add(self.m_staticline6, 0, wx.EXPAND, 5)
        
        self.p_message = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize,
                                     wx.TE_MULTILINE | wx.TE_READONLY)
        self.p_message.Hide()
        
        self.bSizer_top.Add(self.p_message, 1, wx.ALL | wx.EXPAND, 5)
        
        self.SetSizer(self.bSizer_top)
        self.Layout()
        self.bSizer_top.Fit(self)
        
        # Connect Events
        self.p_name.Bind(wx.EVT_TEXT, self.on_text)
        self.p_start_date.Bind(wx.adv.EVT_DATE_CHANGED, self.on_start_date)
        self.p_end_date.Bind(wx.adv.EVT_DATE_CHANGED, self.on_end_date)
    
    def __del__(self):
        pass
    
    # Virtual event handlers, overide them in your derived class
    def on_text(self, event):
        event.Skip()
    
    def on_start_date(self, event):
        event.Skip()
    
    def on_end_date(self, event):
        event.Skip()


###########################################################################
## Class SubCatEdit
###########################################################################

class SubCatEdit(wx.Panel):
    
    def __init__(self, parent, id=wx.ID_ANY, pos=wx.DefaultPosition, size=wx.Size(-1, -1),
                 style=wx.BORDER_THEME | wx.TAB_TRAVERSAL, name=u"subcategories"):
        wx.Panel.__init__(self, parent, id=id, pos=pos, size=size, style=style, name=name)
        
        self.bSizer_top = wx.BoxSizer(wx.VERTICAL)
        
        fgSizer2 = wx.FlexGridSizer(0, 2, 0, 0)
        fgSizer2.AddGrowableCol(1)
        fgSizer2.SetFlexibleDirection(wx.HORIZONTAL)
        fgSizer2.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_NONE)
        
        self.m_staticText6 = wx.StaticText(self, wx.ID_ANY, u"Category", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText6.Wrap(-1)
        
        fgSizer2.Add(self.m_staticText6, 0, wx.ALIGN_CENTER | wx.ALL, 5)
        
        p_parentChoices = []
        self.p_parent = wx.ComboBox(self, wx.ID_ANY, u"Combo!", wx.DefaultPosition, wx.DefaultSize, p_parentChoices,
                                    wx.CB_DROPDOWN | wx.CB_READONLY, wx.DefaultValidator, u"parent")
        fgSizer2.Add(self.p_parent, 1, wx.ALL | wx.EXPAND, 5)
        
        self.m_staticText1 = wx.StaticText(self, wx.ID_ANY, u"Description", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText1.Wrap(-1)
        
        fgSizer2.Add(self.m_staticText1, 0, wx.ALL | wx.EXPAND, 5)
        
        self.p_name = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(-1, -1), 0)
        self.p_name.SetMaxLength(80)
        fgSizer2.Add(self.p_name, 1, wx.ALL | wx.EXPAND, 5)
        
        self.bSizer_top.Add(fgSizer2, 0, wx.LEFT | wx.RIGHT | wx.TOP | wx.EXPAND, 5)
        
        self.m_staticline5 = wx.StaticLine(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL)
        self.bSizer_top.Add(self.m_staticline5, 0, wx.EXPAND, 5)
        
        bSizer_panels = wx.BoxSizer(wx.HORIZONTAL)
        
        gSizer_left = wx.GridSizer(5, 2, 10, 10)
        
        gSizer_left.Add((0, 0), 1, wx.EXPAND, 5)
        
        bSizer_panels.Add(gSizer_left, 1, wx.EXPAND, 5)
        
        self.m_staticline7 = wx.StaticLine(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_VERTICAL)
        bSizer_panels.Add(self.m_staticline7, 0, wx.EXPAND | wx.LEFT | wx.RIGHT, 5)
        
        bSizer49 = wx.BoxSizer(wx.VERTICAL)
        
        bSizer49.Add((0, 0), 1, wx.EXPAND, 5)
        
        fgSizer23 = wx.FlexGridSizer(0, 3, 0, 0)
        fgSizer23.AddGrowableCol(1)
        fgSizer23.AddGrowableCol(2)
        fgSizer23.SetFlexibleDirection(wx.HORIZONTAL)
        fgSizer23.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_NONE)
        
        self.m_staticText5 = wx.StaticText(self, wx.ID_ANY, u"Dates Active", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText5.Wrap(-1)
        
        fgSizer23.Add(self.m_staticText5, 0, wx.ALIGN_CENTER | wx.ALL, 5)
        
        self.p_start_date = wx.adv.DatePickerCtrl(self, wx.ID_ANY, wx.DefaultDateTime, wx.DefaultPosition,
                                                  wx.DefaultSize,
                                                  wx.adv.DP_DEFAULT | wx.adv.DP_DROPDOWN | wx.BORDER_SIMPLE)
        fgSizer23.Add(self.p_start_date, 0, wx.ALIGN_BOTTOM | wx.ALL, 10)
        
        self.p_end_date = wx.adv.DatePickerCtrl(self, wx.ID_ANY, wx.DefaultDateTime, wx.DefaultPosition, wx.DefaultSize,
                                                wx.adv.DP_DEFAULT | wx.adv.DP_DROPDOWN | wx.BORDER_SIMPLE)
        fgSizer23.Add(self.p_end_date, 0, wx.ALIGN_BOTTOM | wx.ALL, 10)
        
        bSizer49.Add(fgSizer23, 0, wx.ALIGN_BOTTOM, 5)
        
        bSizer_panels.Add(bSizer49, 1, wx.EXPAND, 5)
        
        self.bSizer_top.Add(bSizer_panels, 0, wx.EXPAND, 5)
        
        self.m_staticline6 = wx.StaticLine(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL)
        self.bSizer_top.Add(self.m_staticline6, 0, wx.EXPAND, 5)
        
        self.p_message = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize,
                                     wx.TE_MULTILINE | wx.TE_READONLY)
        self.p_message.Hide()
        
        self.bSizer_top.Add(self.p_message, 1, wx.ALL | wx.EXPAND, 5)
        
        self.SetSizer(self.bSizer_top)
        self.Layout()
        self.bSizer_top.Fit(self)
        
        # Connect Events
        self.p_parent.Bind(wx.EVT_COMBOBOX, self._on_lookup)
        self.p_start_date.Bind(wx.adv.EVT_DATE_CHANGED, self.on_start_date)
        self.p_end_date.Bind(wx.adv.EVT_DATE_CHANGED, self.on_end_date)
    
    def __del__(self):
        pass
    
    # Virtual event handlers, overide them in your derived class
    def _on_lookup(self, event):
        event.Skip()
    
    def on_start_date(self, event):
        event.Skip()
    
    def on_end_date(self, event):
        event.Skip()


###########################################################################
## Class DetailEdit
###########################################################################

class DetailEdit(wx.Panel):
    
    def __init__(self, parent, id=wx.ID_ANY, pos=wx.DefaultPosition, size=wx.Size(-1, -1),
                 style=wx.BORDER_THEME | wx.TAB_TRAVERSAL, name=u"details"):
        wx.Panel.__init__(self, parent, id=id, pos=pos, size=size, style=style, name=name)
        
        self.bSizer_top = wx.BoxSizer(wx.VERTICAL)
        
        fgSizer2 = wx.FlexGridSizer(0, 2, 0, 0)
        fgSizer2.AddGrowableCol(1)
        fgSizer2.SetFlexibleDirection(wx.HORIZONTAL)
        fgSizer2.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_NONE)
        
        self.m_staticText71 = wx.StaticText(self, wx.ID_ANY, u"Category", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText71.Wrap(-1)
        
        fgSizer2.Add(self.m_staticText71, 0, wx.ALL, 5)
        
        p_grandparentChoices = []
        self.p_grandparent = wx.ComboBox(self, wx.ID_ANY, u"Combo!", wx.DefaultPosition, wx.DefaultSize,
                                         p_grandparentChoices, wx.CB_DROPDOWN | wx.CB_READONLY, wx.DefaultValidator,
                                         u"grandparent")
        fgSizer2.Add(self.p_grandparent, 1, wx.ALL | wx.EXPAND, 5)
        
        self.m_staticText61 = wx.StaticText(self, wx.ID_ANY, u"Sub Category", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText61.Wrap(-1)
        
        fgSizer2.Add(self.m_staticText61, 0, wx.ALIGN_CENTER | wx.ALL, 5)
        
        p_parentChoices = []
        self.p_parent = wx.ComboBox(self, wx.ID_ANY, u"Combo!", wx.DefaultPosition, wx.DefaultSize, p_parentChoices,
                                    wx.CB_DROPDOWN | wx.CB_READONLY, wx.DefaultValidator, u"parent")
        fgSizer2.Add(self.p_parent, 1, wx.ALL | wx.EXPAND, 5)
        
        self.m_staticText1 = wx.StaticText(self, wx.ID_ANY, u"Description", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText1.Wrap(-1)
        
        fgSizer2.Add(self.m_staticText1, 0, wx.ALL | wx.EXPAND, 5)
        
        self.p_name = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(-1, -1), 0)
        self.p_name.SetMaxLength(80)
        fgSizer2.Add(self.p_name, 1, wx.ALL | wx.EXPAND, 5)
        
        self.bSizer_top.Add(fgSizer2, 0, wx.EXPAND | wx.LEFT | wx.RIGHT | wx.TOP, 5)
        
        self.m_staticline11 = wx.StaticLine(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL)
        self.bSizer_top.Add(self.m_staticline11, 0, wx.EXPAND, 5)
        
        bSizer_panels = wx.BoxSizer(wx.HORIZONTAL)
        
        gSizer_left = wx.GridSizer(5, 2, 10, 10)
        
        gSizer_left.Add((0, 0), 1, wx.EXPAND, 5)
        
        bSizer_panels.Add(gSizer_left, 1, wx.EXPAND, 5)
        
        self.m_staticline8 = wx.StaticLine(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_VERTICAL)
        bSizer_panels.Add(self.m_staticline8, 0, wx.EXPAND | wx.LEFT | wx.RIGHT, 5)
        
        bSizer49 = wx.BoxSizer(wx.VERTICAL)
        
        bSizer49.Add((0, 0), 1, wx.EXPAND, 5)
        
        fgSizer23 = wx.FlexGridSizer(0, 3, 0, 0)
        fgSizer23.AddGrowableCol(1)
        fgSizer23.AddGrowableCol(2)
        fgSizer23.SetFlexibleDirection(wx.HORIZONTAL)
        fgSizer23.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_NONE)
        
        self.m_staticText51 = wx.StaticText(self, wx.ID_ANY, u"Dates Active", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText51.Wrap(-1)
        
        fgSizer23.Add(self.m_staticText51, 0, wx.ALIGN_CENTER | wx.ALL, 5)
        
        self.p_start_date = wx.adv.DatePickerCtrl(self, wx.ID_ANY, wx.DefaultDateTime, wx.DefaultPosition,
                                                  wx.DefaultSize,
                                                  wx.adv.DP_DEFAULT | wx.adv.DP_DROPDOWN | wx.BORDER_SIMPLE)
        fgSizer23.Add(self.p_start_date, 0, wx.ALIGN_BOTTOM | wx.ALL, 10)
        
        self.p_end_date = wx.adv.DatePickerCtrl(self, wx.ID_ANY, wx.DefaultDateTime, wx.DefaultPosition, wx.DefaultSize,
                                                wx.adv.DP_DEFAULT | wx.adv.DP_DROPDOWN | wx.BORDER_SIMPLE)
        fgSizer23.Add(self.p_end_date, 0, wx.ALIGN_BOTTOM | wx.ALL, 10)
        
        bSizer49.Add(fgSizer23, 0, wx.ALIGN_BOTTOM, 5)
        
        bSizer_panels.Add(bSizer49, 1, wx.EXPAND, 5)
        
        self.bSizer_top.Add(bSizer_panels, 0, wx.EXPAND, 5)
        
        self.m_staticline1 = wx.StaticLine(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL)
        self.bSizer_top.Add(self.m_staticline1, 0, wx.EXPAND, 5)
        
        self.p_message = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize,
                                     wx.TE_MULTILINE | wx.TE_READONLY)
        self.p_message.Hide()
        
        self.bSizer_top.Add(self.p_message, 1, wx.ALL | wx.EXPAND, 5)
        
        self.SetSizer(self.bSizer_top)
        self.Layout()
        self.bSizer_top.Fit(self)
        
        # Connect Events
        self.p_grandparent.Bind(wx.EVT_COMBOBOX, self._on_lookup)
        self.p_parent.Bind(wx.EVT_COMBOBOX, self._on_lookup)
        self.p_start_date.Bind(wx.adv.EVT_DATE_CHANGED, self.on_start_date)
        self.p_end_date.Bind(wx.adv.EVT_DATE_CHANGED, self.on_end_date)
    
    def __del__(self):
        pass
    
    # Virtual event handlers, overide them in your derived class
    def _on_lookup(self, event):
        event.Skip()
    
    def on_start_date(self, event):
        event.Skip()
    
    def on_end_date(self, event):
        event.Skip()


###########################################################################
## Class TransactionEdit
###########################################################################

class TransactionEdit(wx.Panel):
    
    def __init__(self, parent, id=wx.ID_ANY, pos=wx.DefaultPosition, size=wx.Size(-1, -1),
                 style=wx.BORDER_THEME | wx.TAB_TRAVERSAL, name=u"transactions"):
        wx.Panel.__init__(self, parent, id=id, pos=pos, size=size, style=style, name=name)
        
        self.bSizer_top = wx.BoxSizer(wx.VERTICAL)
        
        fgSizer23 = wx.FlexGridSizer(0, 7, 0, 0)
        fgSizer23.AddGrowableCol(1)
        fgSizer23.AddGrowableCol(3)
        fgSizer23.AddGrowableCol(5)
        fgSizer23.SetFlexibleDirection(wx.HORIZONTAL)
        fgSizer23.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_NONE)
        
        self.m_staticText51 = wx.StaticText(self, wx.ID_ANY, u"Date ", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText51.Wrap(-1)
        
        fgSizer23.Add(self.m_staticText51, 0, wx.ALIGN_CENTER | wx.ALL, 5)
        
        self.p_date = wx.adv.DatePickerCtrl(self, wx.ID_ANY, wx.DefaultDateTime, wx.DefaultPosition, wx.DefaultSize,
                                            wx.adv.DP_DEFAULT | wx.adv.DP_DROPDOWN | wx.BORDER_SIMPLE)
        fgSizer23.Add(self.p_date, 0, wx.ALIGN_BOTTOM | wx.ALL, 10)
        
        self.m_staticText74 = wx.StaticText(self, wx.ID_ANY, u"Amount", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText74.Wrap(-1)
        
        fgSizer23.Add(self.m_staticText74, 0, wx.ALIGN_BOTTOM | wx.ALIGN_CENTER | wx.ALL, 5)
        
        self.p_amount = wx.SpinCtrlDouble(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize,
                                          wx.ALIGN_RIGHT | wx.SP_ARROW_KEYS, -1e+06, 1e+06, 0.000000, 0.01)
        self.p_amount.SetDigits(2)
        fgSizer23.Add(self.p_amount, 0, wx.ALIGN_BOTTOM | wx.ALIGN_CENTER | wx.ALL, 10)
        
        self.m_staticText61 = wx.StaticText(self, wx.ID_ANY, u"Supplier", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText61.Wrap(-1)
        
        fgSizer23.Add(self.m_staticText61, 0, wx.ALIGN_CENTER | wx.ALL, 5)
        
        p_supplierChoices = []
        self.p_supplier = wx.ComboBox(self, wx.ID_ANY, u"Combo!", wx.DefaultPosition, wx.DefaultSize, p_supplierChoices,
                                      wx.CB_DROPDOWN | wx.CB_SORT)
        fgSizer23.Add(self.p_supplier, 0, wx.ALL, 10)
        
        self.bSizer_top.Add(fgSizer23, 0, wx.ALIGN_BOTTOM | wx.EXPAND | wx.LEFT | wx.RIGHT, 5)
        
        self.m_staticline51 = wx.StaticLine(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL)
        self.bSizer_top.Add(self.m_staticline51, 0, wx.EXPAND, 5)
        
        fgSizer2 = wx.FlexGridSizer(0, 2, 0, 0)
        fgSizer2.AddGrowableCol(1)
        fgSizer2.SetFlexibleDirection(wx.HORIZONTAL)
        fgSizer2.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_NONE)
        
        self.m_staticText1 = wx.StaticText(self, wx.ID_ANY, u"Description", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText1.Wrap(-1)
        
        fgSizer2.Add(self.m_staticText1, 0, wx.ALL | wx.EXPAND, 5)
        
        self.p_name = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(-1, -1), 0)
        self.p_name.SetMaxLength(80)
        fgSizer2.Add(self.p_name, 1, wx.ALL | wx.EXPAND, 5)
        
        self.m_staticText11 = wx.StaticText(self, wx.ID_ANY, u"Bank Description", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText11.Wrap(-1)
        
        fgSizer2.Add(self.m_staticText11, 0, wx.ALL | wx.EXPAND, 5)
        
        self.p_description = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(-1, -1), 0)
        self.p_description.SetMaxLength(80)
        fgSizer2.Add(self.p_description, 1, wx.ALL | wx.EXPAND, 5)
        
        self.bSizer_top.Add(fgSizer2, 0, wx.EXPAND | wx.LEFT | wx.RIGHT, 5)
        
        self.m_staticline51 = wx.StaticLine(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL)
        self.bSizer_top.Add(self.m_staticline51, 0, wx.EXPAND, 5)
        
        bSizer_panels = wx.BoxSizer(wx.HORIZONTAL)
        
        fgSizer14 = wx.FlexGridSizer(0, 2, 0, 0)
        fgSizer14.AddGrowableCol(1)
        fgSizer14.SetFlexibleDirection(wx.HORIZONTAL)
        fgSizer14.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)
        
        self.m_staticText712 = wx.StaticText(self, wx.ID_ANY, u"Bank", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText712.Wrap(-1)
        
        fgSizer14.Add(self.m_staticText712, 0, wx.ALL, 5)
        
        p_grandparentChoices = []
        self.p_grandparent = wx.ComboBox(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize,
                                         p_grandparentChoices, wx.CB_DROPDOWN | wx.CB_READONLY)
        fgSizer14.Add(self.p_grandparent, 0, wx.ALL | wx.EXPAND, 5)
        
        self.m_staticText7111 = wx.StaticText(self, wx.ID_ANY, u"Account", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText7111.Wrap(-1)
        
        fgSizer14.Add(self.m_staticText7111, 0, wx.ALL, 5)
        
        p_parentChoices = []
        self.p_parent = wx.ComboBox(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize,
                                    p_parentChoices, wx.CB_DROPDOWN | wx.CB_READONLY)
        fgSizer14.Add(self.p_parent, 0, wx.ALL | wx.EXPAND, 5)
        
        self.m_staticText73 = wx.StaticText(self, wx.ID_ANY, u"TransType", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText73.Wrap(-1)
        
        fgSizer14.Add(self.m_staticText73, 0, wx.ALL, 5)
        
        p_typeChoices = []
        self.p_type = wx.ComboBox(self, wx.ID_ANY, u"Combo!", wx.DefaultPosition, wx.DefaultSize, p_typeChoices,
                                  wx.CB_DROPDOWN | wx.CB_READONLY)
        fgSizer14.Add(self.p_type, 0, wx.ALL | wx.EXPAND, 5)
        
        bSizer_panels.Add(fgSizer14, 1, wx.ALL | wx.EXPAND, 5)
        
        self.m_staticline32 = wx.StaticLine(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_VERTICAL)
        bSizer_panels.Add(self.m_staticline32, 0, wx.EXPAND | wx.LEFT | wx.RIGHT, 5)
        
        bSizer49 = wx.BoxSizer(wx.VERTICAL)
        
        fgSizer31 = wx.FlexGridSizer(0, 2, 0, 0)
        fgSizer31.AddGrowableCol(1)
        fgSizer31.SetFlexibleDirection(wx.HORIZONTAL)
        fgSizer31.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)
        
        self.m_staticText71 = wx.StaticText(self, wx.ID_ANY, u"Category", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText71.Wrap(-1)
        
        fgSizer31.Add(self.m_staticText71, 0, wx.ALL, 5)
        
        p_categoriesChoices = []
        self.p_categories = wx.ComboBox(self, wx.ID_ANY, u"Combo!", wx.DefaultPosition, wx.DefaultSize,
                                        p_categoriesChoices, wx.CB_DROPDOWN | wx.CB_READONLY)
        fgSizer31.Add(self.p_categories, 0, wx.ALL | wx.EXPAND, 5)
        
        self.m_staticText711 = wx.StaticText(self, wx.ID_ANY, u"SubCategory", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText711.Wrap(-1)
        
        fgSizer31.Add(self.m_staticText711, 0, wx.ALL, 5)
        
        p_subcategoriesChoices = []
        self.p_subcategories = wx.ComboBox(self, wx.ID_ANY, u"Combo!", wx.DefaultPosition, wx.DefaultSize,
                                           p_subcategoriesChoices, wx.CB_DROPDOWN | wx.CB_READONLY)
        self.p_subcategories.Enable(False)
        
        fgSizer31.Add(self.p_subcategories, 0, wx.ALL | wx.EXPAND, 5)
        
        self.m_staticText7112 = wx.StaticText(self, wx.ID_ANY, u"Detail", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText7112.Wrap(-1)
        
        fgSizer31.Add(self.m_staticText7112, 0, wx.ALL, 5)
        
        p_detailsChoices = []
        self.p_details = wx.ComboBox(self, wx.ID_ANY, u"Combo!", wx.DefaultPosition, wx.DefaultSize, p_detailsChoices,
                                     wx.CB_DROPDOWN | wx.CB_READONLY)
        self.p_details.Enable(False)
        
        fgSizer31.Add(self.p_details, 0, wx.ALL | wx.EXPAND, 5)
        
        bSizer49.Add(fgSizer31, 1, wx.ALL | wx.EXPAND, 5)
        
        bSizer_panels.Add(bSizer49, 1, wx.EXPAND, 5)
        
        self.bSizer_top.Add(bSizer_panels, 0, wx.EXPAND, 5)
        
        self.m_staticline511 = wx.StaticLine(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL)
        self.bSizer_top.Add(self.m_staticline511, 0, wx.EXPAND, 5)
        
        fgSizer86 = wx.FlexGridSizer(0, 2, 0, 0)
        fgSizer86.AddGrowableCol(1)
        fgSizer86.SetFlexibleDirection(wx.HORIZONTAL)
        fgSizer86.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)
        
        self.m_staticText55 = wx.StaticText(self, wx.ID_ANY, u"Notes", wx.DefaultPosition, wx.DefaultSize,
                                            wx.ALIGN_LEFT)
        self.m_staticText55.Wrap(-1)
        
        fgSizer86.Add(self.m_staticText55, 1, wx.ALL | wx.EXPAND, 5)
        
        self.p_notes = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize,
                                   wx.TE_MULTILINE | wx.TE_NO_VSCROLL)
        fgSizer86.Add(self.p_notes, 1, wx.ALL | wx.EXPAND, 5)
        
        self.bSizer_top.Add(fgSizer86, 0, wx.EXPAND, 5)
        
        self.m_staticline5 = wx.StaticLine(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL)
        self.bSizer_top.Add(self.m_staticline5, 0, wx.EXPAND, 5)
        
        self.p_message = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize,
                                     wx.TE_MULTILINE | wx.TE_READONLY)
        self.p_message.Hide()
        
        self.bSizer_top.Add(self.p_message, 1, wx.ALL | wx.EXPAND, 5)
        
        self.SetSizer(self.bSizer_top)
        self.Layout()
        self.bSizer_top.Fit(self)
        
        # Connect Events
        self.p_date.Bind(wx.adv.EVT_DATE_CHANGED, self.on_date)
        self.p_supplier.Bind(wx.EVT_COMBOBOX, self.on_parent)
        self.p_grandparent.Bind(wx.EVT_COMBOBOX, self.lookup_supplier)
        self.p_parent.Bind(wx.EVT_COMBOBOX, self.lookup_account)
        self.p_type.Bind(wx.EVT_COMBOBOX, self.lookup_type)
        self.p_categories.Bind(wx.EVT_COMBOBOX, self.lookup_category)
        self.p_subcategories.Bind(wx.EVT_COMBOBOX, self.lookup_subcategory)
        self.p_details.Bind(wx.EVT_COMBOBOX, self.lookup_detail)
    
    def __del__(self):
        pass
    
    # Virtual event handlers, overide them in your derived class
    def on_date(self, event):
        event.Skip()
    
    def on_parent(self, event):
        event.Skip()
    
    def lookup_supplier(self, event):
        event.Skip()
    
    def lookup_account(self, event):
        event.Skip()
    
    def lookup_type(self, event):
        event.Skip()
    
    def lookup_category(self, event):
        event.Skip()
    
    def lookup_subcategory(self, event):
        event.Skip()
    
    def lookup_detail(self, event):
        event.Skip()


###########################################################################
## Class SubAccountEdit
###########################################################################

class SubAccountEdit(wx.Panel):
    
    def __init__(self, parent, id=wx.ID_ANY, pos=wx.DefaultPosition, size=wx.Size(-1, -1),
                 style=wx.BORDER_THEME | wx.TAB_TRAVERSAL, name=u"subaccounts"):
        wx.Panel.__init__(self, parent, id=id, pos=pos, size=size, style=style, name=name)
        
        self.bSizer_top = wx.BoxSizer(wx.VERTICAL)
        
        fgSizer2 = wx.FlexGridSizer(0, 2, 0, 0)
        fgSizer2.AddGrowableCol(1)
        fgSizer2.SetFlexibleDirection(wx.HORIZONTAL)
        fgSizer2.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_NONE)
        
        self.m_staticText61 = wx.StaticText(self, wx.ID_ANY, u"Account", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText61.Wrap(-1)
        
        fgSizer2.Add(self.m_staticText61, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)
        
        p_parentChoices = []
        self.p_parent = wx.ComboBox(self, wx.ID_ANY, u"Combo!", wx.DefaultPosition, wx.DefaultSize, p_parentChoices,
                                    wx.CB_DROPDOWN | wx.CB_READONLY)
        fgSizer2.Add(self.p_parent, 1, wx.ALL | wx.EXPAND, 5)
        
        self.m_staticText1 = wx.StaticText(self, wx.ID_ANY, u"SubAccount Name", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText1.Wrap(-1)
        
        fgSizer2.Add(self.m_staticText1, 0, wx.ALL | wx.EXPAND, 5)
        
        self.p_name = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(-1, -1), 0)
        self.p_name.SetMaxLength(80)
        fgSizer2.Add(self.p_name, 1, wx.ALL | wx.EXPAND, 5)
        
        self.m_staticText11 = wx.StaticText(self, wx.ID_ANY, u"SubAccount Description", wx.DefaultPosition,
                                            wx.DefaultSize, 0)
        self.m_staticText11.Wrap(-1)
        
        fgSizer2.Add(self.m_staticText11, 0, wx.ALL | wx.EXPAND, 5)
        
        self.p_description = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(-1, -1), 0)
        self.p_description.SetMaxLength(80)
        fgSizer2.Add(self.p_description, 1, wx.ALL | wx.EXPAND, 5)
        
        self.bSizer_top.Add(fgSizer2, 0, wx.EXPAND | wx.LEFT | wx.RIGHT, 5)
        
        self.m_staticline51 = wx.StaticLine(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL)
        self.bSizer_top.Add(self.m_staticline51, 0, wx.EXPAND, 5)
        
        bSizer_panels = wx.BoxSizer(wx.HORIZONTAL)
        
        fgSizer14 = wx.FlexGridSizer(0, 2, 0, 0)
        fgSizer14.AddGrowableCol(1)
        fgSizer14.SetFlexibleDirection(wx.HORIZONTAL)
        fgSizer14.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_NONE)
        
        self.m_staticText74 = wx.StaticText(self, wx.ID_ANY, u"Initial Value", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText74.Wrap(-1)
        
        fgSizer14.Add(self.m_staticText74, 0, wx.ALL, 5)
        
        self.p_initial = wx.SpinCtrlDouble(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize,
                                           wx.ALIGN_RIGHT | wx.SP_ARROW_KEYS, -1e+06, 1e+06, 0, 0.01)
        self.p_initial.SetDigits(2)
        fgSizer14.Add(self.p_initial, 0, wx.ALL, 5)
        
        self.m_staticText741 = wx.StaticText(self, wx.ID_ANY, u"Commission", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText741.Wrap(-1)
        
        fgSizer14.Add(self.m_staticText741, 0, wx.ALL, 5)
        
        self.p_commission = wx.SpinCtrlDouble(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize,
                                              wx.ALIGN_RIGHT | wx.SP_ARROW_KEYS, -1e+06, 1e+06, 0, 0.01)
        self.p_commission.SetDigits(2)
        fgSizer14.Add(self.p_commission, 0, wx.ALL, 5)
        
        self.m_staticText7411 = wx.StaticText(self, wx.ID_ANY, u"Rate", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText7411.Wrap(-1)
        
        fgSizer14.Add(self.m_staticText7411, 0, wx.ALL, 5)
        
        self.p_rate = wx.SpinCtrlDouble(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize,
                                        wx.ALIGN_RIGHT | wx.SP_ARROW_KEYS, -1e+06, 1e+06, 0, 0.01)
        self.p_rate.SetDigits(2)
        fgSizer14.Add(self.p_rate, 0, wx.ALL, 5)
        
        bSizer_panels.Add(fgSizer14, 1, wx.ALL | wx.EXPAND, 5)
        
        self.m_staticline32 = wx.StaticLine(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_VERTICAL)
        bSizer_panels.Add(self.m_staticline32, 0, wx.EXPAND | wx.LEFT | wx.RIGHT, 5)
        
        bSizer49 = wx.BoxSizer(wx.VERTICAL)
        
        fgSizer23 = wx.FlexGridSizer(0, 3, 0, 0)
        fgSizer23.AddGrowableCol(1)
        fgSizer23.AddGrowableCol(2)
        fgSizer23.SetFlexibleDirection(wx.HORIZONTAL)
        fgSizer23.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_NONE)
        
        self.m_staticText51 = wx.StaticText(self, wx.ID_ANY, u"Dates Active", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText51.Wrap(-1)
        
        fgSizer23.Add(self.m_staticText51, 0, wx.ALIGN_CENTER | wx.ALL, 5)
        
        self.p_start_date = wx.adv.DatePickerCtrl(self, wx.ID_ANY, wx.DefaultDateTime, wx.DefaultPosition,
                                                  wx.DefaultSize,
                                                  wx.adv.DP_DEFAULT | wx.adv.DP_DROPDOWN | wx.BORDER_SIMPLE)
        fgSizer23.Add(self.p_start_date, 0, wx.ALIGN_BOTTOM | wx.ALL, 10)
        
        self.p_end_date = wx.adv.DatePickerCtrl(self, wx.ID_ANY, wx.DefaultDateTime, wx.DefaultPosition, wx.DefaultSize,
                                                wx.adv.DP_DEFAULT | wx.adv.DP_DROPDOWN | wx.BORDER_SIMPLE)
        fgSizer23.Add(self.p_end_date, 0, wx.ALIGN_BOTTOM | wx.ALL, 10)
        
        bSizer49.Add(fgSizer23, 0, wx.ALIGN_BOTTOM, 5)
        
        bSizer_panels.Add(bSizer49, 1, wx.ALIGN_BOTTOM, 5)
        
        self.bSizer_top.Add(bSizer_panels, 0, wx.EXPAND, 5)
        
        self.m_staticline5 = wx.StaticLine(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL)
        self.bSizer_top.Add(self.m_staticline5, 0, wx.EXPAND, 5)
        
        self.p_message = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize,
                                     wx.TE_MULTILINE | wx.TE_READONLY)
        self.p_message.Hide()
        
        self.bSizer_top.Add(self.p_message, 1, wx.ALL | wx.EXPAND, 5)
        
        self.SetSizer(self.bSizer_top)
        self.Layout()
        self.bSizer_top.Fit(self)
        
        # Connect Events
        self.p_parent.Bind(wx.EVT_COMBOBOX, self.lookup_account)
        self.p_start_date.Bind(wx.adv.EVT_DATE_CHANGED, self.on_start_date)
        self.p_end_date.Bind(wx.adv.EVT_DATE_CHANGED, self.on_end_date)
    
    def __del__(self):
        pass
    
    # Virtual event handlers, overide them in your derived class
    def lookup_account(self, event):
        event.Skip()
    
    def on_start_date(self, event):
        event.Skip()
    
    def on_end_date(self, event):
        event.Skip()


###########################################################################
## Class ContactEdit
###########################################################################

class ContactEdit(wx.Panel):
    
    def __init__(self, parent, id=wx.ID_ANY, pos=wx.DefaultPosition, size=wx.Size(-1, -1),
                 style=wx.BORDER_THEME | wx.TAB_TRAVERSAL, name=u"contacts"):
        wx.Panel.__init__(self, parent, id=id, pos=pos, size=size, style=style, name=name)
        
        self.bSizer_top = wx.BoxSizer(wx.VERTICAL)
        
        fgSizer2 = wx.FlexGridSizer(0, 2, 0, 0)
        fgSizer2.AddGrowableCol(1)
        fgSizer2.SetFlexibleDirection(wx.HORIZONTAL)
        fgSizer2.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_NONE)
        
        self.m_staticText61 = wx.StaticText(self, wx.ID_ANY, u"Company", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText61.Wrap(-1)
        
        fgSizer2.Add(self.m_staticText61, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)
        
        p_parentChoices = []
        self.p_parent = wx.ComboBox(self, wx.ID_ANY, u"Combo!", wx.DefaultPosition, wx.DefaultSize, p_parentChoices,
                                    wx.CB_DROPDOWN | wx.CB_READONLY)
        fgSizer2.Add(self.p_parent, 1, wx.ALL | wx.EXPAND, 5)
        
        self.m_staticText1 = wx.StaticText(self, wx.ID_ANY, u"Name", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText1.Wrap(-1)
        
        fgSizer2.Add(self.m_staticText1, 0, wx.ALL | wx.EXPAND, 5)
        
        self.p_name = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(-1, -1), 0)
        self.p_name.SetMaxLength(80)
        fgSizer2.Add(self.p_name, 1, wx.ALL | wx.EXPAND, 5)
        
        self.bSizer_top.Add(fgSizer2, 0, wx.EXPAND | wx.LEFT | wx.RIGHT, 5)
        
        self.m_staticline51 = wx.StaticLine(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL)
        self.bSizer_top.Add(self.m_staticline51, 0, wx.EXPAND, 5)
        
        bSizer_panels = wx.BoxSizer(wx.HORIZONTAL)
        
        fgSizer14 = wx.FlexGridSizer(0, 2, 20, 0)
        fgSizer14.AddGrowableCol(1)
        fgSizer14.AddGrowableRow(0)
        fgSizer14.SetFlexibleDirection(wx.BOTH)
        fgSizer14.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_NONE)
        
        self.m_staticText73 = wx.StaticText(self, wx.ID_ANY, u"Address", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText73.Wrap(-1)
        
        fgSizer14.Add(self.m_staticText73, 0, wx.ALL, 5)
        
        self.p_address = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize,
                                     wx.TE_MULTILINE)
        fgSizer14.Add(self.p_address, 1, wx.ALL | wx.EXPAND, 5)
        
        bSizer_panels.Add(fgSizer14, 1, wx.ALL | wx.EXPAND, 5)
        
        self.m_staticline32 = wx.StaticLine(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_VERTICAL)
        bSizer_panels.Add(self.m_staticline32, 0, wx.EXPAND | wx.LEFT | wx.RIGHT, 5)
        
        bSizer49 = wx.BoxSizer(wx.VERTICAL)
        
        fgSizer31 = wx.FlexGridSizer(0, 2, 0, 0)
        fgSizer31.AddGrowableCol(1)
        fgSizer31.SetFlexibleDirection(wx.BOTH)
        fgSizer31.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_ALL)
        
        self.m_staticText55 = wx.StaticText(self, wx.ID_ANY, u"Phone", wx.DefaultPosition, wx.DefaultSize,
                                            wx.ALIGN_LEFT)
        self.m_staticText55.Wrap(-1)
        
        fgSizer31.Add(self.m_staticText55, 1, wx.ALL | wx.EXPAND, 5)
        
        self.p_phone = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        fgSizer31.Add(self.p_phone, 1, wx.ALL | wx.EXPAND, 5)
        
        self.m_staticText551 = wx.StaticText(self, wx.ID_ANY, u"Mobile", wx.DefaultPosition, wx.DefaultSize,
                                             wx.ALIGN_LEFT)
        self.m_staticText551.Wrap(-1)
        
        fgSizer31.Add(self.m_staticText551, 0, wx.ALL, 5)
        
        self.p_mobile = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        fgSizer31.Add(self.p_mobile, 0, wx.ALL | wx.EXPAND, 5)
        
        self.m_staticText70 = wx.StaticText(self, wx.ID_ANY, u"e-mail", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText70.Wrap(-1)
        
        fgSizer31.Add(self.m_staticText70, 0, wx.ALL, 5)
        
        self.p_email = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        fgSizer31.Add(self.p_email, 1, wx.ALL | wx.EXPAND, 5)
        
        bSizer49.Add(fgSizer31, 1, wx.ALL | wx.EXPAND, 5)
        
        fgSizer23 = wx.FlexGridSizer(0, 3, 0, 0)
        fgSizer23.AddGrowableCol(1)
        fgSizer23.AddGrowableCol(2)
        fgSizer23.SetFlexibleDirection(wx.HORIZONTAL)
        fgSizer23.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_NONE)
        
        self.m_staticText51 = wx.StaticText(self, wx.ID_ANY, u"Dates Active", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText51.Wrap(-1)
        
        fgSizer23.Add(self.m_staticText51, 0, wx.ALIGN_CENTER | wx.ALL, 5)
        
        self.p_start_date = wx.adv.DatePickerCtrl(self, wx.ID_ANY, wx.DefaultDateTime, wx.DefaultPosition,
                                                  wx.DefaultSize,
                                                  wx.adv.DP_DEFAULT | wx.adv.DP_DROPDOWN | wx.BORDER_SIMPLE)
        fgSizer23.Add(self.p_start_date, 0, wx.ALIGN_BOTTOM | wx.ALL, 10)
        
        self.p_end_date = wx.adv.DatePickerCtrl(self, wx.ID_ANY, wx.DefaultDateTime, wx.DefaultPosition, wx.DefaultSize,
                                                wx.adv.DP_DEFAULT | wx.adv.DP_DROPDOWN | wx.BORDER_SIMPLE)
        fgSizer23.Add(self.p_end_date, 0, wx.ALIGN_BOTTOM | wx.ALL, 10)
        
        bSizer49.Add(fgSizer23, 0, wx.ALIGN_BOTTOM, 5)
        
        bSizer_panels.Add(bSizer49, 1, wx.EXPAND, 5)
        
        self.bSizer_top.Add(bSizer_panels, 0, 0, 5)
        
        self.m_staticline5 = wx.StaticLine(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL)
        self.bSizer_top.Add(self.m_staticline5, 0, wx.EXPAND, 5)
        
        self.p_message = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize,
                                     wx.TE_MULTILINE | wx.TE_READONLY)
        self.p_message.Hide()
        
        self.bSizer_top.Add(self.p_message, 1, wx.ALL | wx.EXPAND, 5)
        
        self.SetSizer(self.bSizer_top)
        self.Layout()
        self.bSizer_top.Fit(self)
        
        # Connect Events
        self.p_parent.Bind(wx.EVT_COMBOBOX, self.lookup_supplier)
        self.p_start_date.Bind(wx.adv.EVT_DATE_CHANGED, self.on_start_date)
        self.p_end_date.Bind(wx.adv.EVT_DATE_CHANGED, self.on_end_date)
    
    def __del__(self):
        pass
    
    # Virtual event handlers, overide them in your derived class
    def lookup_supplier(self, event):
        event.Skip()
    
    def on_start_date(self, event):
        event.Skip()
    
    def on_end_date(self, event):
        event.Skip()


###########################################################################
## Class CardEdit
###########################################################################

class CardEdit(wx.Panel):
    
    def __init__(self, parent, id=wx.ID_ANY, pos=wx.DefaultPosition, size=wx.Size(-1, -1),
                 style=wx.BORDER_THEME | wx.TAB_TRAVERSAL, name=u"cards"):
        wx.Panel.__init__(self, parent, id=id, pos=pos, size=size, style=style, name=name)
        
        self.bSizer_top = wx.BoxSizer(wx.VERTICAL)
        
        fgSizer2 = wx.FlexGridSizer(0, 2, 0, 0)
        fgSizer2.AddGrowableCol(1)
        fgSizer2.SetFlexibleDirection(wx.HORIZONTAL)
        fgSizer2.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_NONE)
        
        self.m_staticText61 = wx.StaticText(self, wx.ID_ANY, u"Account", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText61.Wrap(-1)
        
        fgSizer2.Add(self.m_staticText61, 0, wx.ALL, 5)
        
        p_parentChoices = []
        self.p_parent = wx.ComboBox(self, wx.ID_ANY, u"Combo!", wx.DefaultPosition, wx.DefaultSize, p_parentChoices,
                                    wx.CB_DROPDOWN | wx.CB_READONLY)
        fgSizer2.Add(self.p_parent, 0, wx.ALL | wx.EXPAND, 5)
        
        self.m_staticText1 = wx.StaticText(self, wx.ID_ANY, u"Card Name", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText1.Wrap(-1)
        
        fgSizer2.Add(self.m_staticText1, 0, wx.ALL | wx.EXPAND, 5)
        
        self.p_name = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(-1, -1), 0)
        self.p_name.SetMaxLength(80)
        fgSizer2.Add(self.p_name, 1, wx.ALL | wx.EXPAND, 5)
        
        self.m_staticText11 = wx.StaticText(self, wx.ID_ANY, u"Card Long Number", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText11.Wrap(-1)
        
        fgSizer2.Add(self.m_staticText11, 0, wx.ALL | wx.EXPAND, 5)
        
        self.p_long_number = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(-1, -1), 0)
        self.p_long_number.SetMaxLength(16)
        fgSizer2.Add(self.p_long_number, 1, wx.ALL | wx.EXPAND, 5)
        
        self.bSizer_top.Add(fgSizer2, 0, wx.EXPAND | wx.LEFT | wx.RIGHT, 5)
        
        self.m_staticline51 = wx.StaticLine(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL)
        self.bSizer_top.Add(self.m_staticline51, 0, wx.EXPAND, 5)
        
        bSizer_panels = wx.BoxSizer(wx.HORIZONTAL)
        
        fgSizer14 = wx.FlexGridSizer(0, 2, 20, 0)
        fgSizer14.AddGrowableCol(1)
        fgSizer14.AddGrowableRow(0)
        fgSizer14.SetFlexibleDirection(wx.BOTH)
        fgSizer14.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_NONE)
        
        p_typeChoices = [u"Credit Card", u"Debit Card", u"Store Card"]
        self.p_type = wx.RadioBox(self, wx.ID_ANY, u"Card Type", wx.DefaultPosition, wx.DefaultSize, p_typeChoices, 1,
                                  wx.RA_SPECIFY_ROWS)
        self.p_type.SetSelection(0)
        fgSizer14.Add(self.p_type, 0, wx.ALIGN_BOTTOM | wx.ALL | wx.EXPAND, 5)
        
        bSizer_panels.Add(fgSizer14, 1, wx.ALL | wx.EXPAND, 5)
        
        self.m_staticline32 = wx.StaticLine(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_VERTICAL)
        bSizer_panels.Add(self.m_staticline32, 0, wx.EXPAND | wx.LEFT | wx.RIGHT, 5)
        
        bSizer49 = wx.BoxSizer(wx.VERTICAL)
        
        fgSizer23 = wx.FlexGridSizer(0, 3, 0, 0)
        fgSizer23.AddGrowableCol(1)
        fgSizer23.AddGrowableCol(2)
        fgSizer23.SetFlexibleDirection(wx.HORIZONTAL)
        fgSizer23.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_NONE)
        
        self.m_staticText51 = wx.StaticText(self, wx.ID_ANY, u"Dates Active", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText51.Wrap(-1)
        
        fgSizer23.Add(self.m_staticText51, 0, wx.ALIGN_CENTER | wx.ALL, 5)
        
        self.p_start_date = wx.adv.DatePickerCtrl(self, wx.ID_ANY, wx.DefaultDateTime, wx.DefaultPosition,
                                                  wx.DefaultSize,
                                                  wx.adv.DP_DEFAULT | wx.adv.DP_DROPDOWN | wx.BORDER_SIMPLE)
        fgSizer23.Add(self.p_start_date, 0, wx.ALIGN_BOTTOM | wx.ALL, 10)
        
        self.p_end_date = wx.adv.DatePickerCtrl(self, wx.ID_ANY, wx.DefaultDateTime, wx.DefaultPosition, wx.DefaultSize,
                                                wx.adv.DP_DEFAULT | wx.adv.DP_DROPDOWN | wx.BORDER_SIMPLE)
        fgSizer23.Add(self.p_end_date, 0, wx.ALIGN_BOTTOM | wx.ALL, 10)
        
        bSizer49.Add(fgSizer23, 0, wx.ALIGN_BOTTOM, 5)
        
        bSizer_panels.Add(bSizer49, 0, wx.ALIGN_BOTTOM, 5)
        
        self.bSizer_top.Add(bSizer_panels, 0, wx.ALIGN_BOTTOM, 5)
        
        self.m_staticline5 = wx.StaticLine(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL)
        self.bSizer_top.Add(self.m_staticline5, 0, wx.EXPAND, 5)
        
        self.p_message = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize,
                                     wx.TE_MULTILINE | wx.TE_READONLY)
        self.p_message.Hide()
        
        self.bSizer_top.Add(self.p_message, 1, wx.ALL | wx.EXPAND, 5)
        
        self.SetSizer(self.bSizer_top)
        self.Layout()
        self.bSizer_top.Fit(self)
        
        # Connect Events
        self.p_parent.Bind(wx.EVT_COMBOBOX, self.lookup_account)
        self.p_start_date.Bind(wx.adv.EVT_DATE_CHANGED, self.on_start_date)
        self.p_end_date.Bind(wx.adv.EVT_DATE_CHANGED, self.on_end_date)
    
    def __del__(self):
        pass
    
    # Virtual event handlers, overide them in your derived class
    def lookup_account(self, event):
        event.Skip()
    
    def on_start_date(self, event):
        event.Skip()
    
    def on_end_date(self, event):
        event.Skip()


###########################################################################
## Class RulesEdit
###########################################################################

class RulesEdit(wx.Panel):
    
    def __init__(self, parent, id=wx.ID_ANY, pos=wx.DefaultPosition, size=wx.Size(-1, -1),
                 style=wx.BORDER_THEME | wx.TAB_TRAVERSAL, name=u"rules"):
        wx.Panel.__init__(self, parent, id=id, pos=pos, size=size, style=style, name=name)
        
        self.bSizer_top = wx.BoxSizer(wx.VERTICAL)
        
        fgSizer2 = wx.FlexGridSizer(0, 2, 0, 0)
        fgSizer2.AddGrowableCol(1)
        fgSizer2.SetFlexibleDirection(wx.HORIZONTAL)
        fgSizer2.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_NONE)
        
        self.m_staticText1 = wx.StaticText(self, wx.ID_ANY, u"Rule Name", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText1.Wrap(-1)
        
        fgSizer2.Add(self.m_staticText1, 0, wx.ALL | wx.EXPAND, 5)
        
        self.p_name = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(-1, -1), 0)
        self.p_name.SetMaxLength(80)
        fgSizer2.Add(self.p_name, 1, wx.ALL | wx.EXPAND, 5)
        
        self.bSizer_top.Add(fgSizer2, 0, wx.EXPAND | wx.LEFT | wx.RIGHT, 5)
        
        self.m_staticline51 = wx.StaticLine(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL)
        self.bSizer_top.Add(self.m_staticline51, 0, wx.EXPAND, 5)
        
        bSizer_panels = wx.BoxSizer(wx.HORIZONTAL)
        
        fgSizer14 = wx.FlexGridSizer(0, 2, 0, 0)
        fgSizer14.AddGrowableCol(1)
        fgSizer14.SetFlexibleDirection(wx.HORIZONTAL)
        fgSizer14.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)
        
        self.m_staticText74 = wx.StaticText(self, wx.ID_ANY, u"Credit %", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText74.Wrap(-1)
        
        fgSizer14.Add(self.m_staticText74, 0, wx.ALL, 5)
        
        self.p_credit_pc = wx.SpinCtrlDouble(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize,
                                             wx.ALIGN_RIGHT | wx.SP_ARROW_KEYS, -1e+06, 1e+06, 0, 0.01)
        self.p_credit_pc.SetDigits(4)
        fgSizer14.Add(self.p_credit_pc, 0, wx.ALL, 5)
        
        self.m_staticText741 = wx.StaticText(self, wx.ID_ANY, u"Debit %", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText741.Wrap(-1)
        
        fgSizer14.Add(self.m_staticText741, 0, wx.ALL, 5)
        
        self.p_debit_pc = wx.SpinCtrlDouble(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize,
                                            wx.ALIGN_RIGHT | wx.SP_ARROW_KEYS, -1e+06, 1e+06, 0.000000, 0.01)
        self.p_debit_pc.SetDigits(4)
        fgSizer14.Add(self.p_debit_pc, 0, wx.ALL, 5)
        
        self.m_staticText7411 = wx.StaticText(self, wx.ID_ANY, u"Minimum Payment", wx.DefaultPosition, wx.DefaultSize,
                                              0)
        self.m_staticText7411.Wrap(-1)
        
        fgSizer14.Add(self.m_staticText7411, 0, wx.ALL, 5)
        
        self.p_minimum_pay = wx.SpinCtrlDouble(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize,
                                               wx.ALIGN_RIGHT | wx.SP_ARROW_KEYS, -1e+06, 1e+06, 0, 0.01)
        self.p_minimum_pay.SetDigits(2)
        fgSizer14.Add(self.p_minimum_pay, 0, wx.ALL, 5)
        
        self.m_staticText74111 = wx.StaticText(self, wx.ID_ANY, u"Minimum %", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText74111.Wrap(-1)
        
        fgSizer14.Add(self.m_staticText74111, 0, wx.ALL, 5)
        
        self.p_minimum_pc = wx.SpinCtrlDouble(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize,
                                              wx.ALIGN_RIGHT | wx.SP_ARROW_KEYS, -1e+06, 1e+06, 0, 0.01)
        self.p_minimum_pc.SetDigits(2)
        fgSizer14.Add(self.p_minimum_pc, 0, wx.ALL, 5)
        
        self.m_staticText741111 = wx.StaticText(self, wx.ID_ANY, u"Credit Limit", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText741111.Wrap(-1)
        
        fgSizer14.Add(self.m_staticText741111, 0, wx.ALL, 5)
        
        self.p_limit = wx.SpinCtrlDouble(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize,
                                         wx.ALIGN_RIGHT | wx.SP_ARROW_KEYS, -1e+06, 1e+06, 0, 0.01)
        self.p_limit.SetDigits(2)
        fgSizer14.Add(self.p_limit, 0, wx.ALL, 5)
        
        bSizer_panels.Add(fgSizer14, 1, wx.ALL | wx.EXPAND, 5)
        
        self.m_staticline32 = wx.StaticLine(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_VERTICAL)
        bSizer_panels.Add(self.m_staticline32, 0, wx.EXPAND | wx.LEFT | wx.RIGHT, 5)
        
        bSizer49 = wx.BoxSizer(wx.VERTICAL)
        
        fgSizer31 = wx.FlexGridSizer(0, 2, 0, 0)
        fgSizer31.AddGrowableCol(1)
        fgSizer31.SetFlexibleDirection(wx.BOTH)
        fgSizer31.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_ALL)
        
        self.m_staticText71 = wx.StaticText(self, wx.ID_ANY, u"Account", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText71.Wrap(-1)
        
        fgSizer31.Add(self.m_staticText71, 0, wx.ALL, 10)
        
        p_grandparentChoices = []
        self.p_grandparent = wx.ComboBox(self, wx.ID_ANY, u"Combo!", wx.DefaultPosition, wx.DefaultSize,
                                         p_grandparentChoices, wx.CB_DROPDOWN | wx.CB_READONLY)
        fgSizer31.Add(self.p_grandparent, 1, wx.ALL | wx.EXPAND, 5)
        
        self.m_staticText61 = wx.StaticText(self, wx.ID_ANY, u"SubAccount", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText61.Wrap(-1)
        
        fgSizer31.Add(self.m_staticText61, 0, wx.ALL, 10)
        
        p_parentChoices = []
        self.p_parent = wx.ComboBox(self, wx.ID_ANY, u"Combo!", wx.DefaultPosition, wx.DefaultSize, p_parentChoices,
                                    wx.CB_DROPDOWN | wx.CB_READONLY)
        fgSizer31.Add(self.p_parent, 1, wx.ALL | wx.EXPAND, 5)
        
        bSizer49.Add(fgSizer31, 1, wx.ALL | wx.EXPAND, 5)
        
        fgSizer23 = wx.FlexGridSizer(0, 3, 0, 0)
        fgSizer23.AddGrowableCol(1)
        fgSizer23.AddGrowableCol(2)
        fgSizer23.SetFlexibleDirection(wx.HORIZONTAL)
        fgSizer23.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_NONE)
        
        self.m_staticText51 = wx.StaticText(self, wx.ID_ANY, u"Dates Active", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText51.Wrap(-1)
        
        fgSizer23.Add(self.m_staticText51, 0, wx.ALIGN_CENTER | wx.ALL, 5)
        
        self.p_start_date = wx.adv.DatePickerCtrl(self, wx.ID_ANY, wx.DefaultDateTime, wx.DefaultPosition,
                                                  wx.DefaultSize,
                                                  wx.adv.DP_DEFAULT | wx.adv.DP_DROPDOWN | wx.BORDER_SIMPLE)
        fgSizer23.Add(self.p_start_date, 0, wx.ALIGN_BOTTOM | wx.ALL, 10)
        
        self.p_end_date = wx.adv.DatePickerCtrl(self, wx.ID_ANY, wx.DefaultDateTime, wx.DefaultPosition, wx.DefaultSize,
                                                wx.adv.DP_DEFAULT | wx.adv.DP_DROPDOWN | wx.BORDER_SIMPLE)
        fgSizer23.Add(self.p_end_date, 0, wx.ALIGN_BOTTOM | wx.ALL, 10)
        
        bSizer49.Add(fgSizer23, 0, wx.ALIGN_BOTTOM, 5)
        
        bSizer_panels.Add(bSizer49, 1, wx.EXPAND, 5)
        
        self.bSizer_top.Add(bSizer_panels, 0, wx.EXPAND, 5)
        
        self.m_staticline5 = wx.StaticLine(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL)
        self.bSizer_top.Add(self.m_staticline5, 0, wx.EXPAND, 5)
        
        self.p_message = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize,
                                     wx.TE_MULTILINE | wx.TE_READONLY)
        self.p_message.Hide()
        
        self.bSizer_top.Add(self.p_message, 1, wx.ALL | wx.EXPAND, 5)
        
        self.SetSizer(self.bSizer_top)
        self.Layout()
        self.bSizer_top.Fit(self)
        
        # Connect Events
        self.p_grandparent.Bind(wx.EVT_COMBOBOX, self.lookup_account)
        self.p_parent.Bind(wx.EVT_COMBOBOX, self.lookup_subaccount)
        self.p_start_date.Bind(wx.adv.EVT_DATE_CHANGED, self.on_start_date)
        self.p_end_date.Bind(wx.adv.EVT_DATE_CHANGED, self.on_end_date)
    
    def __del__(self):
        pass
    
    # Virtual event handlers, overide them in your derived class
    def lookup_account(self, event):
        event.Skip()
    
    def lookup_subaccount(self, event):
        event.Skip()
    
    def on_start_date(self, event):
        event.Skip()
    
    def on_end_date(self, event):
        event.Skip()
