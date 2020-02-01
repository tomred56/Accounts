# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Oct 26 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.adv
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
        self.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_WINDOW))
        self.SetBackgroundColour(wx.Colour(213, 255, 255))
        
        self.main_menu = wx.MenuBar(0)
        self.file_menu = wx.Menu()
        self.user = wx.MenuItem(self.file_menu, wx.ID_ANY, u"User Logon", wx.EmptyString, wx.ITEM_NORMAL)
        self.file_menu.Append(self.user)
        
        self.exit = wx.MenuItem(self.file_menu, ID_EXIT, u"Exit" + u"\t" + u"alt-x", wx.EmptyString, wx.ITEM_NORMAL)
        self.file_menu.Append(self.exit)
        
        self.main_menu.Append(self.file_menu, u"File")
        
        self.SetMenuBar(self.main_menu)
        
        self.main_sizer = wx.BoxSizer(wx.VERTICAL)
        
        self.p_notebook = wx.Notebook(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0)
        
        self.main_sizer.Add(self.p_notebook, 1, wx.EXPAND | wx.ALL, 5)
        
        self.SetSizer(self.main_sizer)
        self.Layout()
        self.main_sizer.Fit(self)
        self.status_bar = self.CreateStatusBar(3, wx.STB_DEFAULT_STYLE | wx.BORDER_RAISED, wx.ID_ANY)
        
        self.Centre(wx.BOTH)
        
        # Connect Events
        self.Bind(wx.EVT_MENU, self.on_user_logon, id=self.user.GetId())
        self.Bind(wx.EVT_MENU, self.on_quit_button, id=self.exit.GetId())
        self.p_notebook.Bind(wx.EVT_NOTEBOOK_PAGE_CHANGED, self.on_new_page)
        self.p_notebook.Bind(wx.EVT_NOTEBOOK_PAGE_CHANGING, self.on_changing_page)
        self.status_bar.Bind(wx.EVT_LEFT_DCLICK, self.on_status_dclick)
    
    def __del__(self):
        pass
    
    # Virtual event handlers, overide them in your derived class
    def on_user_logon(self, event):
        event.Skip()
    
    def on_quit_button(self, event):
        event.Skip()
    
    def on_new_page(self, event):
        event.Skip()
    
    def on_changing_page(self, event):
        event.Skip()
    
    def on_status_dclick(self, event):
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
        
        tab_suppliers_top = wx.BoxSizer(wx.VERTICAL)
        
        self.m_panel17 = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                  wx.BORDER_SIMPLE | wx.TAB_TRAVERSAL)
        rows = wx.BoxSizer(wx.VERTICAL)
        
        self.m_grid1 = wx.grid.Grid(self.m_panel17, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0)
        
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
        
        self.m_panel17.SetSizer(rows)
        self.m_panel17.Layout()
        rows.Fit(self.m_panel17)
        tab_suppliers_top.Add(self.m_panel17, 1, wx.EXPAND | wx.ALL, 5)
        
        self.m_panel18 = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                  wx.BORDER_SIMPLE | wx.TAB_TRAVERSAL)
        single = wx.BoxSizer(wx.VERTICAL)
        
        fgSizer21 = wx.FlexGridSizer(0, 2, 0, 0)
        fgSizer21.AddGrowableCol(1)
        fgSizer21.SetFlexibleDirection(wx.HORIZONTAL)
        fgSizer21.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_NONE)
        
        self.m_staticText12 = wx.StaticText(self.m_panel18, wx.ID_ANY, u"Supplier Name", wx.DefaultPosition,
                                            wx.DefaultSize, 0)
        self.m_staticText12.Wrap(-1)
        
        fgSizer21.Add(self.m_staticText12, 0, wx.ALL | wx.EXPAND, 5)
        
        self.p_name1 = wx.TextCtrl(self.m_panel18, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(-1, -1), 0)
        self.p_name1.SetMaxLength(80)
        fgSizer21.Add(self.p_name1, 1, wx.ALL | wx.EXPAND, 5)
        
        self.m_staticText111 = wx.StaticText(self.m_panel18, wx.ID_ANY, u"Web Address", wx.DefaultPosition,
                                             wx.DefaultSize, 0)
        self.m_staticText111.Wrap(-1)
        
        fgSizer21.Add(self.m_staticText111, 0, wx.ALL | wx.EXPAND, 5)
        
        self.p_web1 = wx.TextCtrl(self.m_panel18, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(-1, -1),
                                  wx.TE_AUTO_URL | wx.TE_RICH2)
        self.p_web1.SetMaxLength(80)
        fgSizer21.Add(self.p_web1, 1, wx.ALL | wx.EXPAND, 5)
        
        single.Add(fgSizer21, 0, wx.EXPAND | wx.LEFT | wx.RIGHT, 5)
        
        self.m_staticline511 = wx.StaticLine(self.m_panel18, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                             wx.LI_HORIZONTAL)
        single.Add(self.m_staticline511, 0, wx.EXPAND | wx.ALL, 5)
        
        bSizer_panels1 = wx.BoxSizer(wx.HORIZONTAL)
        
        fgSizer141 = wx.FlexGridSizer(0, 2, 0, 0)
        fgSizer141.AddGrowableCol(1)
        fgSizer141.AddGrowableRow(0)
        fgSizer141.SetFlexibleDirection(wx.BOTH)
        fgSizer141.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_NONE)
        
        self.m_staticText731 = wx.StaticText(self.m_panel18, wx.ID_ANY, u"Address", wx.DefaultPosition, wx.DefaultSize,
                                             0)
        self.m_staticText731.Wrap(-1)
        
        fgSizer141.Add(self.m_staticText731, 0, wx.ALL, 5)
        
        self.p_address1 = wx.TextCtrl(self.m_panel18, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize,
                                      wx.TE_MULTILINE)
        self.p_address1.SetMinSize(wx.Size(-1, 75))
        
        fgSizer141.Add(self.p_address1, 1, wx.ALL | wx.EXPAND, 5)
        
        self.m_staticText551 = wx.StaticText(self.m_panel18, wx.ID_ANY, u"Phone", wx.DefaultPosition, wx.DefaultSize,
                                             wx.ALIGN_LEFT)
        self.m_staticText551.Wrap(-1)
        
        fgSizer141.Add(self.m_staticText551, 1, wx.ALL | wx.EXPAND, 5)
        
        self.p_phone1 = wx.TextCtrl(self.m_panel18, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        fgSizer141.Add(self.p_phone1, 1, wx.ALL | wx.EXPAND, 5)
        
        self.m_staticText701 = wx.StaticText(self.m_panel18, wx.ID_ANY, u"e-mail", wx.DefaultPosition, wx.DefaultSize,
                                             0)
        self.m_staticText701.Wrap(-1)
        
        fgSizer141.Add(self.m_staticText701, 0, wx.ALL, 5)
        
        self.p_email1 = wx.TextCtrl(self.m_panel18, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        fgSizer141.Add(self.p_email1, 1, wx.ALL | wx.EXPAND, 5)
        
        bSizer_panels1.Add(fgSizer141, 0, wx.ALL | wx.EXPAND, 5)
        
        self.m_staticline321 = wx.StaticLine(self.m_panel18, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                             wx.LI_VERTICAL)
        bSizer_panels1.Add(self.m_staticline321, 0, wx.EXPAND | wx.LEFT | wx.RIGHT, 5)
        
        bSizer491 = wx.BoxSizer(wx.VERTICAL)
        
        self.p_is_financial1 = wx.CheckBox(self.m_panel18, wx.ID_ANY, u"Financial Institution?", wx.DefaultPosition,
                                           wx.DefaultSize, 0)
        bSizer491.Add(self.p_is_financial1, 0, wx.ALL, 5)
        
        fgSizer311 = wx.FlexGridSizer(0, 2, 0, 0)
        fgSizer311.AddGrowableCol(1)
        fgSizer311.SetFlexibleDirection(wx.BOTH)
        fgSizer311.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_ALL)
        
        self.m_staticText112 = wx.StaticText(self.m_panel18, wx.ID_ANY, u"Online Access", wx.DefaultPosition,
                                             wx.DefaultSize, 0)
        self.m_staticText112.Wrap(-1)
        
        fgSizer311.Add(self.m_staticText112, 0, wx.ALIGN_CENTER_VERTICAL, 5)
        
        self.p_online = wx.TextCtrl(self.m_panel18, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(-1, -1),
                                    wx.TE_AUTO_URL | wx.TE_RICH2)
        self.p_online.SetMaxLength(80)
        fgSizer311.Add(self.p_online, 0, wx.ALL | wx.EXPAND, 5)
        
        bSizer491.Add(fgSizer311, 1, wx.ALL | wx.EXPAND, 5)
        
        bSizer491.Add((0, 0), 1, wx.EXPAND, 5)
        
        fgSizer231 = wx.FlexGridSizer(0, 3, 0, 0)
        fgSizer231.AddGrowableCol(1)
        fgSizer231.AddGrowableCol(2)
        fgSizer231.SetFlexibleDirection(wx.HORIZONTAL)
        fgSizer231.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_NONE)
        
        self.m_staticText511 = wx.StaticText(self.m_panel18, wx.ID_ANY, u"Dates Active", wx.DefaultPosition,
                                             wx.DefaultSize, 0)
        self.m_staticText511.Wrap(-1)
        
        fgSizer231.Add(self.m_staticText511, 0, wx.ALIGN_CENTER | wx.ALL, 5)
        
        self.p_start_date1 = wx.adv.DatePickerCtrl(self.m_panel18, wx.ID_ANY, wx.DefaultDateTime, wx.DefaultPosition,
                                                   wx.DefaultSize,
                                                   wx.adv.DP_DEFAULT | wx.adv.DP_DROPDOWN | wx.BORDER_SIMPLE)
        fgSizer231.Add(self.p_start_date1, 0, wx.ALIGN_BOTTOM | wx.ALL, 10)
        
        self.p_end_date1 = wx.adv.DatePickerCtrl(self.m_panel18, wx.ID_ANY, wx.DefaultDateTime, wx.DefaultPosition,
                                                 wx.DefaultSize,
                                                 wx.adv.DP_DEFAULT | wx.adv.DP_DROPDOWN | wx.BORDER_SIMPLE)
        fgSizer231.Add(self.p_end_date1, 0, wx.ALIGN_BOTTOM | wx.ALL, 10)
        
        bSizer491.Add(fgSizer231, 0, wx.ALIGN_BOTTOM, 5)
        
        self.m_staticline52 = wx.StaticLine(self.m_panel18, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                            wx.LI_HORIZONTAL)
        bSizer491.Add(self.m_staticline52, 0, wx.EXPAND, 5)
        
        bSizer_panels1.Add(bSizer491, 1, wx.EXPAND, 5)
        
        single.Add(bSizer_panels1, 0, wx.EXPAND, 5)
        
        self.m_panel18.SetSizer(single)
        self.m_panel18.Layout()
        single.Fit(self.m_panel18)
        tab_suppliers_top.Add(self.m_panel18, 0, wx.EXPAND | wx.ALL, 5)
        
        self.tree_buttons1 = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                      wx.BORDER_SIMPLE | wx.TAB_TRAVERSAL)
        buttons_sizer2 = wx.BoxSizer(wx.HORIZONTAL)
        
        buttons_sizer2.Add((0, 0), 1, wx.EXPAND, 5)
        
        self.b_new2 = wx.Button(self.tree_buttons1, wx.ID_ANY, u"New", wx.DefaultPosition, wx.DefaultSize,
                                0 | wx.BORDER_RAISED)
        self.b_new2.Enable(False)
        self.b_new2.SetToolTip(u"Add a New Row")
        
        buttons_sizer2.Add(self.b_new2, 0, wx.ALIGN_BOTTOM | wx.ALIGN_RIGHT | wx.ALL | wx.RESERVE_SPACE_EVEN_IF_HIDDEN,
                           5)
        
        self.b_edit2 = wx.Button(self.tree_buttons1, wx.ID_ANY, u"Edit", wx.DefaultPosition, wx.DefaultSize,
                                 0 | wx.BORDER_RAISED)
        self.b_edit2.Enable(False)
        self.b_edit2.SetToolTip(u"Edit Currently Selected Row")
        
        buttons_sizer2.Add(self.b_edit2, 0, wx.ALIGN_BOTTOM | wx.ALIGN_RIGHT | wx.ALL | wx.RESERVE_SPACE_EVEN_IF_HIDDEN,
                           5)
        
        self.b_reset2 = wx.Button(self.tree_buttons1, wx.ID_ANY, u"Reset", wx.DefaultPosition, wx.DefaultSize,
                                  0 | wx.BORDER_RAISED)
        self.b_reset2.Enable(False)
        self.b_reset2.SetToolTip(u"Reset Original Values")
        
        buttons_sizer2.Add(self.b_reset2, 0,
                           wx.ALIGN_BOTTOM | wx.ALIGN_RIGHT | wx.ALL | wx.RESERVE_SPACE_EVEN_IF_HIDDEN, 5)
        
        self.b_apply2 = wx.Button(self.tree_buttons1, wx.ID_ANY, u"Apply", wx.DefaultPosition, wx.DefaultSize,
                                  0 | wx.BORDER_RAISED)
        self.b_apply2.Enable(False)
        self.b_apply2.SetToolTip(u"Save Changes")
        
        buttons_sizer2.Add(self.b_apply2, 0,
                           wx.ALIGN_BOTTOM | wx.ALIGN_RIGHT | wx.ALL | wx.RESERVE_SPACE_EVEN_IF_HIDDEN, 5)
        
        self.b_cancel2 = wx.Button(self.tree_buttons1, wx.ID_ANY, u"Cancel", wx.DefaultPosition, wx.DefaultSize,
                                   0 | wx.BORDER_RAISED)
        self.b_cancel2.Enable(False)
        self.b_cancel2.SetToolTip(u"Cancel Changes Without Saving")
        
        buttons_sizer2.Add(self.b_cancel2, 0,
                           wx.ALIGN_BOTTOM | wx.ALIGN_RIGHT | wx.ALL | wx.RESERVE_SPACE_EVEN_IF_HIDDEN, 5)
        
        self.b_exit2 = wx.Button(self.tree_buttons1, wx.ID_ANY, u"Exit", wx.DefaultPosition, wx.DefaultSize,
                                 0 | wx.BORDER_RAISED)
        self.b_exit2.SetToolTip(u"Close App")
        
        buttons_sizer2.Add(self.b_exit2, 0,
                           wx.ALIGN_BOTTOM | wx.ALIGN_CENTER | wx.ALIGN_RIGHT | wx.ALL | wx.RESERVE_SPACE_EVEN_IF_HIDDEN,
                           5)
        
        self.tree_buttons1.SetSizer(buttons_sizer2)
        self.tree_buttons1.Layout()
        buttons_sizer2.Fit(self.tree_buttons1)
        tab_suppliers_top.Add(self.tree_buttons1, 0, wx.EXPAND | wx.ALL, 5)
        
        self.bSizer_top.Add(tab_suppliers_top, 1, wx.EXPAND, 5)
        
        self.SetSizer(self.bSizer_top)
        self.Layout()
        self.bSizer_top.Fit(self)
        
        # Connect Events
        self.p_start_date.Bind(wx.adv.EVT_DATE_CHANGED, self.on_start_date)
        self.p_end_date.Bind(wx.adv.EVT_DATE_CHANGED, self.on_end_date)
        self.p_start_date1.Bind(wx.adv.EVT_DATE_CHANGED, self.on_start_date)
        self.p_end_date1.Bind(wx.adv.EVT_DATE_CHANGED, self.on_end_date)
        self.b_new2.Bind(wx.EVT_BUTTON, self.on_new_button)
        self.b_edit2.Bind(wx.EVT_BUTTON, self.on_edit_button)
        self.b_reset2.Bind(wx.EVT_BUTTON, self.on_reset_button)
        self.b_apply2.Bind(wx.EVT_BUTTON, self.on_apply_button)
        self.b_cancel2.Bind(wx.EVT_BUTTON, self.on_cancel_button)
        self.b_exit2.Bind(wx.EVT_BUTTON, self.on_exit_button)
    
    def __del__(self):
        pass
    
    # Virtual event handlers, overide them in your derived class
    def on_start_date(self, event):
        event.Skip()
    
    def on_end_date(self, event):
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
    
    def on_exit_button(self, event):
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
        
        tab_accounts_top = wx.BoxSizer(wx.VERTICAL)
        
        account_rows = wx.BoxSizer(wx.VERTICAL)
        
        self.m_grid11 = wx.grid.Grid(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0)
        
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
        account_rows.Add(self.m_grid11, 0, wx.ALL, 5)
        
        tab_accounts_top.Add(account_rows, 1, wx.EXPAND, 5)
        
        self.account_panel = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                      wx.BORDER_SIMPLE | wx.TAB_TRAVERSAL)
        bSizer56 = wx.BoxSizer(wx.VERTICAL)
        
        fgSizer21 = wx.FlexGridSizer(0, 2, 0, 0)
        fgSizer21.AddGrowableCol(1)
        fgSizer21.SetFlexibleDirection(wx.HORIZONTAL)
        fgSizer21.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_NONE)
        
        self.m_staticText611 = wx.StaticText(self.account_panel, wx.ID_ANY, u"Financial Institution",
                                             wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText611.Wrap(-1)
        
        fgSizer21.Add(self.m_staticText611, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_LEFT | wx.ALL, 5)
        
        p_parent1Choices = [u"Unknown"]
        self.p_parent1 = wx.ComboBox(self.account_panel, wx.ID_ANY, u"Combo!", wx.DefaultPosition, wx.DefaultSize,
                                     p_parent1Choices, wx.CB_DROPDOWN | wx.CB_READONLY, wx.DefaultValidator, u"parent")
        self.p_parent1.SetSelection(0)
        fgSizer21.Add(self.p_parent1, 1, wx.ALL | wx.EXPAND, 5)
        
        self.m_staticText12 = wx.StaticText(self.account_panel, wx.ID_ANY, u"Account Name", wx.DefaultPosition,
                                            wx.DefaultSize, 0)
        self.m_staticText12.Wrap(-1)
        
        fgSizer21.Add(self.m_staticText12, 0, wx.ALL | wx.EXPAND, 5)
        
        self.p_name1 = wx.TextCtrl(self.account_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(-1, -1),
                                   0)
        self.p_name1.SetMaxLength(80)
        fgSizer21.Add(self.p_name1, 1, wx.ALL | wx.EXPAND, 5)
        
        self.m_staticText111 = wx.StaticText(self.account_panel, wx.ID_ANY, u"Account Description", wx.DefaultPosition,
                                             wx.DefaultSize, 0)
        self.m_staticText111.Wrap(-1)
        
        fgSizer21.Add(self.m_staticText111, 0, wx.ALL | wx.EXPAND, 5)
        
        self.p_description1 = wx.TextCtrl(self.account_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                          wx.Size(-1, -1), 0)
        self.p_description1.SetMaxLength(80)
        fgSizer21.Add(self.p_description1, 1, wx.ALL | wx.EXPAND, 5)
        
        bSizer56.Add(fgSizer21, 0, wx.EXPAND | wx.LEFT | wx.RIGHT, 5)
        
        self.m_staticline511 = wx.StaticLine(self.account_panel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                             wx.LI_HORIZONTAL)
        bSizer56.Add(self.m_staticline511, 0, wx.EXPAND, 5)
        
        bSizer_panels1 = wx.BoxSizer(wx.HORIZONTAL)
        
        fgSizer141 = wx.FlexGridSizer(0, 2, 0, 0)
        fgSizer141.AddGrowableCol(1)
        fgSizer141.SetFlexibleDirection(wx.BOTH)
        fgSizer141.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_NONE)
        
        self.m_staticText551 = wx.StaticText(self.account_panel, wx.ID_ANY, u"Sort Code", wx.DefaultPosition,
                                             wx.DefaultSize, wx.ALIGN_LEFT)
        self.m_staticText551.Wrap(-1)
        
        fgSizer141.Add(self.m_staticText551, 0, wx.ALL | wx.EXPAND, 5)
        
        self.p_sort_code1 = wx.lib.masked.TextCtrl(self.account_panel, wx.ID_ANY, u"00-00-00", wx.DefaultPosition,
                                                   wx.DefaultSize, 0, mask=u"##-##-##")
        self.p_sort_code.SetMaxLength(8)
        
        self.p_sort_code1.SetFont(
            wx.Font(wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL,
                    False, wx.EmptyString))
        self.p_sort_code1.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_WINDOW))
        
        fgSizer141.Add(self.p_sort_code1, 0, wx.ALL, 5)
        
        self.m_staticText701 = wx.StaticText(self.account_panel, wx.ID_ANY, u"Account Number", wx.DefaultPosition,
                                             wx.DefaultSize, 0)
        self.m_staticText701.Wrap(-1)
        
        fgSizer141.Add(self.m_staticText701, 0, wx.ALL, 5)
        
        self.p_account_no1 = wx.TextCtrl(self.account_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                         wx.DefaultSize, 0)
        self.p_account_no1.SetMaxLength(8)
        fgSizer141.Add(self.p_account_no1, 1, wx.ALL, 5)
        
        self.m_staticText741 = wx.StaticText(self.account_panel, wx.ID_ANY, u"Initial Value", wx.DefaultPosition,
                                             wx.DefaultSize, 0)
        self.m_staticText741.Wrap(-1)
        
        fgSizer141.Add(self.m_staticText741, 0, wx.ALL, 5)
        
        self.p_initial1 = wx.SpinCtrlDouble(self.account_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                            wx.DefaultSize, wx.ALIGN_RIGHT | wx.SP_ARROW_KEYS, -1e+06, 1e+06, 0, 0.01)
        self.p_initial1.SetDigits(2)
        fgSizer141.Add(self.p_initial1, 0, wx.ALL, 5)
        
        bSizer_panels1.Add(fgSizer141, 0, wx.ALL, 5)
        
        self.m_staticline321 = wx.StaticLine(self.account_panel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                             wx.LI_VERTICAL)
        bSizer_panels1.Add(self.m_staticline321, 0, wx.EXPAND | wx.LEFT | wx.RIGHT, 5)
        
        bSizer491 = wx.BoxSizer(wx.VERTICAL)
        
        fgSizer311 = wx.FlexGridSizer(0, 2, 0, 0)
        fgSizer311.AddGrowableCol(1)
        fgSizer311.SetFlexibleDirection(wx.BOTH)
        fgSizer311.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_ALL)
        
        self.m_staticText711 = wx.StaticText(self.account_panel, wx.ID_ANY, u"Account Holder", wx.DefaultPosition,
                                             wx.DefaultSize, 0)
        self.m_staticText711.Wrap(-1)
        
        fgSizer311.Add(self.m_staticText711, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)
        
        p_holder1Choices = [u"Dermot", u"Fenella", u"Joint", u"Other"]
        self.p_holder1 = wx.ComboBox(self.account_panel, wx.ID_ANY, u"Dermot", wx.DefaultPosition, wx.DefaultSize,
                                     p_holder1Choices, wx.CB_DROPDOWN | wx.CB_READONLY)
        self.p_holder1.SetSelection(0)
        fgSizer311.Add(self.p_holder1, 1, wx.ALL | wx.EXPAND, 5)
        
        self.m_staticText731 = wx.StaticText(self.account_panel, wx.ID_ANY, u"Account Type", wx.DefaultPosition,
                                             wx.DefaultSize, 0)
        self.m_staticText731.Wrap(-1)
        
        fgSizer311.Add(self.m_staticText731, 0, wx.ALL, 5)
        
        p_type1Choices = [u"Current", u"Savings", u"ISA", u"Credit Card", u"Loan", u"Mortgage", u"Cash", u"Shares",
                          u"Current", u"Insurance"]
        self.p_type1 = wx.ComboBox(self.account_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize,
                                   p_type1Choices, wx.CB_DROPDOWN | wx.CB_READONLY)
        self.p_type1.SetSelection(10)
        fgSizer311.Add(self.p_type1, 0, wx.ALL | wx.EXPAND, 5)
        
        bSizer491.Add(fgSizer311, 0, wx.ALL, 5)
        
        bSizer491.Add((0, 0), 1, wx.EXPAND, 5)
        
        fgSizer231 = wx.FlexGridSizer(0, 3, 0, 0)
        fgSizer231.AddGrowableCol(1)
        fgSizer231.AddGrowableCol(2)
        fgSizer231.SetFlexibleDirection(wx.HORIZONTAL)
        fgSizer231.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_NONE)
        
        self.m_staticText511 = wx.StaticText(self.account_panel, wx.ID_ANY, u"Dates Active", wx.DefaultPosition,
                                             wx.DefaultSize, 0)
        self.m_staticText511.Wrap(-1)
        
        fgSizer231.Add(self.m_staticText511, 0, wx.ALIGN_CENTER | wx.ALL, 5)
        
        self.p_start_date1 = wx.adv.DatePickerCtrl(self.account_panel, wx.ID_ANY, wx.DefaultDateTime,
                                                   wx.DefaultPosition, wx.DefaultSize,
                                                   wx.adv.DP_DEFAULT | wx.adv.DP_DROPDOWN | wx.BORDER_SIMPLE)
        fgSizer231.Add(self.p_start_date1, 0, wx.ALIGN_BOTTOM | wx.ALL, 10)
        
        self.p_end_date1 = wx.adv.DatePickerCtrl(self.account_panel, wx.ID_ANY, wx.DefaultDateTime, wx.DefaultPosition,
                                                 wx.DefaultSize,
                                                 wx.adv.DP_DEFAULT | wx.adv.DP_DROPDOWN | wx.BORDER_SIMPLE)
        fgSizer231.Add(self.p_end_date1, 0, wx.ALIGN_BOTTOM | wx.ALL, 10)
        
        bSizer491.Add(fgSizer231, 0, wx.ALIGN_BOTTOM, 5)
        
        bSizer_panels1.Add(bSizer491, 0, wx.EXPAND, 5)
        
        bSizer56.Add(bSizer_panels1, 0, wx.EXPAND, 5)
        
        self.m_staticline52 = wx.StaticLine(self.account_panel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                            wx.LI_HORIZONTAL)
        bSizer56.Add(self.m_staticline52, 0, wx.EXPAND, 5)
        
        self.account_panel.SetSizer(bSizer56)
        self.account_panel.Layout()
        bSizer56.Fit(self.account_panel)
        tab_accounts_top.Add(self.account_panel, 1, wx.EXPAND | wx.ALL, 5)
        
        self.account_buttons = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                        wx.BORDER_SIMPLE | wx.TAB_TRAVERSAL)
        buttons_sizer1 = wx.BoxSizer(wx.HORIZONTAL)
        
        buttons_sizer1.Add((0, 0), 1, wx.EXPAND, 5)
        
        self.b_new1 = wx.Button(self.account_buttons, wx.ID_ANY, u"New", wx.DefaultPosition, wx.DefaultSize,
                                0 | wx.BORDER_RAISED)
        self.b_new1.Enable(False)
        self.b_new1.SetToolTip(u"Add a New Row")
        
        buttons_sizer1.Add(self.b_new1, 0, wx.ALIGN_BOTTOM | wx.ALIGN_RIGHT | wx.ALL | wx.RESERVE_SPACE_EVEN_IF_HIDDEN,
                           5)
        
        self.b_edit1 = wx.Button(self.account_buttons, wx.ID_ANY, u"Edit", wx.DefaultPosition, wx.DefaultSize,
                                 0 | wx.BORDER_RAISED)
        self.b_edit1.Enable(False)
        self.b_edit1.SetToolTip(u"Edit Currently Selected Row")
        
        buttons_sizer1.Add(self.b_edit1, 0, wx.ALIGN_BOTTOM | wx.ALIGN_RIGHT | wx.ALL | wx.RESERVE_SPACE_EVEN_IF_HIDDEN,
                           5)
        
        self.b_reset1 = wx.Button(self.account_buttons, wx.ID_ANY, u"Reset", wx.DefaultPosition, wx.DefaultSize,
                                  0 | wx.BORDER_RAISED)
        self.b_reset1.Enable(False)
        self.b_reset1.SetToolTip(u"Reset Original Values")
        
        buttons_sizer1.Add(self.b_reset1, 0,
                           wx.ALIGN_BOTTOM | wx.ALIGN_RIGHT | wx.ALL | wx.RESERVE_SPACE_EVEN_IF_HIDDEN, 5)
        
        self.b_apply1 = wx.Button(self.account_buttons, wx.ID_ANY, u"Apply", wx.DefaultPosition, wx.DefaultSize,
                                  0 | wx.BORDER_RAISED)
        self.b_apply1.Enable(False)
        self.b_apply1.SetToolTip(u"Save Changes")
        
        buttons_sizer1.Add(self.b_apply1, 0,
                           wx.ALIGN_BOTTOM | wx.ALIGN_RIGHT | wx.ALL | wx.RESERVE_SPACE_EVEN_IF_HIDDEN, 5)
        
        self.b_cancel1 = wx.Button(self.account_buttons, wx.ID_ANY, u"Cancel", wx.DefaultPosition, wx.DefaultSize,
                                   0 | wx.BORDER_RAISED)
        self.b_cancel1.Enable(False)
        self.b_cancel1.SetToolTip(u"Cancel Changes Without Saving")
        
        buttons_sizer1.Add(self.b_cancel1, 0,
                           wx.ALIGN_BOTTOM | wx.ALIGN_RIGHT | wx.ALL | wx.RESERVE_SPACE_EVEN_IF_HIDDEN, 5)
        
        self.b_exit1 = wx.Button(self.account_buttons, wx.ID_ANY, u"Exit", wx.DefaultPosition, wx.DefaultSize,
                                 0 | wx.BORDER_RAISED)
        self.b_exit1.SetToolTip(u"Close App")
        
        buttons_sizer1.Add(self.b_exit1, 0,
                           wx.ALIGN_BOTTOM | wx.ALIGN_CENTER | wx.ALIGN_RIGHT | wx.ALL | wx.RESERVE_SPACE_EVEN_IF_HIDDEN,
                           5)
        
        self.account_buttons.SetSizer(buttons_sizer1)
        self.account_buttons.Layout()
        buttons_sizer1.Fit(self.account_buttons)
        tab_accounts_top.Add(self.account_buttons, 0, wx.EXPAND | wx.ALL, 5)
        
        self.bSizer_top.Add(tab_accounts_top, 1, wx.EXPAND, 5)
        
        self.SetSizer(self.bSizer_top)
        self.Layout()
        self.bSizer_top.Fit(self)
        
        # Connect Events
        self.p_parent.Bind(wx.EVT_COMBOBOX, self._on_lookup)
        self.p_holder.Bind(wx.EVT_COMBOBOX, self.on_grandparent)
        self.p_start_date.Bind(wx.adv.EVT_DATE_CHANGED, self.on_start_date)
        self.p_end_date.Bind(wx.adv.EVT_DATE_CHANGED, self.on_end_date)
        self.p_parent1.Bind(wx.EVT_COMBOBOX, self._on_lookup)
        self.p_holder1.Bind(wx.EVT_COMBOBOX, self.on_grandparent)
        self.p_start_date1.Bind(wx.adv.EVT_DATE_CHANGED, self.on_start_date)
        self.p_end_date1.Bind(wx.adv.EVT_DATE_CHANGED, self.on_end_date)
        self.b_new1.Bind(wx.EVT_BUTTON, self.on_new_button)
        self.b_edit1.Bind(wx.EVT_BUTTON, self.on_edit_button)
        self.b_reset1.Bind(wx.EVT_BUTTON, self.on_reset_button)
        self.b_apply1.Bind(wx.EVT_BUTTON, self.on_apply_button)
        self.b_cancel1.Bind(wx.EVT_BUTTON, self.on_cancel_button)
        self.b_exit1.Bind(wx.EVT_BUTTON, self.on_exit_button)
    
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
    
    def on_exit_button(self, event):
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


