class Television:
    MIN_VOLUME: int = 0
    MAX_VOLUME: int = 2
    MIN_CHANNEL: int = 0
    MAX_CHANNEL: int = 3

    def __init__(self) -> None:
        """Initialize instance variables."""
        self._status: bool = False
        self._muted: bool = False
        self._volume: int = self.MIN_VOLUME
        self._channel: int = self.MIN_CHANNEL

    def power(self) -> None:
        """Turn the TV on and off by changing the value of the status variable."""
        self._status = not self._status

    def mute(self) -> None:
        """Mute and unmute the TV when it's on by changing the value of the muted variable."""
        self._muted = not self._muted

    def channel_up(self) -> None:
        """Increase the TV channel value when the TV is on."""
        if self._status:
            self._channel = (self._channel + 1) % (self.MAX_CHANNEL + 1)

    def channel_down(self) -> None:
        """Decrease the TV channel value when the TV is on."""
        if self._status:
            self._channel = (self._channel - 1) % (self.MAX_CHANNEL + 1)

    def volume_up(self) -> None:
        """Increase the TV volume when the TV is on."""
        if self._status:
            self._muted = False
            self._volume = min(self._volume + 1, self.MAX_VOLUME)

    def volume_down(self) -> None:
        """Decrease the TV volume when the TV is on."""
        if self._status:
            self._muted = False
            self._volume = max(self._volume - 1, self.MIN_VOLUME)

    def display_info(self) -> str:
        """Send the values of the TV object in the specified format.
        :return: A string containing information about the TV."""
        return f"Power = {self._status}, Channel = {self._channel}, Volume = {self._volume}"

    def __str__(self) -> str:
        """Override the string representation of the TV object.
        :return: tv status"""
        return self.display_info()