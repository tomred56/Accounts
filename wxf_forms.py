# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Oct 26 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.adv
import wx.xrc


###########################################################################
## Class SupplierEdit
###########################################################################

class SupplierEdit(wx.Panel):
    
    def __init__(self, parent, id=wx.ID_ANY, pos=wx.DefaultPosition, size=wx.Size(-1, -1), style=wx.TAB_TRAVERSAL,
                 name=wx.EmptyString):
        wx.Panel.__init__(self, parent, id=id, pos=pos, size=size, style=style, name=name)
        
        bSizer_top = wx.BoxSizer(wx.VERTICAL)
        
        self.header = wx.StaticText(self, wx.ID_ANY, u"Supplier Details", wx.DefaultPosition, wx.DefaultSize,
                                    wx.ALIGN_LEFT | wx.BORDER_RAISED)
        self.header.Wrap(-1)
        
        self.header.SetFont(wx.Font(11, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial"))
        
        bSizer_top.Add(self.header, 0, wx.ALIGN_CENTER | wx.EXPAND, 5)
        
        fgSizer2 = wx.FlexGridSizer(0, 2, 0, 0)
        fgSizer2.AddGrowableCol(1)
        fgSizer2.SetFlexibleDirection(wx.HORIZONTAL)
        fgSizer2.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_NONE)
        
        self.m_staticText1 = wx.StaticText(self, wx.ID_ANY, u"Supplier Name", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText1.Wrap(-1)
        
        fgSizer2.Add(self.m_staticText1, 0, wx.ALL | wx.EXPAND, 5)
        
        self.name = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(-1, -1), 0)
        self.name.SetMaxLength(80)
        fgSizer2.Add(self.name, 1, wx.ALL | wx.EXPAND, 5)
        
        self.m_staticText11 = wx.StaticText(self, wx.ID_ANY, u"Web Address", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText11.Wrap(-1)
        
        fgSizer2.Add(self.m_staticText11, 0, wx.ALL | wx.EXPAND, 5)
        
        self.web = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(-1, -1),
                               wx.TE_AUTO_URL | wx.TE_RICH2)
        self.web.SetMaxLength(80)
        fgSizer2.Add(self.web, 1, wx.ALL | wx.EXPAND, 5)
        
        bSizer_top.Add(fgSizer2, 0, wx.EXPAND | wx.LEFT | wx.RIGHT, 5)
        
        self.m_staticline51 = wx.StaticLine(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL)
        bSizer_top.Add(self.m_staticline51, 0, wx.EXPAND, 5)
        
        bSizer_panels = wx.BoxSizer(wx.HORIZONTAL)
        
        fgSizer14 = wx.FlexGridSizer(0, 2, 0, 0)
        fgSizer14.AddGrowableCol(1)
        fgSizer14.AddGrowableRow(0)
        fgSizer14.SetFlexibleDirection(wx.BOTH)
        fgSizer14.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_NONE)
        
        self.m_staticText73 = wx.StaticText(self, wx.ID_ANY, u"Address", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText73.Wrap(-1)
        
        fgSizer14.Add(self.m_staticText73, 0, wx.ALL, 5)
        
        self.address = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE)
        self.address.SetMinSize(wx.Size(-1, 75))
        
        fgSizer14.Add(self.address, 1, wx.ALL | wx.EXPAND, 5)
        
        self.m_staticText55 = wx.StaticText(self, wx.ID_ANY, u"Phone", wx.DefaultPosition, wx.DefaultSize,
                                            wx.ALIGN_LEFT)
        self.m_staticText55.Wrap(-1)
        
        fgSizer14.Add(self.m_staticText55, 1, wx.ALL | wx.EXPAND, 5)
        
        self.phone = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        fgSizer14.Add(self.phone, 1, wx.ALL | wx.EXPAND, 5)
        
        self.m_staticText70 = wx.StaticText(self, wx.ID_ANY, u"e-mail", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText70.Wrap(-1)
        
        fgSizer14.Add(self.m_staticText70, 0, wx.ALL, 5)
        
        self.email = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        fgSizer14.Add(self.email, 1, wx.ALL | wx.EXPAND, 5)
        
        bSizer_panels.Add(fgSizer14, 1, wx.ALL | wx.EXPAND, 5)
        
        self.m_staticline32 = wx.StaticLine(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_VERTICAL)
        bSizer_panels.Add(self.m_staticline32, 0, wx.EXPAND | wx.LEFT | wx.RIGHT, 5)
        
        bSizer49 = wx.BoxSizer(wx.VERTICAL)
        
        fgSizer31 = wx.FlexGridSizer(0, 2, 0, 0)
        fgSizer31.AddGrowableCol(1)
        fgSizer31.SetFlexibleDirection(wx.BOTH)
        fgSizer31.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_ALL)
        
        self.is_financial = wx.CheckBox(self, wx.ID_ANY, u"Financial Institution?", wx.DefaultPosition, wx.DefaultSize,
                                        0)
        fgSizer31.Add(self.is_financial, 0, wx.ALL, 5)
        
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
        
        self.date_from = wx.adv.DatePickerCtrl(self, wx.ID_ANY, wx.DefaultDateTime, wx.DefaultPosition, wx.DefaultSize,
                                               wx.adv.DP_DEFAULT | wx.adv.DP_DROPDOWN | wx.BORDER_SIMPLE)
        fgSizer23.Add(self.date_from, 0, wx.ALIGN_BOTTOM | wx.ALL, 10)
        
        self.date_to = wx.adv.DatePickerCtrl(self, wx.ID_ANY, wx.DefaultDateTime, wx.DefaultPosition, wx.DefaultSize,
                                             wx.adv.DP_DEFAULT | wx.adv.DP_DROPDOWN | wx.BORDER_SIMPLE)
        fgSizer23.Add(self.date_to, 0, wx.ALIGN_BOTTOM | wx.ALL, 10)
        
        bSizer49.Add(fgSizer23, 0, wx.ALIGN_BOTTOM, 5)
        
        bSizer_panels.Add(bSizer49, 1, wx.EXPAND, 5)
        
        bSizer_top.Add(bSizer_panels, 1, wx.EXPAND, 5)
        
        self.m_staticline5 = wx.StaticLine(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL)
        bSizer_top.Add(self.m_staticline5, 0, wx.EXPAND, 5)
        
        self.SetSizer(bSizer_top)
        self.Layout()
        bSizer_top.Fit(self)

        # Connect Events
        self.date_from.Bind(wx.adv.EVT_DATE_CHANGED, self.on_date_from)
        self.date_to.Bind(wx.adv.EVT_DATE_CHANGED, self.on_date_to)
    
    def __del__(self):
        pass
    
    # Virtual event handlers, overide them in your derived class
    def on_date_from(self, event):
        event.Skip()
    
    def on_date_to(self, event):
        event.Skip()


###########################################################################
## Class AccountEdit
###########################################################################

