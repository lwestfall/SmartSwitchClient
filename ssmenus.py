import curses

def selectmenu(title,options):
    screen = curses.initscr()
    curses.start_color()
    curses.init_pair(1,curses.COLOR_RED, curses.COLOR_WHITE)
    screen.keypad(1)
    pos = 1
    x = None
    
    while x != ord('\n'):
        # Gotta reset the screen from the root or lose the border, window, etc.
        screen.clear()
        screen.border(0)
        screen.addstr(2,2, title, curses.A_BOLD + curses.COLOR_GREEN)
        screen.addstr(4,2, "Select a command:", curses.A_BOLD)
        
        for i in range(0,len(options)):
            if i == pos - 1:
                h = curses.color_pair(1)
            else:
                h = curses.A_NORMAL
            screen.addstr(i+6,4, options[i],h)

        screen.refresh()
        x = screen.getch()
        ## Is 'x' 1-5 or arrow up, arrow down?
        #if x == ord('1'):
        #    pos = 1
        #elif x == ord('2'):
        #    pos = 2
        #elif x == ord('3'):
        #    pos = 3
        #elif x == ord('4'):
        #    pos = 4
        #elif x == ord('5'):
        #    pos = 5
        # It was a pain in the ass trying to get the arrows working.
        if x in range(ord('1'), ord(chr(len(options)))):
            pos = x
        elif x == 258:
            if pos < len(options):
                pos += 1
            else:
                pos = 1
        # Since the curses.KEY_* did not work, I used the raw return value.
        elif x == 259:
            if pos > 1:
                pos += -1
            else:
                pos = len(options)
        elif x != ord('\n'):
            curses.flash()
            # show_error() is my custom function for displaying a message:
            # show_error(str:message, int:line#, int:seconds_to_display)
            #show_error('Invalid Key',11,1)
   
    screen.clear()
    curses.endwin()
    return pos

def inputmenu(title, prompt):
    screen = curses.initscr()
    curses.start_color()
    curses.init_pair(1,curses.COLOR_RED, curses.COLOR_WHITE)

    screen.clear()
    screen.border(0)
    screen.addstr(2,2, title, curses.A_BOLD + curses.COLOR_GREEN)
    screen.addstr(4,2, prompt, curses.A_BOLD)

    screen.refresh()
    x = screen.getstr()
    return x