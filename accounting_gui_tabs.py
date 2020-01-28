import wx
import wx.adv
import wx.grid
import wx.lib.stattext

import data_structures as db
import wxf_dialog
# from datetime import datetime
import wxf_tab_forms as wxf
from statics import *

expand_option = dict(flag=wx.EXPAND)
no_options = dict()
empty_space = ((0, 0), expand_option)
LOOKUPS: dict = {
        'parent': None,
        'grandparent': None,
        'category': 'categories',
        'subcategory': 'subcategories',
        'detail': 'details'
}

ANCESTORS = db.ANCESTORS
DESCENDANTS = db.DESCENDANTS
CX_DISCONNECTED = 0
CX_CONNECTED = 1
TX_CLEAN = 0
TX_EDIT = 1
TX_ADD_PEER = 2
TX_ADD_CHILD = 4
TX_CHANGED = 8
TX_UNUSED1 = 16
TX_UNUSED2 = 32
TX_UNUSED3 = 64
TX_UNUSED4 = 128
TX_RESET = 256


class BaseWindow(wxf.MainFrame):
    
    def __init__(self, *args, **kwargs):
        
        super().__init__(*args, **kwargs)
        # self.Bind(wx.EVT_CHAR_HOOK, self.on_key_pressed_somewhere)
        self.database = None
        self.database_host = 'localhost'
        self.database_name = 'test'
        self.database_user = 'dermot'
        self.data = {}
        self.summary_cell_values = []
        self.this_table = None
        self.parent_table = None
        self.grandparent_table = None
        self.this_notebook_page = None
        self.this_page_name = None
        self.is_new = False
        self.is_edit = False
        self.is_tab_dirty = False
        
        self.taxo_root = None
        self.taxo_branch = None
        self.taxo_branch_level = None
        self.taxo_branch_data = None
        self.taxo_child_branch = None
        self.taxo_child_branch_level = None
        self.taxo_child_branch_data = None
        self.taxo_parent_branch = None
        self.taxo_parent_branch_level = None
        self.taxo_parent_branch_data = None
        self.taxo_status = TX_CLEAN
        self.conn_status = CX_DISCONNECTED
        self.connect()
        self.__notebook_init('taxonomy')
        self.__main_refresh()

    def connect(self):
        with SignInDialog(None, self) as dlg:
            result = dlg.ShowModal()
            if result == wx.ID_OK:
                self.__connect_load()
            elif result == wx.ID_CLOSE and self.conn_status & CX_CONNECTED:
                pass
            else:
                self.on_exit_button(None)
        if self.conn_status & CX_CONNECTED:
            self.set_message('CONNECTED', 2, '')
        else:
            self.set_message('DISCONNECTED', 2, '')

    def __notebook_init(self, tab):
        self.all_tabs = {
                'connect': self.tab_connect,
                'suppliers': self.tab_suppliers,
                'accounts': self.tab_accounts,
                'taxonomy': self.tab_taxonomy,
                'summary': self.tab_summary,
        }
        taxonomy = TreeManagement(self.tab_taxonomy, 'taxonomy', self, 'categories')
        # self.tab_taxonomy.AddChild(taxonomy)
        this_tab = self.p_notebook.FindPage(self.all_tabs[tab])
        self.p_notebook.SetSelection(this_tab)

    def on_changing_page(self, event):
        this_page = self.p_notebook.GetSelection()
        this_tab = self.p_notebook.GetPage(this_page)
        this_label = this_tab.Name
    
        if this_label == 'connect':
            if self.conn_status == CX_DISCONNECTED:
                event.Veto()
                self.set_message('Not connected to database')
                self.__main_refresh()
        elif this_label == 'taxonomy':
            if self.taxo_status & TX_CHANGED:
                event.Veto()
                self.set_message('Unsaved changes on this tab')
                self.__main_refresh()

    def on_new_page(self, event):
        this_page = self.p_notebook.GetSelection()
        self.this_notebook_page = self.p_notebook.GetPage(this_page)
        self.this_page_name = self.this_notebook_page.Name
    
        print(self.this_page_name)
        if self.this_page_name == 'suppliers':
            suppliers = TreeManagement(self.tab_suppliers, 'suppliers', self, 'suppliers')
        elif self.this_page_name == 'accounts':
            accounts = TreeManagement(self.tab_accounts, 'accounts', self, 'suppliers')
        elif self.this_page_name == 'taxonomy':
            taxonomy = TreeManagement(self.tab_taxonomy, 'taxonomy', self, 'categories')
            self._button_refresh()
            self.tab_taxonomy.Layout()
        elif self.this_page_name == 'summary':
            self.__summary_init()
    
        self.__main_refresh()

    def __connect_load(self):
        # db.get_structure(self.database)
        self.Freeze()
        self.all_panels = {
                'categories': Categories(self),
                'subcategories': SubCategories(self),
                'details': Details(self),
                'suppliers': Suppliers(self),
                'accounts': Accounts(self),
                'subaccounts': SubAccounts(self),
                'transactions': Transactions(self),
                'rules': Rules(self),
                'cards': Cards(self),
                'contacts': Contacts(self)
        }
        self.Thaw()

    def on_user_logon(self, event):
        pass
    
    def __activate_table(self, activate_this):
        assert activate_this in self.data.keys(), f'{activate_this} is not a valid table name'
        self.this_table = self.data.get(activate_this, None)
        self.parent_table = self.data.get(ANCESTORS[activate_this][0], None)
        self.grandparent_table = self.data.get(ANCESTORS[activate_this][1], None)
        #        self.__rows_refresh()
        #        self.__main_refresh()
    
    def __summary_init(self):
        
        account_data = self.data.get('accounts', None)
        transaction_data = self.data.get('transactions', None)
        if account_data.rowcount != account_data.sel_rowcount:
            account_data.process('fetch')
        if transaction_data.rowcount != transaction_data.sel_rowcount:
            transaction_data.process('fetch')
        values = {}
        values['Income'] = sum(v['amount'] for v in transaction_data.records.values() if v['amount'] > 0)
        values['Expenditure'] = sum(v['amount'] for v in transaction_data.records.values() if v['amount'] < 0)
        values['Balance'] = sum(v['amount'] for v in transaction_data.records.values())
        a_types = set(v['type'] for v in account_data.records.values())
        for a_type in a_types:
            values[a_type] = sum(v['amount'] for v in transaction_data.records.values()
                                 if account_data.records[v['parent']]['account_type'] == a_type)
        self.summary_cell_values = []
        for k, v in values.items():
            self.summary_cell_values.append((wx.StaticText(self.tab_summary, -1, f'{k}:'), wx.EXPAND))
            self.summary_cell_values.append((wx.TextCtrl(self.tab_summary, value=f'{v}',
                                                         style=wx.TE_READONLY | wx.TE_RIGHT), wx.EXPAND))
        
        self.tab_summary.summary_sizer.Clear()
        self.tab_summary.summary_sizer.AddMany(self.summary_cell_values)
        self.tab_summary.summary_sizer.Layout()
    
    def __taxonomy_init(self):
        if not self.taxo_root:
            self.taxo_root = self.tree_taxonomy.AddRoot('Taxonomy')
            self.__taxo_reload_branches(branch=self.taxo_root, level='categories')
            first_item = self.tree_taxonomy.GetFirstChild(self.taxo_root)
            if first_item[0].IsOk():
                self.tree_taxonomy.SelectItem(first_item[0])
                self.tree_taxonomy.SetFocusedItem(first_item[0])
                self.taxo_status = TX_CLEAN
                self.taxo_panel.Hide()
            else:
                self.on_taxo_menu_item(None)
        self.__taxo_tree_accel()
        self._button_refresh()
    
    def __taxo_tree_accel(self):
        up_id = wx.NewId()
        down_id = wx.NewId()
        self.Bind(wx.EVT_MENU, self.on_taxo_key_up, id=up_id)
        self.Bind(wx.EVT_MENU, self.on_taxo_key_down, id=down_id)
        
        self.tree_taxonomy.accel_tbl = wx.AcceleratorTable([(wx.ACCEL_ALT, wx.WXK_UP, up_id),
                                                            (wx.ACCEL_ALT, wx.WXK_DOWN, down_id)
                                                            ])
        self.tree_taxonomy.SetAcceleratorTable(self.tree_taxonomy.accel_tbl)

    def __taxo_reload_branches(self, branch=None, level=None):
        assert branch.IsOk(), f'invalid parent branch passed to reload'
        assert level in ('categories', 'subcategories', 'details'), f'invalid level passed to reload'
        tree = self.tree_taxonomy
        if not branch:
            branch = self.taxo_root
        tree.DeleteChildren(branch)
    
        if level == 'categories':
            next_level = 'subcategories'
            key = 0
        elif level == 'subcategories':
            next_level = 'details'
            itemdata = tree.GetItemData(branch)
            key = itemdata['data']['key']
        else:
            next_level = ''
            itemdata = tree.GetItemData(branch)
            key = itemdata['data']['key']
        
        self.__taxo_refresh_data(level, key)
        db_data = self.data.get(level, None)
        for key, record in db_data.rows.items():
            container = self.tree_taxonomy.AppendItem(branch, record['name'],
                                                      data={'level': level, 'data': record})
            if next_level:
                self.__taxo_reload_branches(container, next_level)
    
    def __taxo_refresh_data(self, level, parent=0):
        db_data = self.data.get(level, None)
        if not parent:
            if db_data.rowcount != db_data.sel_rowcount:
                db_data.process('fetch')
        else:
            db_data.process('fetch', parent=parent)
    
    def on_taxo_key_up(self, event):
        if not self.taxo_status:
            tree = self.tree_taxonomy
            new_pos = tree.GetPrevSibling(self.taxo_branch)
            if new_pos.IsOk():
                self.__taxonomy_swap(self.taxo_branch, new_pos)
            else:
                self.set_message('already at top')
        print(f'Alt-up key press')
        event.Skip()
    
    def on_taxo_key_down(self, event):
        if not self.taxo_status:
            tree = self.tree_taxonomy
            new_pos = tree.GetNextSibling(self.taxo_branch)
            if new_pos.IsOk():
                self.__taxonomy_swap(self.taxo_branch, new_pos)
            else:
                self.set_message('already at bottom')
        print(f'Alt-down key press')
        event.Skip()
    
    def on_edit_taxonomy(self, event):
        print('on_edit_taxonomy')
        action = ['Edit', self.taxo_branch_level]
        self.__taxonomy_get_changes('edit', self.taxo_branch_level.lower())
    
    def on_taxo_edited(self, event):
        print('on_taxo_edited')
        if self.taxo_status:
            self.taxo_status |= TX_CHANGED
            self.taxo_status ^= TX_RESET
            self._button_refresh(show=('reset', 'apply', 'cancel'), enable=('reset', 'apply', 'cancel'))
    
    def on_taxo_enter(self, event):
        print('on_taxo_enter')
        self.on_apply_button(event)
    
    def on_taxo_change_branch(self, event):
        print('on_taxo_change_branch')
        if self.taxo_status & TX_CHANGED:
            event.Veto()
            self.set_message('Unsaved Changes')
            self.__main_refresh()
    
    def on_taxo_changed_branch(self, event):
        print('on_taxo_changed_branch')
        tree = event.GetEventObject()
        self.taxo_branch = tree.GetSelection()
        branch_info = tree.GetItemData(self.taxo_branch)
        self.taxo_branch_level = branch_info['level']
        self.taxo_branch_data = branch_info['data']
        self.taxo_parent_branch = tree.GetItemParent(self.taxo_branch)
        if self.taxo_parent_branch != self.taxo_root:
            parent_branch_info = tree.GetItemData(self.taxo_parent_branch)
            self.taxo_parent_branch_level = parent_branch_info['level']
            self.taxo_parent_branch_data = parent_branch_info['data']
        else:
            self.taxo_parent_branch_level = None
            self.taxo_parent_branch_data = None
        self.taxo_child_branch = None
        self.taxo_child_branch_level = None
        self.taxo_child_branch_data = None
        self.taxo_status = TX_CLEAN
    
    def on_taxo_rdown(self, event):
        print('on_taxo_rdown')
        if self.taxo_status & TX_CHANGED:
            self.set_message('Unsaved Changes')
            self.__main_refresh()
        else:
            tree = self.tree_taxonomy
            pt = event.GetPosition()
            item, flags = tree.HitTest(pt)
            if item.IsOk() and not tree.IsSelected(item):
                tree.SelectItem(item)
                tree.SetFocusedItem(item)
            branch = tree.GetSelection()
            branch_info = tree.GetItemData(branch)
            children = tree.GetChildrenCount(branch)
            level = branch_info['level']
            self.m_add_child.SetItemLabel(' ')
            self.m_add_child.Enable(False)
            if level == 'categories':
                self.m_add_peer.SetItemLabel('Add Category')
                if not children:
                    self.m_add_child.SetItemLabel('Add SubCategory')
                    self.m_add_child.Enable()
            elif level == 'subcategories':
                self.m_add_peer.SetItemLabel('Add SubCategory')
                if not children:
                    self.m_add_child.SetItemLabel('Add Detail')
                    self.m_add_child.Enable()
            elif level == 'details':
                self.m_add_peer.SetItemLabel('Add Detail')
            else:
                pass
            event.Skip()
    
    def on_taxo_menu(self, event):
        print('on_taxo_menu')
        event.Skip()
    
    def on_taxo_menu_called(self, event):
        print('on_taxo_menu_called')
        event.Skip()
    
    def on_taxo_menu_item(self, event):
        print('on_taxo_menu_item')
        if event:
            id_selected = event.GetId()
            menu = event.GetEventObject()
            action = menu.GetLabelText(id_selected).lower().split()
            action[1] = LOOKUPS.get(action[1], '')
        else:
            action = ['add', 'category']
        self.__taxonomy_get_changes(action[0], action[1])
    
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
            table = self.data.get(lookup, None)
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
        self.set_message('', message='')
        self.__single_reset()
    
    def __single_reset(self):
        
        self.single_panel.Show(True)
        self.single_panel.Layout()
        self.single.Layout()
        self.main_single.Layout()
        self.main_sizer.Show(self.single, True, True)
        self.__main_refresh()

    def _button_refresh(self, show=(), enable=(), focus=()):
        self.b_exit.Show()
        self.b_exit.Enable()
        buttons = {
                'new': self.b_new,
                'edit': self.b_edit,
                'reset': self.b_reset,
                'test': self.b_test,
                'connect': self.b_connect,
                'apply': self.b_apply,
                'cancel': self.b_cancel
        }
        for k, v in buttons.items():
            if k in show:
                v.Show()
                if k in enable:
                    v.Enable()
                    if k in focus:
                        v.SetFocus()
            else:
                v.Disable()
                v.Hide()
    
    def __main_refresh(self):
        #        self.p_header.SetLabel(f'Table: {self.this_table_name.capitalize()}')
        self.main_sizer.Layout()
        self.Layout()
        self.SetSizerAndFit(self.main_sizer)
        self.Centre()
        self.Show()
        self.Raise()
    
    def on_key_pressed_somewhere(self, e):
        print(f'a key pressed {e}')
        e.Skip()
    
    def on_table_selected(self, event):
        id_selected = event.GetId()
        obj = event.GetEventObject()
        self.__activate_table(obj.GetLabelText(id_selected).lower())
    
    def on_forecast_tool(self, event):
        self.set_message('No action define for this button')
    
    def on_row_selected(self, e):
        if e.Selecting():
            self.b_edit.Enable()
            self.rows_sizer.cursor = (e.GetTopRow(), e.GetLeftCol())
        e.Skip()
    
    #    def on_date(self, e):
    #        if self.calendar.visible:
    #            self.calendar.Hide()
    #        else:
    #            self.calendar.Show()
    
    def on_new_button(self, event):
        self.is_new = True
        self.main_menu.EnableTop(1, False)
        if event:
            self.__single_load()
        else:
            self.__single_reset_panel()
    
    def on_edit_button(self, event):
        self.main_menu.EnableTop(1, False)
        self.is_edit = True
        if event:
            self.__single_load()
        else:
            self.__single_reset_panel()
    
    def on_reset_button(self, event):
        if self.this_page_name == 'taxonomy':
            if self.taxo_status & (TX_CHANGED):
                action = self.taxo_heading.GetLabel().lower().split()
                self.__taxonomy_get_changes(action[0], action[1])
        elif self.is_new:
            self.on_new_button(None)
        elif self.is_edit:
            self.on_edit_button(None)
        self.set_message('', message='')
        self.__main_refresh()
    
    def on_apply_button(self, event):
        if self.this_page_name == 'taxonomy':
            self.__taxonomy_apply()
        else:
            if self.single_panel.apply():
                if self.is_new:
                    self.on_reset_button(None)
                elif self.is_edit:
                    self.on_cancel_button(None)

    def on_cancel_button(self, event):
        if self.this_page_name == 'taxonomy':
            self.__taxonomy_init()
        else:
            self.is_new = False
            self.is_edit = False
            self.is_tab_dirty = False
        self.set_message('', message='')
        #        self.main_menu.EnableTop(1, True)
        #        self.__summary_refresh()
        #        self.__rows_refresh()
        #        self.main_sizer.Show(self.single, False, True)
        #        self.main_sizer.Show(self.rows, True, True)
        self.__main_refresh()
    
    def on_exit_button(self, event):
        if self.this_page_name == 'taxonomy' and self.taxo_status & TX_CHANGED and not self.taxo_status & TX_RESET:
            self.set_message('Unsaved changes', message='Press again to confirm you want to leave without saving '
                                                        'changes.')
            self.taxo_status |= TX_RESET
            self.__main_refresh()
        else:
            self.taxo_status = TX_CLEAN
            self.is_tab_dirty = False
            self.tree_taxonomy.Unbind(wx.EVT_TREE_SEL_CHANGED)
            self.tree_taxonomy.Unbind(wx.EVT_TREE_SEL_CHANGING)
            try:
                self.database.close()
            except:
                pass
            self.Close()

    def set_message(self, status='', field=1, message=None):
        self.SetStatusText(status, field)
        if isinstance(message, str):
            self.p_message.SetValue(message)
            if message:
                self.p_message.Show()
            else:
                self.p_message.Hide()

    def on_status_dclick(self, event):
        place = self.status_bar.GetFieldRect(2)
        if event.GetX() >= place.GetLeft() and event.GetX() <= place.GetRight():
            self.connect()


