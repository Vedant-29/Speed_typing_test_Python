# Code to calculate accuracy , words per minute and time taken to type a given sentence.


# Importing all the required libraries:
import pygame
import pandas as pd
from pygame.locals import *
import sys
import time
import random

# pandas series containing sample sentences   
sentences=pd.Series(["Code is like humor. When you have to explain it, it's bad.",
                     "In order to be irreplaceable, one must always be different",
                     "Before software can be reusable it first has to be usable.",
                     "You cannot make an omlette without breaking a few eggs.",
                     "They that will not work in summer must hunger in winter.",
                     "If the blind lead the blind, both shall fall into the ditch.",
                     "Custom is the plague of wise men and the idol of fools.",
                     "Those who live in glass houses should not throw stones.",
                     "Coding is today's language of creativity and expression",
                     "Programming is a form of logic based creative expression.",
                     "It always seems impossible until it is finally done.",
                     "If you want the rainbow, you must put up with the rain.",
                     "Failure is not the opposite of success but is a part of it.",
                     "Life has no limitations besides the ones you make.",
                     "Strive not to be a success but rather to be of value.",
                     "We realise the importance of our voices once we are silenced.",
                     "A problem well stated is a problem half solved.",
                     "Dig at the roots instead of just hacking at the leaves.",
                     "Computers have lots of memory but no imagination.",
                     "In any situation, there is a sacred solution.",
                     "A journey of a thousand miles begins with a single step.",
                     "An ounce of prevention is worth a pound of cure.",
                     "Cowards may die many times before their death.",
                     "Do unto others as you would have them do to you.",
                     "He who fights and runs away, may live to fight another day.",
                     "In the kingdom of the blind the one eyed man is king.",
                     "Those who do not learn from history are doomed to repeat it.",
                     "You never really learn much from hearing yourself speak.",
                     "Never put off until tomorrow what you can do today.",
                     "Better to be poor and healthy rather than rich and sick.",
                     "Don't kill the goose that lays the golden eggs.",
                     "Lightning never strikes twice in the same place.",
                     "You can lead a horse to water but you can't make him drink.",
                     "You can catch more flies with honey than with vinegar.",
                     "You show me the man and I'll show you the rule.",
                     "Better to light a candle than to curse the darkness.",
                     "The grass is always greener on the other side of the fence.",
                     "Don't shut the stable door after the horse has bolted.",
                     "Every man for himself, and the Devil take the hindmost.",
                     "Everyone wants to go to heaven but nobody wants to die.",
                     "If God had meant us to fly he'd have given us wings.",
                     "It's the empty can that makes the most noise.",
                     "Keep your friends close and your enemies closer.",
                     "March comes in like a lion, and goes out like a lamb.",
                     "No one can make you feel inferior without your consent.",
                     "One half of the world does not know how the other half lives.",
                     "Opportunity never knocks twice at any man's door.",
                     "A place for everything and everything in its place.",
                     "There are none so blind as those, that will not see.",
                     "There's many a good tune played on an old fiddle",
                     "Thank you for finishing the last slice of pizza!" , 
                     "Al went to the animal shelter and got four cats!",
                     "What should you do if you , find a big spider on your bed?",
                     "Tom stood alone under a big clock in the deserted train station.",
                     "You are so disgraceful I can't even believe it!",
                     "Who wrote the famous book entitled “Treasure Island”?",
                     "How big a chance is there that Tom will come?",
                     "What do you want to do for your next birthday?",
                     "The girl wore her hair in two braids, tied with two blue bows.",
                     "What should you do if you find a big spider on your bed?",
                     "According to the papers, there was a big fire in the town.",
                     "The road to hell is paved with good intentions.",
                     "I brought you into this world so I can take you out!",
                     "What did you dress up last time and what do you want to be this year?",
                     "That would be a really big surprise, wouldn't it?",
                     "Al went to the animal shelter and got four cats!",
                     "My shoes are blue with yellow stripes and green stars on the front.",
                     "I can't tell you who's on the list because I haven't seen the list yet.",
                     "My favorite part about dancing is listening to the music.",
                     "Al went to the animal shelter and got four cats!",
                     "That’s too bad you should have thought of that before!",
                     "It was in the 1920s that a big earthquake destroyed Tokyo.",
                     "Why is everybody making such a big deal about this?",
                     "He's in debt to the bank because he bought that big house.",
                     "I fell in the mud when I was walking home from school today.",
                     "You are so disgraceful I can't even believe it!",
                     "I brought you into this world so I can take you out!",
                     "How big a chance is there that Tom will come?",
                     "A big bomb fell, and a great many people lost their lives.",
                     "Al went to the animal shelter and got four cats!",
                     "That’s too bad you should have thought of that before!",
                     "Is there a big market for this kind of thing these days?"])

