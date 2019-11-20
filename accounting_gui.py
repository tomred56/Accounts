import wx
import wx.adv
import wx.grid
import wx.lib.stattext

expand_option = dict(flag=wx.EXPAND)
no_options = dict()
empty_space = ((0, 0), expand_option)


class BaseWindow(wx.Frame):
    
    def __init__(self, data, *args, **kw):
        
        super().__init__(*args, **kw)
        self.Bind(wx.EVT_CHAR_HOOK, self.on_key_pressed_somewhere)
        self.data = data
        self.toolbar = self.CreateToolBar(wx.TB_VERTICAL | wx.TB_TEXT)
        self.make_toolbar()
        self.toolbar.Realize()
        
        self.status_bar = self.CreateStatusBar()
        self.status_bar.SetFieldsCount(3)
        self.SetStatusBar(self.status_bar)
        
        self.calendar = MyCalendar(self)
        self.SetStatusText(self.calendar.use_date, 1)
        
        self.summary = MakeSummary(self)
        self.list = MakeGrid(self)
        self.main_sizer = wx.BoxSizer(wx.VERTICAL)
        self.main_sizer.SetMinSize(500, 500)
        self.main_sizer.Add(self.summary, wx.EXPAND)
        self.main_sizer.Add(self.list, wx.EXPAND)
        self.SetSizerAndFit(self.main_sizer)
        self.SetTitle('Manage My Accounts')
        self.Centre()
    
    def on_date(self, e):
        if self.calendar.visible:
            self.calendar.Hide()
        else:
            self.calendar.Show()
    
    def on_quit(self, e):
        self.Close()
    
    def on_key_pressed_somewhere(self, e):
        if e.GetKeyCode() == wx.WXK_ESCAPE and self.calendar.visible:
            self.calendar.Hide()
    
    def make_toolbar(self):
        icon1 = wx.Bitmap('System Equalizer.bmp')
        icon2 = wx.Bitmap('Money.bmp')
        icon3 = wx.Bitmap('Drawer Closed.bmp')
        icon4 = wx.Bitmap('Search.bmp')
        icon5 = wx.ArtProvider.GetBitmap(wx.ART_QUIT)
        q_tool1 = self.toolbar.AddTool(1, 'Summary', icon1, 'display overall summary')
        q_tool2 = self.toolbar.AddTool(2, 'Accounts', icon2)
        q_tool3 = self.toolbar.AddTool(3, 'Descriptions', icon3)
        q_tool4 = self.toolbar.AddTool(4, 'Forecast', icon4)
        q_tool5 = self.toolbar.AddTool(5, 'Date', icon4)
        q_tool6 = self.toolbar.AddTool(6, 'Quit', icon5, 'Leave the application')
        self.Bind(wx.EVT_TOOL, self.on_quit, q_tool1)
        self.Bind(wx.EVT_TOOL, self.on_quit, q_tool2)
        self.Bind(wx.EVT_TOOL, self.on_quit, q_tool3)
        self.Bind(wx.EVT_TOOL, self.on_quit, q_tool4)
        self.Bind(wx.EVT_TOOL, self.on_date, q_tool5)
        self.Bind(wx.EVT_TOOL, self.on_quit, q_tool6)


class MakeSummary(wx.Panel):
    
    def __init__(self, *args, **kw):
        super().__init__(*args, **kw)
        self.grid = wx.GridSizer(cols=6, vgap=10, hgap=20)
        values = self.get_values(args[0].data)
        layout = []
        for k, v in values.items():
            layout.append((wx.StaticText(self, -1, k), wx.EXPAND))
            layout.append((wx.TextCtrl(self, value=f'{v}', style=wx.TE_READONLY | wx.TE_RIGHT), wx.EXPAND))
        self.grid.AddMany(layout)
        self.SetSizerAndFit(self.grid)

    def get_values(self, data):
    
        a_data = data['accounts']
        t_data = data['transactions']
        values = {}
        a_types = a_data.fetch_types()
        if a_data.process('fetch'):
            if t_data.process('fetch'):
                values['Income'] = sum(v['amount'] for v in t_data.records if v['amount'] > 0)
                values['Expenditure'] = sum(v['amount'] for v in t_data.records if v['amount'] < 0)
                values['Balance'] = sum(v['amount'] for v in t_data.records)
                for a_type in a_types:
                    values[a_type] = sum(v['amount'] for v in t_data.records
                                         if a_data.records[v['parent']]['account_type'] == a_type)
        return values
        

