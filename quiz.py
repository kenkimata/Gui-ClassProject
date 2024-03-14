from tkinter import *


class Quizstarter:
    def __init__ (self,parent):
        background_colour="yellow2"
        #frame set up
        self.quiz_frame = Frame(parent, bg = background_colour, padx=100, pady=100)
        self.quiz_frame.grid()

        #Label widget for our heading
        self.heading_label = Label (self.quiz_frame, text = "NZ Road Rules", font=("Tw Cen MT", "bold"), bg=background_colour)
        self.heading_label.grid(row=0)

        #Label for user name prompt
        self.user_label = Label ( self.quiz_frame, text="Please enter your name below", font=("Tw Cen Mt", "16"), bg=background_colour)
        self.user_label.grid(row=1)

        #users input is take by Entry widget
        self.entry_box=Entry(self.quiz_frame)
        self.entry_box.grid(row=2, pady=20)
        
        #continue button
        self.continue_button = Button (self.quiz_frame, text="Continue", bg="pink", command=self.name_collection)
        self.continue_button.grid(row=3, pady=20)

        def




#*********************************Starting point of program********************#
if __name__ == "__main__":
    root = Tk()
    root.title("NZ Road Rules Quiz")
    #quizstarter_object = Quizstarter(root) #inisiation, making an instance of the Classquiz starter to create
    root.mainloop()#so the window dont close