#        self.single_panel.bSizer_top.Layout()
#        self.single_panel.SetSizerAndFit(self.single_panel.bSizer_top)
#        self.__single_reset()

class SelectBranch(wx.Dialog):
    def __init__(self, parent, selections, label=''):
        super().__init__(parent)
        boxer = wx.BoxSizer()
        self.radio_box = wx.RadioBox(self, wx.ID_ANY, choices=selections)
        self.radio_box.SetSelection(0)
        if label:
            self.radio_box.SetLabel(label)
        for i in range(0, len(selections)):
            self.radio_box.SetItemLabel(i, selections[i].capitalize())
        boxer.Add(self.radio_box, 0, wx.ALL, 5)
        
        self.SetSizer(boxer)
        self.Layout()
        boxer.Fit(self)
        
        self.Centre(wx.BOTH)
        
        # Connect Events
        self.radio_box.Bind(wx.EVT_RADIOBOX, self.on_selection)
    
    def __del__(self):
        pass
    
    def on_selection(self, event):
        self.EndModal(self.radio_box.GetSelection() - 1)


class SignInDialog(wxf_dialog.db_sign_in):
    def __init__(self, parent, top_win):
        super().__init__(parent)
        self.top_win = top_win
        if top_win.conn_status & CX_CONNECTED:
            self.b_disconnect.Enable()
            self.b_connect.Disable()
            self.b_test.Disable()
        else:
            self.b_connect.Enable()
            self.b_disconnect.Disable()
            self.b_test.Enable()
        self.user_name.SetValue(top_win.database_user)
        self.use_db.SetValue(top_win.database_name)
        self.host_name.SetValue(top_win.database_host)
        self.password.SetValue('')
        self.database = top_win.database
        self.Raise()
    
    def on_test_button(self, event):
        is_valid, message, database = db.select_db(host=self.host_name.GetValue(),
                                                   use_db=self.use_db.GetValue(),
                                                   user=self.user_name.GetValue(),
                                                   password=self.password.GetValue())
        if is_valid:
            database.close()
            self.message.SetValue('connection works')
        else:
            self.message.SetValue(f'error connecting\n{message}')
    
    def on_connect_button(self, event):
        is_valid, message, self.database = db.select_db(host=self.host_name.GetValue(),
                                                        use_db=self.use_db.GetValue(),
                                                        user=self.user_name.GetValue(),
                                                        password=self.password.GetValue())
        if is_valid:
            self.top_win.database = self.database
            self.top_win.database_host = self.host_name.GetValue()
            self.top_win.database_name = self.use_db.GetValue()
            self.top_win.database_user = self.user_name.GetValue()
            db.get_structure(self.database)
            incr = 99 // (len(db._T_STRUCTURE) + 1)
            self.progress.SetRange(100)
            self.progress.SetValue(0)
            for table in db._T_STRUCTURE.keys():
                self.top_win.data[table] = db.DataTables(self.database, table)
                self.progress.SetValue(self.progress.GetValue() + incr)
            self.top_win.conn_status = CX_CONNECTED
            self.EndModal(wx.ID_OK)
        else:
            self.message.SetValue(f'error connecting\n{message}')
    
    def on_disconnect_button(self, event):
        try:
            self.database.close()
        finally:
            self.top_win.data = {}
            self.top_win.conn_status = CX_DISCONNECTED
            self.message.SetValue(f'not connected')
            self.b_connect.Enable()
            self.b_disconnect.Disable()
            self.b_test.Enable()
    
    def on_cancel_button(self, event):
        self.EndModal(wx.ID_CLOSE)
    
    def on_exit_button(self, event):
        self.EndModal(wx.ID_CANCEL)


