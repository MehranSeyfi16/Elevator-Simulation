import threading
import time
from tkinter import *


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
        down_sum = 0

        up_sum = 0
        for i in range(len(self.down) - 1):
            down_sum += abs(self.down[i] - self.down[i + 1])

        for i in range(len(self.up) - 1):
            up_sum += abs(self.up[i] - self.up[i + 1])

        if down_sum == 0:
            return "up"
        elif up_sum == 0:
            return   "down"
        elif down_sum < up_sum:
            return "down"
        else:
            return "up"


class GUI:
    arr1, arr2, arr3 = [], [], []
    head1, head2, head3 = 1, 5, 12

    first_elevator = Elevator("Elevator1", head1, arr1, None)
    second_elevator = Elevator("Elevator2", head2, arr2, None)
    third_elevator = Elevator("Elevator3", head3, arr3, None)

    def __init__(self):

        self.bound = None
        self.Button1, self.Button2, self.Button3 = None, None, None
        self.Button4, self.Button5, self.Button6 = None, None, None
        self.Button7, self.Button8, self.Button9 = None, None, None
        self.Button10, self.Button11, self.Button12 = None, None, None
        self.Button13, self.Button14, self.Button15 = None, None, None
        self.Enter1, self.Enter2, self.Enter3 = None, None, None
        self.Enter4, self.Enter5, self.Enter6 = None, None, None
        self.Enter7, self.Enter8, self.Enter9 = None, None, None
        self.Enter10, self.Enter11, self.Enter12 = None, None, None
        self.Enter13, self.Enter14, self.Enter15 = None, None, None
        self.Exit, self.Stop, self.Status = None, None, None
        self.E2Button1, self.E2Button2, self.E2Button3 = None, None, None
        self.E2Button4, self.E2Button5, self.E2Button6 = None, None, None
        self.E2Button7, self.E2Button8, self.E2Button9 = None, None, None
        self.E2Button10, self.E2Button11, self.E2Button12 = None, None, None
        self.E2Button13, self.E2Button14, self.E2Button15 = None, None, None
        self.E3Button1, self.E3Button2, self.E3Button3 = None, None, None
        self.E3Button4, self.E3Button5, self.E3Button6 = None, None, None
        self.E3Button7, self.E3Button8, self.E3Button9 = None, None, None
        self.E3Button10, self.E3Button11, self.E3Button12 = None, None, None
        self.E3Button13, self.E3Button14, self.E3Button15 = None, None, None
        self.labelBottom, self.labelHead, self.root = None, None, None
        self.rectangle, self.rectangle2, self.rectangle3 = None, None, None
        self.canvas = None

        self.x = 1
        self.y = 0
        self.current_y = 725 - 50 * (GUI.first_elevator.head_tmp - 1)

        self.x2 = 1
        self.y2 = 0
        self.current_y2 = 725 - 50 * (GUI.second_elevator.head_tmp - 1)

        self.x3 = 1
        self.y3 = 0
        self.current_y3 = 725 - 50 * (GUI.third_elevator.head_tmp - 1)

    def root_window(self):
        self.root = Tk()
        self.root.title("Elevator Simulator")
        self.canvas = Canvas(self.root, bg="#991532", height=2000, width=2000)

        self.rectangle = self.canvas.create_rectangle(
            10, 725 - 50 * (GUI.first_elevator.head - 1), 40, 725 - 50 * (GUI.first_elevator.head - 1) + 30,
            fill="#f06b32")

        self.rectangle2 = self.canvas.create_rectangle(
            360, 725 - 50 * (GUI.second_elevator.head - 1), 390, 725 - 50 * (GUI.second_elevator.head - 1) + 30,
            fill="#32f0b7")

        self.rectangle3 = self.canvas.create_rectangle(
            710, 725 - 50 * (GUI.third_elevator.head - 1), 740, 725 - 50 * (GUI.third_elevator.head - 1) + 30,
            fill="#69f06c")

        threading.Thread(target=self.movement).start()

        self.canvas.pack()
        self.Button15 = Button(self.labelBottom, text="15", font=("showcard gothic", 16, "bold"), width=5, bg="#FEC84D",
                               fg="#004369", command=lambda: self.func(15, 1))
        self.Button15.place(x=50, y=25, height=50, width=70)
        self.Button14 = Button(self.labelBottom, text="14", font=("showcard gothic", 16, "bold"), width=5, bg="#FEC84D",
                               fg="#004369", command=lambda: self.func(14, 1))
        self.Button14.place(x=50, y=75, height=50, width=70)
        self.Button13 = Button(self.labelBottom, text="13", font=("showcard gothic", 16, "bold"), width=5, bg="#FEC84D",
                               fg="#004369", command=lambda: self.func(13, 1))
        self.Button13.place(x=50, y=125, height=50, width=70)
        self.Button12 = Button(self.labelBottom, text="12", font=("showcard gothic", 16, "bold"), width=5, bg="#FEC84D",
                               fg="#004369", command=lambda: self.func(12, 1))
        self.Button12.place(x=50, y=175, height=50, width=70)
        self.Button11 = Button(self.labelBottom, text="11", font=("showcard gothic", 16, "bold"), width=5, bg="#FEC84D",
                               fg="#004369", command=lambda: self.func(11, 1))
        self.Button11.place(x=50, y=225, height=50, width=70)
        self.Button10 = Button(self.labelBottom, text="10", font=("showcard gothic", 16, "bold"), width=5, bg="#FEC84D",
                               fg="#004369", command=lambda: self.func(10, 1))
        self.Button10.place(x=50, y=275, height=50, width=70)
        self.Button9 = Button(self.labelBottom, text="9", font=("showcard gothic", 16, "bold"), width=5, bg="#FEC84D",
                              fg="#004369", command=lambda: self.func(9, 1))
        self.Button9.place(x=50, y=325, height=50, width=70)
        self.Button8 = Button(self.labelBottom, text="8", font=("showcard gothic", 16, "bold"), width=5, bg="#FEC84D",
                              fg="#004369", command=lambda: self.func(8, 1))
        self.Button8.place(x=50, y=375, height=50, width=70)
        self.Button7 = Button(self.labelBottom, text="7", font=("showcard gothic", 16, "bold"), width=5, bg="#FEC84D",
                              fg="#004369", command=lambda: self.func(7, 1))
        self.Button7.place(x=50, y=425, height=50, width=70)
        self.Button6 = Button(self.labelBottom, text="6", font=("showcard gothic", 16, "bold"), width=5, bg="#FEC84D",
                              fg="#004369", command=lambda: self.func(6, 1))
        self.Button6.place(x=50, y=475, height=50, width=70)
        self.Button5 = Button(self.labelBottom, text="5", font=("showcard gothic", 16, "bold"), width=5, bg="#FEC84D",
                              fg="#004369", command=lambda: self.func(5, 1))
        self.Button5.place(x=50, y=525, height=50, width=70)
        self.Button4 = Button(self.labelBottom, text="4", font=("showcard gothic", 16, "bold"), width=5, bg="#FEC84D",
                              fg="#004369", command=lambda: self.func(4, 1))
        self.Button4.place(x=50, y=575, height=50, width=70)
        self.Button3 = Button(self.labelBottom, text="3", font=("showcard gothic", 16, "bold"), width=5, bg="#FEC84D",
                              fg="#004369", command=lambda: self.func(3, 1))
        self.Button3.place(x=50, y=625, height=50, width=70)
        self.Button2 = Button(self.labelBottom, text="2", font=("showcard gothic", 16, "bold"), width=5, bg="#FEC84D",
                              fg="#004369", command=lambda: self.func(2, 1))
        self.Button2.place(x=50, y=675, height=50, width=70)
        self.Button1 = Button(self.labelBottom, text="1", font=("showcard gothic", 16, "bold"), width=5, bg="#FEC84D",
                              fg="#004369", command=lambda: self.func(1, 1))
        self.Button1.place(x=50, y=725, height=50, width=70)

        self.E2Button15 = Button(self.labelBottom, text="15", font=("showcard gothic", 16, "bold"), width=5,
                                 bg="#FEC84D",
                                 fg="#004369", command=lambda: self.func(15, 2))
        self.E2Button15.place(x=400, y=25, height=50, width=70)
        self.E2Button14 = Button(self.labelBottom, text="14", font=("showcard gothic", 16, "bold"), width=5,
                                 bg="#FEC84D",
                                 fg="#004369", command=lambda: self.func(14, 2))
        self.E2Button14.place(x=400, y=75, height=50, width=70)
        self.E2Button13 = Button(self.labelBottom, text="13", font=("showcard gothic", 16, "bold"), width=5,
                                 bg="#FEC84D",
                                 fg="#004369", command=lambda: self.func(13, 2))
        self.E2Button13.place(x=400, y=125, height=50, width=70)
        self.E2Button12 = Button(self.labelBottom, text="12", font=("showcard gothic", 16, "bold"), width=5,
                                 bg="#FEC84D",
                                 fg="#004369", command=lambda: self.func(12, 2))
        self.E2Button12.place(x=400, y=175, height=50, width=70)
        self.E2Button11 = Button(self.labelBottom, text="11", font=("showcard gothic", 16, "bold"), width=5,
                                 bg="#FEC84D",
                                 fg="#004369", command=lambda: self.func(11, 2))
        self.E2Button11.place(x=400, y=225, height=50, width=70)
        self.E2Button10 = Button(self.labelBottom, text="10", font=("showcard gothic", 16, "bold"), width=5,
                                 bg="#FEC84D",
                                 fg="#004369", command=lambda: self.func(10, 2))
        self.E2Button10.place(x=400, y=275, height=50, width=70)
        self.E2Button9 = Button(self.labelBottom, text="9", font=("showcard gothic", 16, "bold"), width=5, bg="#FEC84D",
                                fg="#004369", command=lambda: self.func(9, 2))
        self.E2Button9.place(x=400, y=325, height=50, width=70)
        self.E2Button8 = Button(self.labelBottom, text="8", font=("showcard gothic", 16, "bold"), width=5, bg="#FEC84D",
                                fg="#004369", command=lambda: self.func(8, 2))
        self.E2Button8.place(x=400, y=375, height=50, width=70)
        self.E2Button7 = Button(self.labelBottom, text="7", font=("showcard gothic", 16, "bold"), width=5, bg="#FEC84D",
                                fg="#004369", command=lambda: self.func(7, 2))
        self.E2Button7.place(x=400, y=425, height=50, width=70)
        self.E2Button6 = Button(self.labelBottom, text="6", font=("showcard gothic", 16, "bold"), width=5, bg="#FEC84D",
                                fg="#004369", command=lambda: self.func(6, 2))
        self.E2Button6.place(x=400, y=475, height=50, width=70)
        self.E2Button5 = Button(self.labelBottom, text="5", font=("showcard gothic", 16, "bold"), width=5, bg="#FEC84D",
                                fg="#004369", command=lambda: self.func(5, 2))
        self.E2Button5.place(x=400, y=525, height=50, width=70)
        self.E2Button4 = Button(self.labelBottom, text="4", font=("showcard gothic", 16, "bold"), width=5, bg="#FEC84D",
                                fg="#004369", command=lambda: self.func(4, 2))
        self.E2Button4.place(x=400, y=575, height=50, width=70)
        self.E2Button3 = Button(self.labelBottom, text="3", font=("showcard gothic", 16, "bold"), width=5, bg="#FEC84D",
                                fg="#004369", command=lambda: self.func(3, 2))
        self.E2Button3.place(x=400, y=625, height=50, width=70)
        self.E2Button2 = Button(self.labelBottom, text="2", font=("showcard gothic", 16, "bold"), width=5, bg="#FEC84D",
                                fg="#004369", command=lambda: self.func(2, 2))
        self.E2Button2.place(x=400, y=675, height=50, width=70)
        self.E2Button1 = Button(self.labelBottom, text="1", font=("showcard gothic", 16, "bold"), width=5, bg="#FEC84D",
                                fg="#004369", command=lambda: self.func(1, 2))
        self.E2Button1.place(x=400, y=725, height=50, width=70)

        self.E3Button15 = Button(self.labelBottom, text="15", font=("showcard gothic", 16, "bold"), width=5,
                                 bg="#FEC84D", fg="#004369", command=lambda: self.func(15, 3))
        self.E3Button15.place(x=750, y=25, height=50, width=70)
        self.E3Button14 = Button(self.labelBottom, text="14", font=("showcard gothic", 16, "bold"), width=5,
                                 bg="#FEC84D", fg="#004369", command=lambda: self.func(14, 3))
        self.E3Button14.place(x=750, y=75, height=50, width=70)
        self.E3Button13 = Button(self.labelBottom, text="13", font=("showcard gothic", 16, "bold"), width=5,
                                 bg="#FEC84D", fg="#004369", command=lambda: self.func(13, 3))
        self.E3Button13.place(x=750, y=125, height=50, width=70)
        self.E3Button12 = Button(self.labelBottom, text="12", font=("showcard gothic", 16, "bold"), width=5,
                                 bg="#FEC84D", fg="#004369", command=lambda: self.func(12, 3))
        self.E3Button12.place(x=750, y=175, height=50, width=70)
        self.E3Button11 = Button(self.labelBottom, text="11", font=("showcard gothic", 16, "bold"), width=5,
                                 bg="#FEC84D", fg="#004369", command=lambda: self.func(11, 3))
        self.E3Button11.place(x=750, y=225, height=50, width=70)
        self.E3Button10 = Button(self.labelBottom, text="10", font=("showcard gothic", 16, "bold"), width=5,
                                 bg="#FEC84D", fg="#004369", command=lambda: self.func(10, 3))
        self.E3Button10.place(x=750, y=275, height=50, width=70)
        self.E3Button9 = Button(self.labelBottom, text="9", font=("showcard gothic", 16, "bold"), width=5, bg="#FEC84D",
                                fg="#004369", command=lambda: self.func(9, 3))
        self.E3Button9.place(x=750, y=325, height=50, width=70)
        self.E3Button8 = Button(self.labelBottom, text="8", font=("showcard gothic", 16, "bold"), width=5, bg="#FEC84D",
                                fg="#004369", command=lambda: self.func(8, 3))
        self.E3Button8.place(x=750, y=375, height=50, width=70)
        self.E3Button7 = Button(self.labelBottom, text="7", font=("showcard gothic", 16, "bold"), width=5, bg="#FEC84D",
                                fg="#004369", command=lambda: self.func(7, 3))
        self.E3Button7.place(x=750, y=425, height=50, width=70)
        self.E3Button6 = Button(self.labelBottom, text="6", font=("showcard gothic", 16, "bold"), width=5, bg="#FEC84D",
                                fg="#004369", command=lambda: self.func(6, 3))
        self.E3Button6.place(x=750, y=475, height=50, width=70)
        self.E3Button5 = Button(self.labelBottom, text="5", font=("showcard gothic", 16, "bold"), width=5, bg="#FEC84D",
                                fg="#004369", command=lambda: self.func(5, 3))
        self.E3Button5.place(x=750, y=525, height=50, width=70)
        self.E3Button4 = Button(self.labelBottom, text="4", font=("showcard gothic", 16, "bold"), width=5, bg="#FEC84D",
                                fg="#004369", command=lambda: self.func(4, 3))
        self.E3Button4.place(x=750, y=575, height=50, width=70)
        self.E3Button3 = Button(self.labelBottom, text="3", font=("showcard gothic", 16, "bold"), width=5, bg="#FEC84D",
                                fg="#004369", command=lambda: self.func(3, 3))
        self.E3Button3.place(x=750, y=625, height=50, width=70)
        self.E3Button2 = Button(self.labelBottom, text="2", font=("showcard gothic", 16, "bold"), width=5, bg="#FEC84D",
                                fg="#004369", command=lambda: self.func(2, 3))
        self.E3Button2.place(x=750, y=675, height=50, width=70)
        self.E3Button1 = Button(self.labelBottom, text="1", font=("showcard gothic", 16, "bold"), width=5, bg="#FEC84D",
                                fg="#004369", command=lambda: self.func(1, 3))
        self.E3Button1.place(x=750, y=725, height=50, width=70)

        self.Enter6 = Button(self.labelBottom, text="6", font=("showcard gothic", 16, "bold"), width=5, bg="#FEC84D",
                             fg="#004369", command=lambda: self.func(6, 0))
        self.Enter6.place(x=1100, y=25 + 200, height=50, width=50)
        self.Enter5 = Button(self.labelBottom, text="5", font=("showcard gothic", 16, "bold"), width=5, bg="#FEC84D",
                             fg="#004369", command=lambda: self.func(5, 0))
        self.Enter5.place(x=1100, y=75 + 200, height=50, width=50)
        self.Enter4 = Button(self.labelBottom, text="4", font=("showcard gothic", 16, "bold"), width=5, bg="#FEC84D",
                             fg="#004369", command=lambda: self.func(4, 0))
        self.Enter4.place(x=1100, y=125 + 200, height=50, width=50)
        self.Enter3 = Button(self.labelBottom, text="3", font=("showcard gothic", 16, "bold"), width=5, bg="#FEC84D",
                             fg="#004369", command=lambda: self.func(3, 0))
        self.Enter3.place(x=1100, y=175 + 200, height=50, width=50)
        self.Enter2 = Button(self.labelBottom, text="2", font=("showcard gothic", 16, "bold"), width=5, bg="#FEC84D",
                             fg="#004369", command=lambda: self.func(2, 0))
        self.Enter2.place(x=1100, y=225 + 200, height=50, width=50)
        self.Enter1 = Button(self.labelBottom, text="1", font=("showcard gothic", 16, "bold"), width=5, bg="#FEC84D",
                             fg="#004369", command=lambda: self.func(1, 0))
        self.Enter1.place(x=1100, y=275 + 200, height=50, width=50)
        self.Enter7 = Button(self.labelBottom, text="7", font=("showcard gothic", 16, "bold"), width=5, bg="#FEC84D",
                             fg="#004369", command=lambda: self.func(7, 0))
        self.Enter7.place(x=1150, y=25 + 200, height=50, width=50)
        self.Enter8 = Button(self.labelBottom, text="8", font=("showcard gothic", 16, "bold"), width=5, bg="#FEC84D",
                             fg="#004369", command=lambda: self.func(8, 0))
        self.Enter8.place(x=1150, y=75 + 200, height=50, width=50)
        self.Enter9 = Button(self.labelBottom, text="9", font=("showcard gothic", 16, "bold"), width=5, bg="#FEC84D",
                             fg="#004369", command=lambda: self.func(9, 0))
        self.Enter9.place(x=1150, y=125 + 200, height=50, width=50)
        self.Enter10 = Button(self.labelBottom, text="10", font=("showcard gothic", 16, "bold"), width=5, bg="#FEC84D",
                              fg="#004369", command=lambda: self.func(10, 0))
        self.Enter10.place(x=1150, y=175 + 200, height=50, width=50)
        self.Enter11 = Button(self.labelBottom, text="11", font=("showcard gothic", 16, "bold"), width=5, bg="#FEC84D",
                              fg="#004369", command=lambda: self.func(11, 0))
        self.Enter11.place(x=1150, y=225 + 200, height=50, width=50)
        self.Enter12 = Button(self.labelBottom, text="12", font=("showcard gothic", 16, "bold"), width=5, bg="#FEC84D",
                              fg="#004369", command=lambda: self.func(12, 0))
        self.Enter12.place(x=1150, y=275 + 200, height=50, width=50)
        self.Enter13 = Button(self.labelBottom, text="13", font=("showcard gothic", 16, "bold"), width=5, bg="#FEC84D",
                              fg="#004369", command=lambda: self.func(13, 0))
        self.Enter13.place(x=1200, y=25 + 200, height=50, width=50)
        self.Enter14 = Button(self.labelBottom, text="14", font=("showcard gothic", 16, "bold"), width=5, bg="#FEC84D",
                              fg="#004369", command=lambda: self.func(14, 0))
        self.Enter14.place(x=1200, y=75 + 200, height=50, width=50)
        self.Enter15 = Button(self.labelBottom, text="15", font=("showcard gothic", 16, "bold"), width=5, bg="#FEC84D",
                              fg="#004369", command=lambda: self.func(15, 0))
        self.Enter15.place(x=1200, y=125 + 200, height=50, width=50)
        self.Exit = Button(self.labelBottom, text="EXIT", font=("showcard gothic", 14, "bold"), width=5, bg="#FEC84D",
                           fg="#004369", command=lambda: exit(0))
        self.Exit.place(x=1200, y=175 + 200, height=50, width=50)
        self.Stop = Button(self.labelBottom, text="STOP", font=("showcard gothic", 12, "bold"), width=5, bg="#FEC84D",
                           fg="#004369", command=lambda: time.sleep(5))
        self.Stop.place(x=1200, y=225 + 200, height=50, width=50)
        self.Status = Button(self.labelBottom, text="Status", font=("showcard gothic", 8, "bold"), width=5,
                             bg="#FEC84D", fg="#004369")
        self.Status.place(x=1200, y=275 + 200, height=50, width=50)

        self.root.mainloop()

    @staticmethod
    def func(message, elevator):
        if int(elevator) == 0:
            print(f"External Request for Floor {message}")

            difference1 = abs(GUI.first_elevator.head - int(message))
            difference2 = abs(GUI.second_elevator.head - int(message))
            difference3 = abs(GUI.third_elevator.head - int(message))

            min_of_differences = min(difference1, difference2, difference3)

            if difference1 == min_of_differences:
                print(f"Assigned To First Elevator")
                GUI.first_elevator.array.append(int(message))

                if int(message) < GUI.first_elevator.head:
                    GUI.first_elevator.direction = "down"
                else:
                    GUI.first_elevator.direction = "up"

                if GUI.first_elevator.direction == "up":
                    GUI.first_elevator.up.append(int(message))
                    GUI.first_elevator.up.sort()

                elif GUI.first_elevator.direction == "down":
                    GUI.first_elevator.down.append(int(message))
                    GUI.first_elevator.up.sort(reverse=True)


            elif difference2 == min_of_differences:
                print(f"Assigned To Second Elevator")
                GUI.second_elevator.array.append(int(message))
                if int(message) < GUI.second_elevator.head:
                    GUI.second_elevator.direction = "down"
                else:
                    GUI.second_elevator.direction = "up"
                if GUI.second_elevator.direction == "up":
                    GUI.second_elevator.up.append(int(message))
                    GUI.second_elevator.up.sort()
                elif GUI.second_elevator.direction == "down":
                    GUI.second_elevator.down.append(int(message))
                    GUI.second_elevator.down.sort(reverse=True)

            elif difference3 == min_of_differences:
                print(f"Assigned To Third Elevator")
                GUI.third_elevator.array.append(int(message))

                if int(message) < GUI.third_elevator.head:
                    GUI.third_elevator.direction = "down"
                else:
                    GUI.third_elevator.direction = "up"

                if GUI.third_elevator.direction == "up":
                    GUI.third_elevator.up.append(int(message))
                    GUI.third_elevator.up.sort()
                elif GUI.third_elevator.direction == "down":
                    GUI.third_elevator.down.append(int(message))
                    GUI.third_elevator.down.sort(reverse=True)

        if int(elevator) == 1:
            GUI.first_elevator.array.append(int(message))

            if int(message) < GUI.first_elevator.head:
                GUI.first_elevator.direction = "down"
            else:
                GUI.first_elevator.direction = "up"
            print(f"internal request for floor {int(message)} in Elevator {int(elevator)}")

            if GUI.first_elevator.direction == "up":
                GUI.first_elevator.up.append(int(message))
                GUI.first_elevator.up.sort()
            elif GUI.first_elevator.direction == "down":
                GUI.first_elevator.down.append(int(message))
                GUI.first_elevator.down.sort(reverse=True)

        if int(elevator) == 2:
            GUI.second_elevator.array.append(int(message))

            if int(message) < GUI.second_elevator.head:
                GUI.second_elevator.direction = "down"
            else:
                GUI.second_elevator.direction = "up"

            print(f"internal request for floor {int(message)} in Elevator {int(elevator)}")

            if GUI.second_elevator.direction == "up":
                GUI.second_elevator.up.append(int(message))
                GUI.second_elevator.up.sort()
            elif GUI.second_elevator.direction == "down":
                GUI.second_elevator.down.append(int(message))
                GUI.second_elevator.down.sort()
        if int(elevator) == 3:
            GUI.third_elevator.array.append(int(message))

            if int(message) < GUI.third_elevator.head:
                GUI.third_elevator.direction =  "down"
            else:
                GUI.third_elevator.direction = "up"
            print(f"internal request for floor {int(message)} in Elevator {int(elevator)}")
            if GUI.third_elevator.direction == "up":
                GUI.third_elevator.up.append(int(message))
                GUI.third_elevator.up.sort()
            elif GUI.third_elevator.direction == "down":
                GUI.third_elevator.down.append(int(message))
                GUI.third_elevator.down.sort()

    def movement(self):
        if len(GUI.first_elevator.array) != 0:
            self.canvas.move(self.rectangle, self.x, self.y)
        if len(GUI.second_elevator.array) != 0:
            self.canvas.move(self.rectangle2, self.x2, self.y2)
        if len(GUI.third_elevator.array) != 0:
            self.canvas.move(self.rectangle3, self.x3, self.y3)
        self.canvas.after(10, self.movement)

        if GUI.first_elevator.direction == "up":
            try:
                for i in range(len(GUI.first_elevator.up)):
                    GUI.first_elevator.up.sort()
                    up_check_first_elevator = GUI.first_elevator.up[0]

                    if self.current_y == abs(725 - 50 * (up_check_first_elevator - 1)):
                        print(f"Reached Floor {up_check_first_elevator} in First Elevator")
                        GUI.first_elevator.up.remove(up_check_first_elevator)
                        GUI.first_elevator.head = up_check_first_elevator
                        GUI.first_elevator.array.remove(up_check_first_elevator)
                    if i == 0:
                        gui.up1()

            except:
                pass

        if GUI.first_elevator.direction == "down":
            try:
                for i in range(len(GUI.first_elevator.down)):
                    GUI.first_elevator.down.sort(reverse=True)
                    down_check_first_elevator = GUI.first_elevator.down[0]
                    if self.current_y == abs(725 - 50 * (down_check_first_elevator - 1)):
                        print(f"Reached Floor {down_check_first_elevator} in First Elevator")
                        GUI.first_elevator.head = down_check_first_elevator
                        GUI.first_elevator.down.remove(down_check_first_elevator)
                        GUI.first_elevator.array.remove(down_check_first_elevator)
                    if i == 0:
                        gui.down1()
            except:
                pass

        if GUI.second_elevator.direction == "up":
            try:
                for i in range(len(GUI.second_elevator.up)):
                    GUI.second_elevator.up.sort()
                    up_check_second_elevator = GUI.second_elevator.up[0]
                    if self.current_y2 == abs(725 - 50 * (up_check_second_elevator - 1)):
                        print(f"Reached Floor {up_check_second_elevator} in Second Elevator")

                        GUI.second_elevator.up.remove(up_check_second_elevator)
                        GUI.second_elevator.head = up_check_second_elevator
                        GUI.second_elevator.array.remove(up_check_second_elevator)
                    if i == 0:
                        gui.up2()
            except:
                pass

        if GUI.second_elevator.direction == "down":
            try:
                for i in range(len(GUI.second_elevator.down)):
                    GUI.second_elevator.down.sort(reverse=True)
                    down_check_second_elevator = GUI.second_elevator.down[0]
                    if self.current_y2 == abs(725 - 50 * (down_check_second_elevator - 1)):
                        print(f"Reached Floor {down_check_second_elevator} in Second Elevator")

                        GUI.second_elevator.head = down_check_second_elevator
                        GUI.second_elevator.down.remove(down_check_second_elevator)
                        GUI.second_elevator.array.remove(down_check_second_elevator)
                    if i == 0:
                        gui.down2()

            except:
                pass

        if GUI.third_elevator.direction == "up":
            try:
                for i in range(len(GUI.third_elevator.up)):
                    GUI.third_elevator.up.sort()
                    up_check_third_elevator = GUI.third_elevator.up[0]
                    if self.current_y3 == abs(725 - 50 * (up_check_third_elevator - 1)):
                        print(f"Reached Floor {up_check_third_elevator} in Third Elevator")

                        GUI.third_elevator.head = up_check_third_elevator
                        GUI.third_elevator.up.remove(up_check_third_elevator)
                        GUI.third_elevator.array.remove(up_check_third_elevator)
                    if i == 0:
                        gui.up3()
            except:
                pass

        if GUI.third_elevator.direction == "down":
            try:
                for i in range(len(GUI.third_elevator.down)):
                    GUI.third_elevator.down.sort(reverse=True)
                    down_check_third_elevator = GUI.third_elevator.down[0]
                    if self.current_y3 == abs(725 - 50 * (down_check_third_elevator - 1)):
                        print(f"Reached Floor {down_check_third_elevator} in Third Elevator")

                        GUI.third_elevator.head = down_check_third_elevator
                        GUI.third_elevator.down.remove(down_check_third_elevator)
                        GUI.third_elevator.array.remove(down_check_third_elevator)
                    if i == 0:
                        gui.down3()
            except:
                pass

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
