from collections.abc import Callable

from pyscript import document
from pyodide.ffi.wrappers import add_event_listener
from pyodide.ffi import JsProxy


class Input:
    """
    This class represents an input device.
    """

    def __init__(self,
                 input_id: str,
                 event_type: str | None = None,
                 on_update: Callable[[JsProxy], None] | None = None) -> None:
        """
        This creates a new input object with the provided ID

        :param str input_id: the ID of the input element
        :param str event_type: the type of event to listen for (e.g., "click" or "input")
        :param Callable[[JsProxy], None] | None on_update: an optional callback function to be called when the input element is updated
        """
        self._input = document.getElementById(input_id)

        if event_type and on_update:
            add_event_listener(self._input, event_type, on_update)


class Slider(Input):
    """
    This class is used to create a slider that shows and updates its value.
    """

    def __init__(self,
                 input_id: str,
                 on_update: Callable[[JsProxy], None] | None = None) -> None:
        """
        Creates a new slider object with the provided IDs and updates the value
        when the slider is moved.

        :param str input_id: the ID of the slider input element
        :param str value_id: the ID of the value element
        :param Callable[[JsProxy], None] | None on_update: an optional callback function to be called when the slider is moved
        """
        super().__init__(input_id, "input", on_update)

    @property
    def value(self) -> int:
        """
        Returns the current value on the slider.
        
        :return: the current value of the slider
        :rtype: int
        """
        return int(self._input.value)
        
    @value.setter
    def value(self, value: int) -> None:
        """
        Sets the value of the slider.
        """
        self._input.value = value

    @property
    def min(self) -> int:
        """
        Returns the minimum slider value.
        
        :return: the minimum slider value
        :rtype: int
        """
        return self._input.min

    @min.setter
    def min(self, value: int) -> None:
        """
        Sets the minimum value of the slider.

        :param int value: the new minimum value
        """
        self._input.min = value

    @property
    def max(self) -> int:
        """
        Returns the maximum slider size.

        :return: the maximum slider size
        :rtype: int
        """
        return self._input.max

    @max.setter
    def max(self, value: int) -> None:
        """
        Sets the maximum value of the slider.

        :param int value: the new maximum value
        """
        self._input.max = value


class Numerical(Input):
    """
    This class creates a number input object that can be used to enter a number.
    """

    def __init__(self,
            input_id: str,
            on_update: Callable[[JsProxy], None] | None = None) -> None:
        super().__init__(input_id, "input", on_update)

    @property
    def value(self) -> int:
        """
        Returns the current value on the numerical.

        :return: the current value of the numerical
        :rtype: int
        """
        try:
            return int(self._input.value)
        except ValueError:
            return 1

    @value.setter
    def value(self, value: int) -> None:
        """
        Sets the value of the numerical.
        """
        self._input.value = value
        
    @property
    def min(self) -> int:
        """
        Returns the minimum numerical value.

        :return: the minimum numerical value
        :rtype: int
        """
        return self._input.min

    @min.setter
    def min(self, value: int) -> None:
        """
        Sets the minimum value of the numerical.

        :param int value: the new minimum value
        """
        self._input.min = value

    @property
    def max(self) -> int:
        """
        Returns the maximum numerical size.

        :return: the maximum numerical size
        :rtype: int
        """
        return self._input.max

    @max.setter
    def max(self, value: int) -> None:
        """
        Sets the maximum value of the numerical.

        :param int value: the new maximum value
        """
        self._input.max = value


class Dropdown(Input):
    """
    This class represents a dropdown menu that allows the user to select an option.
    """

    def __init__(self,
                 select_id: str,
                 on_update: Callable[[JsProxy], None] | None = None) -> None:
        """
        This creates a new dropdown object with the provided ID

        :param str select_id: the ID of the dropdown select element
        :param Callable[[JsProxy], None] | None on_update: an optional callback function to be called when the dropdown is updated
        """
        super().__init__(select_id, "change", on_update)

    @property
    def options(self) -> list[str]:
        """
        Returns a list of the options in the dropdown.

        :return: a list of the options in the dropdown
        :rtype: list[str]
        """
        return [option.value for option in self._input.options]

    @property
    def value(self) -> str:
        """
        Returns the current value of the dropdown.

        :return: the current value of the dropdown
        :rtype: str
        """
        return self._input.value


class Button(Input):
    """
    This class creates a button object that can be used to trigger an action.
    """

    def __init__(self,
                 button_id: str,
                 on_click: Callable[[JsProxy], None] | None = None) -> None:
        """
        This creates a new button object with the provided ID

        :param str button_id: the ID of the button element
        :param Callable[[JsProxy], None] | None on_click: an optional callback function to be called when the button is clicked
        """
        super().__init__(button_id, "click", on_click)