class TreeManagement(wxf.TreeManager):
    def __init__(self, parent, tab_name, base, base_table):
        super().__init__(parent)
        self.tab_name = tab_name
        self.base = base
        self.base_table = base_table
        self._root = None
        self._status = TX_CLEAN
        self._tree_init()
    
    def _tree_init(self):
        tree = self.tree_trunk
        if not self._root:
            self._root = tree.AddRoot(self.tab_name)
            self._load_branches(branch=self._root, level=self.base_table)
            first_item = tree.GetFirstChild(self._root)
            if first_item[0].IsOk():
                tree.SelectItem(first_item[0])
                tree.SetFocusedItem(first_item[0])
                self._status = TX_CLEAN
                self.tree_panel.Hide()
            else:
                self.on_menu_item(None)
        self.__tree_accel()
        self.Layout()
    
    def __redraw(self):
        tree = self.tree_trunk
        self.__refresh_data(self.branch_level)
        if self.status & TX_ADD_CHILD:
            self.__refresh_data(self.child_branch_level, self.branch_data['key'])
        if self.status & TX_EDIT:
            key = self.branch_data['key']
            new_data = self.this_table.rows[key]
            tree.SetItemText(self.branch, new_data['name'])
            for k, v in new_data.items():
                self.branch_data[k] = v
            self.status = TX_CLEAN
            self._button_refresh()
            self.name.SetLabelText('')
            self.panel.Hide()
        elif self.status & TX_ADD_PEER:
            key = self.this_table.get_next() - 1
            new_data = self.this_table.rows[key]
            self.branch = tree.InsertItem(self.parent_branch, self.branch,
                                          new_data['name'],
                                          data={'level': self.branch_level, 'data': new_data})
            self.status = TX_ADD_PEER
            self._button_refresh(show=('reset', 'apply', 'cancel'), enable=('reset', 'cancel'))
            tree.SelectItem(self.branch)
            self.name.SetLabelText('')
            self.name.SetFocus()
        elif self.status & TX_ADD_CHILD:
            key = self.this_table.get_next() - 1
            self.child_branch_data = self.this_table.rows[key]
            self.child_branch = tree.InsertItem(self.branch, 0,
                                                self.child_branch_data['name'],
                                                data={
                                                        'level': self.child_branch_level,
                                                        'data': self.child_branch_data
                                                })
            self.status = TX_ADD_PEER
            self._button_refresh(show=('reset', 'apply', 'cancel'), enable=('reset', 'cancel'))
            tree.SelectItem(self.child_branch)
            self.name.SetLabelText('')
            self.name.SetFocus()
        self.__tree_accel()
        self.tab_taxonomy.Layout()
    
    def __get_changes(self, action, table):
        assert action in ('add', 'edit'), f'Unrecognised taxonomy action {action} {table} '
        
        level = self.branch_level
        branch_data = self.branch_data
        parent_data = self.parent_branch_data
        self.__activate_table(self.branch_level)
        min_date = START_DATE.date()
        max_date = END_DATE.date()
        self.status = TX_CLEAN
        self.heading.SetLabel(f'{action} {table}'.title())
        if action == 'add':
            self.name.SetValue('')
            if level == table:
                self.status = TX_ADD_PEER
                if parent_data:
                    min_date = parent_data['start_date']
                    max_date = parent_data['end_date']
            else:
                self.status = TX_ADD_CHILD
                min_date = branch_data['start_date']
                max_date = branch_data['end_date']
                self.__activate_table(table)
                self.child_branch_level = table
            self.start_date.SetValue(min_date)
            self.end_date.SetValue(max_date)
        elif action == 'edit':
            self.name.SetValue(branch_data['name'])
            self.start_date.SetValue(max(min_date, min(max_date, branch_data['start_date'])))
            self.end_date.SetValue(min(max_date, max(min_date, branch_data['end_date'])))
            self.status = TX_EDIT
        
        self.start_date.SetRange(min_date, max_date)
        self.end_date.SetRange(min_date, max_date)
        self._button_refresh(show=('reset', 'apply', 'cancel'), enable=('reset', 'cancel'))
        self.panel.Show()
        self.name.SetFocus()
        self.tab_taxonomy.Layout()
        self.__main_refresh()
    
    def __apply(self):
        is_valid = True
        
        this_panel = {v[0]: f'{v[0]}' for v in self.this_table.columns
                      if hasattr(self, f'{v[0]}')}
        if self.status & TX_EDIT:
            row = self.branch_data
        else:
            row = {}
        new_data = {}
        tree = self.tree_trunk
        for v in self.this_table.columns:
            p_field = None
            new_value = None
            if v[0] in this_panel.keys():
                p_field = getattr(self, this_panel[v[0]])
                if v[0] == 'name':
                    new_value = p_field.GetValue().title()
                    if new_value == '':
                        is_valid = False
                        self.set_message('error detected',
                                         message=f'description cannot be blank')
                else:
                    new_value = p_field.GetValue()
            elif v[0] == 'key':
                if self.status & TX_EDIT:
                    new_value = self.branch_data['key']
                else:
                    continue
            elif v[0] == 'sort':
                if self.status & TX_ADD_CHILD:
                    new_value = self.branch_data['sort'] * 1000 + 1
                elif self.status & TX_ADD_PEER:
                    new_value = self.branch_data['sort'] + 1
                else:
                    continue
            elif v[0] == 'parent':
                if self.status & TX_ADD_CHILD:
                    new_value = self.branch_data['key']
                elif self.status & TX_ADD_PEER:
                    new_value = self.parent_branch_data['key']
                else:
                    continue
            elif v[0] == 'grandparent':
                if self.status & TX_ADD_CHILD:
                    new_value = self.parent_branch_data['key']
                elif self.status & TX_ADD_PEER:
                    grandparent_branch = tree.GetItemParent(self.parent_branch)
                    grandparent_branch_data = tree.GetData(grandparent_branch)
                    new_value = grandparent_branch_data['key']
                else:
                    continue
            
            if self.status & (TX_ADD_CHILD | TX_ADD_PEER) or new_value != row.get(v[0], None):
                if isinstance(p_field, wx._adv.DatePickerCtrl):
                    new_data[v[0]] = new_value.FormatISODate()
                else:
                    new_data[v[0]] = new_value
        if is_valid:
            if self.status & TX_EDIT:
                action = 'update'
            else:
                action = 'insert'
            if is_valid := self.this_table.process(action, **new_data):
                self.__redraw()
                self.set_message(f'Successful {action}', message='')
                self.this_table.process('fetch')
                self.status = TX_CLEAN
        if not is_valid:
            self.set_message('Error detected', message=self.this_table.get_message())
        self.__main_refresh()
        return is_valid
    
    def __swap(self, branch1, branch2):
        b1_info = self.tree_trunk.GetItemData(branch1)
        b1_data = b1_info['data']
        b2_info = self.tree_trunk.GetItemData(branch2)
        b2_data = b2_info['data']
        parent = b1_data.get('parent', 0)
        level = b1_info['level']
        new_data1 = {'key': b1_data['key'], 'sort': b2_data['sort']}
        new_data2 = {'key': b2_data['key'], 'sort': b1_data['sort']}
        self.__activate_table(self.branch_level)
        if self.this_table.process('swap', parent, new_data1, new_data2):
            parent_branch = self.tree_trunk.GetItemParent(branch1)
            self.__reload_branches(branch=parent_branch, level=level)
        else:
            self.set_message(f'error swapping branches')
    
    def _load_branches(self, branch=None, level=None):
        assert branch.IsOk(), f'invalid parent branch passed to reload'
        assert level in self.base.data.keys(), f'invalid table name {level} passed to reload'
        tree = self.tree_trunk
        tree.DeleteChildren(branch)
        levels = DESCENDANTS.get(level, ())
        if len(levels):
            if len(levels) == 1:
                next_level = levels[0]
            else:
                with SelectBranch(self, list(levels), 'Select Branch:') as dlg:
                    next_level = dlg.ShowModal()
        else:
            next_level = ''
        if branch == self._root:
            key = 0
        else:
            itemdata = tree.GetItemData(branch)
            key = itemdata['data']['key']
        
        self.__refresh_data(level, key)
        db_data = self.base.data.get(level, None)
        for key, record in db_data.rows.items():
            container = self.tree_trunk.AppendItem(branch, record['name'],
                                                   data={'level': level, 'data': record})
            if next_level:
                self._load_branches(container, next_level)
    
    def __refresh_data(self, level, parent=0):
        db_data = self.base.data.get(level, None)
        if not parent:
            if db_data.rowcount != db_data.sel_rowcount:
                db_data.process('fetch')
        else:
            db_data.process('fetch', parent=parent)
    
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
        if not self._status:
            tree = self.tree_trunk
            new_pos = tree.GetPrevSibling(self._branch)
            if new_pos.IsOk():
                self.__swap(self._branch, new_pos)
            else:
                self.base.set_message('already at top')
        print(f'Alt-up key press')
        event.Skip()
    
    def on_key_down(self, event):
        if not self._status:
            tree = self.tree_trunk
            new_pos = tree.GetNextSibling(self.branch)
            if new_pos.IsOk():
                self.__swap(self._branch, new_pos)
            else:
                self.base.set_message('already at bottom')
        print(f'Alt-down key press')
        event.Skip()
    
    def on_edit(self, event):
        print('on_edit_taxonomy')
        branch = self.tree_trunk.GetSelection()
        branch_info = self.tree_trunk.GetItemData(branch)
        branch_level = branch_info.get('level', '')
        # action = ['Edit', branch_level]
        self.__get_changes('edit', branch_level.lower())
    
    def on_edited(self, event):
        print('on_edited')
        if self.status:
            self.status |= TX_CHANGED
            self.status ^= TX_RESET
            self.base._button_refresh(show=('reset', 'apply', 'cancel'), enable=('reset', 'apply', 'cancel'))
    
    def on_enter(self, event):
        print('on_taxo_enter')
        self.base.on_apply_button(event)
    
    def on_change_branch(self, event):
        print('on_taxo_change_branch')
        if self._status & TX_CHANGED:
            event.Veto()
            self.base.set_message('Unsaved Changes')
            self.base.__main_refresh()
    
    def on_changed_branch(self, event):
        print('on_changed_branch')
        tree = event.GetEventObject()
        self.branch = tree.GetSelection()
        branch_info = tree.GetItemData(self.branch)
        self.branch_level = branch_info['level']
        self.branch_data = branch_info['data']
        self.parent_branch = tree.GetItemParent(self.branch)
        if self.parent_branch != self._root:
            parent_branch_info = tree.GetItemData(self.parent_branch)
            self.parent_branch_level = parent_branch_info['level']
            self.parent_branch_data = parent_branch_info['data']
        else:
            self.parent_branch_level = None
            self.parent_branch_data = None
        self.child_branch = None
        self.child_branch_level = None
        self.child_branch_data = None
        self.status = TX_CLEAN
    
    def on_rdown(self, event):
        print('on_rdown')
        if self._status & TX_CHANGED:
            self.base.set_message('Unsaved Changes')
            self.base.__main_refresh()
        else:
            tree = self.tree_trunk
            pt = event.GetPosition()
            item, flags = tree.HitTest(pt)
            if item.IsOk() and not tree.IsSelected(item):
                tree.SelectItem(item)
                tree.SetFocusedItem(item)
            branch = tree.GetSelection()
            branch_info = tree.GetItemData(branch)
            children = tree.GetChildrenCount(branch)
            level = branch_info['level']
            self.m_add_child.SetItemLabel(' ')
            self.m_add_child.Enable(False)
            if level == 'categories':
                self.m_add_peer.SetItemLabel('Add Category')
                if not children:
                    self.m_add_child.SetItemLabel('Add SubCategory')
                    self.m_add_child.Enable()
            elif level == 'subcategories':
                self.m_add_peer.SetItemLabel('Add SubCategory')
                if not children:
                    self.m_add_child.SetItemLabel('Add Detail')
                    self.m_add_child.Enable()
            elif level == 'details':
                self.m_add_peer.SetItemLabel('Add Detail')
            else:
                pass
            event.Skip()
    
    def on_menu(self, event):
        print('on_menu')
        event.Skip()
    
    def on_menu_called(self, event):
        print('on_menu_called')
        event.Skip()
    
    def on_menu_item(self, event):
        print('on_menu_item')
        if event:
            id_selected = event.GetId()
            menu = event.GetEventObject()
            action = menu.GetLabelText(id_selected).lower().split()
            action[1] = LOOKUPS.get(action[1], '')
        else:
            action = ['add', 'category']
        self.__get_changes(action[0], action[1])


