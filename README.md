# Gone Fishing Application

### Files:
- <span style="color: gray"> [__LongMessage.py/.exe:](__LongMessage.py) </span>
  - <span style="color: gray"> These .exe files are to expedite testing systems. This email is a test for a message that doesn't contain a subject but does contain a message. I made this one a long message so I could also test the spacing for the MDCards. To create the .exe do this: `pyintaller --onefile __LongMessage.py` </span>
- [Gone_toStore.py/.exe](Gone_toStore.py):
  - <span style="color: gray"> Similarly to __LongMessage.exe this one sends a message to mckaygonefishing@gmail.com but this one contains a subject - "Gone" and a body - "Going to the store." makes testing easier as well.  To create the .exe do this: `pyinstaller --onefile Gone_toStore.py`
- [Home_fromStore.py/.exe](Home_fromStore.py):
  - <span style="color: gray"> samuele as the files above but this one contains the subject "Home" and the body "Back Home". to create the .exe do this: `pyintaller --onefile Home_fromStore.py`
  </span>
- [gui.kv](gui.kv):
  - I learned a lot from creating this file. This is the system that Kivy uses to organize widget heirarchy and the creation of custom widgets. In this I create "<span style="color: green;">Frog</span>" which is the custom widget of which there are three in the window. This contains all other widgets such as the MDCards, MDLabels, MDBoxLayouts, MDRelativeLayouts, and FitImage. The sizing it strange with the secondary label which is the message but this is a problem for another time.
- [Main.py](Main.py):
  - This is the brains of the program. When the program is run this is what should be run first as everything else stems from here. This constructs the widgets and window, waits for all of the assets to load, starts the Kivy GUI, and then begins the second (third?) thread which repeatedly runs the login function in receive.py.
- [receive.py](receive.py):
  - Receive.py is wholy responsible for the interactions with the IMAPLIB system that reads emails to the mckaygonefishing@gmail.com address. When it receives an email with the subjects (not case sensitive):
    - "gone"
    - "home" or
    - ""
  - It will call a function within [handle.py](handle.py) which will be covered shortly. Along with a subject being added users are also allowed to send a message within the body of the email which will replace the class variable "message" for the "<span style="color: green;">Frog</span>" class.
- [handle.py](handle.py):
  - Handle.py's logic isn't very complicated as it is merely an intermediate path for other functions within the hierarchy. This was done to reduce clutter in the other files but also retain functions that were relevant in specific files. For example, when an email from samuel McKay is received, it is sent to handle.handle_message(), then to handle.handle_S(), then the class function <span style="color: green;">Frog</span>.setMessage(). Once it reaches <span style="color: green;">Frog</span>.setMessage it modifies self.message to reflect the body of the email on the GUI. After the message has been changed the class function <span style="color: green;">Frog</span>.flip_logic is called with a contextual parameter determining which animation should be performed. Flip_logic() finds the FitImage of the message sender and fades the image out, or in depending on the subject of the email.
- [Frog.png](Frog.png):
  - This is a png created by myself that shows a vector graphics rendering of a <span style="color: green;">Frog</span> which was inspired by the anime "Naruto Shippuden". In a series of episodes A character named "Jiriya" creates a system in which he and two other characters can signal to the other two if they are present or absent from their hideout by flipping cards which have their faces on them. The <span style="color: green;">Frog</span>.png was based on these cards.
- [Gone_fishing_diagram.jpg](Gone_fishing_diagram.jpg):
    - This is a pdf which describes the operational flow of the program and a standard functional procedure. It is similar to a control flow graph but with more actionable knowledge. This does not include the interaction with the Alexa skill or lambda function interaction.
- [request.py](request.py):
  - This is the file that handles the reception of data from the Alexa skill. It is constantly fetching from the s3 database to see if a new object with a name is present. if there is then dump it and call the necessary function, if there isn't then just dump it and continue waiting.



### Operation from the side of Alexa:
1. Start the GUI from main.py
2. Use wake word - Computer, Alexa, etc.
3. say "(open) flip frog"
4. say "flip {firstName}", "flip {firstName}'s card", etc. (there are many different utterances that should work for this.)
