import sys, time
def spin():
    try:
        L="/-\\|"
        for q in range (100):
            time.sleep(0.1)
            sys.stdout.write("\r["+L[q % len(L)]+"]")
            sys.stdout.flush()
    except:
            exit()
spin()