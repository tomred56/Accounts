import datetime

import wx
import wx.lib.agw.floatspin as wx_fs


# import data_structures as db
# import shelve


class Form(wx.Panel):
    """ The Form class is a wx.Panel that creates a bunch of controls
        and handlers for callbacks. Doing the layout of the controls is
        the responsibility of subclasses (by means of the doLayout()
        method). """

    def __init__(self, parent, records, **kwargs):
        super().__init__(parent, **kwargs)
        self.records = records
        self.record = []
        self.fields = []
        self.field = ""
        self.instances_list = []
        self.instances_name = ''
        self.error = ''
        self.load_class_data()
        self.create_controls()
        self.bind_events()
        self.do_layout()

    def load_class_data(self):
        """ expects sub-classes to load data"""
        raise NotImplementedError

    def create_controls(self):
        """
        Defines common fields for all record types
        Sub-classes define local fields
        """
        self.instances = wx.ListBox(self, style=wx.LB_SINGLE | wx.LB_HSCROLL | wx.LB_NEEDED_SB | wx.LB_SORT,
                                    choices=self.instances_list, name=self.instances_name)
        self.add_instance = wx.Button(self, label='Add')
        self.deactivate_instance = wx.CheckBox(self, label='Active', style=wx.ALIGN_RIGHT)
        self.deactivate_instance.Disable()
        self.edit_instance = wx.Button(self, label='Edit')
        self.edit_instance.Disable()
        self.logger = wx.TextCtrl(self, style=wx.TE_MULTILINE | wx.TE_READONLY, value=self.error)

    def do_layout(self):
        self.boxSizer0 = wx.BoxSizer(orient=wx.HORIZONTAL)
        self.gridSizer0 = wx.FlexGridSizer(rows=1, cols=3, vgap=10, hgap=10)

        # Prepare some reusable arguments for calling sizer.Add():
        expandOption = dict(flag=wx.EXPAND)
        noOptions = dict()
        emptySpace = ((0, 0), noOptions)

        for control, options in \
                [(self.add_instance, noOptions),
                 (self.edit_instance, noOptions),
                 (self.deactivate_instance, noOptions)]:
            self.gridSizer0.Add(control, **options)
        # self.gridSizer0.Add(self.new_instance, *noOptions)
        # self.gridSizer0.Add(self.deactivate_instance, *noOptions)
        # self.gridSizer0.Add(self.cancel_change, *noOptions)

        for control, options in \
                [(self.instances, dict(border=5, flag=wx.ALL | wx.EXPAND, proportion=1)),
                 (self.gridSizer0, dict(border=5, flag=wx.ALL))]:
            self.boxSizer0.Add(control, **options)

    def bind_events(self):
        for control, event, handler in \
                [(self.instances, wx.EVT_LISTBOX, self.on_instance_selected),
                 (self.add_instance, wx.EVT_BUTTON, self.on_add_instance),
                 (self.deactivate_instance, wx.EVT_CHECKBOX, self.on_deactivate_instance),
                 (self.edit_instance, wx.EVT_BUTTON, self.on_edit_instance)
                 ]:
            control.Bind(event, handler)

    def on_instance_selected(self, event):
        """ expects sub-classes to load data"""
        raise NotImplementedError

    def on_add_instance(self, event):
        get_new_instance_name = wx.TextEntryDialog()
        get_new_instance_name.Create(None, 'Enter new name', caption=self.instances_name)
        self._log('Clicked: %s' % event.GetString())
        if get_new_instance_name.ShowModal() == wx.ID_OK:
            new_instance_name = get_new_instance_name.GetValue()
            self._log('New name: %s' % new_instance_name)
            self.records.new_instance(new_instance_name, from_date=datetime.date.today(),
                                      parent_ref=self.records.parent_ref)
            self.load_class_data()
            self.instances.Append(new_instance_name)
            selected = self.instances.FindString(new_instance_name)
            self.instances.SetSelection(selected)
            self.instances.EnsureVisible(selected)

    def on_deactivate_instance(self, event):
        instance_name = wx.TextEntryDialog()
        if self.records.deactivate_instance(new_from_date=datetime.date.today()):
            self.load_class_data()
            self.deactivate_instance.SetValue(False)
            self.instances.SetSelection(0)
            self.instances.SetFirstItem(0)
            self._log('Deleted: %s' % instance_name)

    def on_edit_instance(self, event):
        self.record = event.GetString()
        self._log('Selected: %s' % event.GetString())

    # Helper method(s):

    def _log(self, message):
        """ Private method to append a string to the logger text
            control. """
        self.logger.AppendText('%s\n' % message)


