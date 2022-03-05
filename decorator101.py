import time
current_time = time.time()
print(current_time)

def time_decorator(evaluated_function):
    def time_calculator():
        start_time = time.time()
        evaluated_function()
        end_time = time.time()
        print(f"{evaluated_function.__name__} run speed: {end_time - start_time}")

    time_calculator()

@time_decorator
def fast_function():
    for i in range(10000000):
        i * i

@time_decorator
def slow_function():
    for i in range(100000000):
        i * i


