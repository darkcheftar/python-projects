from random import choice
import tkinter as tk
    
r = tk.Tk()
r.title('Jaldi 5')
numbers_labels = [tk.Label(r, text=str(i)) for i in range(1,101)]
it = iter(numbers_labels)
for i in range(10):
    for j in range(10):
        label = it.__next__()
        label['bg'] = 'orange'
        label['width'] = '5'
        label.grid(row=i, column=j, padx=3, pady=3)
numbers = list(range(1, 101))
def nextnum():
    global numbers, numbers_labels, label_big
    if len(numbers)>0:
        c = choice(numbers)
        numbers.remove(c)
        label = numbers_labels[c-1]
        label_big['text'] = str(c)
        label['bg'] = 'lightgreen'
    else:
        numbers = list(range(1,101))
        for i in range(100):
            numbers_labels[i]['bg'] = 'orange'
        label_big['text'] = 'Click Below To Start'
label_big = tk.Label(r, text='Click Below To Start',  font=("Helvetica", 25))
label_big.grid(row=10, column=0,columnspan=10)
button = tk.Button(r, text="Pick A Number",command=nextnum)
button.grid(row=11, column=0,columnspan=10)
r.mainloop()