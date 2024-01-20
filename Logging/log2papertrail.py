import logging
from logging.handlers import SysLogHandler

PAPERTRAIL_HOST = 'logs6.papertrailapp.com'
PAPERTRAIL_PORT = 48767

def main() -> None:
    logger = logging.getLogger('alicemkoyun')
    logger.setLevel(logging.DEBUG)
    handler = SysLogHandler(address=(PAPERTRAIL_HOST, PAPERTRAIL_PORT))
    logger.addHandler(handler)

    logger.debug('This is a debug message.')

    
if __name__ == '__main__':
    main()
    
# We can see the message from events tab in papertrail.com