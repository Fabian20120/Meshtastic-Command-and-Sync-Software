from meshtastic import serial_interface

class NodeSync:
    """
    This class is the backend of the node synchronization.
    Aka the heart of the node synchronization.
    """
    def __init__(self, COM_PORT: str = None, debug: int = 0):
        """
        Initialize the NodeSync instance.
        This class is responsible for managing the node synchronization process.
        It uses the serial interface to communicate with the node.
        Args:
            COM_PORT (str): The communication port to use for the serial interface.
                If not set, it will detect automatically.
                (Can cause issues when using multiple devices at the same time.)
            debug (int): If set, enables debug mode useful for development and troubleshooting.
                Debug levels:
                    0: No debug information. (default)
                    1: Basic debug information printed to the console.
                    2: Advanced debug information printed to the console.
                    3: Verbose debug information printed to the console.
                Debug levels more detailed:
                    level 1 will print debug information to the console. Used for basic debugging.
                    level 2 will print more detailed debug information. Used for advanced debugging.
                    level 3 will print all debug information. Used for developer debugging.
                Caution:
                    Higher values will provide more and more detailed debug output.
                    Higher values may also make output harder to read and understand.
                Warning:
                    A debug level of 3 is known as verbose mode.
                    It will print all information including internal state changes and communication details.
                    And also print the current processing step with detailed information about the operation.
                    A debug level of 3 is not recommended and mostly used by the developer for bug fixing.
                    Its highly recommended to use debug level 1 or 2 for normal debugging.
                    A debug level of 3 may cause performance issues and can confuse you with too much information.
                    Only use debug level 3 if the developer asks you to do so or you are a highly experienced developer.
        """
        try:
            if COM_PORT is None:
                self.interface = serial_interface.SerialInterface()
            else:
                self.interface = serial_interface.SerialInterface(devPath=COM_PORT)
            self.debug = debug
            if self.debug:
                print(f"NodeSync initialized on {COM_PORT}.")
        except Exception as e:
            Warning(f"Error initializing NodeSync: {e}")
            return "NodeSync initialization failed."

class SoftSave:
    """
    Things like the interface will be saved here.
    It does only save for the current session.
    This is useful for debugging and testing purposes.
    It does not save the state permanently.
    """
    def __init__(self):
        self.interface = None
        self.debug = False

    def set_interface(self, interface):
        """
        Set the interface for the SoftSave instance.
        
        Args:
            interface: The serial interface to be set.
        """
        self.interface = interface
    
    def get_interface(self):
        """
        Get the current interface of the SoftSave instance.
        
        Returns:
            The current serial interface.
        If no interface is set, it returns None.
        """
        if self.interface is None:
            if self.debug:
                print("No interface set in SoftSave, returning None.")
            return None
        if self.debug:
            print(f"Returning interface: {self.interface}")
        return self.interface

def prepare_node_sync(COM_PORT: str = None, debug: bool = False):
    """
    Prepare the node for synchronization by setting up the serial interface.
    
    Args:
        COM_PORT (str): The communication port to use for the serial interface.
            If not set, it will detect automatically.
            (Can cause issues when using multiple devices at the same time.)

        debug (bool): If True, enables debug mode for the serial interface.
            Defaults to False.
            If True, debug information will be printed to the console.
    """
    global interface
    if COM_PORT is None:
        interface = serial_interface.SerialInterface()
    else:
        interface = serial_interface.SerialInterface(devPath=COM_PORT)
    
    print(f"Node sync prepared on {COM_PORT}.")