Proceso Costo_Pasajes 
	Escribir "Ingrese cantidad de personas que viajaran"
	leer costoPasaje 
	Si costoPasaje > 100 Entonces
		costo = 20 * costoPasaje
		Escribir  "Precio final del pasaje", costo
		
	SiNo
		si costoPasaje >= 50 y costoPasaje <= 100 Entonces
			costo = 35 * costoPasaje
			Escribir "Precio final del pasaje", costo
		sino 
			si costoPasaje >= 20 y costoPasaje <= 49 Entonces
				costo = 40 * costoPasaje
				Escribir "Precio final del pasaje", costo
			SiNo
				si costoPasaje <= 20 Entonces
					costo = 70 * costoPasaje
					Escribir "Precio final del pasaje", costo
				sino 
					Escribir "Precio final del pasaje", costo 
				FinSi
			FinSi
		FinSi
	Fin Si
FinProceso
