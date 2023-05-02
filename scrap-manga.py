## Importing Necessary Modules
import requests # to get image from the web
import shutil # to save it locally
from bs4 import BeautifulSoup
import tkinter as tk
from tkinter import messagebox
import os



def getUrl():
	# For Url
	url = entryURL.get()
	
	for j in range(1,31):
		f = requests.get(url + str(j))
		if f.status_code == 200:
			soup = BeautifulSoup(f.text, 'html.parser')
			if soup.find_all(id='ppp'):
				for pp in soup.find_all(id='ppp'):
					for image in pp.find_all('img'):
						getImages(image['src'].strip(),j)
			else:
				print('No more page')
				break
		else:
			print('Page not Found')
			break

# getImages Function
def getImages(url, i):
	## Set up the image URL and filename
	#url = 'https://www.scan-vf.net/uploads/manga/kimetsu-no-yaiba/chapters/chapitre-' + entryURL.get() + '/0'
	#ext = entryExt.get()
	#url = 'https://www.scan-vf.net/uploads/manga/boruto/chapters/chapitre-79/'
	
	resp = []
	
	folder = url.split('/')[7][9:]
	if not os.path.exists(os.getcwd() + '/' + folder):
		os.mkdir(folder)
	
	# Open the url image, set stream to True, this will return the stream content.
	r = requests.get(url, stream = True)

	# Check if the image was retrieved successfully
	if r.status_code == 200:
		# Set decode_content value to True, otherwise the downloaded image file's size will be zero.
		r.raw.decode_content = True
		
		# Open a local file with wb ( write binary ) permission.
		with open(folder + '/{:0>2}'.format(i) + '.jpg','wb') as f:
			shutil.copyfileobj(r.raw, f)
		resp.append('\nImage sucessfully Downloaded: ' + '{:0>2}'.format(i) + '.jpg')
		#resp.set(resp + '\nImage sucessfully Downloaded: ','{:0>2}'.format(i) + ext)
		#labelResp.config(text=resp)
		print('Image sucessfully Downloaded: ','{:0>2}'.format(i) + '.jpg')
	else:
		
		#resp.set(resp + '\nImage Couldn\'t be retreived')
		resp.append('Image Couldn\'t be retreived')
		#labelResp.config(text=resp)
		print('Image Couldn\'t be retreived')
	
	# Close the window
	#entryURL.delete(0,tk.END)
	#messagebox.showinfo(title="Info", message="Operation successfull")
	#window.destroy()


# GUI
#resp = StringVar()
#resp.set("")

window = tk.Tk()
window.title("Image downloader")

label = tk.Label(window, text="Helloooo! Please, give me the scan url.")
labelURL = tk.Label(window, text="URL")
#URL
entryURL = tk.Entry()
#Extension
#labelExt = tk.Label(window, text="Extension")
#entryExt = tk.Entry()
#entryExt.insert(0, ".jpg")
btn = tk.Button(text="Generate Images",command=getUrl)
btnQuit = tk.Button(text="Quit",command=window.destroy)
# Response
#labelResp = tk.Label(window, text="")

label.pack()
labelURL.pack()
entryURL.pack()
#labelExt.pack()
#entryExt.pack()
btn.pack()
btnQuit.pack()
#labelResp.pack(expand=True)

window.mainloop()

