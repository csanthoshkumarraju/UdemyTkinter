import tkinter as tk
from tkinter import ttk
# import tkinter.font as font
#
# # def greet():
# #     print(f"Hello, {user_name.get() or 'guest'}")
# # # def greet1():
# # #     print("welcome to tkinter")
# #
# # root = tk.Tk()
# # user_name = tk.StringVar()
# # # ttk.Label(root,text="Hello, World!",padding=(30,10)).pack()
# # name_label = ttk.Label(root,text="Name: ")
# # name_label.pack(side="left",padx=(0,10))
# # name_entry = ttk.Entry(root,width=15,textvariable=user_name)
# # name_entry.pack(side="left")
# # name_entry.focus()
# #
# # greet_button = ttk.Button(root,text="Greet",command=greet)
# # # greet_button1 = ttk.Button(root,text="Welcome",command=greet1)
# # greet_button.pack(side="left", fill="both",expand=True)
# # # greet_button1.pack(side="right")
# # quit_button = ttk.Button(root,text="Quit",command=root.destroy)
# # quit_button.pack()
# # root.mainloop()
#
#
# # =======================================================================================
# # ***************************************************************************************
# # =======================================================================================
# # from windows import set_dpi_awareness
# # set_dpi_awareness()
# # from PIL import ImageTk, Image
# # root = tk.Tk()
# # root.geometry("600x400")
# # root.resizable(False,False)
# # root.title("Widget Examples")
# # # label = ttk.Label(root,text = "Hello World",padding=20)
# # # label.config(font=("Segoe UI",20))
# # # image = Image.open("")
# # # label = ttk.Label(root,image=image,padding=5)
# # # label.pack()
# # text = tk.Text(root,height = 8)
# # text.pack()
# # text.insert("1.0","Please enter a comment................")
# # # text["state"] = "disabled"
# # text["state"] = "normal"
# # text_content = text.get("1.0","end")
# # text_scroll = ttk.Scrollbar(root,orient="vertical",command = text.yview)
# # # text_scroll.grid(row=0,column=1,sticky="ns")
# # text_scroll.pack(side="right", fill="y")
# #   # Use pack for scrollbar
# # text.config(yscrollcommand=text_scroll.set)
# #
# # root.mainloop()
#
# # =======================================================================================
# # ***************************************************************************************
# # =======================================================================================
# # root = tk.Tk()
# # root.geometry("600x400")
# # root.title("Widget Examples")
# # root.resizable(False,False)
# # root.mainloop()
# # text.pack()
# # =======================================================================================
# # ***************************************************************************************
# # =======================================================================================
#
# # root = tk.Tk()
# # root.geometry("600x400")
# # root.resizable(False,False)
# # root.title("Widget Examples")
# # root.grid_columnconfigure(0,weight=1)
# # root.grid_rowconfigure(0,weight=1)
# # ttk.Label(root,text="Hello world",padding = 20).pack()
# # ttk.Separator(root,orient="horizontal").pack(fill="x")
# # ttk.Label(root,text="Hello world",padding = 20).pack()
# # root.mainloop()
#
# # =======================================================================================
# # ***************************************************************************************
# # =======================================================================================
# # root = tk.Tk()
# # root.geometry("600x400")
# # root.title("Widget Examples")
# # root.resizable(False,False)
# # check_button = ttk.Checkbutton(root,text="Check me")
# # check_button.pack()
# # storage_variable = tk.StringVar()
# # option_one = ttk.Radiobutton(root,text="Option 1",variable=storage_variable,value="First option")
# # option_two = ttk.Radiobutton(root,text="Option 2",variable=storage_variable,value="Second option")
# # option_three = ttk.Radiobutton(root,text="Option 3",variable=storage_variable,value="Third option")
# # option_one.pack()
# # option_two.pack()
# # option_three.pack()
# # root.mainloop()
#
#
# # =======================================================================================
# # ***************************************************************************************
# # =======================================================================================
#
# # root = tk.Tk()
# # root.geometry("600x400")
# # root.title("Widget Examples")
# # root.resizable(False,False)
# # # selected_weekday = tk.StringVar()
# # # weekday = ttk.Combobox(root,textvariable=selected_weekday)
# # # weekday["values"] = ("Monday","Tuesday","Wednesday","Thursday","Friday","Saturday")
# # # weekday["state"] = "readonly"
# # # weekday.pack()
# # programming_languages = ("C","GO Lang","Javascript","Perl","Python","Rust")
# # langs = tk.StringVar(value=programming_languages)
# # langs_select = tk.Listbox(root,listvariable=langs,height=6,selectmode="extended")
# # langs_select.pack()
# #
# # root.mainloop()
#
#
# # =======================================================================================
# # ***************************************************************************************
# # =======================================================================================
# #       *****************    Distance Convertor App *************************
# # =======================================================================================
# # ***************************************************************************************
# # =======================================================================================
#
# # root = tk.Tk()
# # root.title("Distance Convertor")
# # font.nametofont("TkDefaultFont").configure(size=15)
# # metres_value = tk.StringVar()
# # feet_value = tk.StringVar(value="Feet shown here")
# # def calculate_feet(*args):
# #     try:
# #         metres = float(metres_value.get())
# #         feet = metres * 3.28084
# #         feet_value.set(f"{feet:.3f}")
# #         # print(f"{metres} metres is equal to {feet:.3f} feet.")
# #     except ValueError:
# #         pass
# #
# #
# # root.columnconfigure(0,weight=1)
# # main = ttk.Frame(root,padding=(30,15))
# # main.grid()
# #
# # metres_label = ttk.Label(main,text="Metres:")
# # metres_input = ttk.Entry(main,width=10,textvariable=metres_value,font=("Segoe UI",15))
# # feet_label = ttk.Label(main,text="Feet:")
# # feet_display = ttk.Label(main,textvariable=feet_value)
# # calc_button = ttk.Button(main,text="Calculate",command=calculate_feet)
# #
# # metres_label.grid(column=0,row=0,sticky="W",padx=5,pady=5)
# # metres_input.grid(column=1,row=0,sticky="EW",padx=5,pady=5)
# # metres_input.focus()
# # feet_label.grid(column=0,row = 1,sticky = "W",padx=5,pady=5)
# # feet_display.grid(column=1,row = 1,sticky="EW",padx=5,pady=5)
# # calc_button.grid(column=1,row = 2,columnspan=2,sticky="EW",padx=5,pady=5)
# # for child in main.winfo_children():
# #     child.grid_configure(padx=15,pady=15)
# #
# # root.bind("<Return>",calculate_feet)
# # root.bind("<KP_Enter>",calculate_feet)
# # root.mainloop()
#
#
# # =======================================================================================
# # ***************************************************************************************
# # =======================================================================================
#
# # class Helloworld(tk.Tk):
# #     def __init__(self):
# #         super().__init__()
# #         self.title("Hello World")
# #         ttk.Label(self,text="Hello World").pack()
# # root = Helloworld()
# # class HelloWorld(tk.Tk):
# #     def __init__(self):
# #         super().__init__()
# #         self.title("Hello World")
# #         UserInputFrame(self).pack()
# #
# #
# # class UserInputFrame(ttk.Frame):
# #     def __init__(self,container):
# #          super().__init__(container)
# #
# #          self.user_input = tk.StringVar()
# #          label = ttk.Label(self,text="Enter your name:")
# #          entry = ttk.Entry(self,textvariable=self.user_input)
# #          button = ttk.Button(self,text="Greet",command=self.greet)
# #          label.pack(side="left")
# #          entry.pack(side="left")
# #          button.pack(side="left")
# #
# #     def greet(self):
# #         print(f"Hello {self.user_input.get()}")
# #
# # # root = tk.Tk()
# # root = HelloWorld()
# # # frame = UserInputFrame(root)
# # # frame.pack()
# # # label = ttk.Label(frame,text="Enter your name:")
# #
# # root.mainloop()
#
#
# # =======================================================================================
# # ***************************************************************************************
# # =======================================================================================
#
# class DistanceConvertor(tk.Tk):
#     def __init__(self,*args,**kwargs):
#         super().__init__(*args,**kwargs)
#
#         self.title("Distance Convertor")
#
#         container = ttk.Frame(self)
#         container.grid(padx=60,pady=30,sticky="EN")
#
#
#         frame =MetresToFeet(self,padding=(30,15))
#         frame.grid(row=0,column=0,sticky="NSEW")
#
#         self.bind("<Return>", frame.calculate_feet)
#         self.bind("<KP_Enter>", frame.calculate_feet)
#
# class MetresToFeet(ttk.Frame):
#     def __init__(self,container,**kwargs):
#         super().__init__(container,**kwargs)
#         self.metres_value = tk.StringVar()
#         self.feet_value = tk.StringVar(value="Feet shown here")
#
#         metres_label = ttk.Label(self, text="Metres:")
#         metres_input = ttk.Entry(self, width=10, textvariable=self.metres_value, font=("Segoe UI", 15))
#         feet_label = ttk.Label(self, text="Feet:")
#         feet_display = ttk.Label(self, textvariable=self.feet_value)
#         calc_button = ttk.Button(self, text="Calculate", command=self.calculate_feet)
#
#         metres_label.grid(column=0, row=0, sticky="W", padx=5, pady=5)
#         metres_input.grid(column=1, row=0, sticky="EW", padx=5, pady=5)
#         metres_input.focus()
#         feet_label.grid(column=0, row=1, sticky="W", padx=5, pady=5)
#         feet_display.grid(column=1, row=1, sticky="EW", padx=5, pady=5)
#         calc_button.grid(column=1, row=2, columnspan=2, sticky="EW", padx=5, pady=5)
#         for child in self.winfo_children():
#             child.grid_configure(padx=15, pady=15)
#
#     def calculate_feet(self,*args):
#         try:
#             metres = float(self.metres_value.get())
#             feet = metres * 3.28084
#             self.feet_value.set(f"{feet:.3f}")
#             # print(f"{metres} metres is equal to {feet:.3f} feet.")
#         except ValueError:
#             pass
#
#
#
#
# # root = DistanceConvertor()
# # root.title("Distance Convertor")
# # font.nametofont("TkDefaultFont").configure(size=15)
# # metres_value = tk.StringVar()
# # feet_value = tk.StringVar(value="Feet shown here")
# # def calculate_feet(*args):
# #     try:
# #         metres = float(metres_value.get())
# #         feet = metres * 3.28084
# #         feet_value.set(f"{feet:.3f}")
# #         # print(f"{metres} metres is equal to {feet:.3f} feet.")
# #     except ValueError:
# #         pass
#
#
# # root.columnconfigure(0,weight=1)
# # main = ttk.Frame(root,padding=(30,15))
# # main.grid()
#
# # metres_label = ttk.Label(root.frame,text="Metres:")
# # metres_input = ttk.Entry(root.frame,width=10,textvariable=metres_value,font=("Segoe UI",15))
# # feet_label = ttk.Label(root.frame,text="Feet:")
# # feet_display = ttk.Label(root.frame,textvariable=feet_value)
# # calc_button = ttk.Button(root.frame,text="Calculate",command=calculate_feet)
#
# # metres_label.grid(column=0,row=0,sticky="W",padx=5,pady=5)
# # metres_input.grid(column=1,row=0,sticky="EW",padx=5,pady=5)
# # metres_input.focus()
# # feet_label.grid(column=0,row = 1,sticky = "W",padx=5,pady=5)
# # feet_display.grid(column=1,row = 1,sticky="EW",padx=5,pady=5)
# # calc_button.grid(column=1,row = 2,columnspan=2,sticky="EW",padx=5,pady=5)
# # for child in root.frame.winfo_children():
# #     child.grid_configure(padx=15,pady=15)
#
# # root.bind("<Return>",calculate_feet)
# # root.bind("<KP_Enter>",calculate_feet)
# # root.mainloop()
#
#
# # =======================================================================================
# # ***************************************************************************************
# # =======================================================================================
# class FeetToMetres(ttk.Frame):
#     def __init__(self ,**kwargs):
#         super().__init__(**kwargs)
#         self.metres_value = tk.StringVar()
#         self.feet_value = tk.StringVar(value="Feet shown here")
#
#         feet_label = ttk.Label(self, text="Fetes:")
#         feet_input = ttk.Entry(self, width=10, textvariable=self.feet_value, font=("Segoe UI", 15))
#         metres_label = ttk.Label(self, text="Metres:")
#         metres_display = ttk.Label(self, textvariable=self.feet_value)
#         calc_button = ttk.Button(self, text="Calculate", command=self.calculate_metres)
#
#         feet_label.grid(column=0, row=0, sticky="W")
#         metres_label.grid(column=0, row=0, sticky="W")
#         feet_input.grid(column=1, row=0, sticky="EW")
#         feet_input.focus()
#
#         metres_display.grid(column=1, row=1, sticky="EW")
#         calc_button.grid(column=1, row=2, columnspan=2, sticky="EW")
#         for child in self.winfo_children():
#             child.grid_configure(padx=15, pady=15)
#
#     def calculate_metres(self, *args):
#         try:
#             feet = float(self.feet_value.get())
#             metres = feet / 3.28084
#             self.feet_value.set(f"{metres:.3f}")
#             # print(f"{metres} metres is equal to {feet:.3f} feet.")
#         except ValueError:
#             pass
#
#
# root = FeetToMetres()
# font.nametofont("TkDefaultFont").configure(size=15)
# root.columnconfigure(0, weight=1)
# root.mainloop()
# 
#
# # =======================================================================================
# # ***************************************************************************************
# # =======================================================================================

