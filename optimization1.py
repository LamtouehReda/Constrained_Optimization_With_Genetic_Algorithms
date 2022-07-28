from imports import *

def Optim1(Contraint,strObjective,OptimizationType,TypeContraint,XBoundries,YBoundries):
    newCon = Contraint
    if newCon.find('exp') == -1:
        newCon = newCon.replace('x', 'x[0]')
    else:
        for i in range(len(newCon)):
            if newCon[i] == 'x':
                if newCon[i - 1] != 'e':
                    newCon = list(newCon)
                    newCon[i] = 'x[0]'
                    newCon = ''.join(newCon)
    newCon = newCon.replace('y', 'x[1]')

    newObj = strObjective
    if strObjective.find('exp') == -1:
        newObj = newObj.replace('x', 'x[0]')
    else:
        for i in range(len(newObj)):
            if newObj[i] == 'x':
                if newObj[i - 1] != 'e':
                    newObj = list(newObj)
                    newObj[i] = 'x[0]'
                    newObj = ''.join(newObj)
    newObj = newObj.replace('y', 'x[1]')

    newObj = f'({OptimizationType})*({newObj})'

    def objective(x, newObj):
        return eval(newObj)

    def constraint(x):
        return eval(newCon)

    x = [0, 0]
    cons = [{'type': TypeContraint, 'fun': constraint}]
    if XBoundries[0] == False and Contraint!='':
        sol = minimize(objective,
                       x,
                       args=(newObj),
                       method='SLSQP',
                       constraints=cons
                       )
    elif XBoundries[0] == False and Contraint=='':
        sol = minimize(objective,
                       x,
                       args=(newObj),
                       method='SLSQP',
                       )
    elif XBoundries[0] != False and Contraint == '':
        sol = minimize(objective,
                       x,
                       args=(newObj),
                       method='SLSQP',
                       bounds=[(XBoundries[0], XBoundries[1]), (YBoundries[0], YBoundries[1])],
                       )
    else:
        sol = minimize(objective,
                       x,
                       args=(newObj),
                       method='SLSQP',
                       bounds=[(XBoundries[0], XBoundries[1]), (YBoundries[0], YBoundries[1])],
                       constraints=cons
                       )
    if sol.message == 'Iteration limit reached':
        newObj = '(-1)*(' + newObj + ')'
        sol = minimize(objective,
                       x,
                       args=(newObj),
                       method='SLSQP',
                       )
        sol.jac = sol.jac * (-1)
    return sol