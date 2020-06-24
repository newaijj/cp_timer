from timeit import timeit

print(timeit(stmt = "subprocess.call('./cpp')", setup = "import subprocess", number = 1))

