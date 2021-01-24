#!/usr/bin/env python
# coding: utf-8

# In[146]:


from tkinter import *
from tkinter import ttk
from tkinter import filedialog


# In[147]:


from pytube import YouTube
Folder_Name = ""
#file loaction
def openLocation():
    global Folder_Name
    Folder_Name = filedialog.askdirectory()
    if(len(Folder_Name)>1):
        locationError.config(text=Folder_Name,fg='green')
    else:
        locationError.config(text="Please Choose Folder!!",fg="red")
        
def Downloader():
    choice = ydchoicebox.get()
    url = link_enter.get()
    if(len(url)>1):
        error.config(text="")
        yt = YouTube(url)
        if(choice == choicebox[0]):
            select = yt.streams.filter(progressive=True).first()
        elif(choice == choicebox[1]):
            select = yt.streams.filter(progressive=True,file_extension='mp4').last()
        elif(choice == choicebox[2]):
            select = yt.streams.filter(only_audio=True).first()
        else:
            error.config(text="Paste Link again!",fg="red")    
            
            
#download function
    select.download(Folder_Name)
    error.config(text="Download Completed!!")


# In[148]:


root = Tk()


# In[149]:


root.title("Aryan's Youtube Downloader")
root.geometry("500x300")
root.columnconfigure(0,weight=1)


# In[150]:


#Youtube Video Dowwnloader heading label
ydmainLabel = Label(root,text = 'Youtube Video Downloader',fg = 'red', font = 'arial 20 bold')
ydmainLabel.grid()
#enter url label
ydLabel = Label(root,text='Enter the URL of the video', font = 'jost 15')
ydLabel.grid()


# In[151]:


#link enter spot
link = StringVar()


# In[ ]:





# In[152]:


link_enter = Entry(root, width =70, textvariable = link)
link_enter.grid()

#for handelling entry box error errors
error = Label(root,text='Error Msg',fg = 'red',font= 'jost 10')
error.grid()

#save file label
save= Label(root,text='Save the Video File',font= 'jost 10')
save.grid()

#save button
savebutton = Button(root,width=10,bg='red',fg='white',text='Choose path', command=openLocation)
savebutton.grid()

#error message loaction
locationError = Label(root,text='error msg of path',fg='red', font ='jost 10')
locationError.grid()

#select quality label
vQuality = Label(root,text='Select Quality',font='jost 10')
vQuality.grid()

#choice filling box
choicebox = ['720p','144p','Only Audio']
ydchoicebox = ttk.Combobox(root,values=choicebox)
ydchoicebox.grid()

#download button
downloadb = Button(root,text='Download',width=10,bg='red',fg='white', command=Downloader)
downloadb.grid()

#end closing label
closel = Label(root,text='YT video downloader (python basic implementation)',font ='jost 5')
closel.grid()
aryan= Label(root,text='Aryan Kumar',fg='red',font='jost 10')
aryan.grid()


# In[153]:


root.mainloop()


# In[ ]:





# In[ ]:





# In[ ]:




