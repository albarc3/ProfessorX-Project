import numpy as np
from pylsl import StreamInlet, resolve_stream, local_clock
import pyqtgraph as pg
from pyqtgraph.Qt import QtCore, QtGui
from scipy.signal import butter, lfilter, lfilter_zi

class BandPass:
    def __init__(self, lowcut, highcut, sr, order=4):    
        self.b, self.a = butter(order, [lowcut, highcut], btype='bandpass', fs=sr)
        self.z = lfilter_zi(self.b, self.a)
        
    
    def filter(self, x):
        y, self.z = lfilter(self.b, self.a, x, zi=self.z)
        return y

class BandStop:
    def __init__(self, lowcut, highcut, sr, order=4):    
        self.b, self.a = butter(order, [lowcut, highcut], btype='bandstop', fs=sr)
        self.z = lfilter_zi(self.b, self.a)
        
    
    def filter(self, x):
        y, self.z = lfilter(self.b, self.a, x, zi=self.z)
        return y
        

class CustomViewBox(pg.ViewBox):
    def __init__(self, viewer, *args, **kwds):
        pg.ViewBox.__init__(self, *args, **kwds)
        self.viewer = viewer

    def wheelEvent(self, ev, axis=None):        
        self.viewer.scale *= 1.25 if ev.delta() < 0 else 1/1.25                
        
        
class EEGViewer:
    def __init__(self):
        self.plot_duration = 7.0
        self.scale = 160
        
    def connect(self):
        # first resolve an EEG stream on the lab network
        print("looking for an EEG stream...")
        streams = resolve_stream('type', 'EEG')
        self.inlet = StreamInlet(streams[0])
        self.prepareFilter()
        self.preparePlot()
        self.start()
        
        
    def prepareFilter(self):
        self.sr = self.inlet.info().nominal_srate()
        n = int(self.sr*self.plot_duration)
        lowcut = 0.5
        highcut = 30
        order = 4        
        self.filter = [BandPass(lowcut, highcut, self.sr, order) for i in range(self.inlet.channel_count)]
        self.notch = [BandStop(48, 52, self.sr, order) for i in range(self.inlet.channel_count)]
        self.buffer = np.zeros((self.inlet.channel_count, n))
        self.t = np.linspace(0, self.plot_duration, n, endpoint=False)


    def preparePlot(self):
        self.win = pg.GraphicsWindow()
        self.win.setWindowTitle('LSL Plot ' + self.inlet.info().name())
        self.vb = CustomViewBox(self)
        self.plt = self.win.addPlot(viewBox=self.vb)
        self.plt.setXRange(0, self.plot_duration)
        self.plt.setYRange(-1 - self.inlet.channel_count, 1)
        self.plt.setMouseEnabled(False, False)
        self.plt.hideAxis('left')
        self.plt.hideButtons()
        self.plt.setMenuEnabled(False)
        self.plt.setTitle(self.inlet.info().name())        
        self.curves = [self.plt.plot() for x in range(self.inlet.channel_count)]
        
           
    def start(self):
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.update)
        self.timer.start(50)
        
        
    def update(self):
        # Read data from the inlet. Use a timeout of 0.0 so we don't block GUI interaction.
        chunk, timestamps = self.inlet.pull_chunk()    
        if timestamps:    
            y = np.asarray(chunk)            
            samples = y.shape[0]
            self.buffer = np.roll(self.buffer, -samples, axis=1)
            for ch_ix in range(self.inlet.channel_count):
                filtered_y = self.filter[ch_ix].filter(self.notch[ch_ix].filter(y[:,ch_ix]))
                self.buffer[ch_ix,-samples:] = filtered_y
                self.curves[ch_ix].setData(self.t, self.buffer[ch_ix,:]/self.scale - ch_ix)

# Start Qt event loop unless running in interactive mode or using pyside.
if __name__ == '__main__':
    import sys
    viewer = EEGViewer()    
    viewer.connect()
    if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
        QtGui.QApplication.instance().exec_()