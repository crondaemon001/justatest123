"""
the ChatGPT prompt was: 'give me a quick fizzbuz example using python 3'

This script implements the FizzBuzz problem, a classic programming exercise.
The FizzBuzz problem requires printing numbers from 1 to n, but with the following rules:
- If the number is divisible by 3, print "Fizz" instead of the number.
- If the number is divisible by 5, print "Buzz" instead of the number.
- If the number is divisible by both 3 and 5, print "FizzBuzz" instead of the number.

"""

# https://github.com/Collinear-Group/sdpdev/settings/security_analysis
# Dependabot should generate some notifications from the next couple of lines:

# Here's something that should trigger in scans, a github token that is revoked already.

GITHUB_TOKEN=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

VARIABLE=VALUE
ENVIRONMENT=PRODUCTION
DB_USERNAME=mydbuser
DB_PASSWORD=mydbpassword
API_KEY=myapikey
API_SECRET=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

print(DB_USERNAME)
print(DB_PASSWORD)

username = "abogususerid"
password = "aboguspassword"

def fizz_buzz(n):
    for i in range(1, n+1):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)

# Example usage:
fizz_buzz(20)

print(" ")
print(username)
print(password)
