import wx
from datetime import datetime

from input import get_data
from engine import transform_matrix

class Matrix():
    def __init__(self):
        self.live_cell = '0'
        self.dead_cell = '.'
        self.dimensions = (50, 50) # (rows, cols)
        self.generation = 0
        
        self.init_empty_matrix()

    def init_empty_matrix(self):
        # list of strings
        self.m = [self.dead_cell*self.dimensions[1] \
            for item in range(self.dimensions[0])]

        self.ml = ''.join(self.m) # string

    def load_data(self):
        self.m = get_data() # list of strings
        self.ml = ''.join(self.m) # string
        self.generation = 0

    def next(self):
        self.m = transform_matrix(self.m, self.live_cell, self.dead_cell)
        self.ml = ''.join(self.m)
        self.generation += 1

    def update_cell(self, id, value):
        n = 50
        row_id = id / n
        col_id = id % n

        # replace char in the list of strings
        # self.m[row_id][col_id] = value 
        row = self.m[row_id]
        row_list = list(row)
        row_list[col_id] = value
        self.m[row_id] = ''.join(row_list)
        
        self.ml = ''.join(self.m)
        
class Game(wx.Frame):
    def __init__(self, parent, id, title):
        wx.Frame.__init__(self, parent, id, title)
        self.matrix = Matrix()

        self.timer = wx.Timer(self, 1)
        self.Bind(wx.EVT_TIMER, self.next_event, self.timer)

        self.bitmap0 = wx.Bitmap('0.png')
        self.bitmap1 = wx.Bitmap('1.png')

        self.gs = wx.GridSizer(50, 50, 1, 1)
        self.gs.AddMany([self.get_bitmap(i) for i in range(2500)])

        self.bitmaps = [item for item in self.Children \
            if item.ClassName == u'wxStaticBitmap']
        
        self.create_buttons()
        self.update_view()
        self.Show(True)

    def create_buttons(self):
        self.next_button = wx.Button(self, wx.ID_ANY, label = 'Next')
        self.next_button.Bind(wx.EVT_BUTTON, self.next_event)

        self.play_button = wx.Button(self, wx.ID_ANY, label = 'Play')
        self.play_button.Bind(wx.EVT_BUTTON, self.play_event)

        self.pause_button = wx.Button(self, wx.ID_ANY, label = 'Pause')
        self.pause_button.Disable()
        self.pause_button.Bind(wx.EVT_BUTTON, self.pause_event)
        
        self.load_button = wx.Button(self, wx.ID_ANY, label = 'Load')
        self.load_button.Bind(wx.EVT_BUTTON, self.load_event)
        
        self.add_buttons()

    def add_buttons(self):
        vbox = wx.BoxSizer(wx.VERTICAL)
        vbox.Add(self.gs, proportion=1, flag=wx.EXPAND)
        vbox.Add(self.next_button, flag=wx.EXPAND|wx.TOP|wx.BOTTOM, border=4)
        vbox.Add(self.play_button, flag=wx.EXPAND|wx.TOP|wx.BOTTOM, border=4)
        vbox.Add(self.pause_button, flag=wx.EXPAND|wx.TOP|wx.BOTTOM, border=4)
        vbox.Add(self.load_button, flag=wx.EXPAND|wx.TOP|wx.BOTTOM, border=4)
        self.SetSizer(vbox)
        
    def get_bitmap(self, id):
        bitmap = wx.StaticBitmap(self, id=id, bitmap=self.bitmap0)
        bitmap.Bind(wx.EVT_LEFT_UP, self.cell_event)
        return bitmap

    def pause_event(self, event):
        print '--- %s Play paused.' % str(datetime.now())[:19]
        self.timer.Stop()
        self.play_button.Enable()
        self.next_button.Enable()
        self.pause_button.Disable()

    def play_event(self, event):
        print '--- %s Play started.' % str(datetime.now())[:19]
        self.timer.Start(milliseconds=1000, oneShot=False)
        self.play_button.Disable()
        self.next_button.Disable()
        self.pause_button.Enable()

    def update_view(self):
        for ii in range(0, 50*50-1):
            if self.matrix.ml[ii] == self.matrix.live_cell:
                self.bitmaps[ii].SetBitmap(bitmap=self.bitmap1)
            else:
                self.bitmaps[ii].SetBitmap(bitmap=self.bitmap0)
        print "--- generation %s" % self.matrix.generation

    def next_event(self, event=None):
        self.matrix.next()
        self.update_view()

    def cell_event(self, event):
        id = event.GetEventObject().Id
        
        if self.matrix.ml[id] == self.matrix.live_cell:
            bitmap = self.bitmap0
            cell = self.matrix.dead_cell
        else:
            bitmap = self.bitmap1
            cell = self.matrix.live_cell

        self.matrix.update_cell(id, cell) # update the data
        event.GetEventObject().SetBitmap(bitmap=bitmap) # update the view

    def load_event(self, event):
        self.matrix.load_data()
        self.update_view()
        print '--- %s Data loaded.' % str(datetime.now())[:19]

app = wx.App()
Game(None, -1, "Conway's Game of Life")
app.MainLoop()