class AccountEdit(wx.Panel):
    
    def __init__(self, parent, id=wx.ID_ANY, pos=wx.DefaultPosition, size=wx.Size(-1, -1), style=wx.TAB_TRAVERSAL,
                 name=wx.EmptyString):
        wx.Panel.__init__(self, parent, id=id, pos=pos, size=size, style=style, name=name)
        
        bSizer_top = wx.BoxSizer(wx.VERTICAL)
        
        self.m_staticText8 = wx.StaticText(self, wx.ID_ANY, u"Account Details", wx.DefaultPosition, wx.DefaultSize,
                                           wx.ALIGN_LEFT | wx.BORDER_RAISED)
        self.m_staticText8.Wrap(-1)
        
        self.m_staticText8.SetFont(
            wx.Font(11, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial"))
        
        bSizer_top.Add(self.m_staticText8, 0, wx.ALIGN_CENTER | wx.EXPAND, 5)
        
        fgSizer2 = wx.FlexGridSizer(0, 2, 0, 0)
        fgSizer2.AddGrowableCol(1)
        fgSizer2.SetFlexibleDirection(wx.HORIZONTAL)
        fgSizer2.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_NONE)
        
        self.m_staticText61 = wx.StaticText(self, wx.ID_ANY, u"Financial Institution", wx.DefaultPosition,
                                            wx.DefaultSize, 0)
        self.m_staticText61.Wrap(-1)
        
        fgSizer2.Add(self.m_staticText61, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_LEFT | wx.ALL, 5)
        
        parentChoices = []
        self.parent = wx.ComboBox(self, wx.ID_ANY, u"Combo!", wx.DefaultPosition, wx.DefaultSize, parentChoices,
                                  wx.CB_DROPDOWN | wx.CB_READONLY)
        fgSizer2.Add(self.parent, 1, wx.ALL | wx.EXPAND, 5)
        
        self.m_staticText1 = wx.StaticText(self, wx.ID_ANY, u"Account Name", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText1.Wrap(-1)
        
        fgSizer2.Add(self.m_staticText1, 0, wx.ALL | wx.EXPAND, 5)
        
        self.name = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(-1, -1), 0)
        self.name.SetMaxLength(80)
        fgSizer2.Add(self.name, 1, wx.ALL | wx.EXPAND, 5)
        
        self.m_staticText11 = wx.StaticText(self, wx.ID_ANY, u"Account Description", wx.DefaultPosition, wx.DefaultSize,
                                            0)
        self.m_staticText11.Wrap(-1)
        
        fgSizer2.Add(self.m_staticText11, 0, wx.ALL | wx.EXPAND, 5)
        
        self.description = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(-1, -1), 0)
        self.description.SetMaxLength(80)
        fgSizer2.Add(self.description, 1, wx.ALL | wx.EXPAND, 5)
        
        bSizer_top.Add(fgSizer2, 0, wx.EXPAND | wx.LEFT | wx.RIGHT, 5)
        
        self.m_staticline51 = wx.StaticLine(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL)
        bSizer_top.Add(self.m_staticline51, 0, wx.EXPAND, 5)
        
        bSizer_panels = wx.BoxSizer(wx.HORIZONTAL)
        
        fgSizer14 = wx.FlexGridSizer(0, 2, 0, 0)
        fgSizer14.AddGrowableCol(1)
        fgSizer14.SetFlexibleDirection(wx.BOTH)
        fgSizer14.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_NONE)
        
        self.m_staticText55 = wx.StaticText(self, wx.ID_ANY, u"Sort Code", wx.DefaultPosition, wx.DefaultSize,
                                            wx.ALIGN_LEFT)
        self.m_staticText55.Wrap(-1)
        
        fgSizer14.Add(self.m_staticText55, 1, wx.ALL | wx.EXPAND, 5)
        
        fgSizer22 = wx.FlexGridSizer(1, 5, 0, 0)
        fgSizer22.SetFlexibleDirection(wx.HORIZONTAL)
        fgSizer22.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)
        
        self.sort1 = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_CENTER)
        self.sort1.SetMaxLength(2)
        self.sort1.SetMaxSize(wx.Size(30, -1))
        
        fgSizer22.Add(self.sort1, 0, wx.ALL, 5)
        
        self.m_staticText68 = wx.StaticText(self, wx.ID_ANY, u"-", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText68.Wrap(-1)
        
        fgSizer22.Add(self.m_staticText68, 0, wx.ALL, 5)
        
        self.sort2 = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_CENTER)
        self.sort2.SetMaxLength(2)
        self.sort2.SetMaxSize(wx.Size(30, -1))
        
        fgSizer22.Add(self.sort2, 0, wx.ALL, 5)
        
        self.m_staticText69 = wx.StaticText(self, wx.ID_ANY, u"-", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText69.Wrap(-1)
        
        fgSizer22.Add(self.m_staticText69, 0, wx.ALL, 5)
        
        self.sort3 = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_CENTER)
        self.sort3.SetMaxLength(2)
        self.sort3.SetMaxSize(wx.Size(30, -1))
        
        fgSizer22.Add(self.sort3, 0, wx.ALL, 5)
        
        fgSizer14.Add(fgSizer22, 0, 0, 5)
        
        self.m_staticText70 = wx.StaticText(self, wx.ID_ANY, u"Account Number", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText70.Wrap(-1)
        
        fgSizer14.Add(self.m_staticText70, 0, wx.ALL, 5)
        
        self.account_no = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        self.account_no.SetMaxLength(8)
        fgSizer14.Add(self.account_no, 1, wx.ALL, 5)
        
        self.m_staticText74 = wx.StaticText(self, wx.ID_ANY, u"Initial Value", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText74.Wrap(-1)
        
        fgSizer14.Add(self.m_staticText74, 0, wx.ALL, 5)
        
        self.initial = wx.SpinCtrlDouble(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize,
                                         wx.ALIGN_RIGHT | wx.SP_ARROW_KEYS, -1e+06, 1e+06, 0, 0.01)
        self.initial.SetDigits(2)
        fgSizer14.Add(self.initial, 0, wx.ALL, 5)
        
        bSizer_panels.Add(fgSizer14, 1, wx.ALL, 5)
        
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
        
        holderChoices = [u"Dermot", u"Fenella", u"Joint", u"Other"]
        self.holder = wx.ComboBox(self, wx.ID_ANY, u"Dermot", wx.DefaultPosition, wx.DefaultSize, holderChoices,
                                  wx.CB_DROPDOWN | wx.CB_READONLY)
        self.holder.SetSelection(0)
        fgSizer31.Add(self.holder, 1, wx.ALL | wx.EXPAND, 5)
        
        self.m_staticText73 = wx.StaticText(self, wx.ID_ANY, u"Account Type", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText73.Wrap(-1)
        
        fgSizer31.Add(self.m_staticText73, 0, wx.ALL, 5)
        
        typeChoices = [u"Current", u"Savings", u"ISA", u"Credit Card", u"Loan", u"Mortgage", u"Cash", u"Shares",
                       u"Current", u"Insurance"]
        self.type = wx.ComboBox(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, typeChoices,
                                wx.CB_DROPDOWN | wx.CB_READONLY)
        self.type.SetSelection(10)
        fgSizer31.Add(self.type, 0, wx.ALL | wx.EXPAND, 5)
        
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
        
        self.date_from = wx.adv.DatePickerCtrl(self, wx.ID_ANY, wx.DefaultDateTime, wx.DefaultPosition, wx.DefaultSize,
                                               wx.adv.DP_DEFAULT | wx.adv.DP_DROPDOWN | wx.BORDER_SIMPLE)
        fgSizer23.Add(self.date_from, 0, wx.ALIGN_BOTTOM | wx.ALL, 10)
        
        self.date_to = wx.adv.DatePickerCtrl(self, wx.ID_ANY, wx.DefaultDateTime, wx.DefaultPosition, wx.DefaultSize,
                                             wx.adv.DP_DEFAULT | wx.adv.DP_DROPDOWN | wx.BORDER_SIMPLE)
        fgSizer23.Add(self.date_to, 0, wx.ALIGN_BOTTOM | wx.ALL, 10)
        
        bSizer49.Add(fgSizer23, 0, wx.ALIGN_BOTTOM, 5)
        
        bSizer_panels.Add(bSizer49, 1, wx.EXPAND, 5)
        
        bSizer_top.Add(bSizer_panels, 1, wx.EXPAND, 5)
        
        self.m_staticline5 = wx.StaticLine(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL)
        bSizer_top.Add(self.m_staticline5, 0, wx.EXPAND, 5)
        
        self.SetSizer(bSizer_top)
        self.Layout()
        bSizer_top.Fit(self)

        # Connect Events
        self.parent.Bind(wx.EVT_COMBOBOX, self.on_parent)
        self.holder.Bind(wx.EVT_COMBOBOX, self.on_grandparent)
        self.date_from.Bind(wx.adv.EVT_DATE_CHANGED, self.on_date_from)
        self.date_to.Bind(wx.adv.EVT_DATE_CHANGED, self.on_date_to)
    
    def __del__(self):
        pass
    
    # Virtual event handlers, overide them in your derived class
    def on_parent(self, event):
        event.Skip()
    
    def on_grandparent(self, event):
        event.Skip()
    
    def on_date_from(self, event):
        event.Skip()
    
    def on_date_to(self, event):
        event.Skip()


###########################################################################
## Class CategoryEdit
###########################################################################

class CategoryEdit(wx.Panel):
    
    def __init__(self, parent, id=wx.ID_ANY, pos=wx.DefaultPosition, size=wx.Size(-1, -1), style=wx.TAB_TRAVERSAL,
                 name=wx.EmptyString):
        wx.Panel.__init__(self, parent, id=id, pos=pos, size=size, style=style, name=name)
        
        bSizer_top = wx.BoxSizer(wx.VERTICAL)
        
        self.m_staticText8 = wx.StaticText(self, wx.ID_ANY, u"Category Details", wx.DefaultPosition, wx.DefaultSize,
                                           wx.ALIGN_LEFT | wx.BORDER_RAISED)
        self.m_staticText8.Wrap(-1)
        
        self.m_staticText8.SetFont(
            wx.Font(11, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial"))
        
        bSizer_top.Add(self.m_staticText8, 0, wx.ALIGN_CENTER | wx.EXPAND, 5)
        
        fgSizer21 = wx.FlexGridSizer(1, 2, 0, 0)
        fgSizer21.AddGrowableCol(1)
        fgSizer21.SetFlexibleDirection(wx.HORIZONTAL)
        fgSizer21.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_NONE)
        
        self.m_staticText11 = wx.StaticText(self, wx.ID_ANY, u"Description", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText11.Wrap(-1)
        
        fgSizer21.Add(self.m_staticText11, 0, wx.ALL | wx.EXPAND, 5)
        
        self.name = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(-1, -1), 0)
        self.name.SetMaxLength(80)
        fgSizer21.Add(self.name, 1, wx.ALL | wx.EXPAND, 5)
        
        bSizer_top.Add(fgSizer21, 0, wx.EXPAND | wx.LEFT | wx.RIGHT | wx.TOP, 5)
        
        self.m_staticline5 = wx.StaticLine(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL)
        bSizer_top.Add(self.m_staticline5, 0, wx.EXPAND, 5)
        
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
        
        self.date_from = wx.adv.DatePickerCtrl(self, wx.ID_ANY, wx.DefaultDateTime, wx.DefaultPosition, wx.DefaultSize,
                                               wx.adv.DP_DEFAULT | wx.adv.DP_DROPDOWN | wx.BORDER_SIMPLE)
        fgSizer23.Add(self.date_from, 0, wx.ALIGN_BOTTOM | wx.ALL, 10)
        
        self.date_to = wx.adv.DatePickerCtrl(self, wx.ID_ANY, wx.DefaultDateTime, wx.DefaultPosition, wx.DefaultSize,
                                             wx.adv.DP_DEFAULT | wx.adv.DP_DROPDOWN | wx.BORDER_SIMPLE)
        fgSizer23.Add(self.date_to, 0, wx.ALIGN_BOTTOM | wx.ALL, 10)
        
        bSizer49.Add(fgSizer23, 0, wx.ALIGN_BOTTOM, 5)
        
        bSizer_panels1.Add(bSizer49, 1, wx.EXPAND, 5)
        
        bSizer_top.Add(bSizer_panels1, 1, wx.EXPAND, 5)
        
        self.m_staticline6 = wx.StaticLine(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL)
        bSizer_top.Add(self.m_staticline6, 0, wx.EXPAND, 5)
        
        self.SetSizer(bSizer_top)
        self.Layout()
        bSizer_top.Fit(self)

        # Connect Events
        self.date_from.Bind(wx.adv.EVT_DATE_CHANGED, self.on_date_from)
        self.date_to.Bind(wx.adv.EVT_DATE_CHANGED, self.on_date_to)
    
    def __del__(self):
        pass
    
    # Virtual event handlers, overide them in your derived class
    def on_date_from(self, event):
        event.Skip()
    
    def on_date_to(self, event):
        event.Skip()


###########################################################################
## Class SubCatEdit
###########################################################################

class SubCatEdit(wx.Panel):
    
    def __init__(self, parent, id=wx.ID_ANY, pos=wx.DefaultPosition, size=wx.Size(-1, -1), style=wx.TAB_TRAVERSAL,
                 name=wx.EmptyString):
        wx.Panel.__init__(self, parent, id=id, pos=pos, size=size, style=style, name=name)
        
        bSizer_top = wx.BoxSizer(wx.VERTICAL)
        
        self.m_staticText8 = wx.StaticText(self, wx.ID_ANY, u"Subcategory Details", wx.DefaultPosition, wx.DefaultSize,
                                           wx.ALIGN_LEFT | wx.BORDER_RAISED)
        self.m_staticText8.Wrap(-1)
        
        self.m_staticText8.SetFont(
            wx.Font(11, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial"))
        
        bSizer_top.Add(self.m_staticText8, 0, wx.ALIGN_CENTER | wx.EXPAND, 5)
        
        fgSizer2 = wx.FlexGridSizer(0, 2, 0, 0)
        fgSizer2.AddGrowableCol(1)
        fgSizer2.SetFlexibleDirection(wx.HORIZONTAL)
        fgSizer2.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_NONE)
        
        self.m_staticText6 = wx.StaticText(self, wx.ID_ANY, u"Category", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText6.Wrap(-1)
        
        fgSizer2.Add(self.m_staticText6, 0, wx.ALIGN_CENTER | wx.ALL, 5)
        
        parentChoices = []
        self.parent = wx.ComboBox(self, wx.ID_ANY, u"Combo!", wx.DefaultPosition, wx.DefaultSize, parentChoices,
                                  wx.CB_DROPDOWN | wx.CB_READONLY)
        fgSizer2.Add(self.parent, 1, wx.ALL | wx.EXPAND, 5)
        
        self.m_staticText1 = wx.StaticText(self, wx.ID_ANY, u"Description", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText1.Wrap(-1)
        
        fgSizer2.Add(self.m_staticText1, 0, wx.ALL | wx.EXPAND, 5)
        
        self.name = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(-1, -1), 0)
        self.name.SetMaxLength(80)
        fgSizer2.Add(self.name, 1, wx.ALL | wx.EXPAND, 5)
        
        bSizer_top.Add(fgSizer2, 0, wx.LEFT | wx.RIGHT | wx.TOP | wx.EXPAND, 5)
        
        self.m_staticline5 = wx.StaticLine(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL)
        bSizer_top.Add(self.m_staticline5, 0, wx.EXPAND, 5)
        
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
        
        self.date_from = wx.adv.DatePickerCtrl(self, wx.ID_ANY, wx.DefaultDateTime, wx.DefaultPosition, wx.DefaultSize,
                                               wx.adv.DP_DEFAULT | wx.adv.DP_DROPDOWN | wx.BORDER_SIMPLE)
        fgSizer23.Add(self.date_from, 0, wx.ALIGN_BOTTOM | wx.ALL, 10)
        
        self.date_to = wx.adv.DatePickerCtrl(self, wx.ID_ANY, wx.DefaultDateTime, wx.DefaultPosition, wx.DefaultSize,
                                             wx.adv.DP_DEFAULT | wx.adv.DP_DROPDOWN | wx.BORDER_SIMPLE)
        fgSizer23.Add(self.date_to, 0, wx.ALIGN_BOTTOM | wx.ALL, 10)
        
        bSizer49.Add(fgSizer23, 0, wx.ALIGN_BOTTOM, 5)
        
        bSizer_panels.Add(bSizer49, 1, wx.EXPAND, 5)
        
        bSizer_top.Add(bSizer_panels, 1, wx.EXPAND, 5)
        
        self.m_staticline6 = wx.StaticLine(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL)
        bSizer_top.Add(self.m_staticline6, 0, wx.EXPAND, 5)
        
        self.SetSizer(bSizer_top)
        self.Layout()
        bSizer_top.Fit(self)

        # Connect Events
        self.parent.Bind(wx.EVT_COMBOBOX, self.on_parent)
        self.date_from.Bind(wx.adv.EVT_DATE_CHANGED, self.on_date_from)
        self.date_to.Bind(wx.adv.EVT_DATE_CHANGED, self.on_date_to)
    
    def __del__(self):
        pass
    
    # Virtual event handlers, overide them in your derived class
    def on_parent(self, event):
        event.Skip()
    
    def on_date_from(self, event):
        event.Skip()
    
    def on_date_to(self, event):
        event.Skip()


###########################################################################
## Class DetailEdit
###########################################################################

class DetailEdit(wx.Panel):
    
    def __init__(self, parent, id=wx.ID_ANY, pos=wx.DefaultPosition, size=wx.Size(-1, -1), style=wx.TAB_TRAVERSAL,
                 name=wx.EmptyString):
        wx.Panel.__init__(self, parent, id=id, pos=pos, size=size, style=style, name=name)
        
        bSizer_top = wx.BoxSizer(wx.VERTICAL)
        
        self.m_staticText8 = wx.StaticText(self, wx.ID_ANY, u"Detail Information", wx.DefaultPosition, wx.DefaultSize,
                                           wx.ALIGN_LEFT | wx.BORDER_RAISED)
        self.m_staticText8.Wrap(-1)
        
        self.m_staticText8.SetFont(
            wx.Font(11, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial"))
        
        bSizer_top.Add(self.m_staticText8, 0, wx.ALIGN_CENTER | wx.EXPAND, 5)
        
        fgSizer2 = wx.FlexGridSizer(0, 2, 0, 0)
        fgSizer2.AddGrowableCol(1)
        fgSizer2.SetFlexibleDirection(wx.HORIZONTAL)
        fgSizer2.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_NONE)
        
        self.m_staticText71 = wx.StaticText(self, wx.ID_ANY, u"Category", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText71.Wrap(-1)
        
        fgSizer2.Add(self.m_staticText71, 0, wx.ALL, 5)
        
        grandparentChoices = []
        self.grandparent = wx.ComboBox(self, wx.ID_ANY, u"Combo!", wx.DefaultPosition, wx.DefaultSize,
                                       grandparentChoices, wx.CB_DROPDOWN | wx.CB_READONLY)
        fgSizer2.Add(self.grandparent, 1, wx.ALL | wx.EXPAND, 5)
        
        self.m_staticText61 = wx.StaticText(self, wx.ID_ANY, u"Sub Category", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText61.Wrap(-1)
        
        fgSizer2.Add(self.m_staticText61, 0, wx.ALIGN_CENTER | wx.ALL, 5)
        
        parentChoices = []
        self.parent = wx.ComboBox(self, wx.ID_ANY, u"Combo!", wx.DefaultPosition, wx.DefaultSize, parentChoices,
                                  wx.CB_DROPDOWN | wx.CB_READONLY)
        fgSizer2.Add(self.parent, 1, wx.ALL | wx.EXPAND, 5)
        
        self.m_staticText1 = wx.StaticText(self, wx.ID_ANY, u"Description", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText1.Wrap(-1)
        
        fgSizer2.Add(self.m_staticText1, 0, wx.ALL | wx.EXPAND, 5)
        
        self.name = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(-1, -1), 0)
        self.name.SetMaxLength(80)
        fgSizer2.Add(self.name, 1, wx.ALL | wx.EXPAND, 5)
        
        bSizer_top.Add(fgSizer2, 0, wx.EXPAND | wx.LEFT | wx.RIGHT | wx.TOP, 5)
        
        self.m_staticline11 = wx.StaticLine(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL)
        bSizer_top.Add(self.m_staticline11, 0, wx.EXPAND, 5)
        
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
        
        self.date_from = wx.adv.DatePickerCtrl(self, wx.ID_ANY, wx.DefaultDateTime, wx.DefaultPosition, wx.DefaultSize,
                                               wx.adv.DP_DEFAULT | wx.adv.DP_DROPDOWN | wx.BORDER_SIMPLE)
        fgSizer23.Add(self.date_from, 0, wx.ALIGN_BOTTOM | wx.ALL, 10)
        
        self.date_to = wx.adv.DatePickerCtrl(self, wx.ID_ANY, wx.DefaultDateTime, wx.DefaultPosition, wx.DefaultSize,
                                             wx.adv.DP_DEFAULT | wx.adv.DP_DROPDOWN | wx.BORDER_SIMPLE)
        fgSizer23.Add(self.date_to, 0, wx.ALIGN_BOTTOM | wx.ALL, 10)
        
        bSizer49.Add(fgSizer23, 0, wx.ALIGN_BOTTOM, 5)
        
        bSizer_panels.Add(bSizer49, 1, wx.EXPAND, 5)
        
        bSizer_top.Add(bSizer_panels, 1, wx.EXPAND, 5)
        
        self.m_staticline1 = wx.StaticLine(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL)
        bSizer_top.Add(self.m_staticline1, 0, wx.EXPAND, 5)
        
        self.SetSizer(bSizer_top)
        self.Layout()
        bSizer_top.Fit(self)

        # Connect Events
        self.grandparent.Bind(wx.EVT_COMBOBOX, self.on_grandparent)
        self.parent.Bind(wx.EVT_COMBOBOX, self.on_parent)
        self.date_from.Bind(wx.adv.EVT_DATE_CHANGED, self.on_date_from)
        self.date_to.Bind(wx.adv.EVT_DATE_CHANGED, self.on_date_to)
    
    def __del__(self):
        pass
    
    # Virtual event handlers, overide them in your derived class
    def on_grandparent(self, event):
        event.Skip()
    
    def on_parent(self, event):
        event.Skip()
    
    def on_date_from(self, event):
        event.Skip()
    
    def on_date_to(self, event):
        event.Skip()


###########################################################################
## Class TransactionEdit
###########################################################################

class TransactionEdit(wx.Panel):
    
    def __init__(self, parent, id=wx.ID_ANY, pos=wx.DefaultPosition, size=wx.Size(-1, -1), style=wx.TAB_TRAVERSAL,
                 name=wx.EmptyString):
        wx.Panel.__init__(self, parent, id=id, pos=pos, size=size, style=style, name=name)
        
        bSizer_top = wx.BoxSizer(wx.VERTICAL)
        
        self.m_staticText8 = wx.StaticText(self, wx.ID_ANY, u"Transaction Details", wx.DefaultPosition, wx.DefaultSize,
                                           wx.ALIGN_LEFT | wx.BORDER_RAISED)
        self.m_staticText8.Wrap(-1)
        
        self.m_staticText8.SetFont(
            wx.Font(11, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial"))
        
        bSizer_top.Add(self.m_staticText8, 0, wx.ALIGN_CENTER | wx.EXPAND, 5)
        
        fgSizer23 = wx.FlexGridSizer(0, 7, 0, 0)
        fgSizer23.AddGrowableCol(1)
        fgSizer23.AddGrowableCol(3)
        fgSizer23.AddGrowableCol(5)
        fgSizer23.SetFlexibleDirection(wx.HORIZONTAL)
        fgSizer23.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_NONE)
        
        self.m_staticText51 = wx.StaticText(self, wx.ID_ANY, u"Date ", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText51.Wrap(-1)
        
        fgSizer23.Add(self.m_staticText51, 0, wx.ALIGN_CENTER | wx.ALL, 5)
        
        self.date = wx.adv.DatePickerCtrl(self, wx.ID_ANY, wx.DefaultDateTime, wx.DefaultPosition, wx.DefaultSize,
                                          wx.adv.DP_DEFAULT | wx.adv.DP_DROPDOWN | wx.BORDER_SIMPLE)
        fgSizer23.Add(self.date, 0, wx.ALIGN_BOTTOM | wx.ALL, 10)
        
        self.m_staticText74 = wx.StaticText(self, wx.ID_ANY, u"Amount", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText74.Wrap(-1)
        
        fgSizer23.Add(self.m_staticText74, 0, wx.ALIGN_BOTTOM | wx.ALIGN_CENTER | wx.ALL, 5)
        
        self.initial = wx.SpinCtrlDouble(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize,
                                         wx.ALIGN_RIGHT | wx.SP_ARROW_KEYS, -1e+06, 1e+06, 0.000000, 0.01)
        self.initial.SetDigits(2)
        fgSizer23.Add(self.initial, 0, wx.ALIGN_BOTTOM | wx.ALIGN_CENTER | wx.ALL, 10)
        
        self.m_staticText61 = wx.StaticText(self, wx.ID_ANY, u"Supplier", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText61.Wrap(-1)
        
        fgSizer23.Add(self.m_staticText61, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        supplierChoices = []
        self.supplier = wx.ComboBox(self, wx.ID_ANY, u"Combo!", wx.DefaultPosition, wx.DefaultSize, supplierChoices,
                                    wx.CB_DROPDOWN | wx.CB_SORT)
        fgSizer23.Add(self.supplier, 0, wx.ALL, 10)
        
        bSizer_top.Add(fgSizer23, 0, wx.ALIGN_BOTTOM | wx.EXPAND | wx.LEFT | wx.RIGHT, 5)
        
        self.m_staticline51 = wx.StaticLine(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL)
        bSizer_top.Add(self.m_staticline51, 0, wx.EXPAND, 5)
        
        fgSizer2 = wx.FlexGridSizer(0, 2, 0, 0)
        fgSizer2.AddGrowableCol(1)
        fgSizer2.SetFlexibleDirection(wx.HORIZONTAL)
        fgSizer2.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_NONE)
        
        self.m_staticText1 = wx.StaticText(self, wx.ID_ANY, u"Description", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText1.Wrap(-1)
        
        fgSizer2.Add(self.m_staticText1, 0, wx.ALL | wx.EXPAND, 5)
        
        self.name = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(-1, -1), 0)
        self.name.SetMaxLength(80)
        fgSizer2.Add(self.name, 1, wx.ALL | wx.EXPAND, 5)
        
        self.m_staticText11 = wx.StaticText(self, wx.ID_ANY, u"Bank Description", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText11.Wrap(-1)
        
        fgSizer2.Add(self.m_staticText11, 0, wx.ALL | wx.EXPAND, 5)
        
        self.bank_description = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(-1, -1), 0)
        self.bank_description.SetMaxLength(80)
        fgSizer2.Add(self.bank_description, 1, wx.ALL | wx.EXPAND, 5)
        
        bSizer_top.Add(fgSizer2, 0, wx.EXPAND | wx.LEFT | wx.RIGHT, 5)
        
        self.m_staticline51 = wx.StaticLine(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL)
        bSizer_top.Add(self.m_staticline51, 0, wx.EXPAND, 5)
        
        bSizer_panels = wx.BoxSizer(wx.HORIZONTAL)
        
        fgSizer14 = wx.FlexGridSizer(0, 2, 0, 0)
        fgSizer14.AddGrowableCol(1)
        fgSizer14.SetFlexibleDirection(wx.HORIZONTAL)
        fgSizer14.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)
        
        self.m_staticText712 = wx.StaticText(self, wx.ID_ANY, u"Bank", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText712.Wrap(-1)
        
        fgSizer14.Add(self.m_staticText712, 0, wx.ALL, 5)

        grandparentChoices = []
        self.grandparent = wx.ComboBox(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize,
                                       grandparentChoices, wx.CB_DROPDOWN | wx.CB_READONLY)
        fgSizer14.Add(self.grandparent, 0, wx.ALL | wx.EXPAND, 5)
        
        self.m_staticText7111 = wx.StaticText(self, wx.ID_ANY, u"Account", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText7111.Wrap(-1)
        
        fgSizer14.Add(self.m_staticText7111, 0, wx.ALL, 5)

        parentChoices = []
        self.parent = wx.ComboBox(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, parentChoices,
                                  wx.CB_DROPDOWN | wx.CB_READONLY)
        fgSizer14.Add(self.parent, 0, wx.ALL | wx.EXPAND, 5)
        
        self.m_staticText73 = wx.StaticText(self, wx.ID_ANY, u"TransType", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText73.Wrap(-1)
        
        fgSizer14.Add(self.m_staticText73, 0, wx.ALL, 5)
        
        transaction_typeChoices = []
        self.transaction_type = wx.ComboBox(self, wx.ID_ANY, u"Combo!", wx.DefaultPosition, wx.DefaultSize,
                                            transaction_typeChoices, wx.CB_DROPDOWN | wx.CB_READONLY)
        fgSizer14.Add(self.transaction_type, 0, wx.ALL | wx.EXPAND, 5)
        
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

        categoryChoices = []
        self.category = wx.ComboBox(self, wx.ID_ANY, u"Combo!", wx.DefaultPosition, wx.DefaultSize, categoryChoices,
                                    wx.CB_DROPDOWN | wx.CB_READONLY)
        fgSizer31.Add(self.category, 0, wx.ALL | wx.EXPAND, 5)
        
        self.m_staticText711 = wx.StaticText(self, wx.ID_ANY, u"SubCategory", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText711.Wrap(-1)
        
        fgSizer31.Add(self.m_staticText711, 0, wx.ALL, 5)

        subcategoryChoices = []
        self.subcategory = wx.ComboBox(self, wx.ID_ANY, u"Combo!", wx.DefaultPosition, wx.DefaultSize,
                                       subcategoryChoices, wx.CB_DROPDOWN | wx.CB_READONLY)
        self.subcategory.Enable(False)
        
        fgSizer31.Add(self.subcategory, 0, wx.ALL | wx.EXPAND, 5)
        
        self.m_staticText7112 = wx.StaticText(self, wx.ID_ANY, u"Detail", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText7112.Wrap(-1)
        
        fgSizer31.Add(self.m_staticText7112, 0, wx.ALL, 5)

        detailChoices = []
        self.detail = wx.ComboBox(self, wx.ID_ANY, u"Combo!", wx.DefaultPosition, wx.DefaultSize, detailChoices,
                                  wx.CB_DROPDOWN | wx.CB_READONLY)
        self.detail.Enable(False)
        
        fgSizer31.Add(self.detail, 0, wx.ALL | wx.EXPAND, 5)
        
        bSizer49.Add(fgSizer31, 1, wx.ALL | wx.EXPAND, 5)
        
        bSizer_panels.Add(bSizer49, 1, wx.EXPAND, 5)
        
        bSizer_top.Add(bSizer_panels, 1, wx.EXPAND, 5)
        
        self.m_staticline511 = wx.StaticLine(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL)
        bSizer_top.Add(self.m_staticline511, 0, wx.EXPAND, 5)
        
        fgSizer86 = wx.FlexGridSizer(0, 2, 0, 0)
        fgSizer86.AddGrowableCol(1)
        fgSizer86.SetFlexibleDirection(wx.HORIZONTAL)
        fgSizer86.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)
        
        self.m_staticText55 = wx.StaticText(self, wx.ID_ANY, u"Notes", wx.DefaultPosition, wx.DefaultSize,
                                            wx.ALIGN_LEFT)
        self.m_staticText55.Wrap(-1)
        
        fgSizer86.Add(self.m_staticText55, 1, wx.ALL | wx.EXPAND, 5)
        
        self.notes = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE)
        self.notes.SetMaxLength(8)
        fgSizer86.Add(self.notes, 1, wx.ALL | wx.EXPAND, 5)
        
        bSizer_top.Add(fgSizer86, 0, wx.EXPAND, 5)
        
        self.m_staticline5 = wx.StaticLine(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL)
        bSizer_top.Add(self.m_staticline5, 0, wx.EXPAND, 5)
        
        self.SetSizer(bSizer_top)
        self.Layout()
        bSizer_top.Fit(self)

        # Connect Events
        self.date.Bind(wx.adv.EVT_DATE_CHANGED, self.on_date)
        self.supplier.Bind(wx.EVT_COMBOBOX, self.on_parent)
        self.grandparent.Bind(wx.EVT_COMBOBOX, self.on_grandparent)
        self.parent.Bind(wx.EVT_COMBOBOX, self.on_grandparent)
        self.category.Bind(wx.EVT_COMBOBOX, self.on_grandparent)
        self.subcategory.Bind(wx.EVT_COMBOBOX, self.on_grandparent)
        self.detail.Bind(wx.EVT_COMBOBOX, self.on_grandparent)
    
    def __del__(self):
        pass
    
    # Virtual event handlers, overide them in your derived class
    def on_date(self, event):
        event.Skip()
    
    def on_parent(self, event):
        event.Skip()
    
    def on_grandparent(self, event):
        event.Skip()


###########################################################################
## Class SubAccountEdit
###########################################################################

class SubAccountEdit(wx.Panel):
    
    def __init__(self, parent, id=wx.ID_ANY, pos=wx.DefaultPosition, size=wx.Size(-1, -1), style=wx.TAB_TRAVERSAL,
                 name=wx.EmptyString):
        wx.Panel.__init__(self, parent, id=id, pos=pos, size=size, style=style, name=name)
        
        bSizer_top = wx.BoxSizer(wx.VERTICAL)
        
        self.header = wx.StaticText(self, wx.ID_ANY, u"SubAccount Details", wx.DefaultPosition, wx.DefaultSize,
                                    wx.ALIGN_LEFT | wx.BORDER_RAISED)
        self.header.Wrap(-1)
        
        self.header.SetFont(wx.Font(11, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial"))
        
        bSizer_top.Add(self.header, 0, wx.ALIGN_CENTER | wx.EXPAND, 5)
        
        fgSizer2 = wx.FlexGridSizer(0, 2, 0, 0)
        fgSizer2.AddGrowableCol(1)
        fgSizer2.SetFlexibleDirection(wx.HORIZONTAL)
        fgSizer2.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_NONE)
        
        self.m_staticText61 = wx.StaticText(self, wx.ID_ANY, u"Account", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText61.Wrap(-1)
        
        fgSizer2.Add(self.m_staticText61, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)
        
        parentChoices = []
        self.parent = wx.ComboBox(self, wx.ID_ANY, u"Combo!", wx.DefaultPosition, wx.DefaultSize, parentChoices,
                                  wx.CB_DROPDOWN | wx.CB_READONLY)
        fgSizer2.Add(self.parent, 1, wx.ALL | wx.EXPAND, 5)
        
        self.m_staticText1 = wx.StaticText(self, wx.ID_ANY, u"SubAccount Name", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText1.Wrap(-1)
        
        fgSizer2.Add(self.m_staticText1, 0, wx.ALL | wx.EXPAND, 5)
        
        self.name = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(-1, -1), 0)
        self.name.SetMaxLength(80)
        fgSizer2.Add(self.name, 1, wx.ALL | wx.EXPAND, 5)
        
        self.m_staticText11 = wx.StaticText(self, wx.ID_ANY, u"SubAccount Description", wx.DefaultPosition,
                                            wx.DefaultSize, 0)
        self.m_staticText11.Wrap(-1)
        
        fgSizer2.Add(self.m_staticText11, 0, wx.ALL | wx.EXPAND, 5)
        
        self.description = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(-1, -1), 0)
        self.description.SetMaxLength(80)
        fgSizer2.Add(self.description, 1, wx.ALL | wx.EXPAND, 5)
        
        bSizer_top.Add(fgSizer2, 0, wx.EXPAND | wx.LEFT | wx.RIGHT, 5)
        
        self.m_staticline51 = wx.StaticLine(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL)
        bSizer_top.Add(self.m_staticline51, 0, wx.EXPAND, 5)
        
        bSizer_panels = wx.BoxSizer(wx.HORIZONTAL)
        
        fgSizer14 = wx.FlexGridSizer(0, 2, 0, 0)
        fgSizer14.AddGrowableCol(1)
        fgSizer14.SetFlexibleDirection(wx.HORIZONTAL)
        fgSizer14.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_NONE)
        
        self.m_staticText74 = wx.StaticText(self, wx.ID_ANY, u"Initial Value", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText74.Wrap(-1)
        
        fgSizer14.Add(self.m_staticText74, 0, wx.ALL, 5)
        
        self.initial = wx.SpinCtrlDouble(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize,
                                         wx.ALIGN_RIGHT | wx.SP_ARROW_KEYS, -1e+06, 1e+06, 0, 0.01)
        self.initial.SetDigits(2)
        fgSizer14.Add(self.initial, 0, wx.ALL, 5)
        
        self.m_staticText741 = wx.StaticText(self, wx.ID_ANY, u"Commission", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText741.Wrap(-1)
        
        fgSizer14.Add(self.m_staticText741, 0, wx.ALL, 5)
        
        self.commission = wx.SpinCtrlDouble(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize,
                                            wx.ALIGN_RIGHT | wx.SP_ARROW_KEYS, -1e+06, 1e+06, 0, 0.01)
        self.commission.SetDigits(2)
        fgSizer14.Add(self.commission, 0, wx.ALL, 5)
        
        self.m_staticText7411 = wx.StaticText(self, wx.ID_ANY, u"Rate", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText7411.Wrap(-1)
        
        fgSizer14.Add(self.m_staticText7411, 0, wx.ALL, 5)
        
        self.rate = wx.SpinCtrlDouble(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize,
                                      wx.ALIGN_RIGHT | wx.SP_ARROW_KEYS, -1e+06, 1e+06, 0, 0.01)
        self.rate.SetDigits(2)
        fgSizer14.Add(self.rate, 0, wx.ALL, 5)
        
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
        
        self.date_from = wx.adv.DatePickerCtrl(self, wx.ID_ANY, wx.DefaultDateTime, wx.DefaultPosition, wx.DefaultSize,
                                               wx.adv.DP_DEFAULT | wx.adv.DP_DROPDOWN | wx.BORDER_SIMPLE)
        fgSizer23.Add(self.date_from, 0, wx.ALIGN_BOTTOM | wx.ALL, 10)
        
        self.date_to = wx.adv.DatePickerCtrl(self, wx.ID_ANY, wx.DefaultDateTime, wx.DefaultPosition, wx.DefaultSize,
                                             wx.adv.DP_DEFAULT | wx.adv.DP_DROPDOWN | wx.BORDER_SIMPLE)
        fgSizer23.Add(self.date_to, 0, wx.ALIGN_BOTTOM | wx.ALL, 10)
        
        bSizer49.Add(fgSizer23, 0, wx.ALIGN_BOTTOM, 5)
        
        bSizer_panels.Add(bSizer49, 1, wx.ALIGN_BOTTOM, 5)
        
        bSizer_top.Add(bSizer_panels, 1, wx.EXPAND, 5)
        
        self.m_staticline5 = wx.StaticLine(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL)
        bSizer_top.Add(self.m_staticline5, 0, wx.EXPAND, 5)
        
        self.SetSizer(bSizer_top)
        self.Layout()
        bSizer_top.Fit(self)

        # Connect Events
        self.parent.Bind(wx.EVT_COMBOBOX, self.on_parent)
        self.date_from.Bind(wx.adv.EVT_DATE_CHANGED, self.on_date_from)
        self.date_to.Bind(wx.adv.EVT_DATE_CHANGED, self.on_date_to)
    
    def __del__(self):
        pass
    
    # Virtual event handlers, overide them in your derived class
    def on_parent(self, event):
        event.Skip()
    
    def on_date_from(self, event):
        event.Skip()
    
    def on_date_to(self, event):
        event.Skip()


###########################################################################
## Class ContactEdit
###########################################################################

class ContactEdit(wx.Panel):
    
    def __init__(self, parent, id=wx.ID_ANY, pos=wx.DefaultPosition, size=wx.Size(-1, -1), style=wx.TAB_TRAVERSAL,
                 name=wx.EmptyString):
        wx.Panel.__init__(self, parent, id=id, pos=pos, size=size, style=style, name=name)
        
        bSizer_top = wx.BoxSizer(wx.VERTICAL)
        
        self.header = wx.StaticText(self, wx.ID_ANY, u"Contact Details", wx.DefaultPosition, wx.DefaultSize,
                                    wx.ALIGN_LEFT | wx.BORDER_RAISED)
        self.header.Wrap(-1)
        
        self.header.SetFont(wx.Font(11, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial"))
        
        bSizer_top.Add(self.header, 0, wx.ALIGN_CENTER | wx.EXPAND, 5)
        
        fgSizer2 = wx.FlexGridSizer(0, 2, 0, 0)
        fgSizer2.AddGrowableCol(1)
        fgSizer2.SetFlexibleDirection(wx.HORIZONTAL)
        fgSizer2.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_NONE)
        
        self.m_staticText61 = wx.StaticText(self, wx.ID_ANY, u"Company", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText61.Wrap(-1)
        
        fgSizer2.Add(self.m_staticText61, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)
        
        parentChoices = []
        self.parent = wx.ComboBox(self, wx.ID_ANY, u"Combo!", wx.DefaultPosition, wx.DefaultSize, parentChoices,
                                  wx.CB_DROPDOWN | wx.CB_READONLY)
        fgSizer2.Add(self.parent, 1, wx.ALL | wx.EXPAND, 5)
        
        self.m_staticText1 = wx.StaticText(self, wx.ID_ANY, u"Name", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText1.Wrap(-1)
        
        fgSizer2.Add(self.m_staticText1, 0, wx.ALL | wx.EXPAND, 5)
        
        self.name = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(-1, -1), 0)
        self.name.SetMaxLength(80)
        fgSizer2.Add(self.name, 1, wx.ALL | wx.EXPAND, 5)
        
        bSizer_top.Add(fgSizer2, 0, wx.EXPAND | wx.LEFT | wx.RIGHT, 5)
        
        self.m_staticline51 = wx.StaticLine(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL)
        bSizer_top.Add(self.m_staticline51, 0, wx.EXPAND, 5)
        
        bSizer_panels = wx.BoxSizer(wx.HORIZONTAL)
        
        fgSizer14 = wx.FlexGridSizer(0, 2, 20, 0)
        fgSizer14.AddGrowableCol(1)
        fgSizer14.AddGrowableRow(0)
        fgSizer14.SetFlexibleDirection(wx.BOTH)
        fgSizer14.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_NONE)
        
        self.m_staticText73 = wx.StaticText(self, wx.ID_ANY, u"Address", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText73.Wrap(-1)
        
        fgSizer14.Add(self.m_staticText73, 0, wx.ALL, 5)
        
        self.address = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE)
        fgSizer14.Add(self.address, 1, wx.ALL | wx.EXPAND, 5)
        
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
        
        self.phone = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        fgSizer31.Add(self.phone, 1, wx.ALL | wx.EXPAND, 5)
        
        self.m_staticText551 = wx.StaticText(self, wx.ID_ANY, u"Mobile", wx.DefaultPosition, wx.DefaultSize,
                                             wx.ALIGN_LEFT)
        self.m_staticText551.Wrap(-1)
        
        fgSizer31.Add(self.m_staticText551, 0, wx.ALL, 5)
        
        self.mobile = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        fgSizer31.Add(self.mobile, 0, wx.ALL | wx.EXPAND, 5)
        
        self.m_staticText70 = wx.StaticText(self, wx.ID_ANY, u"e-mail", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText70.Wrap(-1)
        
        fgSizer31.Add(self.m_staticText70, 0, wx.ALL, 5)
        
        self.email = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        fgSizer31.Add(self.email, 1, wx.ALL | wx.EXPAND, 5)
        
        bSizer49.Add(fgSizer31, 1, wx.ALL | wx.EXPAND, 5)
        
        fgSizer23 = wx.FlexGridSizer(0, 3, 0, 0)
        fgSizer23.AddGrowableCol(1)
        fgSizer23.AddGrowableCol(2)
        fgSizer23.SetFlexibleDirection(wx.HORIZONTAL)
        fgSizer23.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_NONE)
        
        self.m_staticText51 = wx.StaticText(self, wx.ID_ANY, u"Dates Active", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText51.Wrap(-1)
        
        fgSizer23.Add(self.m_staticText51, 0, wx.ALIGN_CENTER | wx.ALL, 5)
        
        self.date_from = wx.adv.DatePickerCtrl(self, wx.ID_ANY, wx.DefaultDateTime, wx.DefaultPosition, wx.DefaultSize,
                                               wx.adv.DP_DEFAULT | wx.adv.DP_DROPDOWN | wx.BORDER_SIMPLE)
        fgSizer23.Add(self.date_from, 0, wx.ALIGN_BOTTOM | wx.ALL, 10)
        
        self.date_to = wx.adv.DatePickerCtrl(self, wx.ID_ANY, wx.DefaultDateTime, wx.DefaultPosition, wx.DefaultSize,
                                             wx.adv.DP_DEFAULT | wx.adv.DP_DROPDOWN | wx.BORDER_SIMPLE)
        fgSizer23.Add(self.date_to, 0, wx.ALIGN_BOTTOM | wx.ALL, 10)
        
        bSizer49.Add(fgSizer23, 0, wx.ALIGN_BOTTOM, 5)
        
        bSizer_panels.Add(bSizer49, 1, wx.EXPAND, 5)
        
        bSizer_top.Add(bSizer_panels, 1, 0, 5)
        
        self.m_staticline5 = wx.StaticLine(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL)
        bSizer_top.Add(self.m_staticline5, 0, wx.EXPAND, 5)
        
        self.SetSizer(bSizer_top)
        self.Layout()
        bSizer_top.Fit(self)

        # Connect Events
        self.parent.Bind(wx.EVT_COMBOBOX, self.on_parent)
        self.date_from.Bind(wx.adv.EVT_DATE_CHANGED, self.on_date_from)
        self.date_to.Bind(wx.adv.EVT_DATE_CHANGED, self.on_date_to)
    
    def __del__(self):
        pass
    
    # Virtual event handlers, overide them in your derived class
    def on_parent(self, event):
        event.Skip()
    
    def on_date_from(self, event):
        event.Skip()
    
    def on_date_to(self, event):
        event.Skip()


###########################################################################
## Class CardEdit
###########################################################################

class CardEdit(wx.Panel):
    
    def __init__(self, parent, id=wx.ID_ANY, pos=wx.DefaultPosition, size=wx.Size(-1, -1), style=wx.TAB_TRAVERSAL,
                 name=wx.EmptyString):
        wx.Panel.__init__(self, parent, id=id, pos=pos, size=size, style=style, name=name)
        
        bSizer_top = wx.BoxSizer(wx.VERTICAL)
        
        self.header = wx.StaticText(self, wx.ID_ANY, u"Card Details", wx.DefaultPosition, wx.DefaultSize,
                                    wx.ALIGN_LEFT | wx.BORDER_RAISED)
        self.header.Wrap(-1)
        
        self.header.SetFont(wx.Font(11, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial"))
        
        bSizer_top.Add(self.header, 0, wx.ALIGN_CENTER | wx.EXPAND, 5)
        
        fgSizer2 = wx.FlexGridSizer(0, 2, 0, 0)
        fgSizer2.AddGrowableCol(1)
        fgSizer2.SetFlexibleDirection(wx.HORIZONTAL)
        fgSizer2.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_NONE)
        
        self.m_staticText61 = wx.StaticText(self, wx.ID_ANY, u"Account", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText61.Wrap(-1)
        
        fgSizer2.Add(self.m_staticText61, 0, wx.ALL, 5)
        
        parentChoices = []
        self.parent = wx.ComboBox(self, wx.ID_ANY, u"Combo!", wx.DefaultPosition, wx.DefaultSize, parentChoices,
                                  wx.CB_DROPDOWN | wx.CB_READONLY)
        fgSizer2.Add(self.parent, 0, wx.ALL | wx.EXPAND, 5)
        
        self.m_staticText1 = wx.StaticText(self, wx.ID_ANY, u"Card Name", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText1.Wrap(-1)
        
        fgSizer2.Add(self.m_staticText1, 0, wx.ALL | wx.EXPAND, 5)
        
        self.name = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(-1, -1), 0)
        self.name.SetMaxLength(80)
        fgSizer2.Add(self.name, 1, wx.ALL | wx.EXPAND, 5)
        
        self.m_staticText11 = wx.StaticText(self, wx.ID_ANY, u"Card Number", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText11.Wrap(-1)
        
        fgSizer2.Add(self.m_staticText11, 0, wx.ALL | wx.EXPAND, 5)
        
        self.number = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(-1, -1), 0)
        self.number.SetMaxLength(16)
        fgSizer2.Add(self.number, 1, wx.ALL | wx.EXPAND, 5)
        
        bSizer_top.Add(fgSizer2, 0, wx.EXPAND | wx.LEFT | wx.RIGHT, 5)
        
        self.m_staticline51 = wx.StaticLine(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL)
        bSizer_top.Add(self.m_staticline51, 0, wx.EXPAND, 5)
        
        bSizer_panels = wx.BoxSizer(wx.HORIZONTAL)
        
        fgSizer14 = wx.FlexGridSizer(0, 2, 20, 0)
        fgSizer14.AddGrowableCol(1)
        fgSizer14.AddGrowableRow(0)
        fgSizer14.SetFlexibleDirection(wx.BOTH)
        fgSizer14.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_NONE)
        
        typeChoices = [u"Credit Card", u"Debit Card", u"Store Card"]
        self.type = wx.RadioBox(self, wx.ID_ANY, u"Card Type", wx.DefaultPosition, wx.DefaultSize, typeChoices, 1,
                                wx.RA_SPECIFY_ROWS)
        self.type.SetSelection(0)
        fgSizer14.Add(self.type, 0, wx.ALIGN_BOTTOM | wx.ALL | wx.EXPAND, 5)
        
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
        
        self.date_from = wx.adv.DatePickerCtrl(self, wx.ID_ANY, wx.DefaultDateTime, wx.DefaultPosition, wx.DefaultSize,
                                               wx.adv.DP_DEFAULT | wx.adv.DP_DROPDOWN | wx.BORDER_SIMPLE)
        fgSizer23.Add(self.date_from, 0, wx.ALIGN_BOTTOM | wx.ALL, 10)
        
        self.date_to = wx.adv.DatePickerCtrl(self, wx.ID_ANY, wx.DefaultDateTime, wx.DefaultPosition, wx.DefaultSize,
                                             wx.adv.DP_DEFAULT | wx.adv.DP_DROPDOWN | wx.BORDER_SIMPLE)
        fgSizer23.Add(self.date_to, 0, wx.ALIGN_BOTTOM | wx.ALL, 10)
        
        bSizer49.Add(fgSizer23, 0, wx.ALIGN_BOTTOM, 5)
        
        bSizer_panels.Add(bSizer49, 0, wx.ALIGN_BOTTOM, 5)
        
        bSizer_top.Add(bSizer_panels, 0, wx.ALIGN_BOTTOM, 5)
        
        self.m_staticline5 = wx.StaticLine(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL)
        bSizer_top.Add(self.m_staticline5, 0, wx.EXPAND, 5)
        
        self.SetSizer(bSizer_top)
        self.Layout()
        bSizer_top.Fit(self)

        # Connect Events
        self.parent.Bind(wx.EVT_COMBOBOX, self.on_parent)
        self.date_from.Bind(wx.adv.EVT_DATE_CHANGED, self.on_date_from)
        self.date_to.Bind(wx.adv.EVT_DATE_CHANGED, self.on_date_to)
    
    def __del__(self):
        pass
    
    # Virtual event handlers, overide them in your derived class
    def on_parent(self, event):
        event.Skip()
    
    def on_date_from(self, event):
        event.Skip()
    
    def on_date_to(self, event):
        event.Skip()


###########################################################################
## Class RulesEdit
###########################################################################

class RulesEdit(wx.Panel):
    
    def __init__(self, parent, id=wx.ID_ANY, pos=wx.DefaultPosition, size=wx.Size(-1, -1), style=wx.TAB_TRAVERSAL,
                 name=wx.EmptyString):
        wx.Panel.__init__(self, parent, id=id, pos=pos, size=size, style=style, name=name)
        
        bSizer_top = wx.BoxSizer(wx.VERTICAL)
        
        self.header = wx.StaticText(self, wx.ID_ANY, u"Rule Details", wx.DefaultPosition, wx.DefaultSize,
                                    wx.ALIGN_LEFT | wx.BORDER_RAISED)
        self.header.Wrap(-1)
        
        self.header.SetFont(wx.Font(11, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial"))
        
        bSizer_top.Add(self.header, 0, wx.ALIGN_CENTER | wx.EXPAND, 5)
        
        fgSizer2 = wx.FlexGridSizer(0, 2, 0, 0)
        fgSizer2.AddGrowableCol(1)
        fgSizer2.SetFlexibleDirection(wx.HORIZONTAL)
        fgSizer2.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_NONE)
        
        self.m_staticText1 = wx.StaticText(self, wx.ID_ANY, u"Rule Name", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText1.Wrap(-1)
        
        fgSizer2.Add(self.m_staticText1, 0, wx.ALL | wx.EXPAND, 5)
        
        self.name = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(-1, -1), 0)
        self.name.SetMaxLength(80)
        fgSizer2.Add(self.name, 1, wx.ALL | wx.EXPAND, 5)
        
        bSizer_top.Add(fgSizer2, 0, wx.EXPAND | wx.LEFT | wx.RIGHT, 5)
        
        self.m_staticline51 = wx.StaticLine(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL)
        bSizer_top.Add(self.m_staticline51, 0, wx.EXPAND, 5)
        
        bSizer_panels = wx.BoxSizer(wx.HORIZONTAL)
        
        fgSizer14 = wx.FlexGridSizer(0, 2, 0, 0)
        fgSizer14.AddGrowableCol(1)
        fgSizer14.SetFlexibleDirection(wx.HORIZONTAL)
        fgSizer14.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)
        
        self.m_staticText74 = wx.StaticText(self, wx.ID_ANY, u"Credit %", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText74.Wrap(-1)
        
        fgSizer14.Add(self.m_staticText74, 0, wx.ALL, 5)
        
        self.initial = wx.SpinCtrlDouble(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize,
                                         wx.ALIGN_RIGHT | wx.SP_ARROW_KEYS, -1e+06, 1e+06, 0, 0.01)
        self.initial.SetDigits(4)
        fgSizer14.Add(self.initial, 0, wx.ALL, 5)
        
        self.m_staticText741 = wx.StaticText(self, wx.ID_ANY, u"Debit %", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText741.Wrap(-1)
        
        fgSizer14.Add(self.m_staticText741, 0, wx.ALL, 5)
        
        self.commission = wx.SpinCtrlDouble(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize,
                                            wx.ALIGN_RIGHT | wx.SP_ARROW_KEYS, -1e+06, 1e+06, 0.000000, 0.01)
        self.commission.SetDigits(4)
        fgSizer14.Add(self.commission, 0, wx.ALL, 5)
        
        self.m_staticText7411 = wx.StaticText(self, wx.ID_ANY, u"Minimum Payment", wx.DefaultPosition, wx.DefaultSize,
                                              0)
        self.m_staticText7411.Wrap(-1)
        
        fgSizer14.Add(self.m_staticText7411, 0, wx.ALL, 5)
        
        self.rate = wx.SpinCtrlDouble(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize,
                                      wx.ALIGN_RIGHT | wx.SP_ARROW_KEYS, -1e+06, 1e+06, 0, 0.01)
        self.rate.SetDigits(2)
        fgSizer14.Add(self.rate, 0, wx.ALL, 5)
        
        self.m_staticText74111 = wx.StaticText(self, wx.ID_ANY, u"Minimum %", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText74111.Wrap(-1)
        
        fgSizer14.Add(self.m_staticText74111, 0, wx.ALL, 5)
        
        self.rate1 = wx.SpinCtrlDouble(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize,
                                       wx.ALIGN_RIGHT | wx.SP_ARROW_KEYS, -1e+06, 1e+06, 0, 0.01)
        self.rate1.SetDigits(2)
        fgSizer14.Add(self.rate1, 0, wx.ALL, 5)
        
        self.m_staticText741111 = wx.StaticText(self, wx.ID_ANY, u"Credit Limit", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText741111.Wrap(-1)
        
        fgSizer14.Add(self.m_staticText741111, 0, wx.ALL, 5)
        
        self.rate11 = wx.SpinCtrlDouble(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize,
                                        wx.ALIGN_RIGHT | wx.SP_ARROW_KEYS, -1e+06, 1e+06, 0, 0.01)
        self.rate11.SetDigits(2)
        fgSizer14.Add(self.rate11, 0, wx.ALL, 5)
        
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

        grandparentChoices = []
        self.grandparent = wx.ComboBox(self, wx.ID_ANY, u"Combo!", wx.DefaultPosition, wx.DefaultSize,
                                       grandparentChoices, wx.CB_DROPDOWN | wx.CB_READONLY)
        fgSizer31.Add(self.grandparent, 1, wx.ALL | wx.EXPAND, 5)
        
        self.m_staticText61 = wx.StaticText(self, wx.ID_ANY, u"SubAccount", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText61.Wrap(-1)
        
        fgSizer31.Add(self.m_staticText61, 0, wx.ALL, 10)

        parentChoices = []
        self.parent = wx.ComboBox(self, wx.ID_ANY, u"Combo!", wx.DefaultPosition, wx.DefaultSize, parentChoices,
                                  wx.CB_DROPDOWN | wx.CB_READONLY)
        fgSizer31.Add(self.parent, 1, wx.ALL | wx.EXPAND, 5)
        
        bSizer49.Add(fgSizer31, 1, wx.ALL | wx.EXPAND, 5)
        
        fgSizer23 = wx.FlexGridSizer(0, 3, 0, 0)
        fgSizer23.AddGrowableCol(1)
        fgSizer23.AddGrowableCol(2)
        fgSizer23.SetFlexibleDirection(wx.HORIZONTAL)
        fgSizer23.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_NONE)
        
        self.m_staticText51 = wx.StaticText(self, wx.ID_ANY, u"Dates Active", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText51.Wrap(-1)
        
        fgSizer23.Add(self.m_staticText51, 0, wx.ALIGN_CENTER | wx.ALL, 5)
        
        self.date_from = wx.adv.DatePickerCtrl(self, wx.ID_ANY, wx.DefaultDateTime, wx.DefaultPosition, wx.DefaultSize,
                                               wx.adv.DP_DEFAULT | wx.adv.DP_DROPDOWN | wx.BORDER_SIMPLE)
        fgSizer23.Add(self.date_from, 0, wx.ALIGN_BOTTOM | wx.ALL, 10)
        
        self.date_to = wx.adv.DatePickerCtrl(self, wx.ID_ANY, wx.DefaultDateTime, wx.DefaultPosition, wx.DefaultSize,
                                             wx.adv.DP_DEFAULT | wx.adv.DP_DROPDOWN | wx.BORDER_SIMPLE)
        fgSizer23.Add(self.date_to, 0, wx.ALIGN_BOTTOM | wx.ALL, 10)
        
        bSizer49.Add(fgSizer23, 0, wx.ALIGN_BOTTOM, 5)
        
        bSizer_panels.Add(bSizer49, 1, wx.EXPAND, 5)
        
        bSizer_top.Add(bSizer_panels, 1, wx.EXPAND, 5)
        
        self.m_staticline5 = wx.StaticLine(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL)
        bSizer_top.Add(self.m_staticline5, 0, wx.EXPAND, 5)
        
        self.SetSizer(bSizer_top)
        self.Layout()
        bSizer_top.Fit(self)

        # Connect Events
        self.grandparent.Bind(wx.EVT_COMBOBOX, self.on_account)
        self.parent.Bind(wx.EVT_COMBOBOX, self.on_subaccount)
        self.date_from.Bind(wx.adv.EVT_DATE_CHANGED, self.on_date_from)
        self.date_to.Bind(wx.adv.EVT_DATE_CHANGED, self.on_date_to)
    
    def __del__(self):
        pass
    
    # Virtual event handlers, overide them in your derived class
    def on_account(self, event):
        event.Skip()
    
    def on_subaccount(self, event):
        event.Skip()
    
    def on_date_from(self, event):
        event.Skip()
    
    def on_date_to(self, event):
        event.Skip()


###########################################################################
## Class Buttons
###########################################################################

class Buttons(wx.Panel):
    
    def __init__(self, parent, id=wx.ID_ANY, pos=wx.DefaultPosition, size=wx.Size(671, 50), style=wx.TAB_TRAVERSAL,
                 name=wx.EmptyString):
        wx.Panel.__init__(self, parent, id=id, pos=pos, size=size, style=style, name=name)
        
        bSizer5 = wx.BoxSizer(wx.HORIZONTAL)
        
        bSizer5.Add((0, 0), 1, wx.EXPAND, 5)
        
        self.new = wx.Button(self, wx.ID_ANY, u"New", wx.DefaultPosition, wx.DefaultSize, 0 | wx.BORDER_RAISED)
        self.new.SetToolTip(u"Add a New Row")
        
        bSizer5.Add(self.new, 0, wx.ALIGN_BOTTOM | wx.ALIGN_RIGHT | wx.ALL | wx.RESERVE_SPACE_EVEN_IF_HIDDEN, 5)
        
        self.edit = wx.Button(self, wx.ID_ANY, u"Edit", wx.DefaultPosition, wx.DefaultSize, 0 | wx.BORDER_RAISED)
        self.edit.Enable(False)
        self.edit.SetToolTip(u"Edit Currently Selected Row")
        
        bSizer5.Add(self.edit, 0, wx.ALIGN_BOTTOM | wx.ALIGN_RIGHT | wx.ALL | wx.RESERVE_SPACE_EVEN_IF_HIDDEN, 5)
        
        self.reset = wx.Button(self, wx.ID_ANY, u"Reset", wx.DefaultPosition, wx.DefaultSize, 0 | wx.BORDER_RAISED)
        self.reset.Enable(False)
        self.reset.SetToolTip(u"Reset Original Values")
        
        bSizer5.Add(self.reset, 0, wx.ALIGN_BOTTOM | wx.ALIGN_RIGHT | wx.ALL | wx.RESERVE_SPACE_EVEN_IF_HIDDEN, 5)
        
        self.apply = wx.Button(self, wx.ID_ANY, u"Apply", wx.DefaultPosition, wx.DefaultSize, 0 | wx.BORDER_RAISED)
        self.apply.Enable(False)
        self.apply.SetToolTip(u"Save Changes")
        
        bSizer5.Add(self.apply, 0, wx.ALIGN_BOTTOM | wx.ALIGN_RIGHT | wx.ALL | wx.RESERVE_SPACE_EVEN_IF_HIDDEN, 5)
        
        self.cancel = wx.Button(self, wx.ID_ANY, u"Cancel", wx.DefaultPosition, wx.DefaultSize, 0 | wx.BORDER_RAISED)
        self.cancel.Enable(False)
        self.cancel.SetToolTip(u"Cancel Changes Without Saving")
        
        bSizer5.Add(self.cancel, 0, wx.ALIGN_BOTTOM | wx.ALIGN_RIGHT | wx.ALL | wx.RESERVE_SPACE_EVEN_IF_HIDDEN, 5)
        
        self.quit = wx.Button(self, wx.ID_ANY, u"Quit", wx.DefaultPosition, wx.DefaultSize, 0 | wx.BORDER_RAISED)
        self.quit.SetToolTip(u"Close App")
        
        bSizer5.Add(self.quit, 0, wx.ALIGN_BOTTOM | wx.ALIGN_RIGHT | wx.ALL | wx.RESERVE_SPACE_EVEN_IF_HIDDEN, 5)
        
        self.SetSizer(bSizer5)
        self.Layout()

        # Connect Events
        self.new.Bind(wx.EVT_BUTTON, self.on_new)
        self.edit.Bind(wx.EVT_BUTTON, self.on_edit)
        self.reset.Bind(wx.EVT_BUTTON, self.on_reset)
        self.apply.Bind(wx.EVT_BUTTON, self.on_apply)
        self.cancel.Bind(wx.EVT_BUTTON, self.on_cancel)
        self.quit.Bind(wx.EVT_BUTTON, self.on_quit)
    
    def __del__(self):
        pass
    
    # Virtual event handlers, overide them in your derived class
    def on_new(self, event):
        event.Skip()
    
    def on_edit(self, event):
        event.Skip()
    
    def on_reset(self, event):
        event.Skip()
    
    def on_apply(self, event):
        event.Skip()
    
    def on_cancel(self, event):
        event.Skip()
    
    def on_quit(self, event):
        event.Skip()
