import wx
from datetime import datetime

from input import get_data
from engine import transform_matrix

class Matrix():
    def __init__(self):
        self.m = get_data() # list of strings
        self.ml = ''.join(self.m) # string
        self.live_cell = '0'
        self.dead_cell = '.'
        self.generation = 0

    def next(self):
        self.m = transform_matrix(self.m, self.live_cell, self.dead_cell)
        self.ml = ''.join(self.m)
        self.generation += 1

class Game(wx.Frame):
    def __init__(self, parent, id, title):
        wx.Frame.__init__(self, parent, id, title)
        self.matrix = Matrix()

        self.timer = wx.Timer(self, 1)
        self.Bind(wx.EVT_TIMER, self.timer_event, self.timer)

        def get_bitmap(id):
            bitmap = wx.StaticBitmap(self, id=id, bitmap=wx.Bitmap('01.png'))
            bitmap.Bind(wx.EVT_LEFT_UP, cell_event)
            return bitmap

        def cell_event(event):
            pass

        # --- next button
        def next_event(event):
            self.next_action()
        
        next_button = wx.Button(self, wx.ID_ANY, label = 'Next')
        next_button.Bind(wx.EVT_BUTTON, next_event)

        # --- play button
        def play_event(event):
            print '--- %s Play started.' % str(datetime.now())[:19]
            self.timer.Start(milliseconds=1000, oneShot=False)
            play_button.Disable()
            next_button.Disable()
            pause_button.Enable()

        play_button = wx.Button(self, wx.ID_ANY, label = 'Play')
        play_button.Bind(wx.EVT_BUTTON, play_event)

        # --- pause button
        def pause_event(event):
            print '--- %s Play paused.' % str(datetime.now())[:19]
            self.timer.Stop()
            play_button.Enable()
            next_button.Enable()
            pause_button.Disable()

        pause_button = wx.Button(self, wx.ID_ANY, label = 'Pause')
        pause_button.Disable()
        pause_button.Bind(wx.EVT_BUTTON, pause_event)

        vbox = wx.BoxSizer(wx.VERTICAL)

        self.gs = wx.GridSizer(50, 50, 1, 1)

        self.gs.AddMany([get_bitmap(i) for i in range(2500)])

        vbox.Add(self.gs, proportion=1, flag=wx.EXPAND)
        vbox.Add(next_button, flag=wx.EXPAND|wx.TOP|wx.BOTTOM, border=4)
        vbox.Add(play_button, flag=wx.EXPAND|wx.TOP|wx.BOTTOM, border=4)
        vbox.Add(pause_button, flag=wx.EXPAND|wx.TOP|wx.BOTTOM, border=4)

        self.SetSizer(vbox)
        self.next_action()

        self.Show(True)

    def timer_event(self, event):
        self.next_action()
        
    def next_action(self):
        print "--- generation %s" % self.matrix.generation
        for ii in range(0, 50*50-1):
            self.gs.Show(ii)
        for ii in range(0, 50*50-1):
            if self.matrix.ml[ii] == self.matrix.live_cell:
                self.gs.Hide(ii)
        self.matrix.next()

app = wx.App()
Game(None, -1, "Conway's Game of Life")
app.MainLoop()
