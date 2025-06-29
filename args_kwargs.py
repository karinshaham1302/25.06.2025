def sum_args(x: float, *args) -> float:
    result = x
    for i in args:
        result += i
    return result

def print_user_info(*args, **kwargs) -> None:
    main_fields = ['name', 'age', 'city']

    for key in main_fields:
        if key in kwargs:
            print(f"{key}: {kwargs[key]}")

    for key, value in kwargs.items():
        if key not in main_fields:
            print(f"{key}: {value}")

def combine_values(x: float, *args, **kwargs) -> None:
    result = x
    for i in args:
        result += i

    print(f"Sum: {result}")

    for key, value in kwargs.items():
        print(f"{key}: {value}")

def greet_user(*args, **kwargs) -> None:
    if 'name' in kwargs:
        print(f"Hello {kwargs['name']}")
    else:
        print("Hello guest")



