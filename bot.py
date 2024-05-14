import pyautogui
import webbrowser
import time
# URL to open



def connect():
    try:
        url = "https://mfs.sharevision.ca/default.aspx"

# Open URL in web browser
        webbrowser.open(url)
        time.sleep(2)
        try:
            username=pyautogui.locateCenterOnScreen(r"new_one/ss.png")
            if username:
                # pyautogui.click(username)
                pyautogui.write("Abhijeet.pabana")
                time.sleep(1)
                try:
                    password=pyautogui.locateCenterOnScreen(r"new_one/pasd.png")
                    if password:
                        pyautogui.click(password)
                        pyautogui.write("APMilieu123!")
                        time.sleep(2)
                        try:
                            login=pyautogui.locateCenterOnScreen(r"new_one/login.png")
                            if login:
                                pyautogui.click(login)
                        except pyautogui.ImageNotFoundException:
                            print("unable to login")
                except pyautogui.ImageNotFoundException:
                    print("Unable to write password")
        except pyautogui.ImageNotFoundException:
            print("Unable to write username")
    except Exception as e:
        print("unable to account")



# connect()



def Enter():
    url = "https://mfs.sharevision.ca/default.aspx"
    # Open URL in web browser
    webbrowser.open(url)
    time.sleep(10)
    try:
        program=pyautogui.locateCenterOnScreen(r"new_one/Pro.png")
        if program:
            pyautogui.click(program)
            try:
                time.sleep(10)
                i=0
                while i<10:
                # Scroll down by a certain amount (adjust the amount as needed)
                    # time.sleep(10)
                    pyautogui.keyDown('down')
                    i+=1  # Negative value for scrolling down
                time.sleep(20)
                partbutton=pyautogui.locateCenterOnScreen(r"new_one/partridgebutton.png")
                if partbutton:
                    pyautogui.click(partbutton)
                    time.sleep(20)
                    try:
                        grade=pyautogui.locateCenterOnScreen(r"new_one/check.png")
                        if grade:
                            pyautogui.click(grade)
                            time.sleep(30)
                            try:
                                print("hello")
                                enter=pyautogui.locateCenterOnScreen(r"new_one/enter3.png")
                                print("hii")
                                if enter:
                                    pyautogui.click(enter)
                                    time.sleep(20)
                                    try:
                                        yes_button=pyautogui.locateCenterOnScreen(r"new_one/yes.png")
                                        if yes_button:
                                            pyautogui.click(yes_button)
                                            time.sleep(1)
                                            try:
                                                text_button=pyautogui.locateCenterOnScreen(r"new_one/text.png")
                                                if text_button:
                                                    pyautogui.click(text_button)
                                                    time.sleep(1)
                                                    try:
                                                        textarea=pyautogui.locateCenterOnScreen(r"new_one/textarea.png")
                                                        if textarea:
                                                            pyautogui.click(textarea)
                                                            pyautogui.write("All Good!!")
                                                            time.sleep(1)
                                                            try:
                                                                again_yes=pyautogui.locateCenterOnScreen(r"new_one/yes.png")
                                                                if again_yes:
                                                                    pyautogui.click(again_yes)
                                                                    try:
                                                                        zeroone=pyautogui.locateCenterOnScreen(r"new_one/zero.png")
                                                                        if zeroone:
                                                                            pyautogui.click(zeroone)
                                                                            time.sleep(1)
                                                                            try:
                                                                                zerotwo=pyautogui.locateCenterOnScreen(r"new_one/zero.png")
                                                                                if zerotwo:
                                                                                    pyautogui.click(zerotwo)
                                                                                    time.sleep(1)
                                                                                    try:
                                                                                        i=0
                                                                                        while i<1:
                                                                                            pyautogui.keyDown("down")
                                                                                            i+=1
                                                                                        pyautogui.scroll(-200)   
                                                                                        time.sleep(5)    
                                                                                        selectbar=pyautogui.locateCenterOnScreen(r"new_one/selecy.png")
                                                                                        if selectbar:
                                                                                            pyautogui.click(selectbar)
                                                                                            pyautogui.write("p")
                                                                                            time.sleep(0.5)
                                                                                            for _ in range(11):
                                                                                                pyautogui.press('down')

                                                                                            time.sleep(5)
                                                                                            pyautogui.click()
                                                                                            time.sleep(1)
                                                                                            try:
                                                                                                submit=pyautogui.locateCenterOnScreen(r"new_one/submit2.png")
                                                                                                if submit:
                                                                                                    pyautogui.click(submit)
                                                                                            except pyautogui.ImageNotFoundException:
                                                                                                print("Bot Fail To submit")
                                                                                    except pyautogui.ImageNotFoundException:
                                                                                        print("Bot failed at end!")
                                                                            except pyautogui.ImageNotFoundException:
                                                                                print("unable to operate")
                                                                    except pyautogui.ImageNotFoundException:
                                                                        print("0 entering")
                                                            except pyautogui.ImageNotFoundException:
                                                                print("No second yess")
                                                    except pyautogui.ImageNotFoundException:
                                                        print("error while selecting")
                                            except pyautogui.ImageNotFoundException:
                                                print("error in processing")
                                    except pyautogui.ImageNotFoundException:
                                        print("error in detail filling")
                            except pyautogui.ImageNotFoundException:
                                print("Bot Error")
                    except pyautogui.ImageNotFoundException:
                        print("unable to print")
                    
                print("done")    
            except pyautogui.ImageNotFoundException:
                print("Unable to enter")
                                    
    except pyautogui.ImageNotFoundException:
        print("unable to Enter")




if __name__=="__main__":
    # connect()
    Enter()
