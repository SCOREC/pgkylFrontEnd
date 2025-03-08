from timeit import default_timer as timer
filename = 'XPointFinder.py'
with open(filename) as file:
  source_code = file.read()

t0 = timer()
compiled_code = compile(source_code, filename, 'exec')
t1 = timer()
exec(compiled_code)
t2 = timer()
print("compile time: " + str(t1-t0))
print("xPointFinder time: " + str(t2-t1))