class GenericPanelActions:
    def __init__(self, **kwargs):
        self.base = kwargs.get('base')
        self.child = kwargs.get('child')
        self.child.Hide()
        self.child.Freeze()
        self.table_name = self.child.Label
        self.this_table = self.base.data[self.table_name]
        self.parent_table = self.base.data.get(ANCESTORS[self.table_name][0], None)
        self.grandparent_table = self.base.data.get(ANCESTORS[self.table_name][1], None)
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
        self.child.Hide()
        self.child.Thaw()

    def new(self, **kwargs):
        self.this_row = None
        self.this_record = 0
        self.parent_row = None
        self.parent_record = 0
        min_date = START_DATE
        max_date = END_DATE
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
                self.set_combo(k)
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
    
    def update(self, **kwargs):
        min_date = START_DATE
        max_date = END_DATE
        self.this_row = self.base.rows_sizer.GetGridCursorRow()
        self.this_record = int(self.base.rows_sizer.GetRowLabelValue(self.this_row))
        row = dict(self.this_table.rows[self.this_record])
        if 'grandparent' in self.this_panel.keys():
            self.set_combo('grandparent', table=self.grandparent_table, key=row['grandparent'])
            self.set_combo('parent', table=self.parent_table, parent=row['grandparent'], key=row['parent'])
            min_date = dict(self.this_table.rows[self.lookup_lists['grandparent'][0]])['start_date']
            max_date = dict(self.this_table.rows[self.lookup_lists['grandparent'][0]])['end_date']
        elif 'parent' in self.this_panel.keys():
            self.set_combo('parent', table=self.parent_table, key=row['parent'])
            min_date = dict(self.this_table.rows[self.lookup_lists['parent'][0]])['start_date']
            max_date = dict(self.this_table.rows[self.lookup_lists['parent'][0]])['end_date']
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
                self.set_combo(k, key=row[k])
            elif isinstance(field, wx._adv.DatePickerCtrl):
                field.SetRange(min_date, max_date)
                field.SetValue(row[k])
            else:
                field.SetValue(row[k])
    
    def apply(self, **kwargs):
        assert self.base.is_new or self.base.is_edit, f'no valid action in progress'
        is_valid = True
        these_dates = {}
        row = dict(self.this_table.rows.get(self.this_record, {}))
        if parent := self.this_panel.get('parent', ''):
            self.parent_record = self.lookup_lists['parent'][1].get(getattr(self, parent).GetValue(), 0)
            self.parent_row = self.parent_table.rows.get(self.parent_record, {})
        else:
            self.parent_record = 0
        
        new_data = {}
        new_value = None
        for k, v in self.this_panel.items():
            p_field = getattr(self, v)
            if k in LOOKUPS.keys():
                if not (new_value := self.lookup_lists[k][0]):
                    is_valid = False
                    self.base.set_message('error detected',
                                          message=f'lookup {p_field.Name} cannot be blank')
            else:
                new_value = p_field.GetValue()
            if self.base.is_new or new_value != row[k]:
                if isinstance(p_field, wx._adv.DatePickerCtrl):
                    new_data[k] = new_value.FormatISODate()
                    these_dates[k] = datetime.strptime(new_data[k], '%Y-%m-%d').date()
                else:
                    new_data[k] = new_value
        if self.parent_record:
            if these_dates.get('start_date') and these_dates['start_date'] < self.parent_row.get('start_date', 0):
                is_valid = False
                self.base.set_message('error detected',
                                      message=f'start_date {these_dates["start_date"]} is before '
                                              f'parent start_date {self.parent_row["start_date"]}')
            if these_dates.get('end_date') and these_dates['end_date'] > self.parent_row.get('end_date', 0):
                is_valid = False
                self.base.set_message('error detected',
                                      message=f'end_date {these_dates["end_date"]} is after '
                                              f'parent end_date {self.parent_row["end_date"]}')
        if is_valid:
            if self.base.is_new:
                new_data['sort'] = self.this_table.rowcount + 1
                action = 'insert'
            else:
                new_data['key'] = self.this_record
                action = 'update'
            if is_valid := self.this_table.process(action, **new_data):
                self.base.set_message(f'Successful {action}', message='')
                self.this_table.process('fetch')
            else:
                self.base.set_message('Error detected', message=self.this_table.get_message())
        
        return is_valid
    
    def set_combo(self, field_name, table=None, child_table=None, parent=0, key=0):
        if not table:
            table = self.base.data[field_name]
        if table.rowcount != len(table.rows):
            table.process('fetch')
        if child_table and child_table.rowcount != len(child_table.rows):
            child_table.process('fetch')
        combo_list = {}
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
            field.Select(field.GetStrings().index(table.get_descriptions(key=key)))
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


