print('''                                                                                                                   
               AAA                    NNNNNNNN        NNNNNNNN             GGGGGGGGGGGGG     HHHHHHHHH     HHHHHHHHH
              A:::A                   N:::::::N       N::::::N          GGG::::::::::::G     H:::::::H     H:::::::H
             A:::::A                  N::::::::N      N::::::N        GG:::::::::::::::G     H:::::::H     H:::::::H
            A:::::::A                 N:::::::::N     N::::::N       G:::::GGGGGGGG::::G     HH::::::H     H::::::HH
           A:::::::::A                N::::::::::N    N::::::N      G:::::G       GGGGGG       H:::::H     H:::::H  
          A:::::A:::::A               N:::::::::::N   N::::::N     G:::::G                     H:::::H     H:::::H  
         A:::::A A:::::A              N:::::::N::::N  N::::::N     G:::::G                     H::::::HHHHH::::::H  
        A:::::A   A:::::A             N::::::N N::::N N::::::N     G:::::G    GGGGGGGGGG       H:::::::::::::::::H  
       A:::::A     A:::::A            N::::::N  N::::N:::::::N     G:::::G    G::::::::G       H:::::::::::::::::H  
      A:::::AAAAAAAAA:::::A           N::::::N   N:::::::::::N     G:::::G    GGGGG::::G       H::::::HHHHH::::::H  
     A:::::::::::::::::::::A          N::::::N    N::::::::::N     G:::::G        G::::G       H:::::H     H:::::H  
    A:::::AAAAAAAAAAAAA:::::A         N::::::N     N:::::::::N      G:::::G       G::::G       H:::::H     H:::::H  
   A:::::A             A:::::A        N::::::N      N::::::::N       G:::::GGGGGGGG::::G     HH::::::H     H::::::HH
  A:::::A               A:::::A       N::::::N       N:::::::N        GG:::::::::::::::G     H:::::::H     H:::::::H
 A:::::A                 A:::::A      N::::::N        N::::::N          GGG::::::GGG:::G     H:::::::H     H:::::::H
AAAAAAA                   AAAAAAA     NNNNNNNN         NNNNNNN             GGGGGG   GGGG     HHHHHHHHH     HHHHHHHHH
                                                                                                                    ''')
import cv2
import pywhatkit as msg
import datetime
import handtracking as htm
from time import strftime
import math




cap = cv2.VideoCapture(1)
cap.set(3,1080)
cap.set(4,720)

detect = htm.handDetector(detectionCon=0.7)

tipIds=[4, 8, 12, 16, 20]

while True:
    success , img = cap.read()
    img = cv2.flip(img,1)
    img = detect.findHands(img)
    
    

    lmList = detect.findPosition(img,draw = False)
    #print(lmList)

    
    hour=int(strftime("%H"))
    min= int(strftime("%M")) + 1
       
    
    

    if len(lmList) != 0:
        x1, y1 = lmList[4][1], lmList[4][2]
        x2, y2 = lmList[8][1], lmList[8][2]
        x3, y3 = lmList[12][1],lmList[12][2]
        x4, y4 = lmList[16][1],lmList[16][2]
        x5, y5 = lmList[20][1],lmList[20][2]

        l1 = math.hypot(x2 - x1, y2 - y1)
        l2 = math.hypot(x3 - x1, y3 - y1)
        l3 = math.hypot(x4 - x1, y4 - y1)
        l4 = math.hypot(x5 - x1, y5 - y1)

        cx, cy = (x1 + x3) // 2, (y1 + y3) // 2


        cv2.circle(img, (x1, y1), 15, (255, 0, 255), cv2.FILLED)
        cv2.circle(img, (x3, y3), 15, (255, 0, 255), cv2.FILLED)
        cv2.circle(img, (cx, cy), 15, (255, 0, 255), cv2.FILLED)
        
        

        if l1< 50:

                        
                        print("hello")
                        #msg.sendwhatmsg("+91 9026353650" , "hello" ,hour,min, 10 , )
                        


        elif l2< 50:

                        
                        print("I want to talk")
                        #msg.sendwhatmsg("+91 6394751253" , "I want to talk" ,hour,min, 10 , tab_close=True)
                        

        elif l3< 50:


                       print("I am thirsty")
                       #msg.sendwhatmsg("+91 6394751253" , "I am thirsty" ,hour,min, 7 , tab_close=True)
                        


        elif l4< 50:

                        
                        print("I am hungry")
                        #msg.sendwhatmsg("+91 6394751253" , "I am hungry" ,hour,min, 7 , tab_close=True)

       
        
    
        

    cv2.imshow("A N G H",img)
    cv2.waitKey(1)
    

