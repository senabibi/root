import numpy as np
import ctypes
import matplotlib.pyplot as plt
import mplhep as hep
from ROOT import ( gPad, gVirtualX, kTRUE,TCanvas, TH2F)
from ROOT import gPad, gVirtualX
from ROOT import kTRUE, kRed
from ROOT import TCanvas, TH2, TH2F
class DynamicExec:
   def __init__( self ):
      self._cX   = None
      self._cY   = None
      self._old  = None
   def __call__( self ):
      h = gPad.GetSelected();
      if not h:
         return
      if not isinstance( h, TH2 ):
         return
      gPad.GetCanvas().FeedbackMode( kTRUE )
      px = gPad.GetEventX()
      py = gPad.GetEventY()
      uxmin, uxmax = gPad.GetUxmin(), gPad.GetUxmax()
      uymin, uymax = gPad.GetUymin(), gPad.GetUymax()
      pxmin, pxmax = gPad.XtoAbsPixel( uxmin ), gPad.XtoAbsPixel( uxmax )
      pymin, pymax = gPad.YtoAbsPixel( uymin ), gPad.YtoAbsPixel( uymax )
      if self._old != None:
         gVirtualX.DrawLine( pxmin, self._old[1], pxmax, self._old[1] )
         gVirtualX.DrawLine( self._old[0], pymin, self._old[0], pymax )
      gVirtualX.DrawLine( pxmin, py, pxmax, py )
      gVirtualX.DrawLine( px, pymin, px, pymax )
      self._old = px, py
      upx = gPad.AbsPixeltoX( px )
      x = gPad.PadtoX( upx )
      upy = gPad.AbsPixeltoY( py )
      y = gPad.PadtoY( upy )
      padsav = gPad
      if not self._cX:
         self._cX = TCanvas( 'c2', 'Projection Canvas in X', 730, 10, 700, 500 )
      else:
         self._DestroyPrimitive( 'X' )
      if not self._cY:
         self._cY = TCanvas( 'c3', 'Projection Canvas in Y', 10, 550, 700, 500 )
      else:
         self._DestroyPrimitive( 'Y' )
      self.DrawSlice( h, y, 'Y' )
      self.DrawSlice( h, x, 'X' )
      padsav.cd()
   def _DestroyPrimitive( self, xy ):
      proj = getattr( self, '_c'+xy ).GetPrimitive( 'Projection '+xy )
      if proj:
         proj.IsA().Destructor( proj )
   def DrawSlice( self, histo, value, xy ):
      yx = xy == 'X' and 'Y' or 'X'
      canvas = getattr( self, '_c'+xy )
      canvas.SetGrid()
      canvas.cd()
      bin = getattr( histo, 'Get%saxis' % xy )().FindBin( value )
      hp = getattr( histo, 'Projection' + yx )( '', bin, bin )
      hp.SetFillColor( 38 )
      hp.SetName( 'Projection ' + xy )
      hp.SetTitle( xy + 'Projection of bin=%d' % bin )
      hp.Fit( 'gaus', 'ql' )
      hp.GetFunction( 'gaus' ).SetLineColor( kRed )
      hp.GetFunction( 'gaus' ).SetLineWidth( 6 )
      canvas.Update()
def main():
    plt.style.use(hep.style.ROOT)
    main_canvas = TCanvas("c1", "Dynamic Slice Example", 10, 10, 700, 500)
    main_canvas.SetFillColor(42)
    main_canvas.SetFrameFillColor(33)
    hpxpy = TH2F('hpxpy', 'py vs px', 40, -4, 4, 40, -4, 4)
    hpxpy.SetStats(0)
    x=np.random.normal(0, 1, 50000)
    y=np.random.normal(0, 1, 50000)
    hpxpy[:, :] = np.histogram2d(x, y, bins=(40, 40), range=[[-4, 4], [-4, 4]])[0]
    hpxpy.Draw("COL")
    input("Move the mouse in the canvas to see dynamic slices")
    import __main__
    __main__.slicer = DynamicSlicer()
    main_canvas.AddExec("dynamic", "TPython::Exec('slicer()')")
    main_canvas.Update()
if __name__ == "__main__":
    main()