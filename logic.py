import eel
import os
""" ----------- IMPORT JAVA ----------- """
from jpype import *
jarpath = "java_is_prime.jar"
startJVM(getDefaultJVMPath(), "-ea", "-Djava.class.path=%s" % (jarpath))
pkgJava = JPackage("pkg_java")

java_prime_class = pkgJava.JavaPrime()
print("JAVA CLASS LOADED")
print("TEST JAVA:", java_prime_class.is_prime_ferma(12))
""" ----------- IMPORT JAVA ----------- """


""" ----------- IMPORT C ----------- """
from ctypes import *
c_prime = WinDLL("./is_prime_c.dll")
print("C MODULE LOADED")
print("TEST C:", bool(c_prime.is_prime_sqrt(12)))
""" ----------- IMPORT C ----------- """

""" ----------- IMPORT C# ----------- """
import clr
path_с_sharp = os.getcwd() + "\\is_prime_csharp.dll"
clr.AddReference(path_с_sharp)
from is_prime_csharp import miler_rabin_csharp
print("C# CLASS LOADED")
print("TEST:", miler_rabin_csharp.test_miler_rabin(12))
""" ----------- IMPORT C# ----------- """

@eel.expose
def start_proc_number_py(number):
    part_answer = {"java": False, "c": False, "c#": False, "python": []}
    part_answer["python"] = factorization(number)
    part_answer["c"] = bool(c_prime.is_prime_sqrt(number))
    part_answer["java"] = java_prime_class.is_prime_ferma(number)
    part_answer["c#"] = miler_rabin_csharp.test_miler_rabin(number)
    part_answer["js"] = eel.solve_example(part_answer["python"], number)()
    rezult = {}
    rezult["python"] = part_answer["python"]
    rezult["c"] = "Простое" if part_answer["c"] else "Составное"
    rezult["java"] = "Простое" if part_answer["java"] else "Составное"
    rezult["c#"] = "Простое" if part_answer["c#"] else "Составное"
    rezult["js"] = part_answer["js"]
    return rezult


def factorization(number):
    parts = []
    delim = 2
    while delim**2 <= number:
        if number % delim == 0:
            parts.append(delim)
            number //= delim
        else:
            delim += 1
    if number > 1:
        parts.append(number)
    return parts
