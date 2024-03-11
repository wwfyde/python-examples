import sys
from http.client import HTTPException

try:
    f = open('myfile.txt')
    s = f.readline()
    i = int(s.strip())
# except OSError as err:
#     print("OS error:", err)
# except ValueError:
#     print("Could not convert data to an integer.")
except Exception as err:
    print(f"Unexpected {err=}, {type(err)=}")
    raise