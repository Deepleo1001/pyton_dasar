import sys,time
def ketik(text):
    for i in text + "\n":
        sys.stdout.write(i)
        sys.stdout.flush()
        time.sleep(0.1)
ketik ("WELCOME TO MY BLOG")