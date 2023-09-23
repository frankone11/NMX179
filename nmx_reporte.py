import parametros
import requests
import xmltodict

def Inicia_Reporte(dia_ini:int, mes_ini:int, anio_ini:int, dia_fin:int, mes_fin:int, anio_fin:int):
	#print("Reporte => Fecha inicial: " + str(anio_ini) + "-" + str(mes_ini).format("2d") + "-" + str(dia_ini) + " Fecha final: " + str(anio_fin) + "-" + str(mes_fin) + "-" + str(dia_fin))
	fecha_inicial = "{}-{:02d}-{:02d}".format(anio_ini, mes_ini, dia_ini)
	fecha_final = "{}-{:02d}-{:02d}".format(anio_fin, mes_fin, dia_fin)
	rfc = "MMP1312017FA"
	formato = "Reporte de {} => Fecha inicial {} Fecha final: {}".format(rfc, fecha_inicial, fecha_final)
	print(formato)

	txml = '<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:tem="http://tempuri.org/" xmlns:syc="http://schemas.datacontract.org/2004/07/SyC.CGRyF.WcfNMXService">\r\n'\
	'	<soapenv:Header/>\r\n'\
	'	<soapenv:Body>\r\n'\
	'		<tem:GetLecturasValidasRango>\r\n'\
	'			<!--Optional:-->\r\n'\
	'			<tem:filtro>\r\n'\
	'				<!--Optional:-->\r\n'\
	'				<syc:NSM></syc:NSM>\r\n'\
	'				<!--Optional:-->\r\n'\
	'				<syc:NSUE></syc:NSUE>\r\n'\
	'				<!--Optional:-->\r\n'\
	'				<syc:NSUT></syc:NSUT>\r\n'\
	'				<!--Optional:-->\r\n'\
	'				<syc:fechaFin>' + fecha_final +'</syc:fechaFin>\r\n'\
	'				<!--Optional:-->\r\n'\
	'				<syc:fechaInicio>' + fecha_inicial + '</syc:fechaInicio>\r\n'\
	'				<!--Optional:-->\r\n'\
	'				<syc:rfc>' + rfc + '</syc:rfc>\r\n'\
	'			</tem:filtro>\r\n'\
	'		</tem:GetLecturasValidasRango>\r\n'\
	'	</soapenv:Body>\r\n'\
	'</soapenv:Envelope>'
	headers = {'Content-Type': 'text/xml;charset=UTF-8',
		'SOAPAction' : 'http://tempuri.org/IServiceLecturas/GetLecturasValidasRango'}
	
	r = requests.post(parametros.URL, headers=headers, data=txml)

	rxml = r.text

	print("Resp: " + str(r.status_code))

	stack = xmltodict.parse(rxml)

	elems = stack['s:Envelope']['s:Body']['GetLecturasValidasRangoResponse']['GetLecturasValidasRangoResult']['a:Datos']['a:LecValidas']

	for elem in elems:
		print(elem)
		print("*****")

	print("Fin de impresión")

