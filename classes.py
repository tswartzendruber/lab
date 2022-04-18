class Television:
    """
    A class representing the functionality of a TV remote
    """

    MIN_CHANNEL = 0     # Minimum TV channel
    MAX_CHANNEL = 3     # Maximum TV channel

    MIN_VOLUME = 0      # Minimum TV volume
    MAX_VOLUME = 2      # Maximum TV volume

    def __init__(self) -> None:
        """
        Constructor to create initial state of a TV remote object
        """
        self.__channel = Television.MIN_CHANNEL
        self.__volume = Television.MIN_VOLUME
        self.__on = False

    def power(self) -> None:
        """
        Method to turn on/off TV (pressing power button on TV remote)
        :return: TV's on/off status
        """
        if self.__on is False:
            self.__on = True
        else:
            self.__on = False

    def channel_up(self) -> None:
        """
        Method to change channel up
        :return: Higher TV channel
        """
        if self.__on is True:
            if self.__channel == Television.MAX_CHANNEL:
                self.__channel = Television.MIN_CHANNEL
            else:
                self.__channel += 1
        else:
            pass

    def channel_down(self) -> None:
        """
        Method to change channel down
        :return: Lower TV channel
        """
        if self.__on is True:
            if self.__channel == Television.MIN_CHANNEL:
                self.__channel = Television.MAX_CHANNEL
            else:
                self.__channel -= 1
        else:
            pass

    def volume_up(self) -> None:
        """
        Method to turn volume up
        :return: Higher TV volume
        """
        if self.__on is True:
            if self.__volume == Television.MAX_VOLUME:
                pass
            else:
                self.__volume += 1
        else:
            pass

    def volume_down(self) -> None:
        """
        Method to turn volume down
        :return: Lower TV volume
        """
        if self.__on is True:
            if self.__volume == Television.MIN_VOLUME:
                pass
            else:
                self.__volume -= 1
        else:
            pass

    def __str__(self) -> str:
        """
        Method to check TV status, channel, and volume
        :return: TV on/off status, TV channel, and TV volume
        """
        return f'TV status: Is on = {self.__on}, Channel = {self.__channel}, Volume = {self.__volume}'
