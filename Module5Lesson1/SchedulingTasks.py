import schedule
import time
from datetime import datetime


def display_time():
    now = datetime.now()
    current_time = now.strftime('%H:%M:%S')
    print('Current time: {}'.format(current_time))


def display_random_time():
    # Called randomly between every 10 and 100 seconds
    print('Randomly called - ', end='')
    display_time()


def daily():
    print('It\'s a new day')


def monday_time():
    print('It\'s 10:25 on Monday')


# Calls the display_time function every 10 seconds
schedule.every(10).seconds.do(display_time)
# Calls the display_random_time function randomly every
# 10 to 100 seconds.
schedule.every(10).to(100).seconds.do(display_random_time)
# Calls the daily method every day at 10:18
schedule.every().day.at('10:25').do(daily)
# Calls the thursday_time method on a Thursday at 10:19
schedule.every().monday.at('10:25').do(monday_time)

# The continue_loop and try / except blocks allow the
# script to be stopped gracefully (by stopping the script).
# Otherwise, the script would generate an error when stopped.

continue_loop = True

try:
    # Since continue_loop is set to True the loop will
    # continue indefinitely.  If anything goes wrong
    # the except statement sets continue_loop to False to
    # gracefully end the script execution.
    while continue_loop:
        # Tells the scheduler to run any outstanding
        # tasks.
        schedule.run_pending()
        # Makes the current thread sleep (pause) for 1
        # second.  This ensures that the run_pending()
        # method is only called once every second.
        time.sleep(1)
except:
    continue_loop = False
    print('Scheduler stopped')
