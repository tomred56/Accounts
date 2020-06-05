import csv

import wx
import wx.adv
import wx.grid
import wx.lib.stattext

import data_structures as db
import wxf_dialog
# from datetime import datetime
import wxf_tab_forms as wxf
from statics import *
from db_signin import *

expand_option = dict(flag=wx.EXPAND)
no_options = dict()
empty_space = ((0, 0), expand_option)
LOOKUPS: dict = {
        'parent': None,
        'grandparent': None,
        'category': 'categories',
        'subcategory': 'subcategories',
        'detail': 'details',
        'supplier': 'suppliers'
        }

ANCESTORS = db.ANCESTORS
DESCENDANTS = db.DESCENDANTS


def db_setup():
    db_details = {
            'db': None,
            'host': '192.168.0.235',
            'name': 'test',
            'user': 'dermot'
            }
    return db_details


def set_message(self, fields=(0,), values=('',), message=None, retain=False):
    '''
    set status and local message fields
    :param self: local message owner
    :param fields: tuple of status bar fields to update: -1 (or any -ve value) = all, 0 = none (default)
    :param values: tuple of status bar field values: if no matching value for field set to blank
    :param message: string displayed in self.p_message, none to leave unchanged (default)
    :param retain: if true, message is prepended to existing contents of p_message (default:False)
    :return:
    '''
    frame = self.GetTopLevelParent()
    count = frame.status_bar.GetFieldsCount()
    assert len(fields) > 0 and ((fields[0] <= 0 and len(fields) == 1)
                                or ((v for v in fields if v <= 0 or v > count - 1))), f'invalid status fields {fields}'
    if fields[0]:
        if fields[0] < 0:
            fields = [i for i in range(0, count)]
        for i in range(0, len(fields)):
            if i < len(values):
                status_msg = values[i]
            else:
                status_msg = ''
            frame.SetStatusText(status_msg, fields[i])
    if getattr(self, 'p_message', None):
        if isinstance(message, str):
            if retain:
                message += f'\n{self.p_message.GetValue()}'
            self.p_message.SetValue(message)
        if self.p_message.GetValue():
            self.message.Show()
        else:
            self.message.Hide()
    self.Layout()


def main_refresh(self, focus=None):
    '''
    :param self:
    :param focus:
    :return:
    '''
    base = self.GetTopLevelParent()
    width, height = wx.GetDisplaySize()
    # page = base.p_notebook.GetPage(base.p_notebook.GetSelection())
    # page_name = page.Name.lower()
    # if page_name == 'taxonomy':
    #     page_w, page_h = page.GetSize()
    #     frame_w, frame_h = self.GetSize()
    #     root_count = page.tree_trunk.GetChildrenCount(page.tree_trunk.GetRootItem(), False)
    #     frame_height = min(height, (root_count * 20) + frame_h)
    #     # frame_height = min(height, (root_count * 20) + frame_h + page_h)
    #     frame_size = wx.Rect((-1,0), (-1,frame_height))
    # else:
    #     frame_size = wx.Rect((-1,-1))
    frame_size = wx.Rect((-1, -1))
    if self != base:
        self.Layout()
        self.SetSizerAndFit(self.top_sizer)
    base.Layout()
    base.SetSizerAndFit(base.top_sizer)
    base.Centre()
    # base.SetSize(frame_size)
    base.Show()
    base.Raise()
    if focus:
        focus.SetFocus()


def _button_refresh(self, refresh=0, default=0, show=('all',), enable=(), focus=()):
    base = self.GetTopLevelParent()
    all_buttons = {
            'refresh': base.b_refresh,
            'import': base.b_import,
            'new': base.b_new,
            'edit': base.b_edit,
            'reset': base.b_reset,
            'apply': base.b_apply,
            'cancel': base.b_cancel,
            'exit': base.b_exit
            }
    
    if refresh:
        show = self.button_settings[0]
        enable = self.button_settings[1]
        focus = self.button_settings[2]
    elif default:
        show = self.button_defaults[0]
        enable = self.button_defaults[1]
        focus = self.button_defaults[2]

    for k, v in all_buttons.items():
        if k == 'exit':
            v.Show()
            v.Enable()
        elif k in self.buttons and (k in show or 'all' in show):
            v.Show()
            if k in enable:
                v.Enable()
                if k in focus:
                    v.SetFocus()
            else:
                v.Disable()
        else:
            v.Hide()
            v.Disable()
            
    self.button_settings[0] = show
    self.button_settings[1] = enable
    self.button_settings[2] = focus


def _activate_table(self, activate_this):
    assert activate_this in self.base.db_tables.keys(), f'{activate_this} is not a valid table name'
    base = self.GetTopLevelParent()
    db_tables = base.db_tables
    return db_tables.get(activate_this, None), db_tables.get(ANCESTORS[activate_this][0], None), db_tables.get(
            ANCESTORS[activate_this][1], None)


class BaseWindow(wxf.MainFrame):
    
    def __init__(self, *args, **kwargs):
        
        super().__init__(*args, **kwargs)
        # self.Bind(wx.EVT_CHAR_HOOK, self.on_key_pressed_somewhere)
        self.Hide()
        self.db_details = db_setup()
        self.db_tables = {}
        self.summary_cell_values = []
        self.this_table = None
        self.parent_table = None
        self.grandparent_table = None
        self.this_page = None
        self.this_page_name = None
        self.is_new = False
        self.is_edit = False
        self.all_tabs = {}
        self.status = {'summary': TX_CLEAN, 'suppliers': TX_CLEAN, 'accounts': TX_CLEAN, 'transactions': TX_CLEAN,
                       'taxonomy': TX_CLEAN,
                       'connect': CX_DISCONNECTED}

        while self.status['connect'] == CX_DISCONNECTED:
            self.status['connect'] = self.connect()
        if self.status['connect'] == CX_CONNECTED:
            self.__notebook_init()
            self.Bind(wx.EVT_BUTTON, self.on_exit_button)
            set_message(self, (2,), ('CONNECTED',), message='')
            main_refresh(self)
        else:
            self.closedown()
    
    def connect(self):
        with SignInDialog(None, self.db_details, self.db_tables, self.status['connect']) as dlg:
            result = dlg.ShowModal()
        return result
    
    def __notebook_init(self):
        self.all_tabs['summary'] = Summary(self.p_notebook, 'summary',
                                           ('accounts', 'transactions'))
        self.all_tabs['suppliers'] = GridManagement(self.p_notebook, 'suppliers',
                                                    ('suppliers', 'contacts'))
        self.all_tabs['accounts'] = GridManagement(self.p_notebook, 'accounts',
                                                   ('accounts', 'transactions'))
        self.all_tabs['transactions'] = GridManagement(self.p_notebook, 'transactions',
                                                       ('transactions',))
        self.all_tabs['transactions_new'] = GridManagement(self.p_notebook, 'transactions_new',
                                                           ('transactions_new',))
        self.all_tabs['taxonomy'] = TreeManagement(self.p_notebook, 'taxonomy',
                                                   ('categories', 'subcategories', 'details'))
        self.p_notebook.AddPage(self.all_tabs['summary'], 'Summary')
        self.p_notebook.AddPage(self.all_tabs['transactions'], 'Transactions')
        self.p_notebook.AddPage(self.all_tabs['transactions_new'], 'Imported Transactions')
        self.p_notebook.AddPage(self.all_tabs['accounts'], 'Accounts')
        self.p_notebook.AddPage(self.all_tabs['suppliers'], 'Suppliers')
        self.p_notebook.AddPage(self.all_tabs['taxonomy'], 'Taxonomy')
        
        this_tab = self.p_notebook.FindPage(self.all_tabs['accounts'])
        self.p_notebook.SetSelection(this_tab)

    def on_changing_page(self, event):
        this_page = event.GetSelection()
        this_tab = self.p_notebook.GetPage(this_page)
        this_label = this_tab.Name.lower()
        if self.status['connect'] == CX_DISCONNECTED:
            event.Veto()
            set_message(self, (1,), ('Not connected to database',))
            main_refresh(self)
        elif self.status[this_label] & TX_CHANGED:
            if not self.status[this_label] & TX_EMPTY:
                event.Veto()
            set_message(self, (1,), (f'Unsaved changes on this tab',))
            main_refresh(self)
    
    def on_new_page(self, event):
        this_page = self.p_notebook.GetSelection()
        self.this_page = self.p_notebook.GetPage(this_page)
        self.this_page_name = self.this_page.Name.lower()
        self.set_refresh(self.this_page_name, self.this_page)
        print(self.this_page_name)
        _button_refresh(self.this_page, refresh=1)
        main_refresh(self)
    
    def set_refresh(self, page_name, page):
        if page_name == 'taxonomy':
            page.tree_trunk.Layout()
        else:
            page._rows_refresh()
            # page.tree.Layout()
            # page.tree.SetSizerAndFit(page.tree_sizer)
        page.Layout()
        page.SetSizerAndFit(page.top_sizer)
        self.p_notebook.Layout()
        # else:
        #     page.Layout()
        #     try:
        #         page.SetSizerAndFit(page.top_sizer)
        #     except Exception as e:
        #         pass
    
    '''
    def __rows_init(self):
        self.rows_sizer = wx.grid.Grid(self)
        self.rows_sizer.CreateGrid(0, 0)
        self.rows_sizer.SetSelectionMode(wx.grid.Grid.SelectRows)
        self.rows_sizer.cursor = (-1, -1)
        self.Bind(wx.grid.EVT_GRID_RANGE_SELECT, self.on_row_selected, self.rows_sizer)
        self.Bind(wx.grid.EVT_GRID_CELL_LEFT_DCLICK, self.on_edit_button, self.rows_sizer)
        self.rows.Add(self.rows_sizer, 1, wx.EXPAND | wx.ALL | wx.ALIGN_CENTER, 5, None)

    def __rows_load(self, my_parent=0, my_grandparent=0):

        if self.rows_sizer.GetNumberRows():
            self.rows_sizer.DeleteRows(0, self.rows_sizer.GetNumberRows())
        if self.rows_sizer.GetNumberCols():
            self.rows_sizer.DeleteCols(0, self.rows_sizer.GetNumberCols())
        self.rows_sizer.Layout()
        columns = self.this_table.columns
        colcount = self.this_table.colcount
        self.rows_sizer.InsertCols(0, colcount - 1)
        filter = self.this_table.get_filter()
        for i in range(1, colcount):
            self.rows_sizer.SetColLabelValue(i - 1, columns[i][0].replace('_', ' ').title())
            if columns[i][1] is int and columns[i][0] not in LOOKUPS.keys():
                self.rows_sizer.SetColFormatNumber(i - 1)
            elif columns[i][1] is float:
                self.rows_sizer.SetColFormatFloat(i - 1, 10, 2)

        if my_parent and (len(filter) != 1 or filter.get('parent', 0) != my_parent):
            self.this_table.process('fetch', parent=my_parent)
        else:
            if self.this_table.rowcount != len(self.this_table.rows):
                self.this_table.process('fetch')
        self.rows_sizer.InsertRows(0, self.this_table.sel_rowcount)
        rows = self.this_table.rows
        row = 0
        for k, v in rows.items():
            self.rows_sizer.SetRowLabelValue(row, f'{k}')
            col = 0
            for k1, v1 in dict(v).items():
                if k1 == 'key':
                    continue
                elif k1 in LOOKUPS.keys():
                    self.rows_sizer.SetCellValue(row, col, f'{self.__lookup_name(k1, v1)}')
                else:
                    self.rows_sizer.SetCellValue(row, col, f'{v1}')
                col += 1
            row += 1
        self.rows_sizer.EnableEditing(False)
        self.rows_sizer.AutoSizeColumns(False)

    def __rows_refresh(self, my_parent=0, my_grandparent=0):
        self.__rows_load(my_parent=0, my_grandparent=0)
        self.rows_sizer.Layout()
        self.rows.Layout()
        if self.rows_sizer.GetNumberRows():
            self.rows_sizer.GoToCell(0, 0)
            self.rows_sizer.cursor = (0, 0)
            self.b_edit.Enable()
        else:
            self.b_edit.Disable()

    def __lookup_name(self, lookup='', key=0):
        table = None
        if lookup == 'parent':
            table = self.parent_table
        elif lookup == 'grandparent':
            table = self.grandparent_table
        else:
            table = self.db_tables.get(lookup, None)
        if table.rowcount != len(table.rows):
            table.process('fetch')
        return dict(table.rows.get(key, {})).get('name', 'Description not found')

    def __main_single_init(self):
        self.single.Layout()
        self.main_single.Layout()
        self.main_sizer.Show(self.main_single, False, True)

    def __single_load(self):
        self.main_sizer.Show(self.rows, False, True)
        self.single.Clear()
        self.b_new.Disable()
        self.b_edit.Disable()
        self.b_reset.Enable()
        self.b_apply.Enable()
        self.b_cancel.Enable()
        self.single_panel = self.all_panels[self.this_table.table_name]
        if self.is_new:
            self.single_panel.new()
        elif self.is_edit:
            self.single_panel.update()
        self.single.Add(self.single_panel)
        self.__single_reset()

    def __single_reset_panel(self):
        if self.is_new:
            self.single_panel.new()
        elif self.is_edit:
            self.single_panel.update()
        set_message(self, (1,))
        self.__single_reset()

    def __single_reset(self):

        self.single_panel.Show(True)
        self.single_panel.Layout()
        self.single.Layout()
        self.main_single.Layout()
        self.main_sizer.Show(self.single, True, True)
        main_refresh(self)
    '''

    def closedown(self):
        for page in self.all_tabs.values():
            try:
                page.tree_trunk.Unbind(wx.EVT_TREE_SEL_CHANGED)
                page.tree_trunk.Unbind(wx.EVT_TREE_SEL_CHANGING)
            except Exception as e:
                pass
        try:
            self.db_details['db'].close()
        except Exception as e:
            pass
        finally:
            self.db_details = {}
            self.db_tables = {}
            self.status['connect'] = CX_DISCONNECTED
            self.Close()
    
    # def main_refresh(self, layers):
    #     #        self.p_header.SetLabel(f'Table: {self.this_table_name.capitalize()}')
    #     self.main_sizer.Layout()
    #     self.Layout()
    #     self.SetSizerAndFit(self.main_sizer)
    #     self.Centre()
    #     self.Show()
    #     self.Raise()

    def on_key_pressed_somewhere(self, e):
        print(f'a key pressed {e}')
        e.Skip()

    #    def on_date(self, e):
    #        if self.calendar.visible:
    #            self.calendar.Hide()
    #        else:
    #            self.calendar.Show()

    def on_refresh_button(self, event):
        self.this_page.on_refresh_button(event)

    def on_import_button(self, event):
        self.this_page.on_import_button(event)

    def on_new_button(self, event):
        self.this_page.on_new_button(event)

    def on_edit_button(self, event):
        self.this_page.on_edit_button(event)

    def on_reset_button(self, event):
        self.this_page.on_reset_button(event)

    def on_apply_button(self, event):
        self.this_page.on_apply_button(event)

    def on_cancel_button(self, event):
        self.this_page.on_cancel_button(event)

    def on_exit_button(self, event):
        self.closedown()

    def on_status_dclick(self, event):
        place = self.status_bar.GetFieldRect(2)
        if event.GetX() >= place.GetLeft() and event.GetX() <= place.GetRight():
            self.connect()


