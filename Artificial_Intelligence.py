""" City Navigator """

from tkinter import *
from tkinter.ttk import *

#Creating a basic window
window = Tk()
window.geometry("350x300")
window.resizable(0, 0)
window.title("City Navigator")

#Label for source
lab = Label(window, text = "Select the place you want to be source ", font = "Arial, 10")
lab.grid(column=1,row=1)

#List of places
source = Combobox(window)
source['values'] = ('Camac Street','Central Avenue','Salt Lake City','Lake Gardens','New Alipore','Tram Depot')
source.current(0)
source.grid(column = 1,row = 2)

#Label for destination
lab1 = Label(window, text = "Select the place you want to be destination ", font = "Arial, 10")
lab1.grid(column=1,row=3)

#List of places
destination = Combobox(window)
destination['values'] = ('Camac Street','Central Avenue','Salt Lake City','Lake Gardens','New Alipore','Tram Depot')
destination.current(5)
destination.grid(column = 1,row = 4)

#Mentioming places
Map = {'Camac Street' : [['Central Avenue',1], ['Salt Lake City',5], ['Dalhousie',8]],
        'Central Avenue' : [['Camac Street',1], ['New Alipore',3], ['Lake Gardens',5], ['Tram Depot',9]],
        'Salt Lake City' : [['Camac Street',5], ['Tram Depot',4]],
        'Dalhousie' : [['Camac Street',8], ['Tram Depot',3], ['Lake Gardens',4]],
        'New Alipore' : [['Central Avenue',3]],
        'Lake Gardens' : [['Central Avenue',7]] }

#mentioning heuristic
heuristic = {'Camac Street' : 40, 'Central Avenue' : 20, 'Salt Lake City' : 50, 'Dalhousie' : 35, 'New Alipore' : 45,
             'Lake Gardens' : 15, 'Tram Depot' : 0}

def AStarSearch () :
    global tree,heuristic
    closed = []
    ch = str(source.get())
    opened = [[ch,0]]
    cost = {ch : 0}
    dest = str(destination.get())

    #Find the visisted nodes // closed
    while True :
        varn = [i[1] for i in  opened]                    #f(n) = f(n) + g(n)
        chosed_index = varn.index(min(varn))                #to get the minimum of it
        node = opened[chosed_index][0]
        closed.append(opened[chosed_index])
        del opened[chosed_index]
        if closed[-1][0] == 'Tram Depot' :
            break
        for item in Map[node] :
            if item[0] in [closed_item[0] for closed_item in closed] :
                continue
            cost.update({item[0] : cost[node] + item[1]})
            varn_node = cost[node] + heuristic[item[0]] + item[1]
            tmp = [item[0], varn_node]
            opened.append(tmp)

    #Find the optimal sequence
    trace_node = dest
    optimal_sequence = [dest]
    for i in range(len(closed)-2, -1, -1):
        check_node = closed[i][0]

        if trace_node in [children[0] for children in Map[check_node]] :
            children_costs = [temp[1] for temp in Map[check_node]]
            children_nodes = [temp[0] for temp in Map[check_node]]

            if cost[check_node] + children_costs[children_nodes.index(trace_node)] == cost[trace_node]:
                optimal_sequence.append(check_node)
                trace_node = check_node

    optimal_sequence.reverse()
    return closed, optimal_sequence

visited_nodes = []
optimal_nodes = []

#Displaying the places to reach the destination
def display(event):
    visited_nodes, optimal_nodes = AStarSearch()
    #print("Visited Nodes : " + str(visited_nodes))
    #print("Optimal node sequence : " + str(optimal_nodes))
    lab2 = Label(window,text = str(optimal_nodes), font = "Arial, 10")
    lab2.grid(column = 1,row=8)

lab3 = Label(window,text = "")
lab3.grid(column = 1,row = 7)
lab4 = Label(window,text = "")
lab4.grid(column = 1,row = 5)

btn = Button(window, text = "Clicke to get direction",)
btn.grid(column = 1, row = 6)
btn.bind('<Button-1>',display)

window.mainloop()