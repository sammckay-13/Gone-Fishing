
##I'm handling the if statment to determine who it is on this side because it'll be easier to read. For safety reasons I'm obfuscating the emails for my parents
def handle_message(sender, subject, content, army): 
    if sender == "Jane Doe <janedoe@gmail.com>":
        handle_J(subject, content, army[1])
    if sender == "John Doe <johndoe@gmail.com>":
        handle_P(subject, content, army[2])
    elif sender == 'Sam McKay <mckaypable@gmail.com':

        handle_S(subject, content, army[0])
    return
        
###Handling and flipping cards based on person sending message
def handle_J(subject, content, J):
    J.setMessage(content)
    if subject == "Gone":
        ##Gone == 1
        J.flip_logic(1, "gone")
    elif subject == "Home":
        ##Home == 0
        J.flip_logic(1, "home")
    else:
        J.flip_logic(1)
    

def handle_P(subject, content, P):
    P.setMessage(content)
    if subject == "gone":
    ##Gone == 1
        P.flip_logic(2, "gone")
    elif subject == "home":
        ##Home == 0
        P.flip_logic(2, "home")
    else:
        P.flip_logic(2)
        
        
        
def handle_S(subject, content, Hokage):
    print("subject")

    print(subject)
    if subject == "gone":     
        ##Gone == 1
        Hokage.flip_logic(0, "gone")
    elif subject == "home":
        ##Home == 0
        Hokage.flip_logic(0, "home")
    else:
        Hokage.flip_logic(0)    