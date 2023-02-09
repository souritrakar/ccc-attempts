string =input()
new=""
        for i in range(len(string)):
          new+=string[i]
          if string[i]!="a" and string[i]!="e" and string[i]!="i" and string[i]!="o" and string[i]!="u":
            next_vowel = ""
            prev_vowel = ""
            next_consonant = ""
            #FROM CURRENT TO A
            for j in range(ord(string[i])-1, 96, -1):
              if chr(j)=="a" or chr(j)=="e" or chr(j)=="i" or chr(j)=="o" or chr(j)=="u":
              prev_vowel = chr(j)
              break
            #FROM CURRENT TO Z
            for j in range(ord(string[i])+1, 123):
              if chr(j)=="a" or chr(j)=="e" or chr(j)=="i" or chr(j)=="o" or chr(j)=="u":
              next_vowel = chr(j)
              break

            for j in range(ord(string[i])+1, 123):
                if chr(j)!="a" and chr(j)!="e" and chr(j)!="i" and chr(j)!="o" and chr(j)!="u":
                    next_consonant = chr(j)
                    break

            #CHECKING WHICH ONE TO ADD with COUNTER
            current = ord(string[i])
            if len(prev_vowel)!=0 and len(next_vowel) == 0:
                new+=prev_vowel
            else:
                if current - ord(prev_vowel) <= ord(next_vowel) - current:
                    new+=prev_vowel
                else:
                    new+=next_vowel

            new+=next_consonant

print(new)
