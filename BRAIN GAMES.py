import pyttsx3
def speak_and_text(text):
    engine = pyttsx3.init()
    engine.setProperty("rate", 100)
    def on_word(name, location, length):
        word = text[location:location + length]
        print(word, end=" ", flush=True)
    connection = engine.connect("started-word", on_word)
    engine.say(text)
    engine.runAndWait()
    print()
    engine.disconnect(connection)
    engine.stop()
name = input("Enter your name: ")


speak_and_text("Hello " + name )
speak_and_text(" lets play some fun brain games")

import pyfiglet
from colorama import Fore, Style, init
tryy = ["starwars"]
for fonts in tryy :
    print(Fore.GREEN+ pyfiglet.figlet_format("BRAIN GAMES", font=fonts))

speak_and_text("Choose the game you want to play")
speak_and_text("1. word scramble game")
speak_and_text("2. Maths quiz")
speak_and_text("3. Riddle game ")
speak_and_text("4. Code breaker game")


pp=int(input("Enter the number: "))
if pp==1 :
    speak_and_text(name +" welcome to the word scramble game")
    import pyfiglet
    from colorama import Fore, Style, init
    tryy = ["standard"]
    for fonts in tryy :
       print(Fore.MAGENTA + pyfiglet.figlet_format("word scramble game", font=fonts))


    speak_and_text("The letters of a word will be shuffled")
    speak_and_text("your task is to guess the orignal word")

    speak_and_text("so lets start")
    input("press enter to start the game")

    print("Shuffled word is : M A E N D R O O")
    print("Enter exit to stop the game or enter hint to view the hint")
    while True :
     do=input("enter the word :")
     if do.lower()=='doraemon' :
      print(" correct ! now move to next question....")
      print(" shuffled word is : Y I N B A R I")
      print("Enter exit to stop the game or enter hint to view the hint")
      import sys 
      while True :
        do=input("enter the word :")
        if do.lower()=='biryani' :
         print(" correct ! now move to next question....") 
         print("shuffled word is : N E G Y R A M")
         print("Enter exit to stop the game or enter hint to view the hint")
         while True :
          do=input("enter the word :")
          if do.lower()=='germany' :
           print(" correct ! now move to next question....")
           print(" shuffled word is : I D G M O A L R")
           print("Enter exit to stop the game or enter hint to view the hint")
           while True :
             do=input("enter the word :")
             if do.lower()=='marigold' :
              print(" correct ! now move to next question....")
              print(" shuffled word is : K I C T C R E")
              print("Enter exit to stop the game or enter hint to view the hint")
              while True :
                    do=input("enter the word :")
                    if do.lower()=='cricket' :
                     print(" correct ! thanks for playing")
                     sys.exit() 
                    elif do.lower()=='exit' :
                      print(" hope you enjoy the game bye")
                      sys.exit()
                    elif do.lower()=='hint':
                     print("a bat ball game")
                    else :
                     print("try again")
             elif do.lower()=='exit' :
              print(" hope you enjoy the game bye")
              sys.exit()
             elif do.lower()=='hint':
              print("a bright yellow flower")
             else :
              print("try again")
          elif do.lower()=='exit' :
           print(" hope you enjoy the game bye")
           sys.exit()
          elif do.lower()=='hint':
           print(" A COUNTRY IN EUROPE")
          else :
           print("try again")
        elif do.lower()=='exit' :
         print(" hope you enjoy the game bye")
         sys.exit()
        elif do.lower()=='hint':
         print("A FAMOUS SPICY RICE DISH")
        else :
         print("try again")
     elif do.lower()=='exit' :
      print(" hope you enjoy the game bye")
      sys.exit()
     elif do.lower()=='hint':
      print("A ROBOT CAT FROM FUTURE")
     else :
      print("try again")