class Categories(wxf.CategoryEdit, GenericPanelActions):
    def __init__(self, base, **kwargs):
        super().__init__(base)
        GenericPanelActions.__init__(self, base=base, child=self)
    
    def _on_lookup(self, event):
        GenericPanelActions._on_lookup(self, event)
    
    """
    def new(self, **kwargs):
        super().new(**kwargs)
    
    def update(self, **kwargs):
        super().update(**kwargs)
    
    def apply(self, **kwargs):
        is_valid = super().apply(**kwargs)
        return is_valid
    """


class SubCategories(wxf.SubCatEdit, GenericPanelActions):
    def __init__(self, base, **kwargs):
        super().__init__(base)
        GenericPanelActions.__init__(self, base=base, child=self)
    
    def _on_lookup(self, event):
        GenericPanelActions._on_lookup(self, event)
    
    """
    def new(self, **kwargs):
        super().new(**kwargs)

    def update(self, **kwargs):
        super().update(**kwargs)

    def apply(self, **kwargs):
        is_valid = super().apply(**kwargs)
        return is_valid
    """


class Details(wxf.DetailEdit, GenericPanelActions):
    def __init__(self, base, **kwargs):
        super().__init__(base)
        GenericPanelActions.__init__(self, base=base, child=self)
    
    def _on_lookup(self, event):
        GenericPanelActions._on_lookup(self, event)
    
    """
    def new(self, **kwargs):
        super().new(**kwargs)

    def update(self, **kwargs):
        super().update(**kwargs)

    def apply(self, **kwargs):
        is_valid = super().apply(**kwargs)
        return is_valid
    """