'''                                                                                                                                                           
                                                                                                                                                           
TTTTTTTTTTTTTTTTTTTTTTThhhhhhh                                                kkkkkkkk                                                                     
T:::::::::::::::::::::Th:::::h                                                k::::::k                                                                     
T:::::::::::::::::::::Th:::::h                                                k::::::k                                                                     
T:::::TT:::::::TT:::::Th:::::h                                                k::::::k                                                                     
TTTTTT  T:::::T  TTTTTT h::::h hhhhh         aaaaaaaaaaaaa  nnnn  nnnnnnnn     k:::::k    kkkkkkkyyyyyyy           yyyyyyy ooooooooooo   uuuuuu    uuuuuu  
        T:::::T         h::::hh:::::hhh      a::::::::::::a n:::nn::::::::nn   k:::::k   k:::::k  y:::::y         y:::::yoo:::::::::::oo u::::u    u::::u  
        T:::::T         h::::::::::::::hh    aaaaaaaaa:::::an::::::::::::::nn  k:::::k  k:::::k    y:::::y       y:::::yo:::::::::::::::ou::::u    u::::u  
        T:::::T         h:::::::hhh::::::h            a::::ann:::::::::::::::n k:::::k k:::::k      y:::::y     y:::::y o:::::ooooo:::::ou::::u    u::::u  
        T:::::T         h::::::h   h::::::h    aaaaaaa:::::a  n:::::nnnn:::::n k::::::k:::::k        y:::::y   y:::::y  o::::o     o::::ou::::u    u::::u  
        T:::::T         h:::::h     h:::::h  aa::::::::::::a  n::::n    n::::n k:::::::::::k          y:::::y y:::::y   o::::o     o::::ou::::u    u::::u  
        T:::::T         h:::::h     h:::::h a::::aaaa::::::a  n::::n    n::::n k:::::::::::k           y:::::y:::::y    o::::o     o::::ou::::u    u::::u  
        T:::::T         h:::::h     h:::::ha::::a    a:::::a  n::::n    n::::n k::::::k:::::k           y:::::::::y     o::::o     o::::ou:::::uuuu:::::u  
      TT:::::::TT       h:::::h     h:::::ha::::a    a:::::a  n::::n    n::::nk::::::k k:::::k           y:::::::y      o:::::ooooo:::::ou:::::::::::::::uu
      T:::::::::T       h:::::h     h:::::ha:::::aaaa::::::a  n::::n    n::::nk::::::k  k:::::k           y:::::y       o:::::::::::::::o u:::::::::::::::u
      T:::::::::T       h:::::h     h:::::h a::::::::::aa:::a n::::n    n::::nk::::::k   k:::::k         y:::::y         oo:::::::::::oo   uu::::::::uu:::u
      TTTTTTTTTTT       hhhhhhh     hhhhhhh  aaaaaaaaaa  aaaa nnnnnn    nnnnnnkkkkkkkk    kkkkkkk       y:::::y            ooooooooooo       uuuuuuuu  uuuu
                                                                                                       y:::::y                                             
                                                                                                      y:::::y                                              
                                                                                                     y:::::y                                               
                                                                                                    y:::::y                                                
                                                                                                   yyyyyyy                                                 
                                                                                                                                                           
                                                                                                                                                           

'''
        
       
