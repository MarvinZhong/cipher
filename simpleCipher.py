import PySimpleGUI as sg
import os

faviconPath = os.path.dirname(__file__)+'/cipher.ico'

def cipher(text, key="xyz"):
    # convert to unicode decimal
    bText = [ord(c) for c in text]
    bKey = [ord(c) for c in key]

    textUB = len(bText)
    keyUB = len(bKey) - 1
    keyPos = 0
    for textPos in range(0, textUB):
        bText[textPos] = bText[textPos] ^ bKey[keyPos]
        if keyPos < keyUB:
            keyPos += 1
        else:
            keyPos = 0
    return ''.join(chr(c) for c in bText)

def main():
    # strInput = input("Enter String to Encrypt or Decrypt \t: ")
    # print("Encrypted or Decrypted String\t\t: ", cipher(strInput))
    sg.theme('Dark')

    layout = [  [sg.Text('Enter String to Encrypt or Decrypt')],
                [sg.InputText(key='-strInput-', change_submits=True, size=(39,1))],
                [sg.Text(key='-Output-'), sg.Button('Copy')] ]
    
    # Create the Window
    window = sg.Window('Simple Cipher', layout, element_justification='right', icon=faviconPath)
    # Event Loop to process "events" and get the "values" of the inputs
    while True:
        event, values = window.read()
        if event in (None, 'Cancel'):
            break
        # if -strInput- changed, update the window
        if event == '-strInput-':
            window['-Output-'].update(cipher(values['-strInput-']))
        if event == 'Copy':
            # copy the output to the clipboard
            sg.clipboard_set(window['-Output-'].get())
    window.close()

if __name__ == '__main__':
    main()