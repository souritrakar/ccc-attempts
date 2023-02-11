keypad = [ ['A', 'B', 'C', 'D', 'E', 'F'], 
           ['G', 'H', 'I', 'J', 'K', 'L'],
           ['M', 'N', 'O', 'P', 'Q', 'R'],
           ['S', 'T', 'U', 'V', 'W', 'X'],
           ['Y', 'Z', ' ', '-', '.', 'enter']
        ]
keypad_letter_dict = {}
for i, subarray in enumerate(keypad):
    for letter in subarray:
        keypad_letter_dict[letter] = i

word = input()
cursor = 'A'
sum_movements = 0
for i in range(0, len(word)):
    char_row = keypad_letter_dict[word[i]]
    char_column = keypad[char_row].index(word[i])
    
    cursor_row = keypad_letter_dict[cursor]
    cursor_column = keypad[cursor_row].index(cursor)

    diff_x = abs((char_column+1) - (cursor_column+1))
    diff_y = abs((char_row+1) - (cursor_row+1))
    
    sum_movements+=diff_x+diff_y
    cursor = word[i]
    
    if i==len(word)-1:
        cursor_row = keypad_letter_dict[cursor]
        cursor_column = keypad[cursor_row].index(cursor)
        enter_row = keypad_letter_dict['enter']
        enter_column = 5
        diff_x_enter = abs((enter_column+1) - (cursor_column+1))
        diff_y_enter = abs((enter_row+1) - (cursor_row+1))
        sum_movements+=diff_x_enter+diff_y_enter

print(sum_movements)