class FormForInstitutions(Form):
    def __init__(self, parent, records, **kwargs):
        super().__init__(parent, records, **kwargs)

    def load_class_data(self):
        self.instances_list = [i for i in self.records.cls_dbr.keys()]
        self.instances_name = self.records.cls_shelf_key

    #        self.referrers = list(self.records.cls_dbr.keys())
    #        self.referrerLabel = self.records.cls_shelf_key

    def create_controls(self):
        super().create_controls()
        for k, v in self.records.cls_attributes.items():
            label = wx.StaticText(self, label=k.title())
            if v is str:
                field = wx.TextCtrl(self, style=wx.TE_MULTILINE | wx.TE_PROCESS_ENTER,
                                    size=wx.Size(-1, 75), value='')
            elif v is int:
                field = wx.SpinCtrl(self, -1, value="0", min=-1000000, max=1000000,
                                    style=wx.SP_VERTICAL | wx.SP_ARROW_KEYS)
            elif v is float:
                field = wx_fs.FloatSpin(self, -1, pos=(-1, -1),
                                        min_val=-1000000, max_val=1000000,
                                        increment=1, value=0, agwStyle=wx_fs.FS_LEFT)
                field.SetDigits(2)
            else:
                field = None
                pass
            if field:
                field.Disable()
            self.fields.append([label, field])
        self.saveButton = wx.Button(self, label="Save")
        self.saveButton.Disable()

    def do_layout(self):
        """ Layout the controls by means of sizers. """
        super().do_layout()
        expandOption = dict(flag=wx.EXPAND)
        noOptions = dict()
        emptySpace = ((0, 0), noOptions)
        layouts = []
        for l, f in self.fields:
            layouts.append((l, noOptions))
            layouts.append((f, expandOption))

        # A horizontal BoxSizer will contain the GridSizer (on the left)
        # and the logger text control (on the right):
        boxSizer1 = wx.BoxSizer(orient=wx.HORIZONTAL)
        boxSizer2 = wx.BoxSizer(orient=wx.VERTICAL)
        # A GridSizer will contain the other controls:
        gridSizer = wx.FlexGridSizer(rows=len(layouts) + 1, cols=2, vgap=10, hgap=10)

        # Prepare some reusable arguments for calling sizer.Add():

        # Add the controls to the sizers:
        for control, options in layouts:
            gridSizer.Add(control, **options)
        for control, options in [
            emptySpace,
            (self.saveButton, dict(flag=wx.ALIGN_CENTER))]:
            gridSizer.Add(control, **options)

        for control, options in \
                [
                    (self.boxSizer0, dict(border=5, flag=wx.ALL)),

                    (gridSizer, dict(border=5, flag=wx.ALL)),
                ]:
            boxSizer1.Add(control, **options)

        for control, options in \
                [
                    (boxSizer1, dict(border=5, flag=wx.ALL)),
                    (self.logger, dict(border=5, flag=wx.ALL | wx.EXPAND,
                                       proportion=1))
                ]:
            boxSizer2.Add(control, **options)

        self.SetSizerAndFit(boxSizer2)

    def bind_events(self):
        super().bind_events()
        for l, f in self.fields:
            f.Bind(wx.EVT_TEXT, self.on_field_changed)
            if type(f) is wx.SpinCtrl:
                f.Bind(wx.EVT_SPINCTRL, self.on_field_changed)
            if type(f) is wx_fs.FloatSpin:
                f.Bind(wx_fs.EVT_FLOATSPIN, self.on_field_changed)
        for control, event, handler in \
                [
                    (self.saveButton, wx.EVT_BUTTON, self.on_save),
                ]:
            control.Bind(event, handler)

    def on_instance_selected(self, event):
        self.record = event.GetString()
        self.records.fetch_instance(unique_name=self.record)
        for l, f in self.fields:
            self.field = l.LabelText.lower()
            if self.field in self.records.attributes.keys():
                f.Value = self.records.attributes[self.field]
            else:
                f.Value = ""
            f.Enable()
        self.deactivate_instance.Enable()
        self.edit_instance.Enable()
        self._log('Selected: %s' % self.record)

    def on_field_changed(self, event):
        value = event.GetString()
        if self.field in self.records.attributes.keys() and self.records.attributes[self.field] != value:
            self.saveButton.Enable()

    def on_save(self, event):
        for l, f in self.fields:
            if self.records[self.record][l.lower()] != f.getvalue():
                self._log(self.records[self.record][l.lower()])
                self.records[self.record][l.lower()] = f.getvalue()
                self._log(self.records[self.record][l.lower()])
        self.saveButton.Disable()