print("Press 'TAB' to start typing.")

class Game:
   # defining functions
    def __init__(self):
        self.w=900
        self.h=500
        self.start=True
        self.active = False
        self.input_text=""
        self.word = ""
        self.time_start = 0
        self.total_time = 0
        self.accuracy = "0%"
        self.results = "Time:0 Accuracy:0 % Wpm:0 "
        self.wpm = 0
        self.end = False
        # Main Heading color of second page:
        self.HEAD_C = (0,0,0)
        # Color of the sentences in the second page:
        self.TEXT_C = (100,100,100)
        # Color of the dashboard obtained:
        self.RESULT_C = (0,0,0)
        
       
        pygame.init()
        # Home Page image
        self.open_img = pygame.image.load('C:/Users/agarw/Desktop/Speed_typing_test_Python/Program files/Home_page.png')
        self.open_img = pygame.transform.scale(self.open_img, (self.w,self.h))

        # Background Image
        self.bg = pygame.image.load('C:/Users/agarw/Desktop/Speed_typing_test_Python/Program files/Background_page.png')
        self.bg = pygame.transform.scale(self.bg,(900 , 500))

        # Caption heading
        self.screen = pygame.display.set_mode((self.w,self.h))
       
        
    def draw_text(self, screen, msg, y ,fsize, color):
        font = pygame.font.SysFont('Montserrat-SemiBold', 32)
        text = font.render(msg, 0.1,color)
        text_rect = text.get_rect(center=(self.w/2, y))
        screen.blit(text, text_rect)
        pygame.display.update()     
        

    def get_sentence(self):
        sentence = random.choice(sentences)
        return sentence

    def show_results(self, screen):
        if(not self.end):
            # Calculating time:
            self.total_time = time.time() - self.time_start
            # Current time - time when input started.
               
            #Calculate accuracy:
            self.inpwords=self.input_text
            # Obtaining input and system generated sentences as list of words:
            self.inplist=(self.inpwords.split(" "))
            self.wordlist=(self.word.split(" "))

            # Sorting alphabetically.
            self.inplist.sort()
            self.wordlist.sort()
            self.negacc=0

            # If input sentence completely matches system generated sentence:
            if self.inplist==self.wordlist:     
                self.accuracy = (len(self.word)-self.negacc)/len(self.word)*100
            # If input sentence doesnt match system generated sentence:
            else:
                self.inpflaw = ""
                self.qflaw = ""
                self.correct=[]
                self.wrong=[]
                self.inaccurate=""
                self.flawlist=[]
                self.inpflawlist = []
                self.qflawlist = []

            # Splitting incorrect words into a list of letters:

                for item in self.inplist:
                    if item not in self.wordlist:
                        self.inpflaw+=item
                        
                for item in self.wordlist:
                    if item not in self.inplist:
                        self.qflaw+=item
                        
                self.inpflawlist=list(self.inpflaw)
                self.qflawlist=list(self.qflaw)
                
               # List containing all letters of incorrect words:
                self.flawlist=self.qflawlist+self.inpflawlist
                for i in (self.flawlist):
                    # Extracting all incorrect letters:
                    if i not in self.wrong:
                        if self.flawlist.count(i)%2==0:
                            for x in range (self.flawlist.count(i)//2):
                                pass
                        else:
                            for x in range ((self.flawlist.count(i)%2)):
                                self.wrong.append(i)
                                
                if len(self.word)>len(self.inpwords):
                    self.lendiff=len(self.word)-len(self.inpwords)
                elif len(self.word)<len(self.inpwords):
                    self.lendiff=len(self.inpwords)-len(self.word)
                else:
                    self.lendiff=0
                self.accuracycount = ((len(self.word)-self.lendiff-len(self.wrong))/len(self.word))*100
                if self.accuracycount<0:
                    self.accuracy=0
                else:
                    self.accuracy=self.accuracycount
                
            
            
            #Calculate words per minute
            self.wpm = len(self.input_text)*60/(5*self.total_time)
            self.end = True
            print(self.total_time)
                
            self.results = "Time:"+str(round(self.total_time)) +" secs   Accuracy:"+ str(round(self.accuracy)) + "%" + "   Wpm: " + str(round(self.wpm))

            # draw icon image
            self.time_img = pygame.image.load('C:/Users/agarw/Desktop/Speed_typing_test_Python/Program files/Reset_icon.png')
            self.time_img = pygame.transform.scale(self.time_img, (150,150))
            #screen.blit(self.time_img, (80,320))
            screen.blit(self.time_img, (self.w/2-75,self.h-140))
            self.draw_text(screen,"", self.h - 70, 26, (100,100,100))
            
            print(self.results)
            pygame.display.update()

    def start_game(self):
        self.screen.blit(self.open_img, (0,0))

        pygame.display.update()
        time.sleep(1)
        
        self.start=False
        self.end = False

        self.input_text=""
        self.word = ""
        self.time_start = 0
        self.total_time = 0
        self.wpm = 0

        # Get random sentence 
        self.word = self.get_sentence()
        if (not self.word): self.reset_game()
        #drawing heading
        self.screen.fill((0,0,0))
        self.screen.blit(self.bg,(0,0))
        # draw the rectangle for input box
        pygame.draw.rect(self.screen,(255,192,25), (75,250,750,50), 1)

        # draw the sentence string
        self.draw_text(self.screen, self.word,200, 28,self.TEXT_C)
        
        pygame.display.update()

    def run(self):
        self.start_game()
    
       
        self.running=True
        while(self.running):
            self.screen.fill((255,255,255), (75,250,750,50))
            pygame.draw.rect(self.screen,self.HEAD_C, (75,250,750,50), 2)
            # update the text of user input
            self.draw_text(self.screen, self.input_text, 274, 26,(0,0,0))
            for event in pygame.event.get():
                if event.type == QUIT:
                    self.running = False
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONUP:
                    x,y = pygame.mouse.get_pos()
                    # position of input box
                    if(x>=75 and x<=750 and y>=250 and y<=300):
                        self.active = True
                        self.input_text = ""
                        self.time_start = time.time()
                     # position of reset box
                    if(x>=310 and x<=510 and y>=390 and self.end):
                        self.start_game()
                        x,y = pygame.mouse.get_pos()
         
                        
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_TAB:
                        self.active = True
                        self.input_text = ""
                        self.time_start = time.time()
                    if self.active and not self.end:
                        if event.key == pygame.K_RETURN:
                            print(self.input_text)
                            self.show_results(self.screen)
                            print(self.results)
                            self.draw_text(self.screen, self.results,350, 28, self.RESULT_C)  
                            self.end = True
                            pygame.display.update()
                            
                        elif event.key == pygame.K_BACKSPACE:
                            self.input_text = self.input_text[:-1]
                            pygame.display.update()
                
                        else:
                            self.input_text += event.unicode
                            pygame.display.update()
Game().run()