class SelectBranch(wx.Dialog):
    def __init__(self, parent, selections, label=''):
        super().__init__(parent)
        boxer = wx.BoxSizer(wx.VERTICAL)
        buttons = wx.BoxSizer()
        self.radio_box = wx.RadioBox(self, wx.ID_ANY, choices=list(selections))
        self.button_ok = wx.Button(self, id=wx.ID_OK)
        self.button_cancel = wx.Button(self, id=wx.ID_CANCEL)
        buttons.Add(self.button_ok, 0, wx.ALL, 5)
        buttons.Add(self.button_cancel, 0, wx.ALL, 5)
        self.radio_box.SetSelection(0)
        if label:
            self.radio_box.SetLabel(label)
        for i in range(0, len(selections)):
            self.radio_box.SetItemLabel(i, selections[i].capitalize())
        boxer.Add(self.radio_box, 0, wx.ALL, 5)
        boxer.Add(buttons, 0, wx.ALL, 5)

        self.SetSizerAndFit(boxer)
        self.Layout()

        self.Centre(wx.BOTH)

        # Connect Events
        self.Bind(wx.EVT_CLOSE, self.on_cancel)
        self.button_ok.Bind(wx.EVT_BUTTON, self.on_selection)
        self.button_cancel.Bind(wx.EVT_BUTTON, self.on_cancel)

    def __del__(self):
        pass

    def on_selection(self, event):
        self.EndModal(self.radio_box.GetSelection())

    def on_cancel(self, event):
        self.EndModal(-1)

'''
class SelectCSV(wxf_dialog.select_file):
    
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.selection = ''
        self.file_selected.SetInitialDirectory(self.parent.import_file)
        self.b_ok.Disable()
    
    def on_select_file(self, event):
        self.selection = self.file_selected.GetPath()
        self.Layout()
        self.b_ok.Enable()
    
    def on_ok_button(self, event):
        self.parent.import_file = self.selection
        self.close_dialog(0)
    
    def on_cancel_button(self, event):
        self.close_dialog(1)
    
    def on_exit_button(self, event):
        self.close_dialog(1)
    
    def close_dialog(self, result):
        self.EndModal(result)


class SignInDialog(wxf_dialog.db_sign_in):
    
    def __init__(self, parent, db_details, db_tables, status):
        super().__init__(parent)
        self.db_details = db_details
        self.db_tables = db_tables
        self.status = status
        self.activity = None
        if self.status & CX_CONNECTED:
            self.b_disconnect.Enable()
            self.b_connect.Disable()
            self.b_test.Disable()
        else:
            self.status = CX_FAILED
            self.b_connect.Enable()
            self.b_disconnect.Disable()
            self.b_test.Enable()
        self.user_name.SetValue(db_details['user'])
        self.use_db.SetValue(db_details['name'])
        self.host_name.SetValue(db_details['host'])
        self.password.SetValue('')
        self.message1.SetValue('')
        # self.message0.Hide()
        # self.message1.Hide()
        self.progress.Hide()
        # self.SetSizerAndFit(self.top_sizer)
        self.Raise()

    def on_test_button(self, event):
        self.activity = 'test'
        if self.validated():
            is_valid, message, database = db.select_db(host=self.host_name.GetValue(),
                                                       use_db=self.use_db.GetValue(),
                                                       user=self.user_name.GetValue(),
                                                       password=self.password.GetValue())
            if is_valid:
                database.close()
                self.send_message(CX_CONNECTED, 'connection works')
                self.status = CX_DISCONNECTED
            else:
                self.send_message(CX_FAILED, f'error connecting\n{message}')
                self.status = CX_FAILED
        else:
            self.send_message(CX_FAILED, f'name, password (if required), host, and database must be entered')

    def on_connect_button(self, event):
        self.activity = 'connect'
        if self.validated():
            is_valid, message, database = db.select_db(host=self.host_name.GetValue(),
                                                       use_db=self.use_db.GetValue(),
                                                       user=self.user_name.GetValue(),
                                                       password=self.password.GetValue())
            if is_valid:
                self.db_details['db'] = database
                self.db_details['host'] = self.host_name.GetValue()
                self.db_details['name'] = self.use_db.GetValue()
                self.db_details['user'] = self.user_name.GetValue()
                db.get_structure(database)
                self.progress.SetRange(len(db._T_STRUCTURE))
                self.progress.SetValue(0)
                self.progress.Show()
                self.Layout()
                # self.SetSizerAndFit(self.top_sizer)
                for table in db._T_STRUCTURE.keys():
                    self.db_tables[table] = db.DataTables(database, table)
                    # self.db_tables[table].process()
                    self.progress.SetValue(self.progress.GetValue() + 1)
                self.progress.Hide()
                self.status = CX_CONNECTED
                self.close_dialog()
            else:
                self.send_message(CX_FAILED, f'error connecting\n{message}')
                self.status = CX_FAILED
        else:
            self.send_message(CX_FAILED, f'name, host and database must be entered')

    def on_disconnect_button(self, event):
        self.activity = 'disconnect'
        try:
            self.db_details['db'].close()
        finally:
            self.db_tables = {}
            self.db_details['db'] = None
            self.status = CX_DISCONNECTED
            self.b_connect.Enable()
            self.b_disconnect.Disable()
            self.b_test.Enable()
            self.send_message(CX_FAILED, f'not connected')

    def validated(self):
        is_valid = True
        if not self.user_name.GetValue() or not self.host_name.GetValue() or not self.use_db.GetValue():
            self.status = CX_FAILED
            is_valid = False
        return is_valid

    def send_message(self, status, message):
        if status == CX_CONNECTED:
            self.message1.SetForegroundColour(wx.GREEN)
            # self.message0.Hide()
        else:
            self.message1.SetForegroundColour(wx.RED)
            # self.message0.Show()
        self.message1.Show()
        self.message1.SetValue(message)
        # self.message1.Layout()
        # self.message_sizer.Layout()
        self.Layout()
        # self.SetSizerAndFit(self.top_sizer)

    def on_left_dclick(self, event):
        if wx.TheClipboard.Open():
            wx.TheClipboard.SetData(wx.TextDataObject(self.message1.GetLabelText()))
            wx.TheClipboard.Close()

    def on_cancel_button(self, event):
        self.close_dialog()
    
    def on_exit_button(self, event):
        if self.status != CX_CONNECTED:
            self.status = CX_FAILED
        self.close_dialog()

    def close_dialog(self):
        if not self.activity or self.status != CX_CONNECTED:
            self.EndModal(CX_FAILED)
        else:
            self.EndModal(self.status)
'''

