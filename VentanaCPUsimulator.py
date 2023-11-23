"""
Proyecto CPU simulator v1.0

"""

from tkinter import *

# Código que crea y configura la ventana del CPU simulator

ventanaCPUsimulator=Tk()
ventanaCPUsimulator.title("CPU simulator")
ventanaCPUsimulator.resizable(False, False)

anchoPantalla=ventanaCPUsimulator.winfo_screenwidth()
altoPantalla=ventanaCPUsimulator.winfo_screenheight()

# Calcula las coordenadas para centrar la ventana
x=(anchoPantalla-1100)//2
y=(altoPantalla-678)//2

# Establece la geometría de la ventana para que al ejecutarse aparezca centrada en la pantalla
ventanaCPUsimulator.geometry(f"1100x678+{x}+{y}")

frameCPUsimulator=Frame(ventanaCPUsimulator, width=1100, height=678)
frameCPUsimulator.config(bg="#707070")
frameCPUsimulator.pack()

# Widgets gráficos del CPU simulator

# Widgets AC y PC

etiquetaAcumulador=Label(frameCPUsimulator, text="AC:", bg="#707070", fg="red", font=("Consolas", 18))
etiquetaAcumulador.place(x=25, y=60)

cajaEntradaAcumulador=Entry(frameCPUsimulator, font=("Consolas", 14), justify=CENTER)
cajaEntradaAcumulador.insert(0, "")
cajaEntradaAcumulador.place(x=70, y=60, width=70, height=35)

etiquetaPC=Label(frameCPUsimulator, text="PC:", bg="#707070", fg="orange", font=("Consolas", 18))
etiquetaPC.place(x=25, y=180)

cajaEntradaPC=Entry(frameCPUsimulator, font=("Consolas", 14), justify=CENTER)
cajaEntradaPC.insert(0, "")
cajaEntradaPC.place(x=70, y=180, width=70, height=35)

# Widgets de la ALU

etiquetaALU=Label(frameCPUsimulator, text="ALU", bg="#707070", fg="blue", font=("Consolas", 18))
etiquetaALU.place(x=500, y=15)

etiquetaOperador1=Label(frameCPUsimulator, text="Operador 1:", bg="#707070", fg="blue", font=("Consolas", 18))
etiquetaOperador1.place(x=300, y=60)

cajaEntradaOperador1=Entry(frameCPUsimulator, font=("Consolas", 14), justify=CENTER)
cajaEntradaOperador1.insert(0, "")
cajaEntradaOperador1.place(x=450, y=60, width=70, height=35)

etiquetaOperador2=Label(frameCPUsimulator, text="Operador 2:", bg="#707070", fg="blue", font=("Consolas", 18))
etiquetaOperador2.place(x=550, y=60)

cajaEntradaOperador2=Entry(frameCPUsimulator, font=("Consolas", 14), justify=CENTER)
cajaEntradaOperador2.insert(0, "")
cajaEntradaOperador2.place(x=700, y=60, width=70, height=35)

etiquetaResultado=Label(frameCPUsimulator, text="Resultado:", bg="#707070", fg="blue", font=("Consolas", 18))
etiquetaResultado.place(x=425, y=120)

cajaEntradaResultado=Entry(frameCPUsimulator, font=("Consolas", 14), justify=CENTER)
cajaEntradaResultado.insert(0, "")
cajaEntradaResultado.place(x=575, y=120, width=70, height=35)

# Widget UC

etiquetaUC=Label(frameCPUsimulator, text="Unidad de control:", bg="#707070", fg="cyan", font=("Consolas", 18))
etiquetaUC.place(x=420, y=180)

cajaEntradaUC=Entry(frameCPUsimulator, font=("Consolas", 14), justify=CENTER)
cajaEntradaUC.insert(0, "")
cajaEntradaUC.place(x=300, y=230, width=470, height=35)

# Widgets de los buses

etiquetaBusDatos=Label(frameCPUsimulator, text="Bus de datos:", bg="#707070", fg="red", font=("Consolas", 18))
etiquetaBusDatos.place(x=25, y=300)

cajaEntradaBusDatos=Entry(frameCPUsimulator, font=("Consolas", 14), justify=CENTER)
cajaEntradaBusDatos.insert(0, "")
cajaEntradaBusDatos.place(x=205, y=300, width=150, height=35)

etiquetaBusControl=Label(frameCPUsimulator, text="Bus de control:", bg="#707070", fg="red", font=("Consolas", 18))
etiquetaBusControl.place(x=25, y=360)

cajaEntradaBusControl=Entry(frameCPUsimulator, font=("Consolas", 14), justify=CENTER)
cajaEntradaBusControl.insert(0, "")
cajaEntradaBusControl.place(x=230, y=360, width=150, height=35)

