## Importing Necessary Modules
import requests # to get image from the web
import shutil # to save it locally
import tkinter as tk
from tkinter import messagebox


# getImages Function
def getImages():
	## Set up the image URL and filename
	url = entryURL.get()
	ext = entryExt.get()
	#url = 'https://www.scan-vf.net/uploads/manga/boruto/chapters/chapitre-79/'
	#'https://www.scan-vf.net/uploads/manga/boruto/chapters/chapitre-71/VA- 02.webp'
	# 'https://www.scan-vf.net/uploads/manga/kimetsu-no-yaiba/chapters/chapitre-105/01.png'
	
	resp = []
	for i in range(1,51):

		# Open the url image, set stream to True, this will return the stream content.
		r = requests.get(url + '{:0>2}'.format(i) + ext, stream = True)

		# Check if the image was retrieved successfully
		if r.status_code == 200:
			# Set decode_content value to True, otherwise the downloaded image file's size will be zero.
			r.raw.decode_content = True
			
			# Open a local file with wb ( write binary ) permission.
			with open('{:0>2}'.format(i) + ext,'wb') as f:
				shutil.copyfileobj(r.raw, f)
			resp.append('\nImage sucessfully Downloaded: ' + '{:0>2}'.format(i) + ext)
			#resp.set(resp + '\nImage sucessfully Downloaded: ','{:0>2}'.format(i) + ext)
			labelResp.config(text=resp)
			print('Image sucessfully Downloaded: ','{:0>2}'.format(i) + ext)
		else:
			#resp.set(resp + '\nImage Couldn\'t be retreived')
			resp.append('Image Couldn\'t be retreived')
			#labelResp.config(text=resp)
			print('Image Couldn\'t be retreived')
			break
	
	# Close the window
	entryURL.delete(0,tk.END)
	messagebox.showinfo(title="Info", message="Operation successfull")
	resp = []
	#window.destroy()


# GUI
#resp = StringVar()
#resp.set("")

window = tk.Tk()
window.title("Image downloader")

label = tk.Label(window, text="Helloooo! Please, give me the url of the images.")
labelURL = tk.Label(window, text="URL")
#URL
entryURL = tk.Entry()
#Extension
labelExt = tk.Label(window, text="Extension")
entryExt = tk.Entry(text='.png')
btn = tk.Button(text="Generate Images",command=getImages)
btnQuit = tk.Button(text="Quit",command=window.destroy)
# Response
labelResp = tk.Label(window, text="")

label.pack()
labelURL.pack()
entryURL.pack()
labelExt.pack()
entryExt.pack()
btn.pack()
btnQuit.pack()
labelResp.pack(expand=True)

window.mainloop()

