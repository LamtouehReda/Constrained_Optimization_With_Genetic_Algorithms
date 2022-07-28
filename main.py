from imports import *
from interface import *
from GA import *
from plot import plot
from retrieveData import retrieve
from optimization1 import Optim1

widgetsInputs={
    'objectiveInput':objectiveInput,
    'contrainInput1':contrainInput1,
    'contraintOp':contraintOp,
    'XupperBoundaryInpt':XupperBoundaryInpt,
    'YupperBoundaryInpt':YupperBoundaryInpt,
    'XlowerBoundaryInpt':XlowerBoundaryInpt,
    'YlowerBoundaryInpt':YlowerBoundaryInpt,
    'popSize':popSize,
    'iterNum':iterNum,
    'crossProb':crossProb,
    'mutationProb':mutationProb
}

def solve():
    [XBoundries, YBoundries, strObjective,
     Contraint, TypeContraint, OptimizationType,
     PopulationSize, Iterations, crossoverProb, mutationProba]=retrieve(widgetsInputs,OpType)

    window.geometry('1060x300')
    frame3 = tk.Frame(window, highlightthickness=2, highlightbackground="black")
    frame3.grid(row=1, column=1)
    traitmentLabel = scrolledtext.ScrolledText(window,
                                          wrap=tk.WORD,
                                          width=70,
                                          font=("Times New Roman",
                                                9))

    traitmentLabel.grid(row=0,column=1, pady=10, padx=10,rowspan=2,sticky='W')


    maximum_generations = Iterations
    if XBoundries[0]==False:
        population = generate_population(int(PopulationSize), (-1,1),(-1,1))
    else:
        population = generate_population(int(PopulationSize), tuple(XBoundries), tuple(YBoundries))
    i = 1
    while True:
        traitmentLabel.insert(tk.INSERT, f'🧬 GENERATION {i}\n\n')

        for individual in population:

            traitmentLabel.insert(tk.INSERT, f'{individual}, {fitness_function(individual,strObjective,Contraint)})\n')

        traitmentLabel.yview(tk.END)

        if i == maximum_generations:
            break

        i += 1
        if XBoundries[0]==False:
            population = make_next_generation(population,strObjective,(-1,1),(-1,1),Contraint)
        else:
            population = make_next_generation(population,strObjective,XBoundries,YBoundries,Contraint)

    best_individual = sort_population_by_fitness(population,strObjective,Contraint)[-1]
    traitmentLabel.insert(tk.INSERT, "\n🔬 FINAL RESULT\n")
    traitmentLabel.insert(tk.INSERT, f'{best_individual}, {fitness_function(best_individual,strObjective,Contraint)}\n')

    sol=best_individual
    solExact=Optim1(Contraint,strObjective,OptimizationType,TypeContraint,XBoundries,YBoundries)
    plot(window, frame2, XBoundries, YBoundries,strObjective, OptimizationType, sol, solExact)

if __name__ == '__main__':

    solveBtn = tk.Button(frame1, text='Solve', activebackground='#119911', command=lambda: [solve()])
    solveBtn.grid(row=6, columnspan=4, pady=20, ipadx=20)

    window.mainloop()

