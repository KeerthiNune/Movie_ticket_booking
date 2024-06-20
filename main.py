import tkinter as tk
from tkinter import Tk, Frame, Label, Entry, Button,messagebox
from PIL import Image, ImageTk
class Home:
    def __init__(self, root):
        self.root = root
        self.frame = Frame(self.root, width = 550, height = 350, bd = 6, relief = 'ridge', bg = 'white')
        self.frame.place(x= 0,y= 0)

        self.bg = Image.open('..\\assets\\image.png')
        self.bg = self.bg.resize((550,350))
        self.bg = ImageTk.PhotoImage(self.bg)

        self.bg_lbl = Label(self.frame, image = self.bg)
        self.bg_lbl.place(x= 0, y= 0)

        self.lbl=  Label(self.frame, text= 'USERNAME', bg = 'white', fg = 'steel blue', font=('Courier New', 20, 'bold'))
        self.lbl.place(x = 30, y = 90)

        self.entry = Entry(self.frame, width = 20, font=('Courier New', 20, 'bold'), bg = 'white')
        self.entry.place(x = 180, y = 90)

        self.lbl=  Label(self.frame, text= 'PASSWORD', bg = 'white', fg = 'steel blue', font=('Courier New', 20, 'bold'))
        self.lbl.place(x = 30, y = 150)

        self.entry = Entry(self.frame, width = 20, font=('Courier New', 20, 'bold'), bg = 'white')
        self.entry.place(x = 180, y = 150)

        self.book_button = tk.Button(root, text="Login", command=self.MovieTicketBookingApp(root))
        self.book_button.place(x = 250, y = 280)

    def MovieTicketBookingApp(self, root):
        self.root = root
        self.root.title("MiniPlex - Movie Ticket Booking")

        self.frame = Frame(self.root, width = 550, height = 350, bd = 6, relief = 'ridge', bg = 'white')
        self.frame.place(x= 0,y= 0)

        # Movie options
        self.movies = ["Devil","Salaar"]  # Replace with actual movie names
        self.selected_movie = tk.StringVar(root)
        self.selected_movie.set(self.movies[0])

        # Booking details
        self.name_label = tk.Label(root, text="Your Name:")
        self.name_label.place(x = 30, y = 90)
        self.name_entry = tk.Entry(root)
        self.name_entry.place(x = 180, y = 90)

        self.movie_label = tk.Label(root, text="Select Movie:")
        self.movie_label.place(x = 30,y = 150)
        self.movie_dropdown = tk.OptionMenu(root, self.selected_movie, *self.movies)
        self.movie_dropdown.place(x = 180, y = 150)

        # Number of tickets
        self.tickets_label = tk.Label(root, text="Number of Tickets:")
        self.tickets_label.place(x = 30, y = 210)
        self.tickets_entry = tk.Entry(root)
        self.tickets_entry.place(x = 180, y = 210)

        # Book button
        self.book_button = tk.Button(root, text="Book Tickets", command=self.book_tickets)
        self.book_button.place(x = 250, y = 250)

    def book_tickets(self):
        name = self.name_entry.get()
        movie = self.selected_movie.get()
        num_tickets = self.tickets_entry.get()

        if not name.strip() or not num_tickets.strip():
            messagebox.showerror("Error", "Please enter your name and the number of tickets.")
        elif not num_tickets.isdigit() or int(num_tickets) <= 0:
            messagebox.showerror("Error", "Please enter a valid number of tickets.")
        else:
            message = f"Tickets booked for {name} for {movie}. Number of tickets: {num_tickets}. Enjoy the movie!"
            messagebox.showinfo("Booking Successful", message)




root = tk.Tk()

root.title('LOGIN PAGE')
root.geometry('550x350+550+200')
home = Home(root)
root.mainloop()