class TreeManagement(wxf.TreeManager):
    
    def __init__(self, parent, tab_name, tables):
        super().__init__(parent, name=tab_name)
        self.Hide()
        self.parent = parent
        self.tab_name = tab_name
        self.base = self.GetTopLevelParent()
        self.status = self.base.status
        self.db_tables = self.base.db_tables
        self.tables = tables
        self.this_table, self.parent_table, self.grandparent_table = _activate_table(self, tables[0])
        self._root = self.tree_trunk.AddRoot(self.tab_name)
        self.status[self.tab_name] = TX_EMPTY
        self.branch_level = None
        self.branch_data = None
        self.parent_branch = None
        self.parent_branch_level = None
        self.parent_branch_data = None
        self.child_branch = None
        self.child_branch_level = None
        self.child_branch_data = None
        if self.tab_name == 'taxonomy':
            self.panel = TaxonomyPanel(self, self.tab_name, self.tables)
            self.panel_sizer.Add(self.panel, 1, wx.ALL, 5)
            self.buttons = ['new', 'edit', 'reset', 'apply', 'cancel']
            self.button_settings = [('all',), ('new', 'edit'), ()]
            self.button_defaults = [('all',), ('new', 'edit'), ()]
        #     self.tree_panel.AddChild(TaxonomyPanel(self, self.tab_name, self.tables))
        #     self.panel = self.tree_panel.GetChildren()[0]
        #     sizer = self.tree_panel.GetContainingSizer()
        #     sizer.Add(self.panel)
        # elif self.tab_name == 'suppliers':
        #     self.tree_panel.AddChild(Suppliers(self, self.tab_name, self.tables))
        #     self.panel = self.tree_panel.GetChildren()[0]
        #     sizer = self.tree_panel.GetContainingSizer()
        #     sizer.Add(self.panel)
        # elif self.tab_name == 'accounts':
        #     self.tree_panel.AddChild(Accounts(self, self.tab_name, self.tables))
        #     self.panel = self.tree_panel.GetChildren()[0]
        #     sizer = self.tree_panel.GetContainingSizer()
        #     sizer.Add(self.panel)
        # elif self.tab_name == 'transactions':
        #     self.tree_panel.AddChild(Transactions(self, self.tab_name, self.tables))
        #     self.panel = self.tree_panel.GetChildren()[0]
        #     sizer = self.tree_panel.GetContainingSizer()
        #     sizer.Add(self.panel)
        else:
            self.panel = None
        # self.top_sizer.Remove(1)
        # self.top_sizer.Insert(1, self.tree_panel, 0, wx.ALL | wx.EXPAND, 5)
        self.branch = self.__tree_init()
        self.tree_sizer.Layout()
        self.panel_sizer.Layout()
        main_refresh(self)

    def __tree_init(self):
        panel = self.tree_panel
        tree = self.tree_trunk
        if self.status[self.tab_name] & TX_EMPTY:
            self.__load_branches(branch=self._root, levels=self.tables)
            first_item = tree.GetFirstChild(self._root)
            if first_item[0].IsOk():
                tree.SelectItem(first_item[0])
                tree.SetFocusedItem(first_item[0])
                self.status[self.tab_name] = TX_CLEAN
                panel.Hide()
                _button_refresh(self, enable=('new', 'edit'))
            else:
                self.status[self.tab_name] = TX_EMPTY
                self.branch_level = self.tables[0]
                self.__get_changes('add', self.tables[0])
                panel.Show()
                _button_refresh(self, enable=('cancel',))
        self.__tree_accel()
        return tree.GetSelection()

    def __redraw(self):
        panel = self.panel
        tree = self.tree_trunk
        if branch := tree.GetSelection():
            info = tree.GetItemData(branch)
            levels = info.get('levels', ())
            data = info.get('data')
        else:
            levels = self.tables
            data = {}
        self.__refresh_data(levels[0])
        if self.status[self.tab_name] & TX_ADD_CHILD:
            self.__refresh_data(levels[1], data['key'])
        if self.status[self.tab_name] & TX_EMPTY:
            self.branch = self.__tree_init()
            # key = self.this_table.get_next() - 1
            # new_data = self.this_table.rows[key]
            # self.branch = tree.InsertItem(self.parent_branch, self.branch,
            #                               new_data['name'],
            #                               data={'levels': levels, 'data': new_data})
            self.status[self.tab_name] = TX_ADD_PEER
            _button_refresh(self, enable=('cancel',))
            tree.SelectItem(self.branch)
            tree.SetFocusedItem(self.branch)
            self.__get_changes('add', levels[0])
        elif self.status[self.tab_name] & TX_EDIT:
            key = data['key']
            new_data = self.this_table.rows[key]
            tree.SetItemText(self.branch, new_data['name'])
            for k, v in new_data.items():
                data[k] = v
            tree.SelectItem(branch)
            tree.SetFocusedItem(branch)
            self.status[self.tab_name] = TX_CLEAN
            _button_refresh(self, enable=('new', 'edit'))
            panel.new_values()
            panel.Hide()
        elif self.status[self.tab_name] & TX_ADD_PEER:
            key = self.this_table.get_next() - 1
            new_data = self.this_table.rows[key]
            self.branch = tree.InsertItem(self.parent_branch, self.branch,
                                          new_data['name'],
                                          data={'levels': levels, 'data': new_data})
            self.status[self.tab_name] = TX_ADD_PEER
            _button_refresh(self, enable=('cancel',))
            tree.SelectItem(self.branch)
            tree.SetFocusedItem(self.branch)
            self.__get_changes('add', levels[0])
        elif self.status[self.tab_name] & TX_ADD_CHILD:
            key = self.this_table.get_next() - 1
            self.child_branch_data = self.this_table.rows[key]
            self.child_branch = tree.InsertItem(self.branch, 0,
                                                self.child_branch_data['name'],
                                                data={
                                                        'levels': levels[1:],
                                                        'data': self.child_branch_data
                                                        })
            self.status[self.tab_name] = TX_ADD_PEER
            _button_refresh(self, enable=('cancel',))
            tree.SelectItem(self.child_branch)
            tree.SetFocusedItem(self.branch)
            self.__get_changes('add', levels[1])
        self.__tree_accel()
        self.SetSizerAndFit(self.top_sizer)
        self.Layout()

    def __get_changes(self, action, table):
        assert action in ('add', 'edit'), f'Unrecognised taxonomy action {action} {table} '
        panel = self.panel
        level = self.branch_level
        branch_data = self.branch_data
        parent_data = self.parent_branch_data
        parent = ''
        self.this_table, self.parent_table, self.grandparent_table = _activate_table(self, self.branch_level)
        min_date = START_DATE.date()
        max_date = END_DATE.date()
        self.status[self.tab_name] |= TX_CLEAN
        if parent_data:
            parent = ' in ' + parent_data.get('name', '')
        if action == 'add':
            # panel.p_name.SetValue('')
            if level == table:
                self.status[self.tab_name] |= TX_ADD_PEER
                if parent_data:
                    min_date = parent_data['start_date']
                    max_date = parent_data['end_date']
            else:
                self.status[self.tab_name] |= TX_ADD_CHILD
                min_date = branch_data['start_date']
                max_date = branch_data['end_date']
                self.this_table, self.parent_table, self.grandparent_table = _activate_table(self, table)
                self.child_branch_level = table
            # panel.p_start_date.SetValue(min_date)
            # panel.p_end_date.SetValue(max_date)
            panel.new_values(min_date, max_date)
        else:
            # panel.p_name.SetValue(branch_data['name'])
            # panel.p_start_date.SetValue(max(min_date, min(max_date, branch_data['start_date'])))
            # panel.p_end_date.SetValue(min(max_date, max(min_date, branch_data['end_date'])))
            panel.load_values_from_branch(self.branch_data)
            self.status[self.tab_name] |= TX_EDIT
    
        panel.p_start_date.SetRange(min_date, max_date)
        panel.p_end_date.SetRange(min_date, max_date)
        _button_refresh(self, enable=('cancel',))
        if self.status[self.tab_name] & TX_ADD_CHILD and self.branch != self._root:
            parent = f" in {branch_data['name']}"
        elif parent_data:
            parent = f" in {parent_data['name']}"
        panel.panel_heading.SetLabel(f'{action} {table} {parent}'.title())
        panel.Layout()
        panel.Show()
        panel.p_name.SetFocus()
        set_message(self, (1,), (f'{action} record',), message='')
        self.Layout()
        self.SetSizerAndFit(self.top_sizer)
        main_refresh(self)
    
    def __apply(self):
        is_valid = True
        
        tree = self.tree_trunk
        if branch := tree.GetSelection():
            info = tree.GetItemData(branch)
            data = info['data']
            table_name = info['level'][0]
        else:
            data = {}
            table_name = ''
        panel = self.panel
        if self.status[self.tab_name] & TX_ADD_CHILD:
            table = self.db_tables.get(self.child_branch_level)
        else:
            table = self.db_tables.get(self.branch_level)
        fields_in_panel = {v[0]: f'p_{v[0]}' for v in table.columns
                           if hasattr(panel, f'p_{v[0]}')}
        if self.status[self.tab_name] & TX_EDIT:
            row = data
        else:
            row = {}
        if parent := fields_in_panel.get('parent', ''):
            self.parent_record = panel.lookup_lists['parent'][1].get(getattr(panel, parent).GetValue(), 0)
            self.parent_branch_data = self.parent_table.rows.get(self.parent_record, {})
        else:
            self.parent_record = 0
        new_data = {}
        for v in table.columns:
            p_field = None
            new_value = None
            if v[0] in fields_in_panel.keys():
                p_field = getattr(panel, fields_in_panel[v[0]])
                if v[0] in LOOKUPS.keys():
                    if not (new_value := panel.lookup_lists[v[0]][0]):
                        is_valid = False
                        set_message(self, (1,), ('error detected',),
                                    message=f'lookup {p_field.Name} cannot be blank')
                else:
                    new_value = p_field.GetValue()
                if v[0] == 'name' and not new_value:
                    is_valid = False
                    set_message(self, (1,), ('error detected',), message=f'description cannot be blank')
                if self.status[self.tab_name] & (TX_ADD_CHILD | TX_ADD_PEER) or new_value != row.get(v[0], None):
                    if isinstance(p_field, wx._adv.DatePickerCtrl):
                        new_data[v[0]] = new_value.FormatISODate()
                    else:
                        new_data[v[0]] = new_value
            elif v[0] == 'key':
                if self.status[self.tab_name] & TX_EDIT:
                    new_data['key'] = data['key']
                continue
            elif v[0] == 'sort':
                if self.status[self.tab_name] & TX_ADD_CHILD:
                    children = tree.GetChildrenCount(branch, False)
                    new_data['sort'] = (data['sort'] * 1000) + children + 1
                elif self.status[self.tab_name] & TX_ADD_PEER:
                    new_data['sort'] = data.get('sort', 0) + 1
                else:
                    continue
            else:
                new_data[v[0]] = v[2]
            
            if v[0] == 'parent':
                if self.status[self.tab_name] & TX_ADD_CHILD:
                    new_data['parent'] = data['key']
                elif self.status[self.tab_name] & TX_ADD_PEER:
                    new_data['parent'] = self.parent_branch_data.get('key', 0)
                else:
                    continue
            elif v[0] == 'grandparent':
                if self.status[self.tab_name] & TX_ADD_CHILD:
                    new_data['grandparent'] = self.parent_branch_data['key']
                elif self.status[self.tab_name] & TX_ADD_PEER:
                    grandparent_branch = tree.GetItemParent(self.parent_branch)
                    grandparent_branch_data = tree.GetData(grandparent_branch)
                    new_data['grandparent'] = grandparent_branch_data['key']
                else:
                    continue

        if is_valid:
            if self.status[self.tab_name] & TX_EDIT:
                action = 'update'
            else:
                action = 'insert'
            if is_valid := self.this_table.process_db(action, **new_data):
                if action == 'update':
                    for table in DESCENDANTS.get(table_name, ()):
                        self.db_tables[table].tab_changed = True
                self.__redraw()
                set_message(self, (1,), (f'Successful {action}',), message='')
                self.this_table.process_db('fetch')
                self.status[self.tab_name] = TX_CLEAN
                self.panel.Hide()
                _button_refresh(self, enable=('new', 'edit'))
        if not is_valid:
            set_message(self, (1,), ('Error detected',), message=self.this_table.get_message(), retain=True)
        main_refresh(self)
        return is_valid

    def __swap(self, branch1, branch2):
        b1_info = self.tree_trunk.GetItemData(branch1)
        b1_data = b1_info['data']
        b2_info = self.tree_trunk.GetItemData(branch2)
        b2_data = b2_info['data']
        parent = b1_data.get('parent', 0)
        levels = b1_info['levels']
        new_data1 = {'key': b1_data['key'], 'sort': b2_data['sort']}
        new_data2 = {'key': b2_data['key'], 'sort': b1_data['sort']}
        self.this_table, self.parent_table, self.grandparent_table = _activate_table(self, levels[0])
        if self.this_table.process_db('swap', parent, new_data1, new_data2):
            parent_branch = self.tree_trunk.GetItemParent(branch1)
            self.__load_branches(branch=parent_branch, levels=levels)
        else:
            set_message(self, (1,), (f'error swapping branches',), self.this_table.get_message())

    def __load_branches(self, branch=None, levels=()):
        assert branch.IsOk(), f'invalid parent branch passed to reload'
        assert len(levels) and levels[0] in self.base.db_tables.keys(), f'invalid table names {levels} passed to reload'
        tree = self.tree_trunk
        tree.DeleteChildren(branch)
        next_levels = levels[1:]
        if branch == self._root:
            key = 0
        else:
            item_data = tree.GetItemData(branch)
            key = item_data['data']['key']
    
        self.__refresh_data(levels[0])
        # self.__refresh_data(levels[0], key)
        db_data = self.base.db_tables.get(levels[0], None)
        # for key, record in db_data.rows.items():
        for record in [v for k, v in db_data.rows.items() if not key or v['parent'] == key]:
            container = self.tree_trunk.AppendItem(branch, record['name'],
                                                   data={'levels': levels, 'data': record})
            if next_levels:
                self.__load_branches(container, next_levels)

    def __refresh_data(self, table, parent=0):
        db_data = self.base.db_tables.get(table, None)
        if not parent:
            if db_data.rowcount != db_data.sel_rowcount or db_data.tab_changed:
                db_data.process_db('fetch')
        else:
            db_data.process_db('fetch', parent=parent)

    def __tree_accel(self):
        up_id = wx.NewId()
        down_id = wx.NewId()
        self.Bind(wx.EVT_MENU, self.on_key_up, id=up_id)
        self.Bind(wx.EVT_MENU, self.on_key_down, id=down_id)

        self.tree_trunk.accel_tbl = wx.AcceleratorTable([(wx.ACCEL_ALT, wx.WXK_UP, up_id),
                                                         (wx.ACCEL_ALT, wx.WXK_DOWN, down_id)
                                                         ])
        self.tree_trunk.SetAcceleratorTable(self.tree_trunk.accel_tbl)
    
    def on_key_up(self, event):
        if not self.status[self.tab_name]:
            self.status[self.tab_name] = TX_MOVING
            tree = self.tree_trunk
            new_pos = tree.GetPrevSibling(self.branch)
            if new_pos.IsOk():
                self.__swap(self.branch, new_pos)
            else:
                set_message(self, (1,), ('already at top',))
            self.status[self.tab_name] = TX_CLEAN
        print(f'Alt-up key press')
        event.Skip()
    
    def on_key_down(self, event):
        if not self.status[self.tab_name]:
            self.status[self.tab_name] = TX_MOVING
            tree = self.tree_trunk
            new_pos = tree.GetNextSibling(self.branch)
            if new_pos.IsOk():
                self.__swap(self.branch, new_pos)
            else:
                set_message(self, (1,), ('already at bottom',))
            self.status[self.tab_name] = TX_CLEAN
        print(f'Alt-down key press')
        event.Skip()

    def on_left_double(self, event):
        print('on_edit')
        tree = self.tree_trunk
        pt = event.GetPosition()
        item, flags = tree.HitTest(pt)
        if item.IsOk() and not tree.IsSelected(item):
            tree.SelectItem(item)
            tree.SetFocusedItem(item)
        branch = self.tree_trunk.GetSelection()
        branch_info = self.tree_trunk.GetItemData(branch)
        levels = branch_info['levels']
        self.__get_changes('edit', levels[0].lower())
    
    def on_changing_branch(self, event):
        print(f'on_changing_branch ')
        if self.status[self.tab_name] & TX_CHANGED:
            event.Veto()
            set_message(self, (1,), ('Unsaved Changes',))
            main_refresh(self)

    def on_changed_branch(self, event):
        print('on_changed_branch')
        tree = event.GetEventObject()
        self.branch = tree.GetSelection()
        branch_info = tree.GetItemData(self.branch)
        self.branch_level = branch_info['levels'][0]
        self.branch_data = branch_info['data']
        self.parent_branch = tree.GetItemParent(self.branch)
        if self.parent_branch != self._root:
            parent_branch_info = tree.GetItemData(self.parent_branch)
            self.parent_branch_level = parent_branch_info['levels'][0]
            self.parent_branch_data = parent_branch_info['data']
        else:
            self.parent_branch_level = None
            self.parent_branch_data = None
        self.child_branch = None
        self.child_branch_level = None
        self.child_branch_data = None
        self.status[self.tab_name] = TX_CLEAN
        if self.tree_panel.IsShown():
            self.tree_panel.Hide()
            _button_refresh(self, )
            main_refresh(self)

    def on_right_down(self, event):
        print('on_rdown')
        if self.status[self.tab_name] & TX_CHANGED:
            set_message(self, (1,), ('Unsaved Changes',))
            main_refresh(self)
        else:
            tree = self.tree_trunk
            pt = event.GetPosition()
            item, flags = tree.HitTest(pt)
            if item.IsOk() and not tree.IsSelected(item):
                tree.SelectItem(item)
                tree.SetFocusedItem(item)
            branch = tree.GetSelection()
            branch_info = tree.GetItemData(branch)
            # children = tree.GetChildrenCount(branch)
            levels = branch_info['levels']
            self.m_add_peer.SetItemLabel(f'Add {levels[0].capitalize()}')
            if len(levels) > 1:
                self.m_add_child.SetItemLabel(f'Add {levels[1].capitalize()}')
                self.m_add_child.Enable()
            else:
                self.m_add_child.SetItemLabel(' ')
                self.m_add_child.Enable(False)
            event.Skip()
    
    # def on_menu(self, event):
    #     print('on_menu')
    #     event.Skip()
    #
    def on_message(self, event):
        print('key pressed in message')
    
    #     event.Skip()
    #
    def on_menu_item(self, event):
        print('on_menu_item')
        if event:
            id_selected = event.GetId()
            menu = event.GetEventObject()
            action = menu.GetLabelText(id_selected).lower().split()
            action[1] = LOOKUPS.get(action[1], action[1])
        else:
            action = ['add', self.tables[0]]
        self.__get_changes(action[0], action[1])

    def on_new_button(self, event):
        branch = self.tree_trunk.GetSelection()
        branch_info = self.tree_trunk.GetItemData(branch)
        levels = branch_info.get('levels', ())
        result = 0
        if len(levels) > 1:
            with SelectBranch(self, levels[0:2], 'Select') as dlg:
                result = dlg.ShowModal()
        if result == -1:
            self.on_cancel_button(None)
        else:
            self.__get_changes('add', levels[result])

    def on_edit_button(self, event):
        branch = self.tree_trunk.GetSelection()
        branch_info = self.tree_trunk.GetItemData(branch)
        branch_level = branch_info.get('level', '')
        levels = branch_info['levels']
        self.__get_changes('edit', levels[0].lower())
    
    def on_reset_button(self, event):
        if self.status[self.tab_name] & (TX_CHANGED):
            action = self.panel.panel_heading.GetLabel().lower().split()
            self.__get_changes(action[0], action[1])
        set_message(self, (1,), ('',), message='')
        main_refresh(self)

    def on_apply_button(self, event):
        self.__apply()

    def on_cancel_button(self, event):
        current = self.tree_trunk.GetSelection()
        self.__tree_init()
        self.tree_trunk.SelectItem(current)
        self.tree_trunk.SetFocusedItem(current)
        set_message(self, (1,), message='')
        self.panel.Hide()
        _button_refresh(self, enable=('new', 'edit'))
        self.status[self.tab_name] = TX_CLEAN
        # self.Layout()
        main_refresh(self)

    def on_exit_button(self, event):
        if self.status[self.tab_name] & TX_CHANGED and not self.status[self.tab_name] & TX_RESET:
            set_message(self, (1,), ('Unsaved changes',),
                        message='Press again to confirm you want to leave without saving changes.')
            self.status[self.tab_name] |= TX_RESET
            main_refresh(self)
        else:
            self.status[self.tab_name] = TX_CLEAN
            self.is_tab_dirty = False
            event.Skip()


