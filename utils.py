# # utils.py
# def get_float_input(prompt):
#     while True:
#         try:
#             return float(input(prompt))
#         except ValueError:
#             print("Please enter a valid floating number.")


# def get_int_input(prompt):
#     while True:
#         try:
#             return int(input(prompt))
#         except ValueError:
#             print("Please enter a valid integer.")
def get_float_input(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a valid floating number.")


def get_int_input(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Please enter a valid integer.")
