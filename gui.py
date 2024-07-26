import tkinter as tk
import database as db

from tkinter import messagebox 


class UserApp(tk.Frame):
    def __init__(self, master)-> None:
        super().__init__(master=master)
        
        self.username_label = tk.Label(self, text="Username (Old)")
        self.username_label.pack()
        
        self.username_entry = tk.Entry(self)
        self.username_entry.pack()
        
        self.add_rm_user_frame = tk.Frame(self)
        self.add_rm_user_frame.pack()
        
        self.add_btn = tk.Button(self.add_rm_user_frame, text="Add user", command=lambda: (self.add_user(), self.show_users()))
        self.add_btn.pack(side=tk.LEFT)
        
        self.delete_btn = tk.Button(self.add_rm_user_frame, text="Remove user", command=lambda: (self.delete_user(), self.show_users()))
        self.delete_btn.pack(side=tk.RIGHT)
        
        self.new_username_label = tk.Label(self, text="Username (New)")
        self.new_username_label.pack()
        
        self.new_username_entry = tk.Entry(self)
        self.new_username_entry.pack()
        
        self.update_user_btn = tk.Button(self, text="Update User", command=lambda: (self.update_user(), self.show_users()))
        self.update_user_btn.pack()
        
        self.show_users_btn = tk.Button(self, text="Show Users", command=self.show_users)
        self.show_users_btn.pack()
        
        self.users_label = tk.Label(self, text="Users")
        self.users_label.pack()
        
        self.users_listbox = tk.Listbox(self)
        self.users_listbox.pack()
        
        db.create_db()
        
    def add_user(self):
        username = self.username_entry.get()
        if username:
            result = db.add_user(username)
            if result == db.OPERATION_SUCCESS:
                messagebox.showinfo("Success", "User added successfully!")
                self.username_entry.delete(0, tk.END)
            elif result == db.INTEGRITY_ERROR:
                messagebox.showerror("Error", "Username already exists!")
            else:
                messagebox.showerror("Error", "Unknown Error!")
        else:
            messagebox.showerror("Error", "Username cannot be empty!")
            
    def show_users(self)-> None:
        self.users_listbox.delete(0, tk.END)
        users = db.get_users()
        for user in users:
            self.users_listbox.insert(tk.END, user[0])
            
    def delete_user(self):
        username = self.username_entry.get()
        if username:
            result = db.delete_user(username)
            if result == db.OPERATION_SUCCESS:
                messagebox.showinfo("Success", "User deleted successfully")
                self.username_entry.delete(0, tk.END)
            else:
                messagebox.showerror("Error", "User not found")
        else:
            messagebox.showerror("Error", "Username connot be empty")
            
    def update_user(self)-> None:
        old_username = self.username_entry.get()
        new_username = self.new_username_entry.get()
        
        if not old_username:
            messagebox.showerror("Error", "The old username must not be empty!")
            return
            
        if not new_username:
            messagebox.showerror("Error", "The new username must not be empty!")
            return
            
        result = db.update_user(old_username, new_username)
            
        if result == db.OPERATION_SUCCESS:
            messagebox.showinfo("Success", "Username updated successfully!")
            self.username_entry.delete(0, tk.END)
            self.new_username_entry.delete(0, tk.END)
        elif result == db.USER_NOT_FOUND_ERROR:
            messagebox.showerror("Error", "User not found!")
        elif result == db.INTEGRITY_ERROR:
            messagebox.showerror("Error", "New username already exists!")
        else:
            messagebox.showerror("Error", "Unknown Error!")