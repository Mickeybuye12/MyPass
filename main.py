from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
def generate_password():
  letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
  numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
  symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

  nr_letters = random.randint(8, 10)
  nr_symbols = random.randint(2, 4)
  nr_numbers = random.randint(2, 4)

  password_list = [random.choice(letters) for char in range(nr_letters)] + [random.choice(symbols) for char in range(nr_symbols)] + [random.choice(numbers) for char in range(nr_numbers)]

  random.shuffle(password_list)

  password = "".join(password_list)
  password_entry.delete(0,END)
  password_entry.insert(0,f"{password}")
  pyperclip.copy(password)
 


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
  website = website_entry.get()
  email = email_entry.get()
  password = password_entry.get()
  new_data = {
    website:{
      "email":email,
      "password":password
    }
  }
  if len(website) == 0 or len(password) == 0:
    messagebox.showinfo(title="Oops",message="Please make sure you haven't left any fields empty!")
  else:  
    # is_ok =messagebox.askokcancel(title=website , message=f"These are the details you have entered: \nEmail: {email} "
    #                               f"\nPassword: {password} \nIs it ok to save? ")
    # if is_ok:
    

    try:
      # Reading old data
      with open("Data.json" ,"r")as data_file:
        data = json.load(data_file)

    except FileNotFoundError:  
      with open("Data.json" ,"w")as data_file:
          json.dump(new_data, data_file,indent=4)
    else:
      # Updating old data with new data
      data.update(new_data)
      #  saving the updated data
      with open("Data.json" ,"w")as data_file:
          json.dump(data, data_file,indent=4)
            
    finally:    
      website_entry.delete(0,END)  
      password_entry.delete(0,END)
#----------------------------- Search ----------------------------- #
def search():
  website = website_entry.get()
  try:
    with open("Data.json","r") as data_file:
      data =  json.load(data_file)  
  except FileNotFoundError :
     messagebox.showinfo(title="Error" , message="File Not Found")
  else:
    if website in data:
      email = data[website]["email"]
      password = data[website]["password"]      
      messagebox.showinfo(title=website ,message=f"Email: {email}\nPassword: {password}")
    else:
      messagebox.showinfo(title="Error" , message=f"No Details for {website} Exists")  

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
logo_img = PhotoImage(file="logo.png")
window.wm_iconphoto(False, logo_img)
window.config(padx=50, pady=50)

canvas = Canvas(height=200, width=200)
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

#Labels
website_label = Label(text="Website:")
website_label.grid(row=1, column=0)
email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)
password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

#Entries
website_entry = Entry(width=21)
website_entry.grid(row=1, column=1)
website_entry.focus()
email_entry = Entry(width=39)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, "michael@gmail.com")
password_entry = Entry(width=21)
password_entry.grid(row=3, column=1)

# Buttons
search_button = Button(text="Search",width =13,command=search)
search_button.grid(row =1 ,column=2)
generate_password_button = Button(text="Generate Password",command=generate_password)
generate_password_button.grid(row=3, column=2)
add_button = Button(text="Add", width=36, command=save)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()