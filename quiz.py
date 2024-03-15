from tkinter import *
import random

names_list = []
global questions_answers
asked = []
score=0

# Dictionary has key of number (for each question number) and : the value for each is a list that has 7 items, so index 0 to 6
questions_answers = {
    1: ["What do you do when you see blue and red flashing lights behind you?", # item 1, index 0 will be the question
        'Speed up to get out of the way', # item 2, index 1 will be the first choice
        'Slow down and frive carefully', # item 3, index will be third choice
        'slow down and stop', # item 4, index will be fourth choice 
        'Drive on usual', # item 5, index will be fourth choice
        'Slow down and stop', # item 6, index 5 will be the write statement we need to display the right statement if the user enters wrong choice
        3], # item 7, index 6 will be the position of the right answer (index where right answer sits), this will be out check if answer is correct or not
    
    2: ["You may stop on a motorway only:", 'if there is an emergency', 'To let down or pick up passengers', 'to make a U-turn', 'to stop and take a photo',
        'if there is an emergency',1],

    3: ["When coming up to a pedestrian crossing without a raised traffic island, what must you do?", "Speed up before the pedestrians cross",
        'Stop and give way to pedestrians on any part of the crossing', "Sound the horn on your vehicle to warn the perestrians", "slow down to 30kmh",
        'Stop and give way to pedestrians on any part of the crossing',2],

    4: ["Can you stop on a bus stop in a private motor vehicle?", 'Only between midnight and 6am", "Under no circumstances',
        "When dropping off passengers", 'Only if it is less than 5 minutes', "Under no circumstances", 2],

    5: ["What is the maximum speed you may drive if you have a 'space saver wheel' fitted? (km/h)", '70 km/h',
       "100 km/h so you do not hold up traffic", "80 km/h and if the wheel spacer displays a lower limit that applies",
       "90 km/h", "80 km/h and if the wheel spacer displays a lower limit that applies", 3],

    6: ["When following another vehicle on a dusty road, you should: ", 'Speed up to get passed',
        "Turn your vehicle's windscreen wipers on", "Stay back from the dust cloud", 'Turn your vehicles headlights on', "Stay back from the dust cloud", 3],

    7: ["What does the sign containing the letters 'LSZ' mean", 'Low safety zone', "Low stability zone", "Lone star zone", 'Limited speed zone', 'Limited speed zone',4],

    8: ["What speed are you allowed to pass a school bus that has stopped to let students get on or off?", '20 km/h', "30 km/h", "70 km/h", '10 km/h', '20 km/h',1],

    9: ["What is the maximum distance a load may extend in front of a car?", '2 meters forward of the front edge of the front seat', "4 meters forward of the front edge of the front seat",
         '3 meters forward of the front edge of the front seat',3],

    10: ["To avoid being blinded by the headlights of another vehicle coming towards you what should you do?", 'Look to the left of the road', "Look to the centre of the road",
          "Wear sunglasses that have sufficient strength", 'Look to the right side of the road', 'Look to the left of the road',1],
}
def randomiser():
    global qnum
    qnum = random.randint(1,10)
    if qnum not in asked:
        asked.append(qnum)
    elif qnum in asked:
        randomiser()


class Quizstarter:
    def __init__ (self,parent):
        background_colour="OldLace"
        #frame set up

        self.quiz_frame = Frame(parent, bg = background_colour, padx=40, pady=40)
        self.quiz_frame.grid()

        #Label widget for our heading
        self.heading_label = Label (self.quiz_frame, text = "NZ Road Rules", font=("Tw Cen MT", "18", "bold"), bg=background_colour)
        self.heading_label.grid(row=0, padx=20, pady=20)

        #Label for user name prompt
        self.user_label = Label ( self.quiz_frame, text="Please enter your name below", font=("Tw Cen Mt", "16"), bg=background_colour)
        self.user_label.grid(row=1, padx=20, pady=20)

        #users input is take by Entry widget
        self.entry_box=Entry(self.quiz_frame)
        self.entry_box.grid(row=2, padx=20, pady=20)
        
        #continue button
        self.continue_button = Button (self.quiz_frame, text="Continue", bg="pink", command=self.name_collection)
        self.continue_button.grid(row=3, stick=W, padx=20, pady=20)

    def name_collection(self):
        name = self.entry_box.get()
        names_list.append(name)
        print(names_list)
        self.quiz_frame.destroy()
        Quiz(root)

class Quiz: 
    
    def __init__ (self,parent):
        background_colour="OldLace"
        #frame set up
        self.quiz_frame = Frame(parent, bg = background_colour, padx=100, pady=100)
        self.quiz_frame.grid()
        randomiser()

        #Label widget for our heading
        self.question_label = Label (self.quiz_frame, text = questions_answers[qnum][0], font=("Tw Cen MT", "18", "bold"), bg=background_colour)
        self.question_label.grid(row=0, padx=10, pady=10)

        self.var1=IntVar()

        

        #radio button 1
        self.rb1 = Radiobutton(self.quiz_frame, text = questions_answers[qnum][1], font=("Helvetica", "12"), bg=background_colour,value=1,padx=10,pady=10,
                     variable=self.var1, background = background_colour)
        self.rb1.grid(row=1, sticky=W)

        # radio button 2
        self.rb2 = Radiobutton(self.quiz_frame, text = questions_answers[qnum][2], font=("Helvetica", "12"), bg=background_colour,value=2,padx=10,pady=10,
                     variable=self.var1, background = background_colour)
        self.rb2.grid(row=2, sticky=W)

        # radio button 3
        self.rb3 = Radiobutton(self.quiz_frame, text = questions_answers[qnum][3], font=("Helvetica", "12"), bg=background_colour,value=3,padx=10,pady=10,
                     variable=self.var1, background = background_colour)
        self.rb3.grid(row=2, sticky=W)
        
         # radio button 4
        self.rb4 = Radiobutton(self.quiz_frame, text = questions_answers[qnum][4], font=("Helvetica", "12"), bg=background_colour,value=4,padx=10,pady=10,
                     variable=self.var1, background = background_colour)
        self.rb4.grid(row=2, sticky=W)

        #confirm answer button
        self.confirm_button = Button(self.quiz_frame, text="Confirm", bg="yellow2", command=self.test_progress)
        self.confirm_button.grid(row=5)

        self.score_label=Label(self.quiz_frame, text="SCORE", font=("TW Cen MT", "16"), bg=background_colour,)
        self.score_label.grid(row=6, pady=1)

    def questions_setup(self):
        randomiser()
        self.var1.set(0)
        self.question_label.config(text=questions_answers[qnum][0])
        self.rb1.config(text=questions_answers[qnum][1])
        self.rb2.config(text=questions_answers[qnum][2])
        self.rb3.config(text=questions_answers[qnum][3])
        self.rb4.config(text=questions_answers[qnum][4])
    
    def test_progress(self):
        global score
       
    
        



#*********************************Starting point of program********************#
randomiser()
if __name__ == "__main__":
    root = Tk()
    root.title("NZ Road Rules Quiz")
    quizStarter_object = Quizstarter(root) #inisiation, making an instance of the Classquiz starter to create
    root.mainloop()#so the window dont close
