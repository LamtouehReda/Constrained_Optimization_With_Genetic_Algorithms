from imports import *

window = tk.Tk(className='Optimization avec GA')

window.geometry('530x300')

frame1 = tk.Frame(window)
frame1.grid(row=0, column=0)

objectiveLabel = tk.Label(frame1, text='fonction objective* : ')
objectiveLabel.grid(row=0, column=0, pady=10)

objectiveInput = tk.Entry(frame1)
objectiveInput.grid(row=0, column=1, columnspan=3, pady=10, ipadx=60)

contraintLabel = tk.Label(frame1, text='Contraint : ')
contraintLabel.grid(row=1, column=0, pady=10)

contrainInput1 = tk.Entry(frame1)
contrainInput1.grid(row=1, column=1, pady=10)

contraintOp = tk.StringVar()
contraintOpSelect = ttk.Combobox(frame1, values=['=', '>'], textvariable=contraintOp, width=5)
contraintOpSelect.grid(row=1, column=2, pady=10, padx=5)

contrainLabel2 = tk.Label(frame1, text='0')
contrainLabel2.grid(row=1, column=3, pady=10, sticky='W')

XboundariesLbl = tk.Label(frame1, text='Les Bornes de x :')
XboundariesLbl.grid(row=2, column=0, pady=10)

XboundariesFrame = tk.Frame(frame1)

XupperBoundaryInpt = tk.Entry(XboundariesFrame, width=5)
XupperBoundaryInpt.grid(row=0, column=0, padx=5)

boundariesXlabel = tk.Label(XboundariesFrame, text='x')
boundariesXlabel.grid(row=0, column=1)

XlowerBoundaryInpt = tk.Entry(XboundariesFrame, width=5)
XlowerBoundaryInpt.grid(row=0, column=2, padx=5)

XboundariesFrame.grid(row=2, column=1, pady=10)

YboundariesLbl = tk.Label(frame1, text='Les Bornes de y :')
YboundariesLbl.grid(row=2, column=2, pady=10)

YboundariesFrame = tk.Frame(frame1)

YupperBoundaryInpt = tk.Entry(YboundariesFrame, width=5)
YupperBoundaryInpt.grid(row=0, column=0, padx=5)

YboundariesXlabel = tk.Label(YboundariesFrame, text='y')
YboundariesXlabel.grid(row=0, column=1)

YlowerBoundaryInpt = tk.Entry(YboundariesFrame, width=5)
YlowerBoundaryInpt.grid(row=0, column=2, padx=5)

YboundariesFrame.grid(row=2, column=3, pady=10)

popSizeLabel = tk.Label(frame1, text='taille du Population* : ')
popSizeLabel.grid(row=3, column=0, pady=10)

popSize = tk.StringVar()
popSizeSelect = ttk.Combobox(frame1, values=[x for x in range(1, 11)], textvariable=popSize, width=5)
popSizeSelect.grid(row=3, column=1, pady=10, padx=5)

IterNumLabel = tk.Label(frame1, text='Nombre D\'iterations* : ')
IterNumLabel.grid(row=3, column=2, pady=10)

iterNum = tk.StringVar()
IterNumSelect = ttk.Combobox(frame1, values=[x for x in range(100, 1001, 100)], textvariable=iterNum, width=5)
IterNumSelect.grid(row=3, column=3, pady=10, padx=5)

CrossLabel = tk.Label(frame1, text='Probabilite du Crossver* : ')
CrossLabel.grid(row=4, column=0, pady=10)

crossProb = tk.StringVar()
CrossSelect = ttk.Combobox(frame1, values=[x for x in range(1, 10, 1)], textvariable=crossProb, width=5)
CrossSelect.grid(row=4, column=1, pady=10, padx=5)

MutationLabel = tk.Label(frame1, text='Probabilite du Mutation* : ')
MutationLabel.grid(row=4, column=2, pady=10)

mutationProb = tk.StringVar()
MutationSelect = ttk.Combobox(frame1, values=[float(f'0.{x}') for x in range(1, 11)], textvariable=mutationProb,
                              width=5)
MutationSelect.grid(row=4, column=3, pady=10, padx=5)

OpType = tk.IntVar()
MaxRadio = tk.Radiobutton(frame1, text='Maximisation', variable=OpType, value=1)
MaxRadio.grid(row=5, column=1)
MinRadio = tk.Radiobutton(frame1, text='Minimisation', variable=OpType, value=-1)
MinRadio.grid(row=5, column=2)

frame2 = tk.Frame(window)
frame2.grid(row=1, column=0)