class Suppliers(wxf.SupplierEdit, GenericPanelActions):
    def __init__(self, base, **kwargs):
        super().__init__(base)
        GenericPanelActions.__init__(self, base=base, child=self)
    
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
    def __init__(self, base, **kwargs):
        super().__init__(base)
        GenericPanelActions.__init__(self, base=base, child=self)
    
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
    def __init__(self, base, **kwargs):
        super().__init__(base)
        GenericPanelActions.__init__(self, base=base, child=self)
    
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
    def __init__(self, base, **kwargs):
        super().__init__(base)
        GenericPanelActions.__init__(self, base=base, child=self)
    
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
    def __init__(self, base, **kwargs):
        super().__init__(base)
        GenericPanelActions.__init__(self, base=base, child=self)
    
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
    def __init__(self, base, **kwargs):
        super().__init__(base)
        GenericPanelActions.__init__(self, base=base, child=self)
    
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
    def __init__(self, base, **kwargs):
        super().__init__(base)
        GenericPanelActions.__init__(self, base=base, child=self)
    
    """
    def new(self, **kwargs):
        super().new(**kwargs)

    def update(self, **kwargs):
        super().update(**kwargs)

    def apply(self, **kwargs):
        is_valid = super().apply(**kwargs)
        return is_valid
    """
