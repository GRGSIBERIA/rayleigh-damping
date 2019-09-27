import wx

if __name__ == "__main__":
    app = wx.App()
    frame = wx.Frame(None, -1, 'Reyleigh Damping',size=(500,500))

    panel = wx.Panel(frame, wx.ID_ANY)

    freqA = wx.TextCtrl(frame, wx.ID_ANY)
    label_freqA = wx.StaticText(panel, wx.ID_ANY, "Low Frequency")

    layout_freqA = wx.BoxSizer(wx.HORIZONTAL)
    layout_freqA.Add(label_freqA)
    layout_freqA.Add(freqA, flag=wx.GROW)
    
    #freqB = wx.TextCtrl(frame, wx.ID_ANY)

    panel.SetSizer(layout_freqA)

    frame.Show()
    app.MainLoop()