etiquetaBusDirecciones=Label(frameCPUsimulator, text="Bus de direcciones:", bg="#707070", fg="red", font=("Consolas", 18))
etiquetaBusDirecciones.place(x=25, y=420)

cajaEntradaBusDirecciones=Entry(frameCPUsimulator, font=("Consolas", 14), justify=CENTER)
cajaEntradaBusDirecciones.insert(0, "")
cajaEntradaBusDirecciones.place(x=280, y=420, width=150, height=35)

# Widgets IR, MAR y MBR

etiquetaIR=Label(frameCPUsimulator, text="IR:", bg="#707070", fg="pink", font=("Consolas", 18))
etiquetaIR.place(x=635, y=300)

cajaEntradaIR=Entry(frameCPUsimulator, font=("Consolas", 14), justify=CENTER)
cajaEntradaIR.insert(0, "")
cajaEntradaIR.place(x=680, y=300, width=70, height=35)

etiquetaMAR=Label(frameCPUsimulator, text="MAR:", bg="#707070", fg="yellow", font=("Consolas", 18))
etiquetaMAR.place(x=635, y=360)

cajaEntradaMAR=Entry(frameCPUsimulator, font=("Consolas", 14), justify=CENTER)
cajaEntradaMAR.insert(0, "")
cajaEntradaMAR.place(x=695, y=360, width=70, height=35)

etiquetaMBR=Label(frameCPUsimulator, text="MBR:", bg="#707070", fg="purple", font=("Consolas", 18))
etiquetaMBR.place(x=635, y=420)

cajaEntradaMBR=Entry(frameCPUsimulator, font=("Consolas", 14), justify=CENTER)
cajaEntradaMBR.insert(0, "")
cajaEntradaMBR.place(x=695, y=420, width=70, height=35)

# Widgets etiquetas, listas de posicion y dato

etiquetaMemoria=Label(frameCPUsimulator, text="Memoria de datos", bg="#707070", fg="red", font=("Consolas", 15))
etiquetaMemoria.place(x=859, y=20)

etiquetaPosicion=Label(frameCPUsimulator, text="Posición", bg="#707070", fg="red", font=("Consolas", 14))
etiquetaPosicion.place(x=858, y=50)

listaBinariaPosicion=Listbox(frameCPUsimulator)
listaBinariaPosicion.place(x=850, y=80, width=100, height=570)

etiquetaDato=Label(frameCPUsimulator, text="Dato", bg="#707070", fg="red", font=("Consolas", 14))
etiquetaDato.place(x=978, y=50)

listaBinariaDato=Listbox(frameCPUsimulator)
listaBinariaDato.place(x=950, y=80, width=100, height=570)

barraDesplazadora=Scrollbar(frameCPUsimulator, command=None)
barraDesplazadora.place(x=1050, y=80, width=20, height=570)

listaBinariaPosicion.config(yscrollcommand=barraDesplazadora.set)
listaBinariaDato.config(yscrollcommand=barraDesplazadora.set)

# Widgets listas de codop, operación 1, operación 2 y resultado

etiquetaCodop=Label(frameCPUsimulator, text="Codop", bg="#707070", fg="#8B4513", font=("Consolas", 14))
etiquetaCodop.place(x=50, y=495)

listaCodop=Listbox(frameCPUsimulator)
listaCodop.place(x=30, y=525, width=100, height=120)

etiquetaOP1=Label(frameCPUsimulator, text="OP 1", bg="#707070", fg="#8B4513", font=("Consolas", 14))
etiquetaOP1.place(x=160, y=495)

listaOperacion1=Listbox(frameCPUsimulator)
listaOperacion1.place(x=131, y=525, width=100, height=120)

etiquetaOP2=Label(frameCPUsimulator, text="OP 2", bg="#707070", fg="#8B4513", font=("Consolas", 14))
etiquetaOP2.place(x=260, y=495)

listaOperacion2=Listbox(frameCPUsimulator)
listaOperacion2.place(x=232, y=525, width=100, height=120)

etiquetaR=Label(frameCPUsimulator, text="Resultado", bg="#707070", fg="#8B4513", font=("Consolas", 14))
etiquetaR.place(x=338, y=495)

listaResultado=Listbox(frameCPUsimulator)
listaResultado.place(x=333, y=525, width=100, height=120)

botonCargarInstrucciones=Button(text="Cargar instrucciones", bg="gray", activebackground="#424242", command=None)
botonCargarInstrucciones.place(x=500, y=570, width=130, height=35)

botonEjecutarInstrucciones=Button(text="Ejecutar instrucciones", bg="#00FF00", activebackground="green", command=None)
botonEjecutarInstrucciones.place(x=650, y=570, width=135, height=35)

# Instrucción cíclica que permite mantener la ventana activa

ventanaCPUsimulator.mainloop()