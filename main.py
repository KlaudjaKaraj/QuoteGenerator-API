from tkinter import *
import requests


def get_quote():
    url = "https://api.quotable.io/random"
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()
    quote = data ["content"]
    author = data ["author"]
    canvas.itemconfig(quote_text, text = f'"{quote}" \n\n - {author}')
    
   
    
window = Tk()
window.title("Famous quotes")
window.config(padx=50, pady=50)

canvas = Canvas(width=300, height=414)
background_img = PhotoImage(file="QuoteGenerator-API/bg.png")
canvas.create_image(150, 207, image=background_img)
quote_text = canvas.create_text(160, 200, text="Famous quotes...", width=200, font=("Arial", 15, "bold"), fill="#375045")

canvas.grid(row=0, column=0)


button = Button( highlightthickness=1, command=get_quote, text="Next quote", bg="#9DBCA5", fg="white", font=("Arial", 10, "bold") )
button.grid(row=3, column=0)

window.mainloop()