class FormForAccounts(Form):
    def load_class_data(self):

        self.instances_list = list(self.records.cls_dbr.keys())
        self.instances_name = self.records.cls_shelf_key
        self.referrers = list(self.records.cls_dbr.keys())
        self.referrerLabel = self.records.cls_shelf_key

    def doLayout(self):
        """ Layout the controls by means of sizers. """

        # A horizontal BoxSizer will contain the GridSizer (on the left)
        # and the logger text control (on the right):
        boxSizer1 = wx.BoxSizer(orient=wx.HORIZONTAL)
        boxSizer2 = wx.BoxSizer(orient=wx.VERTICAL)
        # A GridSizer will contain the other controls:
        gridSizer = wx.FlexGridSizer(rows=5, cols=2, vgap=10, hgap=10)

        # Prepare some reusable arguments for calling sizer.Add():
        expandOption = dict(flag=wx.EXPAND)
        noOptions = dict()
        emptySpace = ((0, 0), noOptions)

        # Add the controls to the sizers:
        for control, options in [
            emptySpace,
            (self.saveButton, dict(flag=wx.ALIGN_CENTER))]:
            gridSizer.Add(control, **options)

        for control, options in \
                [(self.instances, dict(border=5, flag=wx.ALL | wx.EXPAND, proportion=1)),
                 (gridSizer, dict(border=5, flag=wx.ALL)),
                 ]:
            boxSizer1.Add(control, **options)

        for control, options in \
                [(boxSizer1, dict(border=5, flag=wx.ALL)),
                 (self.logger, dict(border=5, flag=wx.ALL | wx.EXPAND,
                                    proportion=1))]:
            boxSizer2.Add(control, **options)

        self.SetSizerAndFit(boxSizer2)

    def create_controls(self):
        super().create_controls()
        self.saveButton = wx.Button(self, label="Save")

    def do_layout(self):
        """ Layout the controls by means of sizers. """

        # A horizontal BoxSizer will contain the GridSizer (on the left)
        # and the logger text control (on the right):
        boxSizer1 = wx.BoxSizer(orient=wx.HORIZONTAL)
        boxSizer2 = wx.BoxSizer(orient=wx.VERTICAL)
        # A GridSizer will contain the other controls:
        gridSizer = wx.FlexGridSizer(rows=5, cols=2, vgap=10, hgap=10)

        # Prepare some reusable arguments for calling sizer.Add():
        expandOption = dict(flag=wx.EXPAND)
        noOptions = dict()
        emptySpace = ((0, 0), noOptions)

        # Add the controls to the sizers:
        for control, options in [
            emptySpace,
            (self.saveButton, dict(flag=wx.ALIGN_CENTER))]:
            gridSizer.Add(control, **options)

        for control, options in \
                [(self.instances, dict(border=5, flag=wx.ALL | wx.EXPAND, proportion=1)),
                 (gridSizer, dict(border=5, flag=wx.ALL)),
                 ]:
            boxSizer1.Add(control, **options)

        for control, options in \
                [(boxSizer1, dict(border=5, flag=wx.ALL)),
                 (self.logger, dict(border=5, flag=wx.ALL | wx.EXPAND,
                                    proportion=1))]:
            boxSizer2.Add(control, **options)

        self.SetSizerAndFit(boxSizer2)

    def bind_events(self):
        super().bind_events()
        if self.records.cls_shelf_key == 'Institutions':
            for control, event, handler in \
                    [(self.saveButton, wx.EVT_BUTTON, self.on_save),
                     ]:
                control.Bind(event, handler)

    def on_save(self, event):
        self.saveButton.Disable()


