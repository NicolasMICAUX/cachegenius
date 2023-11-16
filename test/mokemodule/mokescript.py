"""
Nomenclature:
    - d = deterministic, nd = non deterministic
    - f = fast, s = slow
    - h = heavy storage, l = light storage
    - oc = often called with the same arguments, noc = not called often with the same arguments
"""

import random
from time import sleep

import numpy as np


def d_f_l_oc(x: int) -> int:
    return np.array([x])


def d_f_l_noc(x: int) -> int:
    return np.array([x])


def nd_f_l_oc(x: int) -> int:
    return np.array([x + random.randint(0, 100)])


def nd_f_l_noc(x: int) -> int:
    return np.array([x + random.randint(0, 100)])


def d_s_l_oc(x: int) -> int:
    sleep(0.1)
    return np.array([x])


def d_s_l_noc(x: int) -> int:
    sleep(0.1)
    return np.array([x])


def nd_s_l_oc(x: int) -> int:
    sleep(0.1)
    return np.array([x + random.randint(0, 100)])


def nd_s_l_noc(x: int) -> int:
    sleep(0.1)
    return np.array([x + random.randint(0, 100)])


def d_f_h_oc(x: int) -> int:
    return np.full(100_000, x)


def d_f_h_noc(x: int) -> int:
    return np.full(100_000, x)


def nd_f_h_oc(x: int) -> int:
    return np.random.randint(0, 100, size=100_000)


def nd_f_h_noc(x: int) -> int:
    return np.random.randint(0, 100, size=100_000)


def d_s_h_oc(x: int) -> int:
    sleep(0.1)
    return np.full(100_000, x)


def d_s_h_noc(x: int) -> int:
    sleep(0.1)
    return np.full(100_000, x)


def nd_s_h_oc(x: int) -> int:
    sleep(0.1)
    return np.random.randint(0, 100, size=100_000)


def nd_s_h_noc(x: int) -> int:
    sleep(0.1)
    return np.random.randint(0, 100, size=100_000)
