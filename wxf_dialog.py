# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Oct 26 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc


###########################################################################
## Class db_sign_in
###########################################################################

class db_sign_in(wx.Dialog):
    
    def __init__(self, parent):
        wx.Dialog.__init__(self, parent, id=wx.ID_ANY, title=u"Sign In", pos=wx.DefaultPosition, size=wx.Size(-1, -1),
                           style=wx.DEFAULT_DIALOG_STYLE)
        
        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)
        
        bSizer1 = wx.BoxSizer(wx.VERTICAL)
        
        fgSizer1 = wx.FlexGridSizer(0, 2, 0, 0)
        fgSizer1.AddGrowableCol(1)
        fgSizer1.SetFlexibleDirection(wx.BOTH)
        fgSizer1.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)
        
        self.m_staticText1 = wx.StaticText(self, wx.ID_ANY, u"User Name", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText1.Wrap(-1)
        
        fgSizer1.Add(self.m_staticText1, 0, wx.ALL, 5)
        
        self.user_name = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        self.user_name.SetMaxLength(32)
        fgSizer1.Add(self.user_name, 0, wx.ALL | wx.EXPAND, 5)
        
        self.m_staticText2 = wx.StaticText(self, wx.ID_ANY, u"Password", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText2.Wrap(-1)
        
        fgSizer1.Add(self.m_staticText2, 0, wx.ALL, 5)
        
        self.password = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_PASSWORD)
        self.password.SetMaxLength(32)
        fgSizer1.Add(self.password, 0, wx.ALL | wx.EXPAND, 5)
        
        self.m_staticText3 = wx.StaticText(self, wx.ID_ANY, u"Host", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText3.Wrap(-1)
        
        fgSizer1.Add(self.m_staticText3, 0, wx.ALL, 5)
        
        self.host_name = wx.TextCtrl(self, wx.ID_ANY, u"localhost", wx.DefaultPosition, wx.DefaultSize, 0)
        self.host_name.SetMaxLength(32)
        fgSizer1.Add(self.host_name, 0, wx.ALL | wx.EXPAND, 5)
        
        self.m_staticText4 = wx.StaticText(self, wx.ID_ANY, u"Database", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText4.Wrap(-1)
        
        fgSizer1.Add(self.m_staticText4, 0, wx.ALL, 5)
        
        self.use_db = wx.TextCtrl(self, wx.ID_ANY, u"test", wx.DefaultPosition, wx.DefaultSize, 0)
        self.use_db.SetMaxLength(32)
        fgSizer1.Add(self.use_db, 0, wx.ALL | wx.EXPAND, 5)
        
        bSizer1.Add(fgSizer1, 1, wx.EXPAND, 5)
        
        fgSizer2 = wx.FlexGridSizer(0, 3, 0, 0)
        fgSizer2.AddGrowableCol(0)
        fgSizer2.AddGrowableCol(1)
        fgSizer2.AddGrowableCol(2)
        fgSizer2.SetFlexibleDirection(wx.BOTH)
        fgSizer2.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)
        
        self.b_connect = wx.Button(self, wx.ID_ANY, u"Connect", wx.DefaultPosition, wx.DefaultSize, 0)
        fgSizer2.Add(self.b_connect, 0, wx.ALL | wx.EXPAND, 5)
        
        self.b_test = wx.Button(self, wx.ID_ANY, u"Test Connection", wx.DefaultPosition, wx.DefaultSize, 0)
        fgSizer2.Add(self.b_test, 0, wx.ALIGN_CENTER | wx.ALL | wx.EXPAND, 5)
        
        self.b_cancel = wx.Button(self, wx.ID_ANY, u"Cancel", wx.DefaultPosition, wx.DefaultSize, 0)
        fgSizer2.Add(self.b_cancel, 0, wx.ALL, 5)
        
        bSizer1.Add(fgSizer2, 0, wx.ALL | wx.EXPAND, 5)
        
        bSizer2 = wx.BoxSizer(wx.VERTICAL)
        
        self.progress = wx.Gauge(self, wx.ID_ANY, 100, wx.DefaultPosition, wx.DefaultSize,
                                 wx.GA_HORIZONTAL | wx.GA_SMOOTH)
        self.progress.SetValue(0)
        bSizer2.Add(self.progress, 0, wx.ALL | wx.EXPAND, 5)
        
        self.message = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize,
                                   wx.TE_MULTILINE | wx.TE_READONLY)
        bSizer2.Add(self.message, 1, wx.ALL | wx.EXPAND, 5)
        
        bSizer1.Add(bSizer2, 0, wx.EXPAND, 10)
        
        self.SetSizer(bSizer1)
        self.Layout()
        bSizer1.Fit(self)
        
        self.Centre(wx.BOTH)
        
        # Connect Events
        self.Bind(wx.EVT_CLOSE, self.on_exit_button)
        self.b_connect.Bind(wx.EVT_BUTTON, self.on_connect_button)
        self.b_test.Bind(wx.EVT_BUTTON, self.on_test_button)
        self.b_cancel.Bind(wx.EVT_BUTTON, self.on_cancel_button)
    
    def __del__(self):
        pass
    
    # Virtual event handlers, overide them in your derived class
    def on_exit_button(self, event):
        event.Skip()
    
    def on_connect_button(self, event):
        event.Skip()
    
    def on_test_button(self, event):
        event.Skip()
    
    def on_cancel_button(self, event):
        event.Skip()