class FormForTransactions(Form):
    def load_class_data(self):
        self.instances_list = list(self.records.cls_dbr.keys())
        self.instances_name = self.records.cls_shelf_key
        self.referrers = list(self.records.cls_dbr.keys())
        self.referrerLabel = self.records.cls_shelf_key

    def create_controls(self):
        super().create_controls()
        self.saveButton = wx.Button(self, label="Save")

    def doLayout(self):
        """ Layout the controls by means of sizers. """

        # A horizontal BoxSizer will contain the GridSizer (on the left)
        # and the logger text control (on the right):
        boxSizer1 = wx.BoxSizer(orient=wx.HORIZONTAL)
        boxSizer2 = wx.BoxSizer(orient=wx.VERTICAL)
        # A GridSizer will contain the other controls:
        gridSizer = wx.FlexGridSizer(rows=5, cols=2, vgap=10, hgap=10)

        # Prepare some reusable arguments for calling sizer.Add():
        expandOption = dict(flag=wx.EXPAND)
        noOptions = dict()
        emptySpace = ((0, 0), noOptions)

        # Add the controls to the sizers:
        for control, options in [
            emptySpace,
            (self.saveButton, dict(flag=wx.ALIGN_CENTER))]:
            gridSizer.Add(control, **options)

        for control, options in \
                [(self.instances, dict(border=5, flag=wx.ALL | wx.EXPAND, proportion=1)),
                 (gridSizer, dict(border=5, flag=wx.ALL)),
                 ]:
            boxSizer1.Add(control, **options)

        for control, options in \
                [(boxSizer1, dict(border=5, flag=wx.ALL)),
                 (self.logger, dict(border=5, flag=wx.ALL | wx.EXPAND,
                                    proportion=1))]:
            boxSizer2.Add(control, **options)

        self.SetSizerAndFit(boxSizer2)

    def bind_events(self):
        super().bind_events()
        if self.records.cls_shelf_key == 'Institutions':
            for control, event, handler in \
                    [(self.saveButton, wx.EVT_BUTTON, self.on_save),
                     ]:
                control.Bind(event, handler)

    def on_save(self, event):
        self.saveButton.Disable()


class FrameWithForms(wx.Frame):
    def __init__(self, parent, record_type, **kwargs):
        super().__init__(parent, **kwargs)
        notebook = wx.Notebook(self)
        tabs = []
        for records in record_type:
            tabs.append(FormForInstitutions(notebook, records))
            notebook.AddPage(tabs[-1], records.cls_shelf_key)
        self.SetClientSize(notebook.GetBestSize())


