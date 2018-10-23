import curses
from time import sleep

from pyfiglet import figlet_format

def main():
    # init curses
    stdscr = curses.initscr()
    curses.noecho()
    curses.cbreak()
    stdscr.keypad(True)

    happy_1024 = 'Happy 1024!'
    for x in range(len(happy_1024)):
        greeting = happy_1024[:x + 1]
        greeting_figlet = figlet_format(greeting, font='big')
        stdscr.addstr(0, 0, greeting_figlet)
        stdscr.refresh()
        sleep(0.5)
    sleep(3)

    # exit curses
    curses.nocbreak()
    stdscr.keypad(False)
    curses.echo()
    curses.endwin()

if __name__ == '__main__':
    main()