elif pp==2 :
  import pyttsx3
  def speak_and_text(text):
    engine = pyttsx3.init()
    engine.setProperty("rate", 100)
    def on_word(name, location, length):
        word = text[location:location + length]
        print(word, end=" ", flush=True)
    connection = engine.connect("started-word", on_word)
    engine.say(text)
    engine.runAndWait()
    print()
    engine.disconnect(connection)
    engine.stop()
  speak_and_text(" welcome to the maths quiz game " + name)
  
  import pyfiglet
  from colorama import Fore, Style, init
  tryy = ["standard"]
  for fonts in tryy :
       print(Fore.BLUE + pyfiglet.figlet_format(" MATHS QUIZ GAME", font=fonts))
  speak_and_text("You will be given math questions with 4 options: a, b, c, d.")
  speak_and_text("Solve each question and type the correct option.") 

  input("press enter to start the game")
  ques = [ {"question" : "1. 2 power 9","options":["a.1024", "b.506", "c.256", "d.512"], "answer" : "d"} , {"question" : "2. If a>b and c<0, then which of the following statement is always true ?" ,"options":["a.ac=bc", "b.ac<bc", "c.ac>bc" ,"d.ac>bc"], "answer" : "b"}, {"question" : "3. Two numbers have HCF=6 and LCM=180. If one number is 30, find the other. ", "options":["a.36", "b.42", "c.24" ,"d.26"],"answer" : "a"}, {"question" : "4. Parameter of square = 40cm. then diagonal of square is ?","options":["a.7√2", "b.10", "c.10√2" ,"d.5√2"],"answer" : "c"}, { "question" : "6. Sides of a triangle are 3,4 and 8. true or false.", "options":["a.true", "b.false"], "answer":"b"}]

  for q in ques :
    print(q["question"])
    for option in q["options"] :
      print(option)

    while True :
     print("please answer using a,b,c or d only")
     ans=input("enter your answer: ")

     if ans==(q["answer"]):
      print("correct")
      break
     else :
       print("wrong")
       continue
    print("Thank you for playing")
elif pp==3  :
  import pyttsx3
  def speak_and_text(text):
    engine = pyttsx3.init()
    engine.setProperty("rate", 100)
    def on_word(name, location, length):
        word = text[location:location + length]
        print(word, end=" ", flush=True)
    connection = engine.connect("started-word", on_word)
    engine.say(text)
    engine.runAndWait()
    print()
    engine.disconnect(connection)
    engine.stop()
  speak_and_text(" welcome to the RIDDLE GAME " + name)
  import sys
  import pyfiglet
  from colorama import Fore, Style, init
  tryy = ["standard"]
  for fonts in tryy :
       print(Fore.YELLOW + pyfiglet.figlet_format(" RIDDLE GAME", font=fonts))
  speak_and_text (" Read the riddle carefully, think outside the box, and type your answer.")
  input("press enter to start the game")

  speak_and_text("I have many keys but i cant open a single lock")
  while True :
   ss=input("enter the answer: ") 
   if ss.lower()=="keyboard":
      print("correct ")
      speak_and_text("I follow you everywhere but disappear in the dard")
      while True :
        ss=input("enter the answer: ") 
        if ss.lower()=="shadow":
         print("correct ")
         speak_and_text("I have hands but i cannot clap")
         while True :
          ss=input("enter the answer: ") 
          if ss.lower()=="clock":
              print("correct ")
              speak_and_text("I open when the sky start crying")
              while True :
                  ss=input("enter the answer: ") 
                  if ss.lower()=="umbrella":
                   print("correct ")
                   speak_and_text("The more i work , the more i disappear")
                   while True :
                      ss=input("enter the answer: ") 
                      if ss.lower()=="candle":
                        print("correct ")
                        speak_and_text("I have blades but cannot cut anything")
                        while True :
                            ss=input("enter the answer: ") 
                            if ss.lower()=="fan":
                             print("correct ")
                             sys.exit()
                            elif ss.lower()=="exit" :
                              print("bye bye")
                              break
                            elif ss.lower()=="hint":
                             print("I give you air")
                            else :
                             print("try again")
                      elif ss.lower()=="exit" :
                        print("bye bye")
                        break
                      elif ss.lower()=="hint":
                        print("I cry wax tears when i burn")
                      else :
                        print("try again")
                  elif ss.lower()=="exit" :
                   print("bye bye")
                   break
                  elif ss.lower()=="hint":
                   print("I protect you from rain")
                  else :
                    print("try again")
          elif ss.lower()=="exit" :
              print("bye bye")
              break
          elif ss.lower()=="hint":
              print("I tell you the time")
          else :
              print("try again")
        elif ss.lower()=="exit" :
         print("bye bye")
         break
        elif ss.lower()=="hint":
         print("I have your shape, but no body")
        else :
         print("try again")
   elif ss.lower()=="exit" :
      print("bye bye")
      break
   elif ss.lower()=="hint":
      print("part of computer")
   else :
      print("try again")
        

