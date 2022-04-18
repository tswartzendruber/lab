class Television:
    MIN_CHANNEL = 0     # Minimum TV channel option
    MAX_CHANNEL = 3     # Maximum TV channel

    MIN_VOLUME = 0      # Minimum TV volume
    MAX_VOLUME = 2      # Maximum TV volume

    def __init__(self):
        self.__channel = Television.MIN_CHANNEL
        self.__volume = Television.MIN_VOLUME
        self.__on = False

    def power(self):
        if self.__on is False:
            self.__on = True
        else:
            self.__on = False

    def channel_up(self):
        if self.__on is True:
            if self.__channel == Television.MAX_CHANNEL:
                self.__channel = Television.MIN_CHANNEL
            else:
                self.__channel += 1
        else:
            pass

    def channel_down(self):
        if self.__on is True:
            if self.__channel == Television.MIN_CHANNEL:
                self.__channel = Television.MAX_CHANNEL
            else:
                self.__channel -= 1
        else:
            pass

    def volume_up(self):
        if self.__on is True:
            if self.__volume == Television.MAX_VOLUME:
                pass
            else:
                self.__volume += 1
        else:
            pass

    def volume_down(self):
        if self.__on is True:
            if self.__volume == Television.MIN_VOLUME:
                pass
            else:
                self.__volume -= 1
        else:
            pass

    def __str__(self):
        return f'TV status: Is on = {self.__on}, Channel = {self.__channel}, Volume = {self.__volume}'
