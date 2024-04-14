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
                 value_id: str,
                 on_update: Callable[[JsProxy], None] | None = None) -> None:
        """
        Creates a new slider object with the provided IDs and updates the value
        when the slider is moved.

        :param str input_id: the ID of the slider input element
        :param str value_id: the ID of the value element
        :param Callable[[JsProxy], None] | None on_update: an optional callback function to be called when the slider is moved
        """
        super().__init__(input_id, "input", on_update)
        
        self._display = document.getElementById(value_id)
        self._update_display(None)
        add_event_listener(self._input, "input", self._update_display)

    @property
    def value(self) -> int:
        """
        Returns the current value on the slider.
        
        :return: the current value of the slider
        :rtype: int
        """
        return self._input.value

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
        pass

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
        pass

    def _update_display(self, event) -> None:
        """
        Updates the display value to the slider's value.
        """
        self._display.innerText = self.value


class Dropdown(Input):
    """
    This class represents a dropdown menu that allows the user to select an option.
    """

    def __init__(self,
                 select_id: str,
                 option_values: list[str],
                 on_update: Callable[[JsProxy], None] | None = None) -> None:
        """
        This creates a new dropdown object with the provided ID

        :param str select_id: the ID of the dropdown select element
        :param list[str] option_values: a list of possible options in the dropdown
        :param Callable[[JsProxy], None] | None on_update: an optional callback function to be called when the dropdown is updated
        """
        pass


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
        pass
