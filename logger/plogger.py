import logging
import test_data

# https://docs.python.org/3/howto/logging.html#logging-howto

"""
    How to work with pythong logging - is the tutoral. Logging is a means of tracking events that happen when some software runs.
    The software’s developer adds logging calls to their code to indicate that certain events have occurred.  
"""

#logging.warning("Watch out- will print in the console....")
#logging.info("This message will not print out in the console!") # The INFO message doesn’t appear because the default level is WARNING. 


# logging.basicConfig(filename="example.log", encoding="utf-8", level=logging.DEBUG)
"""
logging.debug("This message should go to the log file")
logging.info("So should go this......")
logging.warning("This should also go in.....")
logging.error("All type of error should go in the file.. including non-ASCII stuff")
"""

# assuming loglevel is bound to the string value obtained from the
# command line argument. Convert to upper case to allow the user to
# specify --log=DEBUG or --log=debug | A faire example below if you want to confgiure the logger's log level from the console.

run_command = False
while run_command:
    loglevel = input("Please enter log level:eg. debug, info, warning, error")
    numeric_level = getattr(logging, loglevel.upper(), None)
    if not isinstance(numeric_level, int):
        raise ValueError('Invalid log level: %s' % loglevel)
    logging.basicConfig(filename="example.log", encoding="utf-8", level= numeric_level) # logging.DEBUG)

    logging.debug("This message should go to the log file")
    logging.info("So should go this......")
    logging.warning("This should also go in.....")
    logging.error("All type of error should go in the file.. including non-ASCII stuff")

    q = input("Enter q to quit...")
    if q == "q":
        break

## Logging from multiple modules


def main():
    logging.basicConfig(filename="example.log", encoding="utf-8", level=logging.DEBUG)
    logging.info("Logging started in logging module...")
    test_data.please_start_something_do_something() # Calling method from other module log stuff. 
    logging.info("The calling from test_data module has been compelted.... ")
    
    # Logging variable data¶

    logging.warning('%s before you %s', 'Look', 'leap!')
    logging.warning('%d this is not acceptable but this is %d', 100 , 60)

if __name__ == "__main__":
    main()