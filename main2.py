import threading
import time
from tkinter import *
import sys


class Elevator:

    def __init__(self, name, head, array, direction):
        self.name = name
        self.array = array
        self.head = head
        self.head_tmp = head
        self.direction = direction
        self.size = len(self.array)
        self.is_finished_2 = False
        self.down = []
        self.up = []

    def find_direction(self):

        down_ = []
        up_ = []
        down_sum = 0
        up_sum = 0

        for i in range(len(self.array)):
            if self.array[i] < self.head:
                down_.append(self.array[i])
            if self.array[i] > self.head:
                up_.append(self.array[i])

        for i in range(len(down_) - 1):
            down_sum = abs(down_[i] - down_[i + 1])

        for i in range(len(up_) - 1):
            up_sum = abs(up_[i] - up_[i + 1])

        if down_sum < up_sum:
            return "down"
        else:
            return "up"

    def scan(self):
        while True:
            self.down = []
            self.up = []
            self.direction = self.find_direction()
            size = len(self.array)
            print(self.name)
            # print(f"current request list for this elevator: {self.array}")
            seek_count = 0
            seek_sequence = []

            for i in range(size):
                if self.array[i] < self.head:
                    self.down.append(self.array[i])
                if self.array[i] > self.head:
                    self.up.append(self.array[i])

            # print(f"up: {self.up}")
            # print(f"down: {self.down}")

            self.down.sort()
            self.up.sort()

            run = 2

            while run != 0:
                if self.direction == "down":

                    for i in range(len(self.down) - 1, -1, -1):
                        try:
                            cur_track = self.down[i]
                            seek_sequence.append(cur_track)
                            # print(f"current floor: {cur_track}")
                            self.array.remove(cur_track)
                            distance = abs(cur_track - self.head)
                            seek_count += distance
                            self.head = cur_track
                        except:
                            pass
                        time.sleep(5)

                    self.direction = "up"

                elif self.direction == "up":
                    for i in range(len(self.up)):
                        try:
                            cur_track = self.up[i]
                            seek_sequence.append(cur_track)
                            # print(f"current floor: {cur_track}")
                            self.array.remove(cur_track)
                            distance = abs(cur_track - self.head)
                            seek_count += distance
                            self.head = cur_track
                        except:
                            pass
                        time.sleep(5)

                    self.direction = "down"

                run -= 1

            if len(seek_sequence) == 0:
                exit(0)

            self.is_finished_2 = True


