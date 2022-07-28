from imports import *

def DetConType(constStr):
    if constStr == '=':
        return 'eq'
    else:
        return 'ineq'

def retrieve(widgetsInputs,OpType):
    strObjective = widgetsInputs['objectiveInput'].get()
    Contraint = widgetsInputs['contrainInput1'].get()
    TypeContraint = DetConType(widgetsInputs['contraintOp'].get())
    try:
        XBoundries = np.array([float(widgetsInputs['XupperBoundaryInpt'].get()),
                               float(widgetsInputs['XlowerBoundaryInpt'].get())])
        YBoundries = np.array([float(widgetsInputs['YupperBoundaryInpt'].get()),
                               float(widgetsInputs['YlowerBoundaryInpt'].get())])
    except:
        XBoundries = [False,False]
        YBoundries = [False,False]

    PopulationSize=float(widgetsInputs['popSize'].get())
    Iterations=int(widgetsInputs['iterNum'].get())
    crossoverProb=float(widgetsInputs['crossProb'].get())
    mutationProba=float(widgetsInputs['mutationProb'].get())
    OptimizationType = OpType.get()
    return [XBoundries, YBoundries, strObjective,
            Contraint, TypeContraint, OptimizationType,
            PopulationSize,Iterations,crossoverProb,mutationProba]
