
def safe_input():
    while True:
        try:
            n = raw_input("Please enter an integer: ")
            n = int(n)
            break
        except ValueError:
            print("No valid integer! Please try again ...")
        except EOFError:
            print 'EOF error try again'
    print "Great, you successfully entered an integer!"