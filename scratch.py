import tkinter as tk
from tkinter import ttk, messagebox
from mysql.connector import connect

conn = connect(
    host = 'localhost',
    user = 'root',
    password = 'Keerthi@1234',
    database = 'demo'
)

cursor = conn.cursor()

class MovieTicketBookingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("MiniPlex - Movie Ticket Booking")
        self.root.configure(bg = "#ADD8E6")

        self.login_frame = tk.Frame(root, bg = "#ADD8E6")
        self.signup_frame = tk.Frame(root, bg = "#ADD8E6")
        self.movie_frame = tk.Frame(root, bg = "#ADD8E6")
        self.tck_frame = tk.Frame(root, bg = "#ADD8E6")
        self.setup_login_frame()

    def setup_login_frame(self):
        self.hide_frame(self.signup_frame)
        self.login_frame.pack(padx = 10,pady=100)

        self.title_label = tk.Label(self.login_frame, text = "Login",bg = "#ADD8E6",fg = "black",font=('Courier New', 30, 'bold'))
        self.title_label.grid(row=0,column = 0,padx=5, pady=40,sticky = "news",columnspan = 2)
        self.username_label = tk.Label(self.login_frame, text="Username:", bg = '#ADD8E6', fg = 'black', font=('Courier New', 20, 'bold'))
        self.username_label.grid(row=1, column=0, padx=5, pady=20, sticky="e")
        self.username_entry = tk.Entry(self.login_frame, width = 20, font=('Courier New', 20, 'bold'), bg = 'white')
        self.username_entry.grid(row=1, column=1, padx=5, pady=20)

        self.password_label = tk.Label(self.login_frame, text="Password:",  bg = '#ADD8E6', fg = 'black', font=('Courier New', 20, 'bold'))
        self.password_label.grid(row=2, column=0, padx=5, pady=5, sticky="e")
        self.password_entry = tk.Entry(self.login_frame, show="*", width = 20, font=('Courier New', 20, 'bold'), bg = 'white')
        self.password_entry.grid(row=2, column=1, padx=5, pady=5)

        self.login_button = tk.Button(self.login_frame, text="Login", command=self.login, width = 10,height = 2, bg = "lightgrey")
        self.login_button.grid(row=3, columnspan=2, pady=30)

        self.label = tk.Label(self.login_frame, text = "Don't have an account?",bg = "#ADD8E6",fg = "black", font=('Courier New', 14, 'normal'))
        self.label.grid(row = 4, column = 0,padx = 5, pady=5,sticky = "e")
        self.signup_button = tk.Button(self.login_frame, text="Sign Up", command=self.setup_signup_frame,width = 10,height = 2, bg = "lightgrey")
        self.signup_button.grid(row=4, columnspan=2, pady=10)

    def setup_signup_frame(self):
        self.hide_frame(self.login_frame)
        self.signup_frame.pack(pady=20)

        self.new_username_label = tk.Label(self.signup_frame, text="New Username:", bg = '#ADD8E6', fg = 'black', font=('Courier New', 20, 'bold'))
        self.new_username_label.grid(row=0, column=0, padx=5, pady=5, sticky="e")
        self.new_username_entry = tk.Entry(self.signup_frame, width = 20, font=('Courier New', 20, 'bold'), bg = 'white')
        self.new_username_entry.grid(row=0, column=1, padx=5, pady=5)

        self.new_rollnumber_label = tk.Label(self.signup_frame, text="Roll Number:", bg = '#ADD8E6', fg = 'black', font=('Courier New', 20, 'bold'))
        self.new_rollnumber_label.grid(row=1, column=0, padx=5, pady=5, sticky="e")
        self.new_rollnumber_entry = tk.Entry(self.signup_frame, width = 20, font=('Courier New', 20, 'bold'), bg = 'white')
        self.new_rollnumber_entry.grid(row=1, column=1, padx=5, pady=5)

        self.new_hostel_label = tk.Label(self.signup_frame, text="Hostel:", bg = '#ADD8E6', fg = 'black', font=('Courier New', 20, 'bold'))
        self.new_hostel_label.grid(row=2, column=0, padx=5, pady=5, sticky="e")
        self.new_hostel_entry = tk.Entry(self.signup_frame, width = 20, font=('Courier New', 20, 'bold'), bg = 'white')
        self.new_hostel_entry.grid(row=2, column=1, padx=5, pady=5)

        self.new_password_label = tk.Label(self.signup_frame, text="New Password:", bg = '#ADD8E6', fg = 'black', font=('Courier New', 20, 'bold'))
        self.new_password_label.grid(row=3, column=0, padx=5, pady=5, sticky="e")
        self.new_password_entry = tk.Entry(self.signup_frame, show="*", width = 20, font=('Courier New', 20, 'bold'), bg = 'white')
        self.new_password_entry.grid(row=3, column=1, padx=5, pady=5)

        self.confirm_password_label = tk.Label(self.signup_frame, text="Confirm Password:", bg = '#ADD8E6', fg = 'black', font=('Courier New', 20, 'bold'))
        self.confirm_password_label.grid(row=4, column=0, padx=5, pady=5, sticky="e")
        self.confirm_password_entry = tk.Entry(self.signup_frame, show="*", width = 20, font=('Courier New', 20, 'bold'), bg = 'white')
        self.confirm_password_entry.grid(row=4, column=1, padx=5, pady=5)

        self.register_button = tk.Button(self.signup_frame, text="Register", command=self.register,bg = "lightgrey")
        self.register_button.grid(row=5, columnspan=2, pady=10)

        self.back_to_login_button = tk.Button(self.signup_frame, text="Back to Login", command=self.setup_login_frame,bg = "lightgrey")
        self.back_to_login_button.grid(row=6, columnspan=2, pady=5)
    

    def setup_movie_frame(self):
        self.hide_frame(self.login_frame)
        self.movie_frame.pack(padx = 100,pady=100)


        self.name_label = tk.Label(self.movie_frame, text="Name:", bg = '#ADD8E6', fg = 'black', font=('Courier New', 20, 'bold'))
        self.name_label.grid(row=0, column=0, padx=5, pady=5, sticky="e")
        self.name_entry = tk.Entry(self.movie_frame, width = 10, font=('Courier New', 20, 'bold'), bg = 'white')
        self.name_entry.grid(row=0, column=1, padx=5, pady=5)

        self.roll_label = tk.Label(self.movie_frame, text="Roll Number:", bg = '#ADD8E6', fg = 'black', font=('Courier New', 20, 'bold'))
        self.roll_label.grid(row=1, column=0, padx=5, pady=5, sticky="e")
        self.roll_entry = tk.Entry(self.movie_frame, width = 10, font=('Courier New', 20, 'bold'), bg = 'white')
        self.roll_entry.grid(row=1, column=1, padx=5, pady=5)
        
        self.movie_label = tk.Label(self.movie_frame, text="Enter Movie :", bg = '#ADD8E6', fg = 'black', font=('Courier New', 20, 'bold'))
        self.movie_label.grid(row=2, column=0, padx=5, pady=5, sticky="e")
        self.movie_entry = tk.Entry(self.movie_frame,width = 10, bg = 'white', font=('Courier New', 15, 'bold'))
        self.movie_entry.grid(row=2, column=1, padx=5, pady=5)

        self.date_label = tk.Label(self.movie_frame, text="Select Date:", bg = '#ADD8E6', fg = 'black', font=('Courier New', 20, 'bold'))
        self.date_label.grid(row=3, column=0, padx=5, pady=5, sticky="e")
        self.date_picker = ttk.Combobox(self.movie_frame, values=["14-03-2024", "15-03-2024", "16-03-2024"])
        self.date_picker.grid(row=3, column=1, padx=5, pady=5)

        self.time_label = tk.Label(self.movie_frame, text="Select Time:", bg = '#ADD8E6', fg = 'black', font=('Courier New', 20, 'bold'))
        self.time_label.grid(row=4, column=0, padx=5, pady=5, sticky="e")
        self.time_picker = ttk.Combobox(self.movie_frame, values=["12:00 PM", "3:00 PM", "6:00 PM"])
        self.time_picker.grid(row=4, column=1, padx=5, pady=5)


        self.tickets_label = tk.Label(self.movie_frame, text="No.of Tickets:",  bg = '#ADD8E6', fg = 'black', font=('Courier New', 20, 'bold'))
        self.tickets_label.grid(row=5, column=0, padx=5, pady=5, sticky="e")
        self.tickets_entry = tk.Entry(self.movie_frame, width = 10, font=('Courier New', 20, 'bold'), bg = 'white')
        self.tickets_entry.grid(row=5, column=1, padx=5, pady=5)

        self.payment1_label = tk.Label(self.movie_frame, text="Enter Card Number:", bg = '#ADD8E6', fg = 'black', font=('Courier New', 20, 'bold'))
        self.payment1_label.grid(row=6, column=0, padx=5, pady=5, sticky="e")
        self.payment1_entry = tk.Entry(self.movie_frame,width = 20,font=('Courier New', 20, 'bold'), bg = 'white')
        self.payment1_entry.grid(row=6, column=1, padx=5, pady=5)

        self.payment2_label = tk.Label(self.movie_frame, text="Enter CVV:", bg = '#ADD8E6', fg = 'black', font=('Courier New', 20, 'bold'))
        self.payment2_label.grid(row=7, column=0, padx=5, pady=5, sticky="e")
        self.payment2_entry = tk.Entry(self.movie_frame,width = 20,font=('Courier New', 20, 'bold'), bg = 'white')
        self.payment2_entry.grid(row=7, column=1, padx=5, pady=5)

        self.book_button = tk.Button(self.movie_frame, text="Book Tickets", command=self.book_tickets, width = 10 ,height = 2, bg = "lightgrey")
        self.book_button.grid(row=8, columnspan=2, pady=10)

        self.back_to_login_button = tk.Button(self.movie_frame, text="Back to Main", command=self.back_to_main,bg = "lightgrey")
        self.back_to_login_button.grid(row=9, columnspan=2, pady=5)
        
    def book_tickets(self):
        selected_date = self.date_picker.get()
        selected_time = self.time_picker.get()
        name = self.name_entry.get()
        roll = self.roll_entry.get()


        if not selected_date or not selected_time or not name or not roll:
            messagebox.showerror("Error", "Please enter the required details")
        else:
            self.name = self.name_entry.get()
            self.roll = self.roll_entry.get()
            self.movie = self.movie_entry.get()
            self.date = self.date_picker.get()
            self.time = self.time_picker.get()
            self.tickets = self.tickets_entry.get()
            self.payment1 = self.payment1_entry.get()
            self.payment2 = self.payment2_entry.get()

            messagebox.showinfo("booked","Tickets are booked successfully.")
            
            self.hide_frame(self.movie_frame)
            self.tck_frame.pack(padx = 100,pady=100)

            self.details_label = tk.Label(self.tck_frame, text = 'Name:    '+  self.name, bg = '#ADD8E6', fg = 'black', font=('Courier New', 20, 'bold'))
            self.details_label.grid(row=1, column=1, padx=5, pady=20)

            self.movie_label = tk.Label(self.tck_frame, text = 'Name of the movie:    ' + self.movie, bg = '#ADD8E6', fg = 'black', font=('Courier New', 20, 'bold'))
            self.movie_label.grid(row=2, column=1, padx=5, pady=20)

            self.booked_tickets_label = tk.Label(self.tck_frame, text = 'Number of tickets booked:    ' + self.tickets, bg = '#ADD8E6', fg = 'black', font=('Courier New', 20, 'bold'))
            self.booked_tickets_label.grid(row=3, column=1, padx=5, pady=20)

            self.movie_date_label = tk.Label(self.tck_frame, text = 'Date:    ' + self.date, bg = '#ADD8E6', fg = 'black', font=('Courier New', 20, 'bold'))
            self.movie_date_label.grid(row=4, column=1, padx=5, pady=20)

            self.movie_time_label = tk.Label(self.tck_frame, text = 'Time:    ' + self.time, bg = '#ADD8E6', fg = 'black', font=('Courier New', 20, 'bold'))
            self.movie_time_label.grid(row=5, column=1, padx=5, pady=20)


            self.query = "INSERT INTO ticket_details (name, roll, movie, date, time, tickets, payment1, payments2) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
            self.values = (self.name, self.roll, self.movie, self.date, self.time, self.tickets, self.payment1, self.payment2)
            cursor.execute(self.query, self.values)
            conn.commit()

            

            messagebox.showinfo('booked',f'Booked Sucessfully')

            

    def hide_frame(self, frame):
        frame.pack_forget()

    def login(self): 
        cursor.execute('select * from users_detail;')
        self.users = cursor.fetchall()
        self.names = [i[0] for i in self.users]
        self.password = [i[3] for i in self.users]
        username1 = self.username_entry.get()
        password1 = self.password_entry.get()
        
        if username1[0].isdigit():
            messagebox.showerror("Error", "Username is invalid.")
        
        if len(password1) < 6:
            messagebox.showerror("Invalid","Password length must be greater than or equal to 6.")

        elif username1 in self.names and self.password_entry.get() in self.password:
            messagebox.showinfo("Login Successful", "Welcome to MiniPlex!")
            self.setup_movie_frame()

        else:
            messagebox.showerror("Login Failed", "Invalid username or password")

    def register(self):
        new_username = self.new_username_entry.get()
        new_rollnumber = self.new_rollnumber_entry.get()
        new_hostel = self.new_hostel_entry.get()
        new_password = self.new_password_entry.get()
        confirm_password = self.confirm_password_entry.get()
    


        cursor.execute("SELECT * FROM users_detail;")
        self.users = cursor.fetchall()
        self.names = [name[0] for name in self.users]

        if not new_username.strip() or not new_password.strip() or not confirm_password.strip():
            messagebox.showerror("Error", "Please fill in all fields.")
        elif new_password != confirm_password:
            messagebox.showerror("Error", "Passwords do not match.")
        elif new_username in self.names:
            messagebox.showerror("Error", "Username already exists. Please choose another one.")
        else:
            messagebox.showinfo("Registration Successful", "Account created successfully!")
            self.query = "insert into users_detail(Name, Roll, Hostel, Password) values(%s,%s,%s,%s)"
            self.values = (new_username,new_rollnumber,new_hostel,new_password)
            cursor.execute(self.query,self.values)
            conn.commit()


    def back_to_main(self):
        self.hide_frame(self.payment_frame)
        self.home = MovieTicketBookingApp(root)

    def pay(self):
        card_number = self.payment1_entry.get()
        cvv = self.payment2_entry.get()

        if (not card_number or not card_number.isdigit() or len(card_number) != 12) and (not cvv or not cvv.isdigit() or len(cvv) != 3):
            messagebox.showerror("Error", "Please enter a valid 16-digit card number.")
        else:
            return self.tck_details()
            
    def tck_details(self):
        self.rollnumber = self.new_rollnumber_entry.get()
        self.hide_frame(self.payment_frame)
        self.msg_frame.pack(padx = 100,pady=100)
        

root = tk.Tk()
movie_booking_app = MovieTicketBookingApp(root)

root.mainloop()
