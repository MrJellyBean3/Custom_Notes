import json
import wx

CONFIG_FILE = "config.json"

class TextBoxFrame(wx.MiniFrame):
    def __init__(self, parent, pos=(200,200), size=(200,200), content="", title="Text Box"):
        super().__init__(parent, pos=pos, size=size, style=wx.RESIZE_BORDER | wx.CAPTION | wx.CLOSE_BOX)
        self.parent = parent

        self.main_sizer = wx.BoxSizer(wx.VERTICAL)

        # Add an editable title to the top of the text box
        self.title_edit = wx.TextCtrl(self, value=title, style=wx.BORDER_NONE)
        font = self.title_edit.GetFont()
        font.PointSize += 3
        font.Bold = True
        self.title_edit.SetFont(font)
        self.title_edit.SetBackgroundColour(wx.WHITE)  # Change the color here

        self.main_sizer.Add(self.title_edit, 0, wx.ALL, 5)

        self.text_box = wx.TextCtrl(self, value=content, style=wx.TE_MULTILINE)
        self.main_sizer.Add(self.text_box, 1, wx.EXPAND)

        # Add a delete button
        delete_button = wx.Button(self, label="Delete")
        delete_button.Bind(wx.EVT_BUTTON, self.on_delete)
        self.main_sizer.Add(delete_button, 0, wx.ALL, 5)

        self.SetSizer(self.main_sizer)

    def on_delete(self, event):
        self.parent.text_box_frames.remove(self)  # Remove this frame from parent's list
        self.Destroy()  # Close and destroy this frame

class MyFrame(wx.Frame):
    def __init__(self, parent):
        super().__init__(parent, title="My wxPython App")

        self.SetSize(1920,1080)
        self.SetPosition((0,0))

        self.text_box_frames = []

        menu_bar = wx.MenuBar()
        file_menu = wx.Menu()
        edit_menu = wx.Menu()

        make_new_textbox = edit_menu.Append(wx.ID_ANY, "New Text Box", "Create a new Text Box")
        save_item = file_menu.Append(wx.ID_SAVE, "Save", "Save current configuration and text box contents")
        exit_item = file_menu.Append(wx.ID_EXIT, "Exit", "Exit the program")

        menu_bar.Append(file_menu, "File")
        menu_bar.Append(edit_menu, "Edit")

        self.SetMenuBar(menu_bar)

        self.Bind(wx.EVT_MENU, lambda event: self.Close(True), exit_item)
        self.Bind(wx.EVT_MENU, self.new_textbox, make_new_textbox)
        self.Bind(wx.EVT_MENU, self.save, save_item)

        self.load()
        self.Show()

    def new_textbox(self, event):
        frame = TextBoxFrame(self)
        self.text_box_frames.append(frame)
        frame.Show()

    def save(self, event):
        config = {"text_boxes": []}
        for child in self.GetChildren():
            if isinstance(child, TextBoxFrame):
                box_config = {
                    "position": child.GetPosition().Get(),
                    "size": child.GetSize().Get(),
                    "content": child.text_box.GetValue(),
                    "title": child.title_edit.GetValue()
                }
                config["text_boxes"].append(box_config)

        with open(CONFIG_FILE, "w") as file:
            json.dump(config, file)


    def load(self):
        try:
            with open("config.json", "r") as file:
                config = json.load(file)

            for box in config["text_boxes"]:
                frame = TextBoxFrame(self, box["position"], box["size"], box["content"], box["title"])  # Load the title here
                frame.Show()
        except FileNotFoundError:
            pass


app = wx.App()
frame = MyFrame(None)
app.MainLoop()
