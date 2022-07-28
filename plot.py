from imports import *

def optType(OptimizationType):
    if OptimizationType == 1:
        return 'Max'
    return 'Min'

def plot(window,frame2,XBoundries, YBoundries,strObjective, OptimizationType,sol,solExact):
    window.geometry('1060x650')
    txt=f'{optType(OptimizationType)}(x,y)=({sol["x"]} , {sol["y"]})'
    resultLabel = tk.Label(frame2,text=txt)
    resultLabel.grid(row=0, column=0)

    if XBoundries[0] == False:
        XBoundries = np.array([-4, 4])
        YBoundries = np.array([-4, 4])

    x = np.linspace(XBoundries[0], XBoundries[1], 30)
    y = np.linspace(YBoundries[0], YBoundries[1], 30)

    x, y = np.meshgrid(x, y)
    Z = eval(strObjective)

    fig = Figure(figsize=(4, 3), dpi=100)
    ax = fig.add_subplot(111, projection='3d')
    surf = ax.plot_surface(x, y, Z, rstride=1, cstride=1, cmap=cm.jet, linewidth=0)
    ax.plot(sol["x"], sol["x"], marker="o", markersize=5, markeredgecolor="red", markerfacecolor="red")
    ax.plot(solExact.jac[0], solExact.jac[1], marker="o", markersize=5, markeredgecolor="green", markerfacecolor="green")
    fig.colorbar(surf)
    title = ax.set_title("Title")
    title.set_y(1.01)

    ax.xaxis.set_major_locator(MaxNLocator(5))
    ax.yaxis.set_major_locator(MaxNLocator(6))
    ax.zaxis.set_major_locator(MaxNLocator(5))

    fig.tight_layout()

    canvas = FigureCanvasTkAgg(fig, master=frame2)
    canvas.draw()
    canvas.get_tk_widget().grid(row=1, column=0)