class GridManagement(wxf.GridManager):
    
    def __init__(self, parent, tab_name, tables):
        super().__init__(parent, name=tab_name)
        self.Hide()
        self.parent = parent
        self.tab_name = tab_name
        self.base = self.GetTopLevelParent()
        self.import_file = ''
        self.status = self.base.status
        self.db_tables = self.base.db_tables
        self.tables = tables
        self.this_table, self.parent_table, self.grandparent_table = _activate_table(self, tables[0])
        self.parent_filter = []
        self.grandparent_filter = []
        if self.tab_name == 'suppliers':
            self.panel = Suppliers(self, self.tab_name, self.tables)
            self.panel_sizer.Add(self.panel, 1, wx.ALL, 5)
            self.buttons = ['new', 'edit', 'reset', 'apply', 'cancel']
            self.button_settings = [('all',), ('new', 'edit'), ()]
            self.button_defaults = [('all',), ('new', 'edit'), ()]
            # self.panel_sizer.Add(Suppliers(self, self.tab_name, self.tables), 1, wx.ALL, 5)
            # self.panel = self.panel_sizer.GetChildren()[0]
            # sizer = self.grid_panel.GetContainingSizer()
            # sizer.Add(self.panel)
        elif self.tab_name == 'accounts':
            self.panel = Accounts(self, self.tab_name, self.tables)
            self.panel_sizer.Add(self.panel, 1, wx.ALL, 5)
            self.buttons = ['new', 'edit', 'reset', 'apply', 'cancel']
            self.button_settings = [('all',), ('new', 'edit'), ()]
            self.button_defaults = [('all',), ('new', 'edit'), ()]
            # self.panel_sizer.Add(Accounts(self, self.tab_name, self.tables))
            # self.panel = self.panel_sizer.GetChildren()[0]
            # sizer = self.grid_panel.GetContainingSizer()
            # sizer.Add(self.panel)
        elif self.tab_name in ('transactions', 'transactions_new'):
            self.panel = Transactions(self, self.tab_name, self.tables)
            self.panel_sizer.Add(self.panel, 1, wx.ALL, 5)
            if self.tab_name =='transactions':
                self.buttons = ['import', 'new', 'edit', 'reset', 'apply', 'cancel']
                self.button_settings = [('all',), ('import', 'new', 'edit'), ()]
                self.button_defaults = [('all',), ('import', 'new', 'edit'), ()]
            else:
                self.buttons = ['edit', 'reset', 'apply', 'cancel']
                self.button_settings = [('all',), ('edit',), ()]
                self.button_defaults = [('all',), ('edit',), ()]

            # self.panel_sizer.Add(Transactions(self, self.tab_name, self.tables))
            # self.panel = self.panel_sizer.GetChildren()[0]
            # sizer = self.grid_panel.GetContainingSizer()
            # sizer.Add(self.panel)
        else:
            self.panel = None
        # self.top_sizer.Remove(1)
        # self.top_sizer.Insert(1, self.tree_panel, 0, wx.ALL | wx.EXPAND, 5)
        self.panel.Hide()
        self.__rows_init()
        self._rows_refresh()
        self.grid_sizer.Layout()
        self.panel_sizer.Layout()
        main_refresh(self)
    
    def __rows_init(self):
        self.grid_sizer = wx.grid.Grid(self)
        self.grid_sizer.CreateGrid(0, 0)
        self.grid_sizer.SetSelectionMode(wx.grid.Grid.SelectRows)
        self.grid_sizer.cursor = (-1, -1)
        self.Bind(wx.grid.EVT_GRID_RANGE_SELECT, self.on_row_selected, self.grid_sizer)
        self.Bind(wx.grid.EVT_GRID_CELL_LEFT_DCLICK, self.on_edit_button, self.grid_sizer)
        self.rows.Add(self.grid_sizer, 1, wx.EXPAND | wx.ALL | wx.ALIGN_CENTER, 5, None)
        self.__grid_accel()
        
    def __rows_load(self, my_parent=0, my_grandparent=0):
    
        panel = self.panel
        if self.grid_sizer.GetNumberRows():
            self.grid_sizer.DeleteRows(0, self.grid_sizer.GetNumberRows())
        if self.grid_sizer.GetNumberCols():
            self.grid_sizer.DeleteCols(0, self.grid_sizer.GetNumberCols())
        self.grid_sizer.Layout()
        columns = self.this_table.columns
        colcount = self.this_table.colcount
        self.grid_sizer.InsertCols(0, colcount - 1)
        # filter = self.this_table.get_filter()
        for i in range(1, colcount):
            self.grid_sizer.SetColLabelValue(i - 1, columns[i][0].replace('_', ' ').title())
            if columns[i][1] is int and columns[i][0] not in LOOKUPS.keys():
                self.grid_sizer.SetColFormatNumber(i - 1)
            elif columns[i][1] is float:
                self.grid_sizer.SetColFormatFloat(i - 1, 10, 2)
        
        if self.grandparent_filter:
            self.this_table.process_db('fetch', grandparent=self.grandparent_filter)
        elif self.parent_filter:
            self.this_table.process_db('fetch', parent=self.parent_filter)
        else:
            if self.this_table.rowcount != self.this_table.sel_rowcount or self.this_table.tab_changed:
                self.this_table.process_db('fetch')
        self.grid_sizer.InsertRows(0, self.this_table.sel_rowcount)
        rows = self.this_table.rows
        row = 0
        for k, v in rows.items():
            self.grid_sizer.SetRowLabelValue(row, f'{k}')
            col = 0
            for k1, v1 in dict(v).items():
                if k1 == 'key':
                    continue
                elif k1 in LOOKUPS.keys():
                    self.grid_sizer.SetCellValue(row, col, f'{self.__lookup_name(k1, v1)}')
                else:
                    self.grid_sizer.SetCellValue(row, col, f'{v1}')
                col += 1
            row += 1
        self.grid_sizer.EnableEditing(False)
        self.grid_sizer.AutoSizeColumns(False)
        if len(rows) == 0:
            self.status[self.tab_name] = TX_EMPTY
            self.__get_changes('add', self.tables[0])
            panel.Show()
            _button_refresh(self, enable=('cancel',))
    
    def _rows_refresh(self, my_parent=0, my_grandparent=0):
        self.__rows_load(my_parent=0, my_grandparent=0)
        self.grid_sizer.Layout()
        self.rows.Layout()
        if self.grid_sizer.GetNumberRows():
            self.grid_sizer.GoToCell(0, 0)
            self.grid_sizer.cursor = (0, 0)
            self.this_row = int(self.grid_sizer.GetRowLabelValue(self.grid_sizer.GetGridCursorRow()))
            self.panel.this_record = int(self.grid_sizer.GetRowLabelValue(self.this_row))
            _button_refresh(self, default=1)
        else:
            _button_refresh(self, enable=('import', 'new'))
    
    def __lookup_name(self, lookup='', key=0):
        table = None
        if lookup == 'parent':
            table = self.parent_table
        elif lookup == 'grandparent':
            table = self.grandparent_table
        else:
            table = self.db_tables.get(LOOKUPS.get(lookup, None), None)
        if table.rowcount != table.sel_rowcount or table.tab_changed:
            table.process_db('fetch')
        return dict(table.rows.get(key, {})).get('name', 'Description not found')
    
    def __get_changes(self, action, table):
        assert action in ('add', 'edit'), f'Unrecognised taxonomy action {action} {table} '
        panel = self.panel
        # self.this_table, self.parent_table, self.grandparent_table = _activate_table(self, table)
        min_date = START_DATE.date()
        max_date = END_DATE.date()
        self.status[self.tab_name] |= TX_CLEAN
        if action == 'add':
            # panel.p_name.SetValue('')
            self.status[self.tab_name] |= TX_ADD_PEER
            # if parent_data:
            #     min_date = parent_data['start_date']
            #     max_date = parent_data['end_date']
            panel.new_values(min_date, max_date)
        else:
            panel.load_values_from_row()
            self.status[self.tab_name] |= TX_EDIT
        
        panel.p_start_date.SetRange(min_date, max_date)
        panel.p_end_date.SetRange(min_date, max_date)
        _button_refresh(self, enable=('cancel',))
        panel.panel_heading.SetLabel(f'{action} {table}')
        panel.Layout()
        panel.Show()
        panel.p_name.SetFocus()
        self.Layout()
        self.SetSizerAndFit(self.top_sizer)
        main_refresh(self)
    
    def __apply(self):
        is_valid = True
        
        panel = self.panel
        table = self.this_table
        table_name = self.tables[0]
        fields_in_panel = {v[0]: f'p_{v[0]}' for v in table.columns
                           if hasattr(panel, f'p_{v[0]}')}
        new_data = {}
        for v in table.columns:
            p_field = None
            new_value = None
            if v[0] in fields_in_panel.keys():
                p_field = getattr(panel, fields_in_panel[v[0]])
                if v[0] in LOOKUPS.keys():
                    if not (new_value := panel.lookup_lists[v[0]][0]):
                        is_valid = False
                        set_message(self, (1,), ('error detected',),
                                    message=f'lookup {p_field.Name} cannot be blank')
                else:
                    new_value = p_field.GetValue()
                if v[0] == 'name' and not new_value:
                    is_valid = False
                    set_message(self, (1,), ('error detected',), message=f'description cannot be blank')
                if self.status[self.tab_name] & (TX_ADD_CHILD | TX_ADD_PEER) or new_value != panel.this_table.rows[
                    panel.this_record].get(v[0], None):
                    if isinstance(p_field, wx._adv.DatePickerCtrl):
                        new_data[v[0]] = new_value.FormatISODate()
                    else:
                        new_data[v[0]] = new_value
            elif v[0] == 'key':
                if self.status[self.tab_name] & TX_EDIT:
                    new_data['key'] = panel.this_record
                continue
            elif v[0] == 'sort':
                if self.status[self.tab_name] & TX_ADD_PEER:
                    new_data['sort'] = panel.this_table.rows[self.this_row].get('sort', 0) + 1
                else:
                    continue
            else:
                new_data[v[0]] = v[2]
            
            # elif v[0] == 'parent':
            #     if self.status[self.tab_name] & TX_ADD_PEER:
            #         new_data['parent'] = self.parent_branch_data.get('key', 0)
            #     else:
            #         continue
            # elif v[0] == 'grandparent':
            #     if self.status[self.tab_name] & TX_ADD_PEER:
            #         grandparent_branch = tree.GetItemParent(self.parent_branch)
            #         grandparent_branch_data = tree.GetData(grandparent_branch)
            #         new_data['grandparent'] = grandparent_branch_data['key']
            #     else:
            #         continue
        
        if is_valid:
            if self.status[self.tab_name] & TX_EDIT:
                action = 'update'
            else:
                action = 'insert'
            if is_valid := self.this_table.process_db(action, **new_data):
                if action == 'update':
                    for table in DESCENDANTS.get(table_name, ()):
                        self.db_tables[table].tab_changed = True
                self._rows_refresh()
                set_message(self, (1,), (f'Successful {action}',), message='')
                # self.this_table.process_db('fetch')
                self.status[self.tab_name] = TX_CLEAN
                self.panel.Hide()
        if not is_valid:
            set_message(self, (1,), ('Error detected',), message=self.this_table.get_message(), retain=True)
        
        main_refresh(self)
        return is_valid
    
    def __swap(self, row1, row2):
        grid = self.grid_sizer
        table = self.this_table
        old_key = int(grid.GetRowLabelValue(row1))
        old_parent = table.rows[old_key].get('parent', 0)
        swap_key = int(grid.GetRowLabelValue(row2))
        swap_parent = table.rows[swap_key].get('parent', 0)
        if old_parent == swap_parent:
            old_sort = table.rows[old_key]['sort']
            swap_sort = table.rows[swap_key]['sort']
            new_data1 = {'key': old_key, 'sort': swap_sort}
            new_data2 = {'key': swap_key, 'sort': old_sort}
            self.this_table, self.parent_table, self.grandparent_table = _activate_table(self, self.tables[0])
            if self.this_table.process_db('swap', None, new_data1, new_data2):
                for table in DESCENDANTS.get(self.tables[0], ()):
                    self.db_tables[table].tab_changed = True
                self._rows_refresh()
                set_message(self, (1,), (f'Successful swap',), message='')
                # self.this_table.process_db('fetch')
                self.status[self.tab_name] = TX_CLEAN
            else:
                set_message(self, (1,), (f'error swapping rows',), self.this_table.get_message())
        else:
            set_message(self, (1,), ('already at top/bottom within the parent group',))

    def __swapb(self, branch1, branch2):
        b1_info = self.tree_trunk.GetItemData(branch1)
        b1_data = b1_info['data']
        b2_info = self.tree_trunk.GetItemData(branch2)
        b2_data = b2_info['data']
        parent = b1_data.get('parent', 0)
        levels = b1_info['levels']
        new_data1 = {'key': b1_data['key'], 'sort': b2_data['sort']}
        new_data2 = {'key': b2_data['key'], 'sort': b1_data['sort']}
        self.this_table, self.parent_table, self.grandparent_table = _activate_table(self, levels[0])
        if self.this_table.process_db('swap', parent, new_data1, new_data2):
            parent_branch = self.tree_trunk.GetItemParent(branch1)
            self.__load_branches(branch=parent_branch, levels=levels)
        else:
            set_message(self, (1,), (f'error swapping branches',), self.this_table.get_message())
    
    def __load_branches(self, branch=None, levels=()):
        assert branch.IsOk(), f'invalid parent branch passed to reload'
        assert len(levels) and levels[0] in self.base.db_tables.keys(), f'invalid table names {levels} passed to reload'
        tree = self.tree_trunk
        tree.DeleteChildren(branch)
        next_levels = levels[1:]
        if branch == self._root:
            key = 0
        else:
            item_data = tree.GetItemData(branch)
            key = item_data['data']['key']
        
        self.__refresh_data(levels[0])
        # self.__refresh_data(levels[0], key)
        db_data = self.base.db_tables.get(levels[0], None)
        # for key, record in db_data.rows.items():
        for record in [v for k, v in db_data.rows.items() if not key or v['parent'] == key]:
            container = self.tree_trunk.AppendItem(branch, record['name'],
                                                   data={'levels': levels, 'data': record})
            if next_levels:
                self.__load_branches(container, next_levels)
    
    def __refresh_data(self, table, parent=0):
        db_data = self.base.db_tables.get(table, None)
        if not parent:
            if db_data.rowcount != db_data.sel_rowcount or db_data.tab_changed:
                db_data.process_db('fetch')
        else:
            db_data.process_db('fetch', parent=parent)
    
    def __grid_accel(self):
        up_id = wx.NewId()
        down_id = wx.NewId()
        self.Bind(wx.EVT_MENU, self.on_key_up, id=up_id)
        self.Bind(wx.EVT_MENU, self.on_key_down, id=down_id)
        
        self.grid_sizer.accel_tbl = wx.AcceleratorTable([(wx.ACCEL_ALT, wx.WXK_UP, up_id),
                                                         (wx.ACCEL_ALT, wx.WXK_DOWN, down_id)
                                                         ])
        self.grid_sizer.SetAcceleratorTable(self.grid_sizer.accel_tbl)
    
    def on_key_up(self, event):
        if not self.status[self.tab_name]:
            self.status[self.tab_name] = TX_MOVING
            grid = self.grid_sizer
            cur_pos = grid.GetGridCursorRow()
            new_pos = max(0, cur_pos - 1)
            if new_pos < cur_pos:
                self.__swap(cur_pos, new_pos)
            else:
                set_message(self, (1,), ('already at top',))
            self.status[self.tab_name] = TX_CLEAN
        print(f'Alt-up key press')
        event.Skip()
    
    def on_key_down(self, event):
        if not self.status[self.tab_name]:
            self.status[self.tab_name] = TX_MOVING
            grid = self.grid_sizer
            cur_pos = grid.GetGridCursorRow()
            new_pos = min(grid.NumberRows, cur_pos + 1)
            if new_pos > cur_pos:
                self.__swap(cur_pos, new_pos)
            else:
                set_message(self, (1,), ('already at bottom',))
            self.status[self.tab_name] = TX_CLEAN
        print(f'Alt-down key press')
        event.Skip()
    
    def on_left_double(self, event):
        print('on_edit')
        grid = self.grid_sizer
        pt = event.GetPosition()
        item, flags = grid.HitTest(pt)
        if item.IsOk() and not item.IsSelection():
            grid.SelectRow(item)
            grid.SetFocus()
        self.__get_changes('edit', self.tables[0].lower())
    
    def on_row_selected(self, e):
        if self.status[self.tab_name] & TX_CHANGED:
            e.Veto()
        elif e.Selecting():
            _button_refresh(self, default=1)
            self.grid_sizer.cursor = (e.GetTopRow(), e.GetLeftCol())
            self.panel.this_row = self.grid_sizer.GetGridCursorRow()
            self.panel.this_record = int(self.grid_sizer.GetRowLabelValue(self.panel.this_row))
        e.Skip()
    
    def on_right_down(self, event):
        print('on_rdown')
        if self.status[self.tab_name] & TX_CHANGED:
            set_message(self, (1,), ('Unsaved Changes',))
            main_refresh(self)
        else:
            tree = self.tree_trunk
            pt = event.GetPosition()
            item, flags = tree.HitTest(pt)
            if item.IsOk() and not tree.IsSelected(item):
                tree.SelectItem(item)
                tree.SetFocusedItem(item)
            branch = tree.GetSelection()
            branch_info = tree.GetItemData(branch)
            # children = tree.GetChildrenCount(branch)
            levels = branch_info['levels']
            self.m_add_peer.SetItemLabel(f'Add {levels[0].capitalize()}')
            if len(levels) > 1:
                self.m_add_child.SetItemLabel(f'Add {levels[1].capitalize()}')
                self.m_add_child.Enable()
            else:
                self.m_add_child.SetItemLabel(' ')
                self.m_add_child.Enable(False)
            event.Skip()
    
    # def on_menu(self, event):
    #     print('on_menu')
    #     event.Skip()
    #
    # def on_menu_called(self, event):
    #     print('on_menu_called')
    #     event.Skip()
    #
    def on_menu_item(self, event):
        print('on_menu_item')
        if event:
            id_selected = event.GetId()
            menu = event.GetEventObject()
            action = menu.GetLabelText(id_selected).lower().split()
            action[1] = LOOKUPS.get(action[1], action[1])
        else:
            action = ['add', self.tables[0]]
        self.__get_changes(action[0], action[1])
    
  
    def on_import_button(self, event):
        home = wx.GetHomeDir()
        if import_file := wx.FileSelector('select csv file to import',
                                          f'{home}\\OneDrive', wildcard='*.csv'):
            # with SelectCSV(self) as dlg:
            #     result = dlg.ShowModal()
            with open(import_file, newline='') as csv_file:
                reader = csv.reader(csv_file)
                for row in reader:
                    print(f'{row}')
    
    def on_new_button(self, event):
        # branch = self.tree_trunk.GetSelection()
        # branch_info = self.tree_trunk.GetItemData(branch)
        # levels = branch_info.get('levels', ())
        # result = 0
        # if len(levels) > 1:
        #     with SelectBranch(self, levels[0:2], 'Select') as dlg:
        #         result = dlg.ShowModal()
        # if result == -1:
        #     self.on_cancel_button(None)
        # else:
        self.__get_changes('add', self.tables[0].lower())
    
    def on_edit_button(self, event):
        # branch = self.tree_trunk.GetSelection()
        # branch_info = self.tree_trunk.GetItemData(branch)
        # branch_level = branch_info.get('level', '')
        # levels = branch_info['levels']
        self.__get_changes('edit', self.tables[0].lower())
    
    def on_reset_button(self, event):
        if self.status[self.tab_name] & TX_CHANGED:
            action = self.panel.panel_heading.GetLabel().lower().split()
            self.__get_changes(action[0], action[1])
        set_message(self, (1,), ('',), message='')
        main_refresh(self)
    
    def on_apply_button(self, event):
        self.__apply()
    
    def on_cancel_button(self, event):
        set_message(self, (1,), message='')
        self.panel.Hide()
        _button_refresh(self, default=1)
        self.status[self.tab_name] = TX_CLEAN
        # self.Layout()
        main_refresh(self)
    
    def on_exit_button(self, event):
        if self.status[self.tab_name] & TX_CHANGED and not self.status[self.tab_name] & TX_RESET:
            set_message(self, (1,), ('Unsaved changes',),
                        message='Press again to confirm you want to leave without saving changes.')
            self.status[self.tab_name] |= TX_RESET
            main_refresh(self)
        else:
            self.status[self.tab_name] = TX_CLEAN
            event.Skip()


