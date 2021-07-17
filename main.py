import tkinter as tk   #Out of all the GUI methods, tkinter is the most commonly used method. It is a standard Python interface to the Tk GUI toolkit shipped with Python.
import requests   #beacause we get data from server
from PIL  import Image   #pip install pillow..........PIL is the Python Imaging Library
from PIL  import ImageTk
#To initialize tkinter, we have to create a Tk root widget, which is a window with a title bar and other decoration provided by the window manager.
# The root widget has to be created before any other widgets and there can only be one root widget.

root=tk.Tk()   # tkinter module, containing the Tk toolkit
root.title("Weather Application")   
root.geometry("600x500")
#Key: fa5457e009f1f70534f97e9ed8dfc11a
#APi url: api.openweathermap.org/data/2.5/weather?q={city name}&appid={API key}

def format_response(weather):
    try:
        city=weather['name']
        condition=weather['weather'][0]['description']
        temp=weather['main']['temp']
        final_str='City:%s\nCondition:%s\nTemperature:%s'%(city, condition, temp)
    except:
        final_str='there is problem in retrieving that information'
    return final_str                            


def get_weather(city):
    weather_key="fa5457e009f1f70534f97e9ed8dfc11a"
    url="https://api.openweathermap.org/data/2.5/weather"
    params={'APPID':weather_key,'q':city, 'units':'imperial'}  #APPID for api key (which is placed in weather_key),q for city name, units for units in measurement
    response=requests.get(url,params)  #get data from server 
    #print(response.json())

    weather=response.json()
    #print(weather['name'])
    #print(weather['weather'][0]['description'])
    #print(weather['main']['temp'])

    result['text']=format_response(weather)

    icon_name=weather['weather'][0]['icon']
    open_image(icon_name)

def open_image(icon ):
    size=int(frame_two.winfo_height()*0.25)
    img=ImageTk.PhotoImage(Image.open('./img/'+ icon +'.png').resize((size,size)))
    weather_icon.delete('all')
    weather_icon.create_image(0,0,anchor='nw',image=img)
    weather_icon.image=img
        

img=Image.open("./sunset.jpg")
img=img.resize((600,500),Image.ANTIALIAS)   #ANTIALIAS convert high level images to low level images
img_photo=ImageTk.PhotoImage(img)    #Tkinter Photoimage is one of the built-in methods which has been used to add the user-defined images in the application.

# show image in background with help of Label
bg_lal=tk.Label(root,image=img_photo)   #Label is in tk and in that we pass root(i.e. our window and the image(as it is)=(pass name of variable in which image is stored)img_photo )
bg_lal.place(x=0,y=0,width=600,height=500)   #place for where to place particular thing and give respective coordinates of x and y


# Label for heading and placed over image(bg_lal)
heading_title=tk.Label(bg_lal,text="Earth including over 200,000 cities!",fg="red",bg="#000000",font=("times new roman",18,"bold")) #bg for backgroud color
heading_title.place(x=80,y=18)   

#frame in which button and search bar is placed
frame_one=tk.Frame(bg_lal,bg="#A19882",bd=5)  
frame_one.place(x=80,y=60,width=450,height=50)

#Entry for search bar and placed over frame_one
#sticky − What to do if the cell is larger than widget. By default, with sticky='', widget is centered in its cell. 
#sticky may be the string concatenation of zero or more of N, E, S, W, NE, NW, SE, and SW, compass directions indicating the sides and corners of the cell to which widget sticks.
txt_box=tk.Entry(frame_one,font=("times new roman",25),width=17)   
txt_box.grid(row=0,column=0 ,sticky="w") # grid method to arrange labels in respective rows and columns as specified


#Button for search and placed over frame_one
btn=tk.Button(frame_one,text="get weather",fg='green',font=("times new roman",16,"bold"),command=lambda:get_weather(txt_box.get()))  #fg - forecolor(color of text), 
#A lambda function is a small anonymous function. A lambda function can take any number of arguments, but can only have one expression.
btn.grid(row=0,column=1,padx=10)  #padx- padding along x axis

#frame placed over bg_lal for info of weather
frame_two=tk.Frame(bg_lal,bg="#A19882",bd=5)
frame_two.place(x=80,y=130,width=450,height=300)

#label for displaying information of weather and placed over frame_two
result=tk.Label(frame_two,font=40,bg="white",justify='left',anchor='nw')  #justify and anchor for make data align on left in result
result.place(relwidth=1,relheight=1)   #make relation with parent class(frame_two)

weather_icon=tk.Canvas(result,bg='white',bd=0,highlightthickness=8)   #for icon
weather_icon.place(relx=.75,rely=0,relwidth=1,relheight=0.5)
root.mainloop()