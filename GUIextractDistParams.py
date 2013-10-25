# -*- coding: utf-8 -*-
# date: 25/10/13
# username: bia1992
# name: Bannov Il'ya
# description: GUI for function: extractDistParams
__author__ = 'Bannov Ilya'
__copyright__ = "Copyright 2013, Bannov Ilya"
__credits__ = ["Bannov Ilya"]
__license__ = "GPL"
__version__ = "1.0.0"
__email__ = "bannov.ilya@gmail.com"
__status__ = "Development"

import numpy as np
from traits.api import HasTraits, Float, Button, Array
from traitsui.api import View,Item, Group

class extractDistParams(HasTraits):
    x1 = Float(0)
    x2 = Float(0)
    f1 = Float(0)
    f2 = Float(0)
    E = Float(0)
    m1 = Float(0)
    m2 = Float(0)
    med = Array(shape=(None,))
    k = Float(0)
    peak = Float(0)
    peak_loc = Array(shape=(None,))
    entropy = Float(0)
    skew = Float(0)
    start = Button('Start')
    traits_view = View (Group(
                            Group(
                                Item('x1', label = ' x:'), 
                                Item('f1', label = ' f:')
                                ),
                            Group(
                                Item('x2', show_label = False),
                                Item('f2', show_label = False) 
                                ),
                                orientation = 'horizontal',
                                show_border=True
                            ),                                                       
                        Item('start', show_label = False, resizable = True),
                        Group(
                            Group(                                
                                Item('E', label = ' E:'),
                                Item('m1', label = ' m1:'),
                                Item('m2', label = ' m2:'),
                                Item('med', label = ' med:'),
                                Item('k', label = ' k:'),
                            ),
                            Group(
                                Item('peak', label = ' peak:'),
                                Item('peak_loc', label = ' peak_loc:'),
                                Item('entropy', label = ' entropy:'),
                                Item('skew', label = ' skew:')
                            ),
                            orientation = 'horizontal',
                            show_border=True  
                            ),
                        title = 'extractDistParams'
                        )
    
    def _start_fired(self):
        if self.f1 > 0 or self.f2 > 0:  
            print self.extractDistParams(np.array([[self.x1],[self.x2]]), np.array([[self.f1],[self.f2]]))
            self.E, self.m1, self.m2, self.med, self.k, self.peak, self.peak_loc, self.entropy, self.skew = self.extractDistParams(np.array([[self.x1],[self.x2]]), np.array([[self.f1],[self.f2]]))
        else:
            print "Error"

        
  
    def extractDistParams(self, x, f):
        # Energy
        E = np.sum(f)
        # Normalized psd
        fn = f / E
        # First central moment
        m1 = np.sum(x * fn)
        # Second central moment
        m2 = np.sum(((x - m1) ** 2) * fn)
        # Third central moment
        m3 = np.sum(((x - m1) ** 3) * fn)
        # Fourth central moment
        m4 = np.sum(((x - m1) ** 4) * fn)
        # kurtosis
        k = m4 / (m2 ** 2) - 3
        # median
        cs = np.cumsum(fn)
        med = x[cs >= .5][0]
        # skeweness
        skew = m3 / (m2 ** (3 / 2))
        # A0
        peak = np.max(f)
        # A0 location
        peak_loc = x[np.argmax(f)]    
        # Entropy
        # It make sense just for the positive values
        p = (x[x > 0] * fn[x > 0])
        p = p[p > 0]
        entropy = -np.sum((p) * np.log2(p))
    
        return E, m1, m2, med, k, peak, peak_loc, entropy, skew      

 
    
if __name__ == '__main__':
   cl = extractDistParams()
   cl.configure_traits()  