class GenericPanelActions:
    
    def __init__(self, **kwargs):
        self.child = kwargs.get('child')
        self.parent = kwargs.get('parent')
        self.base = self.parent.GetTopLevelParent()
        self.child.Hide()
        self.tables = kwargs.get('tables', ())
        self.this_table_name = self.tables[0]
        self.tab_name = kwargs.get('tab_name', 'unknown')
        self.this_table = self.base.db_tables[self.this_table_name]
        self.parent_table = self.base.db_tables.get(ANCESTORS[self.this_table_name][0], None)
        self.grandparent_table = self.base.db_tables.get(ANCESTORS[self.this_table_name][1], None)
        self.parent_row = {}
        self.parent_record = 0
        self.these_grandparents = []
        self.this_grandparent = 0
        self.this_parent = 0
        self.this_record = 0
        self.this_row = 0
        self.this_panel = {v[0]: f'p_{v[0]}' for v in self.this_table.columns
                           if hasattr(self.child, f'p_{v[0]}')}
        self.lookup_lists = {k: (0, {'': 0}) for k in LOOKUPS.keys()}
        self.these_taxonomies = {}
        self.this_taxonomy = [0, 0, 0]
        self.status = self.base.status
        self.child.Hide()
    
    def new_values(self, min_date=START_DATE, max_date=END_DATE):
        if 'grandparent' in self.this_panel.keys():
            self.set_combo('grandparent', table=self.grandparent_table, child_table=self.parent_table)
            for value in range(0, len(self.lookup_lists['grandparent'])):
                if self.set_combo('parent', table=self.parent_table, parent=self.lookup_lists['grandparent'][0]):
                    if parent_row := self.lookup_lists['parent'][0]:
                        min_date = self.parent_table.rows[parent_row]['start_date']
                        max_date = self.parent_table.rows[parent_row]['end_date']
                    break
        elif 'parent' in self.this_panel.keys():
            self.set_combo('parent', table=self.parent_table)
            if parent_row := self.lookup_lists['parent'][0]:
                min_date = self.parent_table.rows[parent_row]['start_date']
                max_date = self.parent_table.rows[parent_row]['end_date']
        elif 'categories' in self.this_panel.keys():
            self.set_combo('categories')
            for value in range(0, len(self.lookup_lists['categories'])):
                if self.set_combo('subcategories', parent=self.lookup_lists['categories'][value]):
                    for value1 in range(0, len(self.lookup_lists['subcategories'])):
                        if self.set_combo('details', parent=self.lookup_lists['subcategories'][value1]):
                            break
        elif 'subcategories' in self.this_panel.keys():
            self.set_combo('subcategories')
            for value in range(0, len(self.lookup_lists['subcategories'])):
                if self.set_combo('details', parent=self.lookup_lists['subcategories'][value]):
                    break
        elif 'details' in self.this_panel.keys():
            self.set_combo('details', parent=self.lookup_lists['subcategories'][0])

        for k, v in self.this_panel.items():
            field = getattr(self, v)
            if k in ('parent', 'grandparent'):
                pass
            elif k in ('category', 'subcategory', 'detail'):
                pass
            elif k in LOOKUPS.keys():
                self.set_combo(k, table=self.base.db_tables[LOOKUPS[k]])
            elif isinstance(field, wx._adv.DatePickerCtrl):
                field.SetRange(min_date, max_date)
                if k == 'start_date':
                    field.SetValue(min_date)
                elif k == 'end_date':
                    field.SetValue(max_date)
                else:
                    field.SetValue(NOW)
            elif isinstance(field, wx.CheckBox):
                field.SetValue(False)
            elif isinstance(field, wx.RadioBox):
                field.SetSelection(0)
            elif isinstance(field, wx.SpinCtrlDouble):
                field.SetValue(0.0)
            else:
                field.SetValue('')
    
    # def new(self, **kwargs):
    #     self.this_row = None
    #     self.this_record = 0
    #     self.parent_row = None
    #     self.parent_record = 0
    #     min_date = START_DATE
    #     max_date = END_DATE
    #     if 'grandparent' in self.this_panel.keys():
    #         self.set_combo('grandparent', table=self.grandparent_table, child_table=self.parent_table)
    #         for value in range(0, len(self.lookup_lists['grandparent'])):
    #             if self.set_combo('parent', table=self.parent_table, parent=self.lookup_lists['grandparent'][0]):
    #                 if parent_row := self.lookup_lists['parent'][0]:
    #                     min_date = self.parent_table.rows[parent_row]['start_date']
    #                     max_date = self.parent_table.rows[parent_row]['end_date']
    #                 break
    #     elif 'parent' in self.this_panel.keys():
    #         self.set_combo('parent', table=self.parent_table)
    #         if parent_row := self.lookup_lists['parent'][0]:
    #             min_date = self.parent_table.rows[parent_row]['start_date']
    #             max_date = self.parent_table.rows[parent_row]['end_date']
    #     elif 'categories' in self.this_panel.keys():
    #         self.set_combo('categories')
    #         for value in range(0, len(self.lookup_lists['categories'])):
    #             if self.set_combo('subcategories', parent=self.lookup_lists['categories'][value]):
    #                 for value1 in range(0, len(self.lookup_lists['subcategories'])):
    #                     if self.set_combo('details', parent=self.lookup_lists['subcategories'][value1]):
    #                         break
    #     elif 'subcategories' in self.this_panel.keys():
    #         self.set_combo('subcategories')
    #         for value in range(0, len(self.lookup_lists['subcategories'])):
    #             if self.set_combo('details', parent=self.lookup_lists['subcategories'][value]):
    #                 break
    #     elif 'details' in self.this_panel.keys():
    #         self.set_combo('details', parent=self.lookup_lists['subcategories'][0])
    #
    #     for k, v in self.this_panel.items():
    #         field = getattr(self, v)
    #         if k in ('parent', 'grandparent'):
    #             pass
    #         elif k in ('category', 'subcategory', 'detail'):
    #             pass
    #         elif k in LOOKUPS.keys():
    #             self.set_combo(k)
    #         elif isinstance(field, wx._adv.DatePickerCtrl):
    #             field.SetRange(min_date, max_date)
    #             if k == 'start_date':
    #                 field.SetValue(min_date)
    #             elif k == 'end_date':
    #                 field.SetValue(max_date)
    #             else:
    #                 field.SetValue(NOW)
    #         elif isinstance(field, wx.CheckBox):
    #             field.SetValue(False)
    #         elif isinstance(field, wx.RadioBox):
    #             field.SetSelection(0)
    #         elif isinstance(field, wx.SpinCtrlDouble):
    #             field.SetValue(0.0)
    #         else:
    #             field.SetValue('')
    
    def load_values_from_branch(self, branch_data):
        row = branch_data
        if 'parent' in self.this_panel.keys():
            self.this_parent = row.get('parent', 0)
            prow = self.parent_table.rows.get(self.this_parent, {})
        else:
            prow = {}

        min_date = prow.get('start_date', START_DATE)
        max_date = prow.get('end_date', END_DATE)

        if 'grandparent' in self.this_panel.keys():
            self.set_combo('grandparent', table=self.grandparent_table, key=row['grandparent'])
            self.set_combo('parent', table=self.parent_table, parent=row['grandparent'], key=row['parent'])
        elif 'parent' in self.this_panel.keys():
            self.set_combo('parent', table=self.parent_table, key=row['parent'])
        elif 'categories' in self.this_panel.keys():
            self.set_combo('categories', key=row['category'])
            self.set_combo('subcategories', key=row['subcategory'])
            self.set_combo('details', parent=row['subcategory'], key=row['detail'])
        elif 'subcategories' in self.this_panel.keys():
            self.set_combo('subcategories', key=row['subcategory'])
            self.set_combo('details', parent=row['subcategory'], key=row['detail'])
        elif 'details' in self.this_panel.keys():
            self.set_combo('details', parent=row['subcategory'])
        
        for k, v in self.this_panel.items():
            field = getattr(self, v)
            if k in ('parent', 'grandparent'):
                pass
            elif k in ('categories', 'subcategories', 'details'):
                pass
            elif k in LOOKUPS.keys():
                self.set_combo(k, table=self.base.db_tables[LOOKUPS[k]], key=row[k])
            elif isinstance(field, wx._adv.DatePickerCtrl):
                field.SetRange(min_date, max_date)
                field.SetValue(row[k])
            else:
                field.SetValue(row[k])
    
    def load_values_from_row(self, **kwargs):
        self.this_row = self.parent.grid_sizer.GetGridCursorRow()
        self.this_record = int(self.parent.grid_sizer.GetRowLabelValue(self.this_row))
        row = self.this_table.rows.get(self.this_record, {})
        if 'parent' in self.this_panel.keys():
            self.this_parent = row.get('parent', 0)
            prow = self.parent_table.rows.get(self.this_parent, {})
        else:
            prow = {}

        min_date = prow.get('start_date', START_DATE)
        max_date = prow.get('end_date', END_DATE)

        if 'grandparent' in self.this_panel.keys():
            self.set_combo('grandparent', table=self.grandparent_table, key=row['grandparent'])
            self.set_combo('parent', table=self.parent_table, parent=row['grandparent'], key=row['parent'])
        elif 'parent' in self.this_panel.keys():
            self.set_combo('parent', table=self.parent_table, key=row['parent'])
        elif 'categories' in self.this_panel.keys():
            self.set_combo('categories', key=row['category'])
            self.set_combo('subcategories', key=row['subcategory'])
            self.set_combo('details', parent=row['subcategory'], key=row['detail'])
        elif 'subcategories' in self.this_panel.keys():
            self.set_combo('subcategories', key=row['subcategory'])
            self.set_combo('details', parent=row['subcategory'], key=row['detail'])
        elif 'details' in self.this_panel.keys():
            self.set_combo('details', parent=row['subcategory'])

        for k, v in self.this_panel.items():
            field = getattr(self, v)
            if k in ('parent', 'grandparent'):
                pass
            elif k in ('categories', 'subcategories', 'details'):
                pass
            elif k in LOOKUPS.keys():
                self.set_combo(k, table=self.base.db_tables[LOOKUPS[k]], key=row[k])
            elif isinstance(field, wx._adv.DatePickerCtrl):
                field.SetRange(min_date, max_date)
                field.SetValue(row[k])
            else:
                field.SetValue(row[k])
    
    # def apply_values(self, **kwargs):
    #     assert self.base.is_new or self.base.is_edit, f'no valid action in progress'
    #     is_valid = True
    #     these_dates = {}
    #     row = dict(self.this_table.rows.get(self.this_record, {}))
    #     if parent := self.this_panel.get('parent', ''):
    #         self.parent_record = self.lookup_lists['parent'][1].get(getattr(self, parent).GetValue(), 0)
    #         self.parent_row = self.parent_table.rows.get(self.parent_record, {})
    #     else:
    #         self.parent_record = 0
    #
    #     new_data = {}
    #     new_value = None
    #     for k, v in self.this_panel.items():
    #         p_field = getattr(self, v)
    #         if k in LOOKUPS.keys():
    #             if not (new_value := self.lookup_lists[k][0]):
    #                 is_valid = False
    #                 set_message(self, (1,), ('error detected',),
    #                             message=f'lookup {p_field.Name} cannot be blank')
    #         else:
    #             new_value = p_field.GetValue()
    #         if self.base.is_new or new_value != row[k]:
    #             if isinstance(p_field, wx._adv.DatePickerCtrl):
    #                 new_data[k] = new_value.FormatISODate()
    #                 these_dates[k] = datetime.strptime(new_data[k], '%Y-%m-%d').date()
    #             else:
    #                 new_data[k] = new_value
    #     if self.parent_record:
    #         if these_dates.get('start_date') and these_dates['start_date'] < self.parent_row.get('start_date', 0):
    #             is_valid = False
    #             set_message(self, (1,), ('error detected',),
    #                         message=f'start_date {these_dates["start_date"]} is before '
    #                                 f'parent start_date {self.parent_row["start_date"]}')
    #         if these_dates.get('end_date') and these_dates['end_date'] > self.parent_row.get('end_date', 0):
    #             is_valid = False
    #             set_message(self, (1,), ('error detected',),
    #                         message=f'end_date {these_dates["end_date"]} is after '
    #                                 f'parent end_date {self.parent_row["end_date"]}')
    #     if is_valid:
    #         if self.base.is_new:
    #             new_data['sort'] = self.this_table.rowcount + 1
    #             action = 'insert'
    #         else:
    #             new_data['key'] = self.this_record
    #             action = 'update'
    #         if is_valid := self.this_table.process_db(action, **new_data):
    #             set_message(self, (1,), (f'Successful {action}',), message='')
    #             self.this_table.process_db('fetch')
    #         else:
    #             set_message(self, (1,), ('Error detected',), message=self.this_table.get_message())
    #
    #     return is_valid
    #
    # def apply(self, **kwargs):
    #     assert self.base.is_new or self.base.is_edit, f'no valid action in progress'
    #     is_valid = True
    #     these_dates = {}
    #     row = dict(self.this_table.rows.get(self.this_record, {}))
    #     if parent := self.this_panel.get('parent', ''):
    #         self.parent_record = self.lookup_lists['parent'][1].get(getattr(self, parent).GetValue(), 0)
    #         self.parent_row = self.parent_table.rows.get(self.parent_record, {})
    #     else:
    #         self.parent_record = 0
    #
    #     new_data = {}
    #     new_value = None
    #     for k, v in self.this_panel.items():
    #         p_field = getattr(self, v)
    #         if k in LOOKUPS.keys():
    #             if not (new_value := self.lookup_lists[k][0]):
    #                 is_valid = False
    #                 set_message(self, (1,), ('error detected',),
    #                             message=f'lookup {p_field.Name} cannot be blank')
    #         else:
    #             new_value = p_field.GetValue()
    #         if self.base.is_new or new_value != row[k]:
    #             if isinstance(p_field, wx._adv.DatePickerCtrl):
    #                 new_data[k] = new_value.FormatISODate()
    #                 these_dates[k] = datetime.strptime(new_data[k], '%Y-%m-%d').date()
    #             else:
    #                 new_data[k] = new_value
    #     if self.parent_record:
    #         if these_dates.get('start_date') and these_dates['start_date'] < self.parent_row.get('start_date', 0):
    #             is_valid = False
    #             set_message(self, (1,), ('error detected',),
    #                         message=f'start_date {these_dates["start_date"]} is before '
    #                                 f'parent start_date {self.parent_row["start_date"]}')
    #         if these_dates.get('end_date') and these_dates['end_date'] > self.parent_row.get('end_date', 0):
    #             is_valid = False
    #             set_message(self, (1,), ('error detected',),
    #                         message=f'end_date {these_dates["end_date"]} is after '
    #                                 f'parent end_date {self.parent_row["end_date"]}')
    #     if is_valid:
    #         if self.base.is_new:
    #             new_data['sort'] = self.this_table.rowcount + 1
    #             action = 'insert'
    #         else:
    #             new_data['key'] = self.this_record
    #             action = 'update'
    #         if is_valid := self.this_table.process(action, **new_data):
    #             set_message(self, (1,), (f'Successful {action}',), message='')
    #             self.this_table.process('fetch')
    #         else:
    #             set_message(self, (1,), ('Error detected',), message=self.this_table.get_message())
    #
    #     return is_valid
    
    def set_combo(self, field_name, table=None, child_table=None, parent=0, key=0):
        if not table:
            table = self.base.db_tables[field_name]
        if table.rowcount != table.sel_rowcount or table.tab_changed:
            table.process('fetch')
        if child_table and (child_table.rowcount != child_table.sel_rowcount or
                            child_table.tab_changed):
            child_table.process_db('fetch')
        combo_list = {'description not found': 0}
        for test_key, row in (
                d := {k: v for k, v in table.rows.items() if not parent or parent == v['parent']}).items():
            #            if child_table and child_table.process(parent=test_key) and not child_table.sel_rowcount:
            if child_table:
                for child_row in (
                        d1 := {k: v for k, v in child_table.rows.items() if test_key == v['parent']}).values():
                    combo_list[row['name']] = row['key']
            else:
                combo_list[row['name']] = row['key']
        field = getattr(self, f'p_{field_name}')
        field.Set(list(combo_list.keys()))
        field.Select(0)
        if key:
            try:
                field.Select(field.GetStrings().index(table.get_descriptions(key=key)))
            except Exception as e:
                pass
        self.lookup_lists[field_name] = [combo_list.get(field.GetValue(), 0), combo_list]
        return field.GetCount()

    def _on_lookup(self, event):
        combo = event.EventObject
        field_name = combo.Name
        field = getattr(self, f'p_{field_name}')
        if field_name == 'grandparent':
            grandparent_row = self.lookup_lists['grandparent'][0] = self.lookup_lists['grandparent'][1][
                field.GetValue()]
            self.set_combo('parent', table=self.parent_table, parent=self.lookup_lists['grandparent'][0])
            min_date = self.grandparent_table.rows[grandparent_row]['start_date']
            max_date = self.grandparent_table.rows[grandparent_row]['end_date']
            if parent_row := self.lookup_lists['parent'][0]:
                min_date = self.parent_table.rows[parent_row]['start_date']
                max_date = self.parent_table.rows[parent_row]['end_date']
            field_start = getattr(self, 'p_start_date')
            field_value = field_start.GetValue()
            field_start.SetValue(max(field_value, min_date))
            field_start.SetRange(min_date, max_date)
            field_end = getattr(self, 'p_end_date')
            field_value = field_end.GetValue()
            field_end.SetValue(min(field_value, max_date))
            field_end.SetRange(min_date, max_date)
        elif field_name == 'parent':
            self.lookup_lists['parent'][0] = self.lookup_lists['parent'][1][field.GetValue()]
            if parent_row := self.lookup_lists['parent'][0]:
                min_date = self.parent_table.rows[parent_row]['start_date']
                max_date = self.parent_table.rows[parent_row]['end_date']
                field_start = getattr(self, 'p_start_date')
                field_value = field_start.GetValue()
                field_start.SetValue(max(field_value, min_date))
                field_start.SetRange(min_date, max_date)
                field_end = getattr(self, 'p_end_date')
                field_value = field_end.GetValue()
                field_end.SetValue(min(field_value, max_date))
                field_end.SetRange(min_date, max_date)
        elif field_name == 'categories':
            self.lookup_lists['categories'][0] = self.lookup_lists['categories'][1][field.GetValue()]
            for value in range(0, len(self.lookup_lists['categories'])):
                if self.set_combo('subcategories', parent=self.lookup_lists['categories'][value]):
                    for value1 in range(0, len(self.lookup_lists['subcategories'])):
                        if self.set_combo('details', parent=self.lookup_lists['subcategories'][value1]):
                            break
        elif field_name == 'subcategories':
            self.lookup_lists['subcategories'][0] = self.lookup_lists['subcategories'][1][field.GetValue()]
            for value in range(0, len(self.lookup_lists['subcategories'])):
                if self.set_combo('details', parent=self.lookup_lists['subcategories'][value]):
                    break
        elif field_name == 'details':
            self.lookup_lists['details'][0] = self.lookup_lists['details'][1][field.GetValue()]
        elif field_name in LOOKUPS.keys():
            self.lookup_lists[field_name][0] = self.lookup_lists[field_name][1][field.GetValue()]
    
    def _on_edited(self, event):
        print('on_edited')
        if self.status[self.tab_name]:
            self.status[self.tab_name] |= TX_CHANGED
            if self.status[self.tab_name] | TX_RESET:
                self.status[self.tab_name] ^= TX_RESET
            _button_refresh(self.parent, enable=('reset', 'apply', 'cancel'))
        # event.Skip()
    
    def _on_enter(self, event):
        print('on_enter')
        self.parent.__apply()


