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
                           style=0)

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)
        self.SetForegroundColour(wx.Colour(0, 0, 255))
        self.SetBackgroundColour(wx.Colour(213, 255, 255))

        self.top_sizer = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText6 = wx.StaticText(self, wx.ID_ANY, u"Enter Connection Details ", wx.DefaultPosition,
                                           wx.DefaultSize, 0 | wx.BORDER_RAISED)
        self.m_staticText6.Wrap(-1)

        self.m_staticText6.SetFont(
            wx.Font(wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD,
                    False, wx.EmptyString))
        self.m_staticText6.SetForegroundColour(wx.Colour(0, 0, 255))

        self.top_sizer.Add(self.m_staticText6, 0, wx.ALL, 5)

        fgSizer1 = wx.FlexGridSizer(0, 2, 0, 0)
        fgSizer1.AddGrowableCol(1)
        fgSizer1.SetFlexibleDirection(wx.HORIZONTAL)
        fgSizer1.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        self.m_staticText1 = wx.StaticText(self, wx.ID_ANY, u"User Name", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText1.Wrap(-1)

        self.m_staticText1.SetForegroundColour(wx.Colour(0, 0, 255))

        fgSizer1.Add(self.m_staticText1, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 10)

        self.user_name = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize,
                                     wx.TE_PROCESS_ENTER)
        self.user_name.SetMaxLength(32)
        fgSizer1.Add(self.user_name, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL | wx.EXPAND, 10)

        self.m_staticText2 = wx.StaticText(self, wx.ID_ANY, u"Password", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText2.Wrap(-1)

        self.m_staticText2.SetForegroundColour(wx.Colour(0, 0, 255))

        fgSizer1.Add(self.m_staticText2, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 10)

        self.password = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize,
                                    wx.TE_PASSWORD | wx.TE_PROCESS_ENTER)
        self.password.SetMaxLength(32)
        fgSizer1.Add(self.password, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL | wx.EXPAND, 10)

        self.m_staticText3 = wx.StaticText(self, wx.ID_ANY, u"Host", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText3.Wrap(-1)

        self.m_staticText3.SetForegroundColour(wx.Colour(0, 0, 255))

        fgSizer1.Add(self.m_staticText3, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 10)

        self.host_name = wx.TextCtrl(self, wx.ID_ANY, u"localhost", wx.DefaultPosition, wx.DefaultSize,
                                     wx.TE_PROCESS_ENTER)
        self.host_name.SetMaxLength(32)
        fgSizer1.Add(self.host_name, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL | wx.EXPAND, 10)

        self.m_staticText4 = wx.StaticText(self, wx.ID_ANY, u"Database", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText4.Wrap(-1)

        self.m_staticText4.SetForegroundColour(wx.Colour(0, 0, 255))

        fgSizer1.Add(self.m_staticText4, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 10)

        self.use_db = wx.TextCtrl(self, wx.ID_ANY, u"test", wx.DefaultPosition, wx.DefaultSize, wx.TE_PROCESS_ENTER)
        self.use_db.SetMaxLength(32)
        fgSizer1.Add(self.use_db, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL | wx.EXPAND, 10)

        self.top_sizer.Add(fgSizer1, 0, wx.EXPAND, 5)

        fgSizer2 = wx.FlexGridSizer(0, 4, 0, 0)
        fgSizer2.AddGrowableCol(0)
        fgSizer2.AddGrowableCol(1)
        fgSizer2.AddGrowableCol(2)
        fgSizer2.AddGrowableCol(3)
        fgSizer2.SetFlexibleDirection(wx.BOTH)
        fgSizer2.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        self.b_connect = wx.Button(self, wx.ID_ANY, u"Connect", wx.DefaultPosition, wx.DefaultSize, 0)

        self.b_connect.SetDefault()
        fgSizer2.Add(self.b_connect, 0, wx.ALL | wx.EXPAND, 5)

        self.b_disconnect = wx.Button(self, wx.ID_ANY, u"Disconnect", wx.DefaultPosition, wx.DefaultSize, 0)
        self.b_disconnect.Enable(False)

        fgSizer2.Add(self.b_disconnect, 0, wx.ALL, 5)

        self.b_test = wx.Button(self, wx.ID_ANY, u"Test", wx.DefaultPosition, wx.DefaultSize, 0)
        fgSizer2.Add(self.b_test, 0, wx.ALIGN_CENTER | wx.ALL | wx.EXPAND, 5)

        self.b_cancel = wx.Button(self, wx.ID_ANY, u"Cancel", wx.DefaultPosition, wx.DefaultSize, 0)
        fgSizer2.Add(self.b_cancel, 0, wx.ALL, 5)

        self.top_sizer.Add(fgSizer2, 0, wx.ALL, 5)

        guage_sizer = wx.BoxSizer(wx.VERTICAL)

        self.progress = wx.Gauge(self, wx.ID_ANY, 100, wx.DefaultPosition, wx.DefaultSize,
                                 wx.GA_HORIZONTAL | wx.GA_SMOOTH)
        self.progress.SetValue(0)
        self.progress.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_WINDOW))
        self.progress.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_WINDOW))

        guage_sizer.Add(self.progress, 0, wx.ALL | wx.EXPAND, 5)

        self.top_sizer.Add(guage_sizer, 0, wx.ALL | wx.EXPAND, 5)

        self.message_sizer = wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, wx.EmptyString), wx.VERTICAL)

        self.message0 = wx.StaticText(self.message_sizer.GetStaticBox(), wx.ID_ANY,
                                      u"Double click to copy message to clipboard", wx.DefaultPosition, wx.DefaultSize,
                                      0)
        self.message0.Wrap(-1)

        self.message0.SetForegroundColour(wx.Colour(0, 0, 255))

        self.message_sizer.Add(self.message0, 0, wx.LEFT | wx.EXPAND, 5)

        self.message1 = wx.StaticText(self.message_sizer.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                      wx.DefaultSize, wx.ALIGN_LEFT | wx.BORDER_STATIC)
        self.message1.Wrap(-1)

        self.message1.SetBackgroundColour(wx.Colour(255, 255, 255))
        self.message1.SetToolTip(u"Double Click to copy to clipboard")

        self.message_sizer.Add(self.message1, 1, wx.ALIGN_CENTER | wx.BOTTOM | wx.LEFT | wx.RIGHT | wx.EXPAND, 5)

        self.top_sizer.Add(self.message_sizer, 1, wx.ALIGN_CENTER | wx.BOTTOM | wx.EXPAND | wx.LEFT | wx.RIGHT, 1)

        self.SetSizer(self.top_sizer)
        self.Layout()
        self.top_sizer.Fit(self)

        self.Centre(wx.BOTH)

        # Connect Events
        self.Bind(wx.EVT_CLOSE, self.on_exit_button)
        self.user_name.Bind(wx.EVT_TEXT_ENTER, self.on_connect_button)
        self.password.Bind(wx.EVT_TEXT_ENTER, self.on_connect_button)
        self.host_name.Bind(wx.EVT_TEXT_ENTER, self.on_connect_button)
        self.use_db.Bind(wx.EVT_TEXT_ENTER, self.on_connect_button)
        self.b_connect.Bind(wx.EVT_BUTTON, self.on_connect_button)
        self.b_disconnect.Bind(wx.EVT_BUTTON, self.on_disconnect_button)
        self.b_test.Bind(wx.EVT_BUTTON, self.on_test_button)
        self.b_cancel.Bind(wx.EVT_BUTTON, self.on_cancel_button)
        self.message0.Bind(wx.EVT_LEFT_DCLICK, self.on_left_dclick)
        self.message1.Bind(wx.EVT_LEFT_DCLICK, self.on_left_dclick)

    def __del__(self):
        pass

    # Virtual event handlers, overide them in your derived class
    def on_exit_button(self, event):
        event.Skip()

    def on_connect_button(self, event):
        event.Skip()

    def on_disconnect_button(self, event):
        event.Skip()

    def on_test_button(self, event):
        event.Skip()

    def on_cancel_button(self, event):
        event.Skip()

    def on_left_dclick(self, event):
        event.Skip()
