songs = ["A","B","C","D","E"]
def button_press(button, arr, presses):
    res = arr
    if button==1:
        res.append(res[0])
        res.pop(0)
    elif button==2:
        res.insert(0, res[len(res)-1])
        res.pop()
    elif button==3 and presses%2==1:
        temp = res[0]
        res[0] = res[1]
        res[1] = temp
    return res
while True:
    button = int(input())
    presses = int(input())
    
    if button==4 and presses>0:
        break
    else:
        for i in range(presses):
          button_press(button, songs, presses)

print(' '.join(songs))