# def greet():
#     print(f"Hello, {user_name.get() or 'guest'}")
# # def greet1():
# #      print("welcome to tkinter")
# root = tk.Tk()
# # root.resizable(False,False)
# root.title("Greeter")
# style = ttk.Style(root)
# # print(style.theme_names()) --('aqua', 'clam', 'alt', 'default', 'classic')
# # print(style.theme_use())  --aqua
# # print(style.theme_use('classic'))
#
# user_name = tk.StringVar()
# # ttk.Label(root,text="Hello, World!",padding=(30,10)).pack()
# name_label = ttk.Label(root,text="Name: ")
# name_label.pack(side="left",padx=(0,10))
# name_entry = ttk.Entry(root,width=15,textvariable=user_name)
# name_entry.pack(side="left")
# name_entry.focus()
#
# greet_button = ttk.Button(root,text="Greet",command=greet)
# # greet_button1 = ttk.Button(root,text="Welcome",command=greet1)
# greet_button.pack(side="left", fill="both",expand=True)
# # greet_button1.pack(side="right")
# quit_button = ttk.Button(root,text="Quit",command=root.destroy)
# quit_button.pack()
# root.mainloop()

# # =======================================================================================
# # ***************************************************************************************
# # =======================================================================================
#
# root = tk.Tk()
# root.title("Widget")
# style = ttk.Style(root)
# style.configure("CustomerEntryStyle.TEntry",padding=30)
# # print(style.theme_use('classic'))
# name = ttk.Label(root,text="Hello world")
# entry = ttk.Entry(root,width=15)
# # entry = ttk.Entry(root,width=15)
# name.pack()
# entry.pack()
# entry["style"] = "CustomerEntryStyle.TEntry"
# style.configure("TLabel",font=("Segoe UI",20))
# # print(name["style"])
# # print(name.winfo_class())
# # print(style.layout("TLabel"))
# # print(style.element_options("Label.border"))
# # print(style.element_options("Label.padding"))
# # print(style.element_options("Label.label"))
# entry1 = ttk.Entry(root,width=15)
# entry1["style"] = "CustomerEntryStyle.TEntry"
# entry1.pack()
# root.mainloop()

