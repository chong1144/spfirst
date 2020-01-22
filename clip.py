#!/usr/bin/env python

import numpy as np


def clip(x , lo , hi):

  """
  CLIP	Clips a signal so laves fall between "lo" and "hi".
    usage:    y = clip( x, low, high )
      x = input image
      low = set everything below here to low
      high = set everything above here to high
      y = output image

  """
    

  y = x*np.less_equal(x,hi) + hi*np.greater(x,hi)
  y = y*np.greater(x,lo-1) + lo*np.less(x,lo)

  return y



