class TaxonomyPanel(wxf.TaxonomyEdit, GenericPanelActions):
    
    def __init__(self, parent, tab_name, tables):
        # super().__init__(parent, name=tab_name)
        super().__init__(parent)
        self.Hide()
        self.parent = parent
        self.tab_name = tab_name
        self.base = self.GetTopLevelParent()
        self.status = self.base.status
        self.SetSizerAndFit(self.top_sizer)
        self.Layout()
        GenericPanelActions.__init__(self, parent=parent, child=self, tab_name=tab_name, tables=tables)
    
    def on_edited(self, event):
        self._on_edited(event)
        event.Skip()
    
    """
    def _on_lookup(self, event):
        GenericPanelActions._on_lookup(self, event)
    
    def new(self, **kwargs):
        super().new(**kwargs)
    
    def update(self, **kwargs):
        super().update(**kwargs)
    
    def apply(self, **kwargs):
        is_valid = super().apply(**kwargs)
        return is_valid
    """


class Suppliers(wxf.SupplierEdit, GenericPanelActions):
    
    def __init__(self, parent, tab_name, tables):
        # super().__init__(parent, name=tab_name)
        super().__init__(parent)
        self.Hide()
        self.parent = parent
        self.tab_name = tab_name
        self.base = self.GetTopLevelParent()
        self.status = self.base.status
        self.SetSizerAndFit(self.top_sizer)
        self.Layout()
        GenericPanelActions.__init__(self, parent=parent, child=self, tab_name=tab_name, tables=tables)
    
    def on_edited(self, event):
        self._on_edited(event)
        event.Skip()
    
    """
    def new(self, **kwargs):
        super().new(**kwargs)

    def update(self, **kwargs):
        super().update(**kwargs)

    def apply(self, **kwargs):
        is_valid = super().apply(**kwargs)
        return is_valid
    """


