"""There is a restriction in the authorization system: the password must begin with a Latin letter, consist of Latin letters, numbers, dot and minuses, but end only with a Latin letter or number;
the minimum password length is one character, the maximum is 20. Write a code that checks whether the input string matches this rule.
Come up with several ways to solve the problem and compare them."""

import re

passRank = {
        0: "TWO SHORT",
        1: "VERY_WEAK",
        2: "WEAK",
        3: "MEDIUM",
        4: "STRONG",
        5: "VERY_STRONG"
        }

def method1(password):
  """
  Stric Password validation Function
  Using regex to validate password
  My assumptions:
   password at least have  a-zA-Z, 0-9, ., -

  """
  pattern1 = "^[a-zA-Z].*[a-zA-Z]$"
  pattern2 = "[0-9]"
  pattern3 = "[\S]{5,20}"
  return (re.match(pattern1, password) and
       re.search(pattern2, password) and
       re.search(pattern3, password) and
       "." in password and "-" in password)


def method2(password): 
  """
  This function will score the password
  """
  score = 0
  pattern1 = "^[a-zA-Z].*[a-zA-Z]$"
  pattern2 = "[0-9]"
  pattern3 = "[\S]{5,20}"
  if re.search(pattern3, password):
    score += 1
    if re.search(pattern1, password):
      score += 1
    if re.search(pattern2, password):
      score +=1
    if "." in password:
      score +=1
    if "-" in password:
      score +=1
  return passRank[score]


