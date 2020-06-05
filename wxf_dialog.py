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

class db_sign_in ( wx.Dialog ):

    def __init__( self, parent ):
        wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Sign In", pos = wx.DefaultPosition, size = wx.Size( -1,-1 ), style = 0 )

        self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
        self.SetForegroundColour( wx.Colour( 0, 0, 255 ) )
        self.SetBackgroundColour( wx.Colour( 213, 255, 255 ) )

        fgsizer0 = wx.BoxSizer( wx.VERTICAL )

        self.header = wx.StaticText( self, wx.ID_ANY, u"Enter Connection Details ", wx.DefaultPosition, wx.DefaultSize, 0|wx.BORDER_RAISED )
        self.header.Wrap( -1 )

        self.header.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )
        self.header.SetForegroundColour( wx.Colour( 0, 0, 255 ) )
        self.header.SetBackgroundColour( wx.Colour( 213, 255, 255 ) )

        fgsizer0.Add( self.header, 0, wx.ALL|wx.EXPAND, 5 )

        fgSizer1 = wx.FlexGridSizer( 0, 2, 0, 0 )
        fgSizer1.AddGrowableCol( 1 )
        fgSizer1.SetFlexibleDirection( wx.HORIZONTAL )
        fgSizer1.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

        self.m_staticText1 = wx.StaticText( self, wx.ID_ANY, u"User Name", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText1.Wrap( -1 )

        self.m_staticText1.SetForegroundColour( wx.Colour( 0, 0, 255 ) )

        fgSizer1.Add( self.m_staticText1, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 10 )

        self.user_name = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_PROCESS_ENTER )
        self.user_name.SetMaxLength( 32 )
        fgSizer1.Add( self.user_name, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL|wx.EXPAND, 10 )

        self.m_staticText2 = wx.StaticText( self, wx.ID_ANY, u"Password", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText2.Wrap( -1 )

        self.m_staticText2.SetForegroundColour( wx.Colour( 0, 0, 255 ) )

        fgSizer1.Add( self.m_staticText2, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 10 )

        self.password = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_PASSWORD|wx.TE_PROCESS_ENTER )
        self.password.SetMaxLength( 32 )
        fgSizer1.Add( self.password, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL|wx.EXPAND, 10 )

        self.m_staticText3 = wx.StaticText( self, wx.ID_ANY, u"Host", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText3.Wrap( -1 )

        self.m_staticText3.SetForegroundColour( wx.Colour( 0, 0, 255 ) )

        fgSizer1.Add( self.m_staticText3, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 10 )

        self.host_name = wx.TextCtrl( self, wx.ID_ANY, u"localhost", wx.DefaultPosition, wx.DefaultSize, wx.TE_PROCESS_ENTER )
        self.host_name.SetMaxLength( 32 )
        fgSizer1.Add( self.host_name, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL|wx.EXPAND, 10 )

        self.m_staticText4 = wx.StaticText( self, wx.ID_ANY, u"Database", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText4.Wrap( -1 )

        self.m_staticText4.SetForegroundColour( wx.Colour( 0, 0, 255 ) )

        fgSizer1.Add( self.m_staticText4, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 10 )

        self.use_db = wx.TextCtrl( self, wx.ID_ANY, u"test", wx.DefaultPosition, wx.DefaultSize, wx.TE_PROCESS_ENTER )
        self.use_db.SetMaxLength( 32 )
        fgSizer1.Add( self.use_db, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL|wx.EXPAND, 10 )


        fgsizer0.Add( fgSizer1, 0, wx.EXPAND, 5 )

        fgSizer2 = wx.FlexGridSizer( 0, 4, 0, 0 )
        fgSizer2.AddGrowableCol( 0 )
        fgSizer2.AddGrowableCol( 1 )
        fgSizer2.AddGrowableCol( 2 )
        fgSizer2.AddGrowableCol( 3 )
        fgSizer2.SetFlexibleDirection( wx.BOTH )
        fgSizer2.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

        self.b_connect = wx.Button( self, wx.ID_ANY, u"Connect", wx.DefaultPosition, wx.DefaultSize, 0 )

        self.b_connect.SetDefault()
        fgSizer2.Add( self.b_connect, 0, wx.ALL|wx.EXPAND|wx.RESERVE_SPACE_EVEN_IF_HIDDEN, 5 )

        self.b_disconnect = wx.Button( self, wx.ID_ANY, u"Disconnect", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.b_disconnect.Enable( False )

        fgSizer2.Add( self.b_disconnect, 0, wx.ALL|wx.EXPAND|wx.RESERVE_SPACE_EVEN_IF_HIDDEN, 5 )

        self.b_test = wx.Button( self, wx.ID_ANY, u"Test", wx.DefaultPosition, wx.DefaultSize, 0 )
        fgSizer2.Add( self.b_test, 0, wx.ALL|wx.EXPAND|wx.RESERVE_SPACE_EVEN_IF_HIDDEN, 5 )

        self.b_cancel = wx.Button( self, wx.ID_ANY, u"Cancel", wx.DefaultPosition, wx.DefaultSize, 0 )
        fgSizer2.Add( self.b_cancel, 0, wx.ALL|wx.EXPAND|wx.RESERVE_SPACE_EVEN_IF_HIDDEN, 5 )


        fgsizer0.Add( fgSizer2, 0, wx.ALL, 5 )

        guage_sizer = wx.BoxSizer( wx.VERTICAL )

        self.progress = wx.Gauge( self, wx.ID_ANY, 100, wx.DefaultPosition, wx.DefaultSize, wx.GA_HORIZONTAL|wx.GA_SMOOTH )
        self.progress.SetValue( 0 )
        self.progress.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )
        self.progress.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )

        guage_sizer.Add( self.progress, 0, wx.ALL|wx.EXPAND, 5 )


        fgsizer0.Add( guage_sizer, 0, wx.ALL|wx.EXPAND, 5 )

        self.message1 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE )
        fgsizer0.Add( self.message1, 1, wx.ALL|wx.EXPAND, 5 )


        self.SetSizer( fgsizer0 )
        self.Layout()
        fgsizer0.Fit( self )

        self.Centre( wx.BOTH )

        # Connect Events
        self.Bind( wx.EVT_CLOSE, self.on_exit_button )
        self.user_name.Bind( wx.EVT_TEXT_ENTER, self.on_connect_button )
        self.password.Bind( wx.EVT_TEXT_ENTER, self.on_connect_button )
        self.host_name.Bind( wx.EVT_TEXT_ENTER, self.on_connect_button )
        self.use_db.Bind( wx.EVT_TEXT_ENTER, self.on_connect_button )
        self.b_connect.Bind( wx.EVT_BUTTON, self.on_connect_button )
        self.b_disconnect.Bind( wx.EVT_BUTTON, self.on_disconnect_button )
        self.b_test.Bind( wx.EVT_BUTTON, self.on_test_button )
        self.b_cancel.Bind( wx.EVT_BUTTON, self.on_cancel_button )

    def __del__( self ):
        pass


    # Virtual event handlers, overide them in your derived class
    def on_exit_button( self, event ):
        event.Skip()

    def on_connect_button( self, event ):
        event.Skip()





    def on_disconnect_button( self, event ):
        event.Skip()

    def on_test_button( self, event ):
        event.Skip()

    def on_cancel_button( self, event ):
        event.Skip()