class MakeGrid(wx.Panel):
    def __init__(self, *args, **kw):
        wx.Panel.__init__(self, *args, **kw)
        
        # Create a wxGrid object
        self.grid = wx.grid.Grid(self)
        
        # Then we call CreateGrid to set the dimensions of the grid
        # (100 rows and 10 columns in this example)
        self.grid.CreateGrid(100, 10)
        
        # We can set the sizes of individual rows and columns
        # in pixels
        self.grid.SetRowSize(0, 60)
        self.grid.SetColSize(0, 120)
        
        # And set grid cell contents as strings
        self.grid.SetCellValue(0, 0, 'wxGrid is good')
        
        # We can specify that some cells are read.only
        self.grid.SetCellValue(0, 3, 'This is read.only')
        self.grid.SetReadOnly(0, 3)
        
        # Colours can be specified for grid cell contents
        self.grid.SetCellValue(3, 3, 'green on grey')
        self.grid.SetCellTextColour(3, 3, wx.GREEN)
        self.grid.SetCellBackgroundColour(3, 3, wx.LIGHT_GREY)
        
        # We can specify the some cells will store numeric
        # values rather than strings. Here we set grid column 5
        # to hold floating point values displayed with width of 6
        # and precision of 2
        self.grid.SetColFormatFloat(5, 6, 2)
        self.grid.SetCellValue(0, 6, '3.1415')
        
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.grid)
        self.SetSizerAndFit(sizer)


class MyCalendar(wx.Frame):
    
    def __init__(self, *args, **kargs):
        wx.Frame.__init__(self, *args, style=(wx.FRAME_FLOAT_ON_PARENT | wx.CAPTION |
                                              wx.FRAME_TOOL_WINDOW), **kargs)
        self.parent = args[0]
        self.visible = False
        self.Bind(wx.EVT_SHOW, self.OnShowChanged)
        self.calctrl = wx.adv.GenericCalendarCtrl(self, -1, wx.DateTime.Now())
        self.calctrl.Bind(wx.adv.EVT_CALENDAR, self.OnDateChanged)
        self.calctrl.Bind(wx.adv.EVT_CALENDAR_SEL_CHANGED, self.OnDate)
        self.use_date = self.calctrl.GetDate().Format('%d-%b-%Y')
        self.sizer1 = wx.BoxSizer()
        self.sizer1.Add(self.calctrl)
        self.SetSizerAndFit(self.sizer1)
        self.SetTitle('Calendar')
        self.Centre()
    
    def OnDate(self, event):
        pass
    
    def OnDateChanged(self, event):
        self.use_date = self.calctrl.GetDate().Format('%d-%b-%Y')
        self.parent.SetStatusText(self.use_date, 2)
        self.Hide()
    
    def OnShowChanged(self, event):
        if event.IsShown():
            self.visible = True
        else:
            self.visible = False


def main():
    import data_structures as db
    data = {
            'categories': db.Categories(),
            'sub_categories': db.SubCategories(),
            'details': db.Details(),
            'companies': db.Companies(),
            'accounts': db.Accounts(),
            'transactions': db.Transactions(),
            'rules': db.Rules(),
            'cards': db.Cards(),
            'contacts': db.Contacts()
    }
    app = wx.App()
    mainframe = BaseWindow(data, parent=None)
    mainframe.Show()
    
    app.MainLoop()


if __name__ == '__main__':
    main()
