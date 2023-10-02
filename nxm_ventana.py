import wx
from wx import adv
import nmx_reporte


class VentanaNmx(wx.Frame):
	def __init__(self, *args, **kw):
		super().__init__(*args, **kw)
		pnl = wx.Panel(self)
		st = wx.StaticText(pnl, label="Fecha de inicio:\t\t\tNMX179 by FJGO\t\t\tFecha Fin:", pos=wx.Point(10,10), size=wx.Size(550, 20))
		self.cal1 = adv.CalendarCtrl(pnl, pos=wx.Point(10,50))
		self.cal2 = adv.CalendarCtrl(pnl, pos=wx.Point(270,50))
		bot = wx.Button(pnl, label="Iniciar Reporte", pos=wx.Point(10, 250))
		self.Bind(wx.EVT_BUTTON, self.OnButton, bot)

	def OnButton(self, event):
		resp = wx.MessageBox("Se va a iniciar el proceso", 'NMX179', wx.YES | wx.NO | wx.ICON_ASTERISK)
		if resp == wx.NO:
			print("Cancelado")
		else:
			fecha_ini = self.cal1.GetDate()
			fecha_fin = self.cal2.GetDate()

			if fecha_fin > fecha_ini:
				dia_ini = fecha_ini.GetDay()
				mes_ini = fecha_ini.GetMonth() + 1 #Se suma uno porque es un dato de base cero
				anio_ini = fecha_ini.GetYear()

				dia_fin = fecha_fin.GetDay()
				mes_fin = fecha_fin.GetMonth() + 1 #Se suma uno porque es un dato de base cero
				anio_fin = fecha_fin.GetYear()

				resp = False
				resp = nmx_reporte.Inicia_Reporte(dia_ini, mes_ini, anio_ini, dia_fin, mes_fin, anio_fin)
				if resp == True:
					wx.MessageBox("El reporte ha finalizado.", style=wx.ICON_ASTERISK)
				else:
					wx.MessageBox("Se ha producido un error durante el reporte", style=wx.ICON_ERROR)
			else:
				wx.MessageBox("Las fecha final debe de ser mayor a fecha de inicio.", style=wx.ICON_EXCLAMATION)

def IniciaVentana():
	app = wx.App()
	frm = VentanaNmx(None, title = "NMX179 by FJGO", size=wx.Size(550,350))
	frm.Show()
	app.MainLoop()