###########################################################################
## Class select_file
###########################################################################

class select_file ( wx.Dialog ):

    def __init__( self, parent ):
        wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Select a CSV file...", pos = wx.DefaultPosition, size = wx.DefaultSize, style = wx.DEFAULT_DIALOG_STYLE )

        self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

        bSizer3 = wx.BoxSizer( wx.VERTICAL )

        self.file_selected = wx.FilePickerCtrl( self, wx.ID_ANY, wx.EmptyString, u"Select a file", u"*.*", wx.DefaultPosition, wx.DefaultSize, wx.FLP_CHANGE_DIR|wx.FLP_DEFAULT_STYLE|wx.FLP_SMALL )
        bSizer3.Add( self.file_selected, 0, wx.ALL|wx.EXPAND, 5 )

        bSizer4 = wx.BoxSizer( wx.HORIZONTAL )

        self.b_ok = wx.Button( self, wx.ID_ANY, u"OK", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer4.Add( self.b_ok, 0, wx.ALL|wx.EXPAND|wx.RESERVE_SPACE_EVEN_IF_HIDDEN, 5 )

        self.b_cancel = wx.Button( self, wx.ID_ANY, u"Cancel", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer4.Add( self.b_cancel, 0, wx.ALL|wx.EXPAND|wx.RESERVE_SPACE_EVEN_IF_HIDDEN, 5 )


        bSizer3.Add( bSizer4, 1, wx.EXPAND, 5 )


        self.SetSizer( bSizer3 )
        self.Layout()
        bSizer3.Fit( self )

        self.Centre( wx.BOTH )

        # Connect Events
        self.Bind( wx.EVT_CLOSE, self.on_exit_button )
        self.file_selected.Bind( wx.EVT_FILEPICKER_CHANGED, self.on_select_file )
        self.b_ok.Bind( wx.EVT_BUTTON, self.on_ok_button )
        self.b_cancel.Bind( wx.EVT_BUTTON, self.on_cancel_button )

    def __del__( self ):
        pass


    # Virtual event handlers, overide them in your derived class
    def on_exit_button( self, event ):
        event.Skip()

    def on_select_file( self, event ):
        event.Skip()

    def on_ok_button( self, event ):
        event.Skip()

    def on_cancel_button( self, event ):
        event.Skip()


