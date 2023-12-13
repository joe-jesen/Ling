import tkinter as tk
from time import strftime

def update_time():
    time_string = strftime('%H:%M:%S')  # 获取当前时间
    time_label.config(text=time_string)  # 更新标签文本
    root.after(1000, update_time)  # 每隔一秒更新时间

# 创建主窗口
root = tk.Tk()
root.title("时钟")

# 创建标签用于显示时间
time_label = tk.Label(root, font=('Arial', 80), bg='white')
time_label.pack(padx=50, pady=50)

# 启动时钟
update_time()

# 运行主循环
root.mainloop()

# 这段代码使用了tkinter模块创建了一个简单的GUI窗口，并在窗口中创建了一个标签用于显示当前时间。
# update_time函数通过调用strftime函数获取当前时间，并通过config方法更新标签的文本内容。然后，使用root.after方法设定每隔一秒调用一次update_time函数来更新时间。
# 通过调用root.mainloop方法运行主循环，使得窗口保持显示并持续更新时间。
# 你可以将这段代码保存为.py文件并运行，即可看到一个实时更新的时钟显示。
