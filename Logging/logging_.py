'''
It is better to use logging on logging service for complex application for 
tracking, control over how logging happens, to debug easily and logs servers
gives us to visualise log, how long logs are going to be saved, search through
logs, backup logs. And we can share with other devs or live track the logs on
mobile or web app. One of the best company is Papertrail app.
'''

import logging

def main() -> None:
    logging.basicConfig(level=logging.DEBUG) # INFO # DEBUG
    
    # Hierarchy is below:
    # DEBUG logs every log because it is the lowest level
    # INFO logs info and below only, except debug
    # WARNING logs warning and below logs only
    
    logging.debug('This is a debug message.') # DEBUG 
    logging.info('This is an info message.') # INFO
    logging.warning('This is a warning message.') # WARNING
    logging.error('This is an error message.') # WARNING
    logging.critical('This is a critical message.') # WARNING


def main_formatted() -> None:
    logging.basicConfig(
        level=logging.DEBUG,
        format='%(asctime)s %(levelname)s %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S',
        filename='./Logging/basic.log' # This wont print the logs to terminal anymore. It will save the logs to a file into given path.
    )

    logging.debug('This is a debug message.') 
    logging.info('This is an info message.') 
    logging.warning('This is a warning message.') 
    logging.error('This is an error message.') 
    logging.critical('This is a critical message.') 




if __name__ == '__main__':
    #main()
    main_formatted()