class Accounts(wxf.AccountEdit, GenericPanelActions):
    
    def __init__(self, parent, tab_name, tables):
        # super().__init__(parent, name=tab_name)
        super().__init__(parent)
        self.Hide()
        self.parent = parent
        self.tab_name = tab_name
        self.base = self.GetTopLevelParent()
        self.status = self.base.status
        self.SetSizerAndFit(self.top_sizer)
        self.Layout()
        GenericPanelActions.__init__(self, parent=parent, child=self, tab_name=tab_name, tables=tables)
    
    def on_edited(self, event):
        self._on_edited(event)
        event.Skip()
    
    """
    def new(self, **kwargs):
        super().new(**kwargs)

    def update(self, **kwargs):
        super().update(**kwargs)

    def apply(self, **kwargs):
        is_valid = super().apply(**kwargs)
        return is_valid
    """


class SubAccounts(wxf.SubAccountEdit, GenericPanelActions):
    
    def __init__(self, parent, tab_name, tables):
        # super().__init__(parent, name=tab_name)
        super().__init__(parent)
        self.Hide()
        self.parent = parent
        self.tab_name = tab_name
        self.base = self.GetTopLevelParent()
        self.status = self.base.status
        self.SetSizerAndFit(self.top_sizer)
        self.Layout()
        GenericPanelActions.__init__(self, parent=parent, child=self, tab_name=tab_name, tables=tables)
    
    def on_edited(self, event):
        self._on_edited(event)
        event.Skip()
    
    """
    def new(self, **kwargs):
        super().new(**kwargs)

    def update(self, **kwargs):
        super().update(**kwargs)

    def apply(self, **kwargs):
        is_valid = super().apply(**kwargs)
        return is_valid
    """


