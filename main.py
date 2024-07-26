#!/usr/bin/env python3
# -*-coding:UTF-8 -*

import tkinter as tk

from gui import UserApp

if __name__ == '__main__':
    root = tk.Tk()
    root.title("User Management")
    app = UserApp(root)
    app.pack()
    input("Glad to have served you! Press 'Enter' to quit.")