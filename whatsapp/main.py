import pyautogui as pt
from time import sleep
import pyperclip
import random

sleep(2)

#position1 = pt.locateOnScreen("smiley_clip.png", confidence=.6) #bez confidence ako slika ima najmanju razliku u pixelima nece je prepoznati, u ovom slucaju ako se poklapa 60% bice prepoznata
#x = position1[0]
#y = position1[1]

# Dobija poruku
def get_message():
    global x, y, position

    position = pt.locateOnScreen("a_message.png", confidence=.6)
    x = position[0]
    y = position[1]
    pt.moveTo(x, y, duration=.5) #duration uglavnom na mac sistemima
    pt.moveTo(x, y - 40, duration=.5)
    pt.tripleClick()
    pt.rightClick()
    pt.moveRel(12, 15)
    pt.click()
    pt.moveRel(-12, -15)
    position = pt.locateOnScreen("reply_menu.png", confidence=.9)
    x = position[0]
    y = position[1]
    pt.moveTo(x, y, duration=.5)
    pt.click()
    pt.moveTo(x - 1, y, duration=.5) #for some reason it fixes the problem????
    position = pt.locateOnScreen("odgovor.png", confidence=.7)
    x = position[0]
    y = position[1]
    pt.moveTo(x, y, duration=.5)
    pt.click()
    whatsapp_message = pyperclip.paste()
    print("Message received: " + whatsapp_message)

    return whatsapp_message

# Posts
def post_response(message):
    #global x, y

    #position = pt.locateOnScreen("smiley_clip.png", confidence=.6)
   # x = position[0]
   # y = position[1]
   # pt.moveTo(x + 200, y + 20, duration=.5)
   # pt.click()
    pt.typewrite(message, interval=.01)

    pt.typewrite("\n", interval=.01)



# Processes response
def process_response(message):
    random_no = random.randrange(3)

    if "?" in str(message).lower():
        return "Don't ask me any questions at the moment!"

    else:
        if random_no == 0:
            return "That's cool!"
        elif random_no == 1:
            return "Automated response. Do not reply!"
        else:
            return "I want to eat something."


# Check for new messages
def check_for_new_messages():
   # pt.moveTo(x+50, y-35, duration=.5)

    while True:
        # Continuously checks for green dot and new messagesd
        try:
            position = pt.locateOnScreen("green.png", confidence=.7, tolerance=10)

            if position is not None:
                pt.moveTo(position)
                pt.moveRel(-100,0)
                pt.click()
                sleep(.5)
                processed_message = process_response(get_message())
                post_response(processed_message)
            else:
                print("no new messages...")

        except(Exception):
            print("no new other users with new messages located")




check_for_new_messages()
#processed_message = process_response(get_message())
#post_response(processed_message)