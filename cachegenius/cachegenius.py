import inspect
import os
import pickle
import time
from typing import Callable, List, Any
from types import ModuleType

import numpy as np


def _index_in_list(list_: List, item: Any) -> int:
    """
    Return the index of an item in a list.
    :param list_: the list to search
    :param item: the item to search for
    :return: the index of the item
    """
    for i, x in enumerate(list_):
        if isinstance(x, np.ndarray) and isinstance(item, np.ndarray):
            return i if np.array_equal(x, item) else -1
        elif x == item:  # this assumes __eq__ is implemented between the two objects
            return i
    return -1


def autocache_func(
    func: Callable, autocache_path: str = "cachegenius_data/"
) -> Callable:
    """
    Replace the function with a wrapper than runs the function but
    record some analytics to determine if caching is a good idea.
    :param func: the function to wrap
    :param autocache_path: the path to store the output
    :return: the wrapped function
    """
    if hasattr(func, "__cachegenius__"):
        return func

    # noinspection PyUnresolvedReferences
    def wrapper(*args, **kwargs):
        """
        The wrapper function.
        :param args: the arguments to the function
        :param kwargs: the keyword arguments to the function
        :return: the result of the function
        """
        inputs = (args, kwargs)
        begin = time.time()
        outputs = func(*args, **kwargs)
        end = time.time()

        file_path = os.path.join(
            autocache_path, *func.__module__.split("."), func.__name__ + ".pkl"
        )

        if os.path.exists(file_path):
            with open(file_path, "rb") as f:
                all_inputs, all_outputs, nb_calls, total_time = pickle.load(f)
                index = _index_in_list(all_inputs, inputs)
                if index >= 0:
                    # if the inputs are already in the file, update the outputs
                    index_out = _index_in_list(all_outputs[index], outputs)
                    if index_out < 0:
                        all_outputs[index].append(outputs)
                    nb_calls[index] += 1
                    total_time[index] += end - begin
                else:
                    # otherwise, add the new inputs and outputs
                    all_inputs.append(inputs)
                    all_outputs.append([outputs])
                    nb_calls.append(1)
                    total_time.append(end - begin)
        else:
            all_inputs = [inputs]
            all_outputs = [[outputs]]
            nb_calls = [1]
            total_time = [end - begin]

        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, "wb") as f:
            pickle.dump((all_inputs, all_outputs, nb_calls, total_time), f)

        return outputs

    # add a custom attribute to the wrapper so that it can be identified as a cachegenius function
    wrapper.__cachegenius__ = True
    return wrapper


def autocache_module(module: ModuleType, autocache_path: str = "cachegenius_data/"):
    """
    Replace all functions in a module with a wrapper that compute some analytics.
    :param module: the module to wrap
    :param autocache_path: the path to store the files required by CacheGenius
    :return: the wrapped module
    """
    print(f"Analyzing module {module.__name__} using 🧞‍♂️ CacheGenius...")
    for name, obj in module.__dict__.items():
        if (
            inspect.isfunction(obj)
            and not hasattr(obj, "__cachegenius__")
            and obj.__module__ == module.__name__
        ):
            obj = autocache_func(obj, autocache_path)
            setattr(module, name, obj)
        elif isinstance(obj, ModuleType) and (module.__name__ == obj.__package__):
            autocache_module(obj)
        elif inspect.isclass(obj) and obj.__module__ == module.__name__:
            for method_name, m_obj in obj.__dict__.items():
                if (
                    inspect.isfunction(m_obj)
                    and not hasattr(m_obj, "__cachegenius__")
                    and m_obj.__module__ == module.__name__
                ):
                    obj = autocache_func(m_obj, autocache_path)
                    setattr(obj, method_name, obj)


def report(
    autocache_path: str = "cachegenius_data/",
    debug: bool = True,
    cost_per_comput_hr: float = 0.1,
    cost_per_mem_gb: float = 0.2,
) -> set:
    print(f"🧞‍♂️ CacheGenius report :")
    results = set()
    # for all `pkl` files in `autocache_path`
    for root, _, files in os.walk(autocache_path):
        for file in files:
            if file.endswith(".pkl"):
                file_path = os.path.join(root, file)
                with open(file_path, "rb") as f:
                    # Compute some statistics that shows if caching is a good idea
                    try:
                        all_inputs, all_outputs, nb_calls, total_time = pickle.load(f)
                    except EOFError:
                        continue

                    time_gain = sum(
                        [(nc - 1) * mt for nc, mt in zip(nb_calls, total_time)]
                    ) / sum(nb_calls)

                    function_name = file_path[len(autocache_path) : -4].replace(
                        "/", "."
                    )
                    calls_more_than_once = any([nc > 1 for nc in nb_calls])
                    is_deterministic = (
                        not any([len(out) > 1 for out in all_outputs])
                        if calls_more_than_once
                        else None
                    )
                    cache_size = os.path.getsize(file_path)

                    should_cache = (
                        (is_deterministic == True)  # not False and not None
                        and calls_more_than_once
                        and (
                            time_gain * cost_per_comput_hr / 3600
                            - cache_size * cost_per_mem_gb * 1e-9
                            > 0
                        )
                    )

                    if debug or should_cache:
                        print(f"Function: {function_name}")
                    if debug:
                        print(f"Is deterministic: {is_deterministic}")
                        print(f"Any func calls more than once: {calls_more_than_once}")
                        print(f"Avg time gained per function call: {time_gain}")
                        print(f"Caching size: {cache_size} bytes")
                    if debug or should_cache:
                        print(f"Should cache: {should_cache}")
                        print()

                    results.add(
                        (
                            function_name,
                            is_deterministic,
                            calls_more_than_once,
                            time_gain,
                            cache_size,
                            should_cache,
                        )
                    )
    return results


def empty(autocache_path: str = "cachegenius_data/"):
    # for all `pkl` files in `autocache_path`
    for root, _, files in os.walk(autocache_path):
        for file in files:
            if file.endswith(".pkl"):
                file_path = os.path.join(root, file)
                os.remove(file_path)
