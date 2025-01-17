import logging
from colorama import Fore, Style

class ColorLogger:
    def __init__(self, name: str):
        self.logger = logging.getLogger(name)
        self.logger.setLevel(logging.DEBUG)

        # Create console handler and set level to debug
        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)

        # Create formatter
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

        # Add formatter to ch
        ch.setFormatter(formatter)

        # Add ch to logger
        self.logger.addHandler(ch)

    def debug(self, message: str):
        self.logger.debug(Fore.CYAN + message + Style.RESET_ALL)

    def info(self, message: str):
        self.logger.info(Fore.GREEN + message + Style.RESET_ALL)

    def warning(self, message: str):
        self.logger.warning(Fore.YELLOW + message + Style.RESET_ALL)

    def error(self, message: str):
        self.logger.error(Fore.RED + message + Style.RESET_ALL)

    def critical(self, message: str):
        self.logger.critical(Fore.MAGENTA + message + Style.RESET_ALL)