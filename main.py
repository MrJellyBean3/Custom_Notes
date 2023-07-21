#This code will be a custom note taking application that will allow users to make highly customized notes
#import wxpython


text_box_setup=[[5,5],[300,300]]#x,y,width,height

import wx

class MyFrame(wx.Frame):
    def __init__(self, parent):
        super().__init__(parent, title="My wxPython App")
        
        # Create a panel inside the frame
        self.panel = wx.Panel(self)
        
        # Create a text box inside the panel
        self.text_box = wx.TextCtrl(self.panel, style=wx.TE_MULTILINE)
        
        # Create a box sizer
        self.sizer = wx.BoxSizer(wx.VERTICAL)
        
        # Add the text box to the sizer
        self.sizer.Add(self.text_box, 1, wx.EXPAND)
        
        # Set the sizer for the panel
        self.panel.SetSizer(self.sizer)
        

        #Create the panel object
        #panel = wx.Panel(self)

        #Create the text box object
        text_box = wx.TextCtrl(self.panel, style = wx.TE_MULTILINE)




        #Create the menu bar object
        menu_bar = wx.MenuBar()

        #Create the file menu object
        file_menu = wx.Menu()

        #Create the edit menu object
        edit_menu = wx.Menu()

        #Create the help menu object
        help_menu = wx.Menu()

        #Create the file menu items
        new_file_item = file_menu.Append(wx.ID_NEW, "New File", "Create a new file")
        open_file_item = file_menu.Append(wx.ID_OPEN, "Open File", "Open an existing file")
        save_file_item = file_menu.Append(wx.ID_SAVE, "Save File", "Save the current file")
        save_as_file_item = file_menu.Append(wx.ID_SAVEAS, "Save As File", "Save the current file as a new file")
        exit_file_item = file_menu.Append(wx.ID_EXIT, "Exit", "Exit the program")

        #Create the edit menu items
        undo_edit_item = edit_menu.Append(wx.ID_UNDO, "Undo", "Undo the last action")
        redo_edit_item = edit_menu.Append(wx.ID_REDO, "Redo", "Redo the last action")
        cut_edit_item = edit_menu.Append(wx.ID_CUT, "Cut", "Cut the selected text")
        copy_edit_item = edit_menu.Append(wx.ID_COPY, "Copy", "Copy the selected text")
        paste_edit_item = edit_menu.Append(wx.ID_PASTE, "Paste", "Paste the selected text")
        delete_edit_item = edit_menu.Append(wx.ID_DELETE, "Delete", "Delete the selected text")
        select_all_edit_item = edit_menu.Append(wx.ID_SELECTALL, "Select All", "Select all text")

        #Create the help menu items
        about_help_item = help_menu.Append(wx.ID_ABOUT, "About", "About the program")

        #Add the file menu to the menu bar
        menu_bar.Append(file_menu, "File")

        #Add the edit menu to the menu bar
        menu_bar.Append(edit_menu, "Edit")

        #Add the help menu to the menu bar
        menu_bar.Append(help_menu, "Help")

        #Set the menu bar
        self.SetMenuBar(menu_bar)

        #Bind the menu items to their respective functions
        self.Bind(wx.EVT_MENU, lambda event: self.Close(True), exit_file_item)
        self.Bind(wx.EVT_MENU, lambda event: wx.MessageBox("This is a custom note taking application that will allow users to make highly customized notes", "About", wx.OK), about_help_item)





        self.Show()

#Create the application object
app = wx.App()
#Create the frame object
frame = MyFrame(parent=None)

#start app
app.MainLoop()









#display finished message
print("finished")