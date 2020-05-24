import requests
# import sys

# print(sys.version)
# print(sys.executable)


# def greet(who_to_greet):
#     test = 'test'
#     greeting = 'Hello, {}'.format(who_to_greet)
#     return greeting


# print(greet('World'))
# print(greet('Anisa'))
r = requests.get('https://coreyms.com')
print(r.status_code)

# name = input("Your Name? ")
# print("Hello,", name)