elif pp==4  :
  import pyttsx3
  def speak_and_text(text):
    engine = pyttsx3.init()
    engine.setProperty("rate", 100)
    def on_word(name, location, length):
        word = text[location:location + length]
        print(word, end=" ", flush=True)
    connection = engine.connect("started-word", on_word)
    engine.say(text)
    engine.runAndWait()
    print()
    engine.disconnect(connection)
    engine.stop()
  speak_and_text(" welcome to the CODE BREAKER GAME " + name)
  import sys
  import pyfiglet
  from colorama import Fore, Style, init
  tryy = ["standard"]
  for fonts in tryy :
       print(Fore.MAGENTA + pyfiglet.figlet_format(" CODE BREAKER GAME", font=fonts))
  speak_and_text (" Read the clues carefully and try to guess the correct code...")
input("press enter to start the game")

speak_and_text("I am a Four digit number,If you double me,I become a five digit number,What is the smallest number I could be?")
while True :
   ss=input("enter the answer: ") 
   if ss.lower()== '5000':
     print("correct ")
     speak_and_text("The sum of my four digits is ten,I am the smallest four digit number with this property,starting with 1,Who am I?")
     while True :
      ss=input("enter the answer: ") 
      if ss.lower()== '1009':
       print("correct ")
       speak_and_text("I am a perfect square,a four digit number,My square root is a two digit number,The smallest I could be is...?")
       while True :
        ss=input("enter the answer: ") 
        if ss.lower()=='1024':
          print("correct ")
          speak_and_text("I am a four digit number,All four of my digits are different,I am the smallest four digit number possible with this rule,Who am I?")
          while True :
              ss=input("enter the answer: ") 
              if ss.lower()== '1023':
               print("correct ")
               speak_and_text("I am greater than 3 thousand but less than 4 thousand,My last digit is 2.My middle digits are consecutive numbers,My digits add up to 14,”Who am I?")
               while True :
                   ss=input("enter the answer: ") 
                   if ss.lower()== '3245':
                    print("correct ")
                    speak_and_text("I am a four digit number,I'm divisible by both 3 and 4,My digits sum to 9, I lie between 1 thousand and 12 hundred,Who am I?")
                    while True :
                        ss=input("enter the answer: ") 
                        if ss.lower()== '1116':
                         print("correct ")
                         sys.exit()
                        elif ss.lower()=="exit" :
                         print("bye bye")
                         break
                        else :
                         print("try again")
                   elif ss.lower()=="exit" :
                    print("bye bye")
                    break
                   else :
                    print("try again")
              elif ss.lower()=="exit" :
               print("bye bye")
               break
              else :
                print("try again")
        elif ss.lower()=="exit" :
          print("bye bye")
          break
        else :
          print("try again")
      elif ss.lower()=="exit" :
       print("bye bye")
       break
      else :
       print("try again")
   elif ss.lower()=="exit" :
    print("bye bye")
    break
   else :
     print("try again")