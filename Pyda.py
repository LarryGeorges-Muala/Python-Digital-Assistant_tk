#App Name: Python Digital Assistant
#Python Version 3.5
#Developper: Larry Georges Muala

import tkinter
from tkinter import messagebox
import wikipedia
import wolframalpha


window = tkinter.Tk()


window.title('Python Digital Assistant')

window.geometry("450x50")

window.resizable(0,0)

window.configure(background="gray1")

#header label
lbl_main = tkinter.Label(window, text="Welcome to the Python Interactive and Vocal Assistant. How can I help you?", font=("Helvetica", 10), bg="beige", fg="black")
lbl_main.pack(fill=tkinter.X)

#text entry for search
ent_main = tkinter.Entry(window)
ent_main.pack(fill=tkinter.X)
ent_main.focus()

############################################################################################

#Menu Bar
def about_app():
	print("App Name: Python Digital Assistant GUI")
	print("App Description: Python Digital Assistant GUI with tkinter")
	print("Python Version 3.5")
	print("Developper: Larry Georges Muala")
	
	messagebox.showinfo("App Info", "App Name: Python Digital Assistant GUI\n" + 
						"\nApp description:  Python Digital Assistant GUI with tkinter\n" + 
						"\nPython Version 3.5 \n" + 
						"\nDevelopper: Larry Georges Muala")

menubar = tkinter.Menu(window)
myMenu = tkinter.Menu(menubar, tearoff=0)
myMenu.add_command(label="About", command=about_app)
myMenu.add_separator()
myMenu.add_command(label="Exit", command=window.quit)
menubar.add_cascade(label="App Info", menu=myMenu)

#display the menu
window.config(menu=menubar)

############################################################################################

#search function with button Enter
def onEnter(event):
		
		#getting search text input
		input = ent_main.get()
		input = input.lower()
		
		#toplevel pop up window
		toplevel = tkinter.Toplevel()
		toplevel.configure(background="black")
		
		#header label
		label1 = tkinter.Label(toplevel, text="Search Results", font=("Helvetica", 10), bg="gray1", fg="white")
		label1.pack()
		
		#search result textfield
		answer_text = tkinter.Text(toplevel)
		answer_text.pack(fill=tkinter.X)
	
		
		try:
			#WolfRamAlpha database search
			
			app_id = "G639QJ-GRP8YT7V92"

			client = wolframalpha.Client(app_id)

			res = client.query(input)

			answer = next(res.results).text
	
			print(answer)
			
			#displaying answer
			answer_text.insert(tkinter.INSERT, answer)
			
			#disabling textfield for editing
			answer_text.configure(state=tkinter.DISABLED)
			
			#clearing text entry for new search
			ent_main.delete(0, tkinter.END)
	
		except:
			#Wikipedia database search
			
			answer = wikipedia.summary(input)
			
			#displaying answer			
			answer_text.insert(tkinter.INSERT, answer)
			
			#disabling textfield for editing
			answer_text.configure(state=tkinter.DISABLED)
			
			#clearing text entry for new search
			ent_main.delete(0, tkinter.END)
	
#bind function Search Contacts to button Enter		
window.bind("<Return>", onEnter)

window.mainloop()