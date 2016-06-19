"""
Simple UI that lets you select which corner
notifications pop up in the Steam in-game overlay.
"""

import subprocess, tkinter, re, os

cmd = 'WMIC PROCESS get Caption,Commandline,Processid'
p = subprocess.Popen(cmd, stdout=subprocess.PIPE)
isRunning = False
for line in p.stdout:
        if re.search(b'Steam.exe',line):
                isRunning = True
                break
p.kill()
if not isRunning:
        subprocess.Popen(['C:\\Program Files (x86)\\Steam\\Steam.exe'])
        
root = tkinter.Tk()
root.title('Steam Overlay Position')
root.minsize(width=200, height=125)
root.maxsize(width=200, height=125)

def setOverlay():
	filename = 'C:\\Program Files (x86)\\Steam\\resource\\styles\\gameoverlay.styles'
	with open(filename) as file:
		lines = file.read()
		lines = re.sub('TopLeft|TopRight|BottomLeft|BottomRight', var.get(), lines)
	with open(filename,'w') as fileN:
		fileN.write(lines)
	label.config(text = 'Overlay Position = ' + var.get())

positions = [('TopLeft'), ('TopRight'), ('BottomLeft'), ('BottomRight')]

var = tkinter.StringVar()
var.set("L")

for position in positions:
        b = tkinter.Radiobutton(root, text=position,
        variable=var, value=position, command=setOverlay)
        b.pack(anchor='w')
        if (position == 'BottomRight'):
                defaultButton = b

label = tkinter.Label(root)
label.pack()
defaultButton.invoke()
root.mainloop()
