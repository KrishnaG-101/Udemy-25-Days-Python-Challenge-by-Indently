# This file contains a version of custom print function

from typing import Any

def x_print(*values : Any, sep : str = " ", end : str = "\n", count_items : bool = False, include_types : bool = False, line_present : bool = False, format : str | None = None) -> None:
    """Customized print function with additional parameters to introduce a bit more functionality.

    Args:
        sep (str, optional): determines separator string between items. Defaults to " ".
        end (str, optional): determines end string for the print function. Defaults to "\\n".
        count_items (bool, optional): adds a count of items printed if set to True. Defaults to False.
        include_types (bool, optional): adds item and its type in a tuple for each item. Defaults to False.
        line_present (bool, optional): prints each item line by line with line number if set to True. Defaults to False.
        format (str | None, optional): determines format of string items given as argument. Defaults to None.

    Returns:
        None: The function directly prints values and does not return anything.
    """
    
    values_list : list[Any] = list(values)
    
    if format != None:
        if format == "lower":
            values_list = list(map(lambda item : item.lower() if isinstance(item, str) else item, values_list))
        elif format == "upper":
            values_list = list(map(lambda item : item.upper() if isinstance(item, str) else item, values_list))
        elif format == "title":
            values_list = list(map(lambda item : item.title() if isinstance(item, str) else item, values_list))
    
    if include_types:
        for index in range(len(values_list)):
            values_list[index] = (values_list[index], type(values_list[index]))
    
    if count_items:
        print(f"Count: {len(values_list)}")
    
    if line_present:
        for index in range(len(values_list)):
            print(f"{index + 1}.", values_list[index])
        return None
    
    print(*values_list, sep=sep, end=end)


x_print("hello world", 5, 7.7, True, "nano", "banana", ["hello", 1, 2.2, 5], sep=", ", end=".\n")
x_print("hello world", 5, 7.7, True, "nano", "banana", ["hello", 1, 2.2, 5], sep=", ", end=".\n", count_items=True, line_present=True)
x_print("hello world", 5, 7.7, True, "nano", "banana", ["hello", 1, 2.2, 5], sep=", ", end=".\n", count_items=True, include_types=True, line_present=False)
x_print("hello world", 5, 7.7, True, "nano", "banana", ["hello", 1, 2.2, 5], sep=", ", end=".\n", count_items=True, format="upper", line_present=True)

# Its maybe not a very good quality code right now, but it will be refactored and improved later.