class GUI:
    arr1 = [1,5,2,4]
    arr2 = [1]
    arr3 = [1]

    head1 = 3
    head2 = 5
    head3 = 5

    first_elevator = Elevator("Elevator1", head1, arr1, None)
    second_elevator = Elevator("Elevator2", head2, arr2, None)
    third_elevator = Elevator("Elevator3", head3, arr3, None)

    def __init__(self):

        self.bound = None
        self.paused = False
        self.Button1 = None
        self.Button2 = None
        self.Button3 = None
        self.Button4 = None
        self.Button5 = None
        self.Button6 = None
        self.E2Button1 = None
        self.E2Button2 = None
        self.E2Button3 = None
        self.E2Button4 = None
        self.E2Button5 = None
        self.E2Button6 = None
        self.Enter1 = None
        self.Enter2 = None
        self.Enter3 = None
        self.Enter4 = None
        self.Enter5 = None
        self.Enter6 = None
        self.E2Button1 = None
        self.E2Button2 = None
        self.E2Button3 = None
        self.E2Button4 = None
        self.E2Button5 = None
        self.E2Button6 = None
        self.E3Button1 = None
        self.E3Button2 = None
        self.E3Button3 = None
        self.E3Button4 = None
        self.E3Button5 = None
        self.E3Button6 = None
        self.labelBottom = None
        self.labelHead = None
        self.root = None
        self.canvas = None
        self.rectangle = None
        self.rectangle2 = None
        self.rectangle3 = None
        # self.master = master

        self.x = 1
        self.y = 0
        self.current_y = 275 - 50 * (GUI.first_elevator.head_tmp - 1)

        self.x2 = 1
        self.y2 = 0
        self.current_y2 = 275 - 50 * (GUI.second_elevator.head_tmp - 1)

        self.x3 = 1
        self.y3 = 0
        self.current_y3 = 275 - 50 * (GUI.third_elevator.head_tmp - 1)

    def root_window(self):
        self.root = Tk()

        # self.root.withdraw()
        # self.root.deiconify()

        self.root.title("Elevator Simulator")
        # self.root.resizable(width=False,
        #                     height=False)
        #
        # self.root.configure(width=900,
        #                     height=550,
        #                     bg="#991532")

        self.canvas = Canvas(self.root, bg="#991532", height=550, width=1000)

        self.rectangle = self.canvas.create_rectangle(
            20, 275 - 50 * (GUI.first_elevator.head - 1), 45, 275 - 50 * (GUI.first_elevator.head - 1) + 25,
            fill="#f06b32")

        self.rectangle2 = self.canvas.create_rectangle(
            220, 275 - 50 * (GUI.second_elevator.head - 1), 245, 275 - 50 * (GUI.second_elevator.head - 1) + 25,
            fill="#32f0b7")

        self.rectangle3 = self.canvas.create_rectangle(
            420, 275 - 50 * (GUI.second_elevator.head - 1), 445, 275 - 50 * (GUI.second_elevator.head - 1) + 25,
            fill="#69f06c")

        self.movement()

        self.canvas.pack()

        self.Button6 = Button(self.labelBottom, text="6", font=("showcard gothic", 16, "bold"), width=5, bg="#FEC84D", fg="#004369")
        self.Button6.place(x=50, y=25, height=50, width=50)
        self.Button5 = Button(self.labelBottom, text="5", font=("showcard gothic", 16, "bold"), width=5, bg="#FEC84D", fg="#004369", )
        self.Button5.place(x=50, y=75, height=50, width=50)
        self.Button4 = Button(self.labelBottom, text="4", font=("showcard gothic", 16, "bold"), width=5, bg="#FEC84D", fg="#004369", )
        self.Button4.place(x=50, y=125, height=50, width=50)
        self.Button3 = Button(self.labelBottom, text="3", font=("showcard gothic", 16, "bold"), width=5, bg="#FEC84D", fg="#004369", )
        self.Button3.place(x=50, y=175, height=50, width=50)
        self.Button2 = Button(self.labelBottom, text="2", font=("showcard gothic", 16, "bold"), width=5, bg="#FEC84D", fg="#004369", )
        self.Button2.place(x=50, y=225, height=50, width=50)
        self.Button1 = Button(self.labelBottom, text="1", font=("showcard gothic", 16, "bold"), width=5, bg="#FEC84D", fg="#004369", )
        self.Button1.place(x=50, y=275, height=50, width=50)

        self.E2Button6 = Button(self.labelBottom, text="6", font=("showcard gothic", 16, "bold"), width=5, bg="#FEC84D", fg="#004369", )
        self.E2Button6.place(x=250, y=25, height=50, width=50)
        self.E2Button5 = Button(self.labelBottom, text="5", font=("showcard gothic", 16, "bold"), width=5, bg="#FEC84D", fg="#004369", )
        self.E2Button5.place(x=250, y=75, height=50, width=50)
        self.E2Button4 = Button(self.labelBottom, text="4", font=("showcard gothic", 16, "bold"), width=5, bg="#FEC84D", fg="#004369", )
        self.E2Button4.place(x=250, y=125, height=50, width=50)
        self.E2Button3 = Button(self.labelBottom, text="3", font=("showcard gothic", 16, "bold"), width=5, bg="#FEC84D", fg="#004369", )
        self.E2Button3.place(x=250, y=175, height=50, width=50)
        self.E2Button2 = Button(self.labelBottom, text="2", font=("showcard gothic", 16, "bold"), width=5, bg="#FEC84D", fg="#004369", )
        self.E2Button2.place(x=250, y=225, height=50, width=50)
        self.E2Button1 = Button(self.labelBottom, text="1", font=("showcard gothic", 16, "bold"), width=5, bg="#FEC84D", fg="#004369", )
        self.E2Button1.place(x=250, y=275, height=50, width=50)

        self.E3Button6 = Button(self.labelBottom, text="6", font=("showcard gothic", 16, "bold"),  width=5,  bg="#FEC84D",  fg="#004369", )
        self.E3Button6.place(x=450, y=25, height=50, width=50)
        self.E3Button5 = Button(self.labelBottom, text="5", font=("showcard gothic", 16, "bold"), width=5, bg="#FEC84D", fg="#004369", )
        self.E3Button5.place(x=450, y=75, height=50, width=50)
        self.E3Button4 = Button(self.labelBottom, text="4", font=("showcard gothic", 16, "bold"), width=5, bg="#FEC84D", fg="#004369", )
        self.E3Button4.place(x=450, y=125, height=50, width=50)
        self.E3Button3 = Button(self.labelBottom, text="3", font=("showcard gothic", 16, "bold"), width=5, bg="#FEC84D", fg="#004369", )
        self.E3Button3.place(x=450, y=175, height=50, width=50)
        self.E3Button2 = Button(self.labelBottom, text="2", font=("showcard gothic", 16, "bold"), width=5, bg="#FEC84D", fg="#004369", )
        self.E3Button2.place(x=450, y=225, height=50, width=50)
        self.E3Button1 = Button(self.labelBottom, text="1", font=("showcard gothic", 16, "bold"), width=5, bg="#FEC84D", fg="#004369", )
        self.E3Button1.place(x=450, y=275, height=50, width=50)

        self.Enter6 = Button(self.labelBottom, text="6", font=("showcard gothic", 16, "bold"), width=5, bg="#FEC84D", fg="#004369", command=lambda: self.func(6))
        self.Enter6.place(x=750, y=25, height=50, width=50)
        self.Enter5 = Button(self.labelBottom, text="5", font=("showcard gothic", 16, "bold"), width=5, bg="#FEC84D", fg="#004369", command=lambda: self.func(5))
        self.Enter5.place(x=750, y=75, height=50, width=50)
        self.Enter4 = Button(self.labelBottom, text="4", font=("showcard gothic", 16, "bold"), width=5, bg="#FEC84D", fg="#004369", command=lambda: self.func(4))
        self.Enter4.place(x=750, y=125, height=50, width=50)
        self.Enter3 = Button(self.labelBottom, text="3", font=("showcard gothic", 16, "bold"), width=5, bg="#FEC84D", fg="#004369", command=lambda: self.func(3))
        self.Enter3.place(x=750, y=175, height=50, width=50)
        self.Enter2 = Button(self.labelBottom, text="2", font=("showcard gothic", 16, "bold"), width=5, bg="#FEC84D", fg="#004369", command=lambda: self.func(2))
        self.Enter2.place(x=750, y=225, height=50, width=50)
        self.Enter1 = Button(self.labelBottom, text="1", font=("showcard gothic", 16, "bold"), width=5,bg="#FEC84D", fg="#004369", command=lambda: self.func(1))
        self.Enter1.place(x=750, y=275, height=50, width=50)

        threading.Thread(target=self.first_elevator.scan).start()
        threading.Thread(target=self.second_elevator.scan).start()
        threading.Thread(target=self.third_elevator.scan).start()

        self.root.mainloop()

    def func(self, message):

        # message = input()
        print(f"Request in floor {message}")
        difference1 = abs(GUI.first_elevator.head - int(message))
        difference2 = abs(GUI.second_elevator.head - int(message))
        difference3 = abs(GUI.third_elevator.head - int(message))

        min_of_differences = min(difference1, difference2, difference3)

        if difference1 == min_of_differences:
            print(f"Assigned to first elevator")
            GUI.first_elevator.array.append(int(message))
            print("Assigend!")
            print(GUI.first_elevator.array)

        elif difference2 == min_of_differences:
            print(f"Assigned to second elevator")
            GUI.second_elevator.array.append(int(message))
            print("Assigend!")
            print(GUI.second_elevator.array)

        elif difference3 == min_of_differences:
            print(f"Assigned to third elevator")
            GUI.third_elevator.array.append(int(message))
            print("Assigend!")
            print(GUI.third_elevator.array)

    def movement(self):

        self.canvas.move(self.rectangle, self.x, self.y)
        self.canvas.move(self.rectangle2, self.x2, self.y2)
        self.canvas.move(self.rectangle3, self.x3, self.y3)
        self.canvas.after(200, self.movement)

        if GUI.first_elevator.direction == "up":
            try:
                up_check_first_elevator = GUI.first_elevator.up[0]
                if abs(self.current_y) == abs(275 - 50 * (up_check_first_elevator - 1)):
                    # threading.Thread(target=self.pause).start()
                    print(f"reached floor up1________________________________________________:{up_check_first_elevator}")
                    GUI.first_elevator.up.remove(up_check_first_elevator)
                    GUI.first_elevator.array.remove(up_check_first_elevator)

            except:
                pass
            if len(GUI.first_elevator.up) == 0:
                gui.down1()
            else:
                gui.up1()

        if GUI.first_elevator.direction == "down":
            try:
                down_check_first_elevator = GUI.first_elevator.down[len(GUI.first_elevator.down)-1]
                if abs(self.current_y) == abs(275 - 50 * (down_check_first_elevator - 1)):
                    # threading.Thread(target=self.pause).run()

                    print(f"reached floor down1________________________________________________:{down_check_first_elevator}")
                    GUI.first_elevator.down.remove(down_check_first_elevator)
                    GUI.first_elevator.array.remove(down_check_first_elevator)
            except:
                pass
            if len(GUI.first_elevator.down) == 0:
                gui.up1()
            else:
                gui.down1()

        if GUI.second_elevator.direction == "up":
            try:
                up_check_second_elevator = GUI.second_elevator.up[0]
                if abs(self.current_y2) == abs(275 - 50 * (up_check_second_elevator - 1)):
                    # threading.Thread(target=self.pause).run()

                    print(f"reached floor up2________________________________________________:{up_check_second_elevator}")
                    GUI.second_elevator.up.remove(up_check_second_elevator)
                    GUI.second_elevator.array.remove(up_check_second_elevator)
            except:
                pass
            if len(GUI.second_elevator.up) == 0:
                gui.down2()
            else:
                gui.up2()

        if GUI.second_elevator.direction == "down":
            try:
                down_check_second_elevator = GUI.second_elevator.down[len(GUI.second_elevator.down)-1]
                if abs(self.current_y2) == abs(275 - 50 * (down_check_second_elevator - 1)):
                    # threading.Thread(target=self.pause).run()

                    print(f"reached floor down2________________________________________________:{down_check_second_elevator}")
                    GUI.second_elevator.down.remove(down_check_second_elevator)
                    GUI.second_elevator.array.remove(down_check_second_elevator)
            except:
                pass
            if len(GUI.second_elevator.down):
                gui.up2()
            else:
                gui.down2()

        if GUI.third_elevator.direction == "up":
            try:
                up_check_third_elevator = GUI.third_elevator.up[0]
                if abs(self.current_y3) == abs(275 - 50 * (up_check_third_elevator - 1)):
                    # threading.Thread(target=self.pause).run()

                    print(f"reached floor up3________________________________________________:{up_check_third_elevator}")
                    GUI.third_elevator.up.remove(up_check_third_elevator)
                    GUI.third_elevator.array.remove(up_check_third_elevator)
            except:
                pass

            if len(GUI.third_elevator.up) == 0:
                gui.down3()
            else:
                gui.up3()

        if GUI.third_elevator.direction == "down":
            try:
                down_check_third_elevator = GUI.third_elevator.down[len(GUI.third_elevator.down)-1]
                if abs(self.current_y3) == abs(275 - 50 * (down_check_third_elevator - 1)):
                    # threading.Thread(target=self.pause).run()

                    print(f"reached floor down3________________________________________________:{down_check_third_elevator}")
                    GUI.third_elevator.down.remove(down_check_third_elevator)
                    GUI.third_elevator.array.remove(down_check_third_elevator)
            except:
                pass
            if GUI.third_elevator.down == 0:
                gui.up3()
            else:
                gui.down3()

    def pause(self):
        time1 = time.time()
        print(f"time1:{time1}")
        # print(f"time1:{time1}")
        while True:
            self.x = 0
            self.y = 0
            self.current_y -= 0
            return


    def up1(self):
        self.x = 0
        self.y = -5
        self.current_y -= 5

    def down1(self):
        self.x = 0
        self.y = 5
        self.current_y += 5

    def up2(self):
        self.x2 = 0
        self.y2 = -5
        self.current_y2 -= 5

    def down2(self):
        self.x2 = 0
        self.y2 = 5
        self.current_y2 += 5

    def up3(self):
        self.x3 = 0
        self.y3 = -5
        self.current_y3 -= 5

    def down3(self):
        self.x3 = 0
        self.y3 = 5
        self.current_y3 += 5


gui = GUI()
gui.root_window()