class Transactions(wxf.TransactionEdit, GenericPanelActions):
    
    def __init__(self, parent, tab_name, tables):
        # super().__init__(parent, name=tab_name)
        super().__init__(parent)
        self.Hide()
        self.parent = parent
        self.tab_name = tab_name
        self.base = self.GetTopLevelParent()
        self.status = self.base.status
        self.p_duplicate.Hide()
        self.p_duplicate.Disable()
        self.p_reconciled.Hide()
        self.p_reconciled.Disable()
        self.SetSizerAndFit(self.top_sizer)
        self.Layout()
        GenericPanelActions.__init__(self, parent=parent, child=self, tab_name=tab_name, tables=tables)
    
    def on_edited(self, event):
        self._on_edited(event)
        event.Skip()


class TransactionsNew(wxf.TransactionEdit, GenericPanelActions):
    
    def __init__(self, parent, tab_name, tables):
        # super().__init__(parent, name=tab_name)
        super().__init__(parent)
        self.Hide()
        self.parent = parent
        self.tab_name = tab_name
        self.base = self.GetTopLevelParent()
        self.status = self.base.status
        self.SetSizerAndFit(self.top_sizer)
        self.Layout()
        GenericPanelActions.__init__(self, parent=parent, child=self, tab_name=tab_name, tables=tables)
    
    def on_edited(self, event):
        self._on_edited(event)
        event.Skip()
    
    """
    def new(self, **kwargs):
        super().new(**kwargs)

    def update(self, **kwargs):
        super().update(**kwargs)

    def apply(self, **kwargs):
        is_valid = super().apply(**kwargs)
        return is_valid
    """


class Rules(wxf.RulesEdit, GenericPanelActions):
    
    def __init__(self, parent, tab_name, tables):
        # super().__init__(parent, name=tab_name)
        super().__init__(parent)
        self.Hide()
        self.parent = parent
        self.tab_name = tab_name
        self.base = self.GetTopLevelParent()
        self.status = self.base.status
        self.SetSizerAndFit(self.top_sizer)
        self.Layout()
        GenericPanelActions.__init__(self, parent=parent, child=self, tab_name=tab_name, tables=tables)
    
    def on_edited(self, event):
        self._on_edited(event)
        event.Skip()
    
    """
    def new(self, **kwargs):
        super().new(**kwargs)

    def update(self, **kwargs):
        super().update(**kwargs)

    def apply(self, **kwargs):
        is_valid = super().apply(**kwargs)
        return is_valid
    """


class Cards(wxf.CardEdit, GenericPanelActions):
    
    def __init__(self, parent, tab_name, tables):
        # super().__init__(parent, name=tab_name)
        super().__init__(parent)
        self.Hide()
        self.parent = parent
        self.tab_name = tab_name
        self.base = self.GetTopLevelParent()
        self.status = self.base.status
        self.SetSizerAndFit(self.top_sizer)
        self.Layout()
        GenericPanelActions.__init__(self, parent=parent, child=self, tab_name=tab_name, tables=tables)
    
    def on_edited(self, event):
        self._on_edited(event)
        event.Skip()
    
    """
    def new(self, **kwargs):
        super().new(**kwargs)

    def update(self, **kwargs):
        super().update(**kwargs)

    def apply(self, **kwargs):
        is_valid = super().apply(**kwargs)
        return is_valid
    """


class Contacts(wxf.ContactEdit, GenericPanelActions):
    
    def __init__(self, parent, tab_name, tables):
        # super().__init__(parent, name=tab_name)
        super().__init__(parent)
        self.Hide()
        self.parent = parent
        self.tab_name = tab_name
        self.base = self.GetTopLevelParent()
        self.status = self.base.status
        self.SetSizerAndFit(self.top_sizer)
        self.Layout()
        GenericPanelActions.__init__(self, parent=parent, child=self, tab_name=tab_name, tables=tables)
    
    def on_edited(self, event):
        self._on_edited(event)
        event.Skip()
    
    """
    def new(self, **kwargs):
        super().new(**kwargs)

    def update(self, **kwargs):
        super().update(**kwargs)

    def apply(self, **kwargs):
        is_valid = super().apply(**kwargs)
        return is_valid
    """


class Summary(wxf.Summary):
    
    def __init__(self, parent, tab_name, tables):
        super().__init__(parent, name=tab_name)
        self.base = self.GetTopLevelParent()
        self.tables = tables
        self.buttons = ['refresh']
        self.button_settings = [('all',), ('refresh'), ()]
        self.button_defaults = [('all',), ('refresh'), ()]
        self.__summary_init()
    
    def __summary_init(self):
        
        account_data = self.base.db_tables.get(self.tables[0], None)
        transaction_data = self.base.db_tables.get(self.tables[1], None)
        if account_data.rowcount != account_data.sel_rowcount or account_data.tab_changed:
            account_data.process_db('fetch')
        if transaction_data.rowcount != transaction_data.sel_rowcount or transaction_data.tab_changed:
            transaction_data.process_db('fetch')
        values = {'Income': sum(v['amount'] for v in transaction_data.rows.values() if v['amount'] > 0),
                  'Expenditure': sum(v['amount'] for v in transaction_data.rows.values() if v['amount'] < 0),
                  'Balance': sum(v['initial'] for v in account_data.rows.values()) + sum(
                          v['amount'] for v in transaction_data.rows.values())}
        a_types = set(v['type'] for v in account_data.rows.values())
        for a_type in a_types:
            values[a_type] = sum(v['amount'] for v in transaction_data.rows.values()
                                 if account_data.rows[v['parent']]['type'] == a_type)
        self.summary_cell_values = []
        for k, v in values.items():
            self.summary_cell_values.append((wx.StaticText(self, -1, f'{k}:'), wx.EXPAND))
            self.summary_cell_values.append((wx.TextCtrl(self, value=f'{v}',
                                                         style=wx.TE_READONLY | wx.TE_RIGHT), wx.EXPAND))
        
        self.summary_sizer.Clear()
        self.summary_sizer.AddMany(self.summary_cell_values)
        _button_refresh(self, default=1)
        main_refresh(self)
        
    def on_refresh_button(self, event):
        self.__summary_init()