class FrameForCategory(wx.Frame):
    def __init__(self, parent, cat, sub_cat, detail, **kwargs):
        super().__init__(parent, **kwargs)
        self.cat = cat
        self.sub_cat = sub_cat
        self.detail = detail
        self.error = ''
        self.create_controls()
        self.bind_events()
        self.do_layout()
    
    def create_controls(self):
        """
        Defines common fields for all record types
        Sub-classes define local fields
        """
        #        instances = self.cat.all_values()
        self.categories = wx.ListBox(self, style=wx.LB_SINGLE | wx.LB_HSCROLL | wx.LB_NEEDED_SB | wx.LB_SORT,
                                     choices=self.cat.fetch(), name='Categories')
        self.add_category = wx.Button(self, label='Add')
        self.active_category = wx.CheckBox(self, label='Active', style=wx.ALIGN_RIGHT)
        self.active_category.Disable()
        self.edit_category = wx.Button(self, label='Edit')
        self.edit_category.Disable()
        
        self.sub_categories = wx.ListBox(self, style=wx.LB_SINGLE | wx.LB_HSCROLL | wx.LB_NEEDED_SB | wx.LB_SORT,
                                         choices=[], name='SubCategories')
        self.sub_categories.Disable()
        self.add_sub_category = wx.Button(self, label='Add')
        self.add_sub_category.Disable()
        self.active_sub_category = wx.CheckBox(self, label='Active', style=wx.ALIGN_RIGHT)
        self.active_sub_category.Disable()
        self.edit_sub_category = wx.Button(self, label='Edit')
        self.edit_sub_category.Disable()
        
        self.details = wx.ListBox(self, style=wx.LB_SINGLE | wx.LB_HSCROLL | wx.LB_NEEDED_SB | wx.LB_SORT,
                                  choices=[], name='Details')
        self.details.Disable()
        self.add_detail = wx.Button(self, label='Add')
        self.add_detail.Disable()
        self.active_detail = wx.CheckBox(self, label='Active', style=wx.ALIGN_RIGHT)
        self.active_detail.Disable()
        self.edit_detail = wx.Button(self, label='Edit')
        self.edit_detail.Disable()
        
        self.logger = wx.TextCtrl(self, style=wx.TE_MULTILINE | wx.TE_READONLY, value=self.error)
    
    def do_layout(self):
        self.boxSizer0 = wx.BoxSizer(orient=wx.HORIZONTAL)
        self.gridSizer0 = wx.GridSizer(rows=2, cols=3, vgap=10, hgap=10)
        self.gridSizer1 = wx.GridSizer(rows=2, cols=3, vgap=10, hgap=10)
        self.gridSizer2 = wx.GridSizer(rows=2, cols=3, vgap=10, hgap=10)
        
        # Prepare some reusable arguments for calling sizer.Add():
        expandOption = dict(flag=wx.EXPAND)
        noOptions = dict()
        emptySpace = ((0, 0), noOptions)
        
        for control, options in \
                [
                        emptySpace,
                        (self.categories, expandOption),
                        emptySpace,
                        (self.add_category, noOptions),
                        (self.edit_category, noOptions),
                        (self.active_category, noOptions)
                ]:
            self.gridSizer0.Add(control, **options)
        for control, options in \
                [
                        emptySpace,
                        (self.sub_categories, expandOption),
                        emptySpace,
                        (self.add_sub_category, noOptions),
                        (self.edit_sub_category, noOptions),
                        (self.active_sub_category, noOptions)
                ]:
            self.gridSizer1.Add(control, **options)
        for control, options in \
                [
                        emptySpace,
                        (self.details, expandOption),
                        emptySpace,
                        (self.add_detail, noOptions),
                        (self.edit_detail, noOptions),
                        (self.active_detail, noOptions)
                ]:
            self.gridSizer2.Add(control, **options)
        
        for control, options in \
                [
                        (self.gridSizer0, dict(border=5, flag=wx.ALL)),
                        (self.gridSizer1, dict(border=5, flag=wx.ALL)),
                        (self.gridSizer2, dict(border=5, flag=wx.ALL))
                ]:
            self.boxSizer0.Add(control, **options)
        
        self.SetSizerAndFit(self.boxSizer0)
    
    def bind_events(self):
        for control, event, handler in \
                [
                        (self.categories, wx.EVT_LISTBOX, self.on_instance_selected),
                        (self.add_category, wx.EVT_BUTTON, self.on_add_instance),
                        (self.active_category, wx.EVT_CHECKBOX, self.on_deactivate_instance),
                        (self.edit_category, wx.EVT_BUTTON, self.on_edit_instance),
                        (self.sub_categories, wx.EVT_LISTBOX, self.on_instance_selected),
                        (self.add_sub_category, wx.EVT_BUTTON, self.on_add_instance),
                        (self.active_sub_category, wx.EVT_CHECKBOX, self.on_deactivate_instance),
                        (self.edit_sub_category, wx.EVT_BUTTON, self.on_edit_instance),
                        (self.details, wx.EVT_LISTBOX, self.on_instance_selected),
                        (self.add_detail, wx.EVT_BUTTON, self.on_add_instance),
                        (self.active_detail, wx.EVT_CHECKBOX, self.on_deactivate_instance),
                        (self.edit_detail, wx.EVT_BUTTON, self.on_edit_instance)
                ]:
            control.Bind(event, handler)
    
    def on_instance_selected(self, event):
        source = event.EventObject.Name
        if source.lower() == 'categories':
            self.sub_categories.Set(self.sub_cat.all_values(cat=event.GetString()))
        self.record = event.GetString()
        self.records.fetch_instance(unique_name=self.record)
        for l, f in self.fields:
            self.field = l.LabelText.lower()
            if self.field in self.records.attributes.keys():
                f.Value = self.records.attributes[self.field]
            else:
                f.Value = ""
            f.Enable()
        self.deactivate_instance.Enable()
        self.edit_instance.Enable()
        self._log('Selected: %s' % self.record)
    
    def on_add_instance(self, event):
        get_new_instance_name = wx.TextEntryDialog()
        get_new_instance_name.Create(None, 'Enter new name', caption=self.instances_name)
        self._log('Clicked: %s' % event.GetString())
        if get_new_instance_name.ShowModal() == wx.ID_OK:
            new_instance_name = get_new_instance_name.GetValue()
            self._log('New name: %s' % new_instance_name)
            self.records.new_instance(new_instance_name, from_date=datetime.date.today(),
                                      parent_ref=self.records.parent_ref)
            self.load_class_data()
            self.instances.Append(new_instance_name)
            selected = self.instances.FindString(new_instance_name)
            self.instances.SetSelection(selected)
            self.instances.EnsureVisible(selected)
    
    def on_deactivate_instance(self, event):
        instance_name = wx.TextEntryDialog()
        if self.records.deactivate_instance(new_from_date=datetime.date.today()):
            self.load_class_data()
            self.deactivate_instance.SetValue(False)
            self.instances.SetSelection(0)
            self.instances.SetFirstItem(0)
            self._log('Deleted: %s' % instance_name)
    
    def on_edit_instance(self, event):
        self.record = event.GetString()
        self._log('Selected: %s' % event.GetString())
    
    # Helper method(s):
    
    def _log(self, message):
        """ Private method to append a string to the logger text
            control. """
        self.logger.AppendText('%s\n' % message)

"""
            if records.cls_shelf_key == 'Institutions':
                tabs.append(FormForInstitutions(notebook, records))
            elif records.cls_shelf_key == 'Accounts':
                tabs.append(FormForAccounts(notebook, records))
            elif records.cls_shelf_key == 'Transactions':
                tabs.append(FormForTransactions(notebook, records))
            else:
                pass
"""