###########################################################################
## Class TreeManager
###########################################################################

class TreeManager(wx.Panel):
    
    def __init__(self, parent, id=wx.ID_ANY, pos=wx.DefaultPosition, size=wx.Size(-1, -1), style=wx.TAB_TRAVERSAL,
                 name=wx.EmptyString):
        wx.Panel.__init__(self, parent, id=id, pos=pos, size=size, style=style, name=name)
        
        self.SetBackgroundColour(wx.Colour(213, 255, 255))
        
        tree_top = wx.BoxSizer(wx.VERTICAL)
        
        self.tree_tree = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        bSizer50 = wx.BoxSizer(wx.VERTICAL)
        
        self.tree_trunk = wx.TreeCtrl(self.tree_tree, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                      wx.TR_DEFAULT_STYLE | wx.TR_HIDE_ROOT | wx.BORDER_SUNKEN)
        self.tree_menu = wx.Menu()
        self.m_add_peer = wx.MenuItem(self.tree_menu, wx.ID_ANY, u"Add Peer" + u"\t" + u"alt-1", wx.EmptyString,
                                      wx.ITEM_NORMAL)
        self.tree_menu.Append(self.m_add_peer)
        
        self.m_add_child = wx.MenuItem(self.tree_menu, wx.ID_ANY, u"Add Child" + u"\t" + u"alt-2", wx.EmptyString,
                                       wx.ITEM_NORMAL)
        self.tree_menu.Append(self.m_add_child)
        
        self.tree_trunk.Bind(wx.EVT_RIGHT_DOWN, self.tree_trunkOnContextMenu)
        
        bSizer50.Add(self.tree_trunk, 1, wx.ALL | wx.EXPAND, 5)
        
        self.tree_tree.SetSizer(bSizer50)
        self.tree_tree.Layout()
        bSizer50.Fit(self.tree_tree)
        tree_top.Add(self.tree_tree, 1, wx.EXPAND | wx.ALL, 5)
        
        self.tree_panel = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                   wx.BORDER_SIMPLE | wx.TAB_TRAVERSAL)
        self.tree_panel.SetBackgroundColour(wx.Colour(244, 255, 255))
        
        panel_top = wx.BoxSizer(wx.VERTICAL)
        
        self.panel_heading = wx.StaticText(self.tree_panel, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize,
                                           0)
        self.panel_heading.Wrap(-1)
        
        self.panel_heading.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_HIGHLIGHTTEXT))
        self.panel_heading.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_ACTIVECAPTION))
        
        panel_top.Add(self.panel_heading, 0, wx.ALL | wx.EXPAND, 5)
        
        fgSizer211 = wx.FlexGridSizer(1, 2, 0, 0)
        fgSizer211.AddGrowableCol(1)
        fgSizer211.SetFlexibleDirection(wx.HORIZONTAL)
        fgSizer211.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_NONE)
        
        self.m_staticText113 = wx.StaticText(self.tree_panel, wx.ID_ANY, u"Description", wx.DefaultPosition,
                                             wx.DefaultSize, 0)
        self.m_staticText113.Wrap(-1)
        
        fgSizer211.Add(self.m_staticText113, 0, wx.ALL | wx.EXPAND, 5)
        
        self.name = wx.TextCtrl(self.tree_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(-1, -1),
                                wx.TE_PROCESS_ENTER)
        self.name.SetMaxLength(80)
        fgSizer211.Add(self.name, 1, wx.ALL | wx.EXPAND, 5)
        
        panel_top.Add(fgSizer211, 0, wx.EXPAND | wx.LEFT | wx.RIGHT | wx.TOP, 5)
        
        self.m_staticline53 = wx.StaticLine(self.tree_panel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                            wx.LI_HORIZONTAL)
        panel_top.Add(self.m_staticline53, 0, wx.EXPAND, 5)
        
        bSizer_panels11 = wx.BoxSizer(wx.HORIZONTAL)
        
        bSizer_panels11.Add((0, 0), 1, wx.EXPAND, 5)
        
        self.m_staticline7 = wx.StaticLine(self.tree_panel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                           wx.LI_VERTICAL)
        bSizer_panels11.Add(self.m_staticline7, 0, wx.EXPAND | wx.LEFT | wx.RIGHT, 5)
        
        self.m_staticText512 = wx.StaticText(self.tree_panel, wx.ID_ANY, u"Dates Active", wx.DefaultPosition,
                                             wx.DefaultSize, 0)
        self.m_staticText512.Wrap(-1)
        
        bSizer_panels11.Add(self.m_staticText512, 0, wx.ALIGN_CENTER | wx.ALL, 5)
        
        self.start_date = wx.adv.DatePickerCtrl(self.tree_panel, wx.ID_ANY, wx.DefaultDateTime, wx.DefaultPosition,
                                                wx.DefaultSize,
                                                wx.adv.DP_DEFAULT | wx.adv.DP_DROPDOWN | wx.BORDER_SIMPLE)
        bSizer_panels11.Add(self.start_date, 0, wx.ALIGN_BOTTOM | wx.ALL, 10)
        
        self.m_staticText86 = wx.StaticText(self.tree_panel, wx.ID_ANY, u"To", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText86.Wrap(-1)
        
        bSizer_panels11.Add(self.m_staticText86, 0, wx.ALIGN_CENTER | wx.ALL, 5)
        
        self.end_date = wx.adv.DatePickerCtrl(self.tree_panel, wx.ID_ANY, wx.DefaultDateTime, wx.DefaultPosition,
                                              wx.DefaultSize, wx.adv.DP_DEFAULT | wx.adv.DP_DROPDOWN | wx.BORDER_SIMPLE)
        bSizer_panels11.Add(self.end_date, 0, wx.ALIGN_BOTTOM | wx.ALL, 10)
        
        panel_top.Add(bSizer_panels11, 0, wx.ALL | wx.EXPAND, 5)
        
        self.tree_panel.SetSizer(panel_top)
        self.tree_panel.Layout()
        panel_top.Fit(self.tree_panel)
        tree_top.Add(self.tree_panel, 0, wx.ALL | wx.EXPAND, 5)
        
        self.tree_buttons = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                     wx.BORDER_SIMPLE | wx.TAB_TRAVERSAL)
        buttons_sizer = wx.BoxSizer(wx.HORIZONTAL)
        
        buttons_sizer.Add((0, 0), 0, wx.EXPAND, 5)
        
        self.b_new = wx.Button(self.tree_buttons, wx.ID_ANY, u"New", wx.DefaultPosition, wx.DefaultSize,
                               0 | wx.BORDER_RAISED)
        self.b_new.Enable(False)
        self.b_new.SetToolTip(u"Add a New Row")
        
        buttons_sizer.Add(self.b_new, 0,
                          wx.ALIGN_BOTTOM | wx.ALIGN_RIGHT | wx.ALL | wx.EXPAND | wx.RESERVE_SPACE_EVEN_IF_HIDDEN, 5)
        
        self.b_edit = wx.Button(self.tree_buttons, wx.ID_ANY, u"Edit", wx.DefaultPosition, wx.DefaultSize,
                                0 | wx.BORDER_RAISED)
        self.b_edit.Enable(False)
        self.b_edit.SetToolTip(u"Edit Currently Selected Row")
        
        buttons_sizer.Add(self.b_edit, 0,
                          wx.ALIGN_BOTTOM | wx.ALIGN_RIGHT | wx.ALL | wx.EXPAND | wx.RESERVE_SPACE_EVEN_IF_HIDDEN, 5)
        
        self.b_reset = wx.Button(self.tree_buttons, wx.ID_ANY, u"Reset", wx.DefaultPosition, wx.DefaultSize,
                                 0 | wx.BORDER_RAISED)
        self.b_reset.Enable(False)
        self.b_reset.SetToolTip(u"Reset Original Values")
        
        buttons_sizer.Add(self.b_reset, 0,
                          wx.ALIGN_BOTTOM | wx.ALIGN_RIGHT | wx.ALL | wx.EXPAND | wx.RESERVE_SPACE_EVEN_IF_HIDDEN, 5)
        
        self.b_apply = wx.Button(self.tree_buttons, wx.ID_ANY, u"Apply", wx.DefaultPosition, wx.DefaultSize,
                                 0 | wx.BORDER_RAISED)
        self.b_apply.Enable(False)
        self.b_apply.SetToolTip(u"Save Changes")
        
        buttons_sizer.Add(self.b_apply, 0,
                          wx.ALIGN_BOTTOM | wx.ALIGN_RIGHT | wx.ALL | wx.EXPAND | wx.RESERVE_SPACE_EVEN_IF_HIDDEN, 5)
        
        self.b_cancel = wx.Button(self.tree_buttons, wx.ID_ANY, u"Cancel", wx.DefaultPosition, wx.DefaultSize,
                                  0 | wx.BORDER_RAISED)
        self.b_cancel.Enable(False)
        self.b_cancel.SetToolTip(u"Cancel Changes Without Saving")
        
        buttons_sizer.Add(self.b_cancel, 0,
                          wx.ALIGN_BOTTOM | wx.ALIGN_RIGHT | wx.ALL | wx.EXPAND | wx.RESERVE_SPACE_EVEN_IF_HIDDEN, 5)
        
        self.b_exit = wx.Button(self.tree_buttons, wx.ID_ANY, u"Exit", wx.DefaultPosition, wx.DefaultSize,
                                0 | wx.BORDER_RAISED)
        self.b_exit.SetToolTip(u"Close App")
        
        buttons_sizer.Add(self.b_exit, 0,
                          wx.ALIGN_BOTTOM | wx.ALIGN_CENTER | wx.ALIGN_RIGHT | wx.ALL | wx.EXPAND | wx.RESERVE_SPACE_EVEN_IF_HIDDEN,
                          5)
        
        self.tree_buttons.SetSizer(buttons_sizer)
        self.tree_buttons.Layout()
        buttons_sizer.Fit(self.tree_buttons)
        tree_top.Add(self.tree_buttons, 0, wx.ALL | wx.EXPAND, 5)
        
        self.tree_message = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        bSizer49 = wx.BoxSizer(wx.VERTICAL)
        
        self.p_message = wx.TextCtrl(self.tree_message, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize,
                                     wx.TE_MULTILINE | wx.TE_READONLY | wx.BORDER_THEME | wx.FULL_REPAINT_ON_RESIZE)
        self.p_message.Enable(False)
        self.p_message.Hide()
        
        bSizer49.Add(self.p_message, 1, wx.ALL | wx.EXPAND, 5)
        
        self.tree_message.SetSizer(bSizer49)
        self.tree_message.Layout()
        bSizer49.Fit(self.tree_message)
        tree_top.Add(self.tree_message, 0, wx.EXPAND | wx.ALL, 5)
        
        self.SetSizer(tree_top)
        self.Layout()
        tree_top.Fit(self)
        
        # Connect Events
        self.tree_trunk.Bind(wx.EVT_LEFT_DCLICK, self.on_edit)
        self.tree_trunk.Bind(wx.EVT_RIGHT_DOWN, self.on_rdown)
        self.tree_trunk.Bind(wx.EVT_TREE_ITEM_MENU, self.on_menu_called)
        self.tree_trunk.Bind(wx.EVT_TREE_ITEM_RIGHT_CLICK, self.on_menu)
        self.tree_trunk.Bind(wx.EVT_TREE_SEL_CHANGED, self.on_changed_branch)
        self.tree_trunk.Bind(wx.EVT_TREE_SEL_CHANGING, self.on_change_branch)
        self.Bind(wx.EVT_MENU, self.on_menu_item, id=self.m_add_peer.GetId())
        self.Bind(wx.EVT_MENU, self.on_menu_item, id=self.m_add_child.GetId())
        self.name.Bind(wx.EVT_TEXT, self.on_edited)
        self.name.Bind(wx.EVT_TEXT_ENTER, self.on_enter)
        self.start_date.Bind(wx.adv.EVT_DATE_CHANGED, self.on_edited)
        self.end_date.Bind(wx.adv.EVT_DATE_CHANGED, self.on_edited)
        self.b_new.Bind(wx.EVT_BUTTON, self.on_new_button)
        self.b_edit.Bind(wx.EVT_BUTTON, self.on_edit_button)
        self.b_reset.Bind(wx.EVT_BUTTON, self.on_reset_button)
        self.b_apply.Bind(wx.EVT_BUTTON, self.on_apply_button)
        self.b_cancel.Bind(wx.EVT_BUTTON, self.on_cancel_button)
        self.b_exit.Bind(wx.EVT_BUTTON, self.on_exit_button)
    
    def __del__(self):
        pass
    
    # Virtual event handlers, overide them in your derived class
    def on_edit(self, event):
        event.Skip()
    
    def on_rdown(self, event):
        event.Skip()
    
    def on_menu_called(self, event):
        event.Skip()
    
    def on_menu(self, event):
        event.Skip()
    
    def on_changed_branch(self, event):
        event.Skip()
    
    def on_change_branch(self, event):
        event.Skip()
    
    def on_menu_item(self, event):
        event.Skip()
    
    def on_edited(self, event):
        event.Skip()
    
    def on_enter(self, event):
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
    
    def on_exit_button(self, event):
        event.Skip()
    
    def tree_trunkOnContextMenu(self, event):
        self.tree_trunk.PopupMenu(self.tree_menu, event.GetPosition())


###########################################################################
## Class Summary
###########################################################################

class Summary(wx.Panel):
    
    def __init__(self, parent, id=wx.ID_ANY, pos=wx.DefaultPosition, size=wx.Size(500, 300), style=wx.TAB_TRAVERSAL,
                 name=wx.EmptyString):
        wx.Panel.__init__(self, parent, id=id, pos=pos, size=size, style=style, name=name)
        
        tab_summary_top = wx.BoxSizer(wx.VERTICAL)
        
        self.summary_sizer = wx.FlexGridSizer(0, 6, 5, 10)
        self.summary_sizer.AddGrowableCol(0)
        self.summary_sizer.AddGrowableCol(2)
        self.summary_sizer.AddGrowableCol(4)
        self.summary_sizer.SetFlexibleDirection(wx.HORIZONTAL)
        self.summary_sizer.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)
        
        tab_summary_top.Add(self.summary_sizer, 0, wx.ALIGN_CENTER | wx.ALL, 10)
        
        self.SetSizer(tab_summary_top)
        self.Layout()
    
    def __del__(self):
        pass