# # =======================================================================================
# # ***************************************************************************************
# # =======================================================================================


# root = tk.Tk()
# root.title("Widget")
# style = ttk.Style(root)
# # style.configure("CustomButton.TButton")
# style.map("CustomButton.TButton",
#           foreground=[("pressed","red"),("active","green")],
#           background=[("pressed","!disabled","black")],
#           font=[("pressed",("TkDefaultFont",15))]
#           )
# name = ttk.Label(root,text="Hello world")
# entry = ttk.Entry(root,width=15)
# button = ttk.Button(root,text="Press me",style="CustomButton.TButton")
# name.pack()
# entry.pack()
# button.pack()
# root.mainloop()

# # =======================================================================================
# # ***************************************************************************************
# # =======================================================================================
# # Pomodoro Timer
# # =======================================================================================
# # ***************************************************************************************
# # =======================================================================================
# from collections import deque
# class PomodoroTimer(tk.Tk):
#     def __init__(self,*args,**kwargs):
#         super().__init__(*args,**kwargs)
#
#         self.title("Pomodoro Timer")
#         self.columnconfigure(0,weight=1)
#         self.rowconfigure(1,weight=1)
#
#         self.pomodoro = tk.StringVar(value=25)
#         self.long_break = tk.StringVar(value=15)
#         self.short_break = tk.StringVar(value=5)
#         self.timer_order = ["Pomodoro", "Short Break", "Pomodoro", "Short Break", "Pomodoro", "Long Break"]
#         self.timer_schedule = deque(self.timer_order)
#
#
#         container = ttk.Frame(self)
#         container.grid()
#         container.columnconfigure(0,weight=1)
#
#         timer_frame = Timer(container,self)
#         timer_frame.grid(row=0,column=0,sticky="NESW")
#
# class Timer(ttk.Frame):
#     def __init__(self,parent,controller):
#         super().__init__(parent)
#
#         self.controller = controller
#         pomodoro_time = int(controller.pomodoro.get())
#         self.current_time = tk.StringVar(value=f"{pomodoro_time:02d}:00")
#         self.timer_order = ["Pomodoro","Short Break","Pomodoro","Short Break","Pomodoro","Long Break"]
#         self.timer_schedule = deque(self.timer_order)
#         self.current_time_label = tk.StringVar(value=controller.timer_schedule[0])
#         self.timer_running = False
#
#         timer_description = ttk.Label(
#             self,
#             textvariable= self.current_time_label,
#         )
#
#         timer_description.grid(row=0,column=0,sticky="w",padx=(10,0),pady=(10,0))
#         timer_frame = ttk.Frame(self,height="100")
#         timer_frame.grid(row=1,column=0,pady=(10,0),sticky="NSEW")
#
#         timer_counter = ttk.Label(
#             timer_frame,
#             textvariable=self.current_time
#
#         )
#         timer_counter.place(relx=0.5,rely=0.5)
#         button_container = ttk.Frame(self,padding=10)
#         button_container.grid(row=2,column=0,sticky="EW")
#         button_container.columnconfigure((0,1,2),weight=1)
#
#         self.start_button = ttk.Button(
#             button_container,
#             text="Start",
#             command=self.start_timer,
#             cursor="hand2"
#         )
#         self.start_button.grid(row=0,column=0,sticky="EW")
#
#         self.stop_button = ttk.Button(
#             button_container,
#             text="Stop",
#             state = "disabled",
#             command=self.stop_timer,
#             cursor="hand2"
#         )
#         self.stop_button.grid(row=0, column=1, sticky="EW",padx=5)
#         reset_button = ttk.Button(
#             button_container,
#             text="Reset",
#             command=self.reset_timer,
#             cursor="hand2"
#         )
#
#         reset_button.grid(row=0,column=2,sticky="EW")
#     def start_timer(self):
#         self.timer_running = True
#         self.start_button["state"] = "disabled"
#         self.stop_button["state"] = "enabled"
#         self.decrement_time()
#
#     def stop_timer(self):
#         self.timer_running = False
#         self.start_button["state"] = "enabled"
#         self.stop_button["state"] = "disabled"
#         # self._timer_decrement_job = None
#         if self._timer_decrement_job:
#             self.after_cancel(self._timer_decrement_job)
#             self._timer_decrement_job = None
#
#     def reset_timer(self):
#         self.stop_timer()
#         pomodoro_time = int(self.controller.pomodoro.get())
#         self.current_time.set(f"{pomodoro_time:02d}:00")
#         self.controller.timer_schedule = deque(self.controller.timer_order)
#         self.current_time_label.set(self.controller.timer_schedule[0])
#
#     def decrement_time(self):
#         current_time = self.current_time.get()
#
#         if self.timer_running and current_time != "00:00":
#             minutes, seconds = map(int, current_time.split(":"))
#
#             if seconds > 0:
#                 seconds -= 1
#             elif minutes > 0:
#                 minutes -= 1
#                 seconds = 59
#
#             self.current_time.set(f"{minutes:02d}:{seconds:02d}")
#
#             # Schedule the next call to decrement_time
#             self._timer_decrement_job = self.after(1000, self.decrement_time)
#
#         elif self.timer_running and current_time == "00:00":
#             self.controller.timer_schedule.rotate(-1)
#             next_up = self.timer_schedule[0]
#             self.current_time_label.set(next_up)
#
#             if next_up == "Pomodoro":
#                 pomodoro_time = int(self.controller.pomodoro.get())
#                 self.current_time.set(f"{pomodoro_time:02d}:00")
#             elif next_up == "Short Break":
#                 short_break_time = int(self.controller.short_break.get())
#                 self.current_time.set(f"{short_break_time:02d}:00")
#             elif next_up == "Long Break":
#                 long_break_time = int(self.controller.long_break.get())
#                 self.current_time.set(f"{long_break_time:02d}:00")
#
#             # Schedule the next call to decrement_time
#             self._timer_decrement_job = self.after(1000, self.decrement_time)
#
#
# app = PomodoroTimer()
# app.mainloop()
#
#










