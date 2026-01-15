def is_palindrome_reversed(text):
  reversed_text = ''.join(reversed(text))
  return text == reversed_text

user_input = raw_input("Enter a string to check if it's a palindrome: ")

if is_palindrome_reversed(user_input):
  print "'" + user_input + "' is a palindrome."
else:
  print "'" + user_input + "' is not a palindrome."
