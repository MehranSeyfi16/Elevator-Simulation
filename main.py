import threading
import time
import sys


def SCAN_E2(direction, size):
    is_finished_2 = False
    print("im in thread2")
    global arr2
    global head2
    print(arr2)

    seek_count = 0
    distance, cur_track = 0, 0
    down = []
    up = []
    seek_sequence = []

    for i in range(size):
        if (arr2[i] < head2):
            down.append(arr2[i])
        if (arr2[i] > head2):
            up.append(arr2[i])

    down.sort()
    up.sort()

    run = 2

    while (run != 0):
        if (direction == "down"):

            for i in range(len(down) - 1, -1, -1):
                current_size = len(arr2)
                cur_track = down[i]
                seek_sequence.append(cur_track)
                arr2.remove(cur_track)
                # down.remove(cur_track)
                distance = abs(cur_track - head2)
                seek_count += distance
                head2 = cur_track

                # print(f"current floor:{head2}")
                # time.sleep(distance * 0.00005)
                time.sleep(2)

            direction = "up"

        elif (direction == "up"):
            for i in range(len(up)):
                current_size_2 = len(arr2)
                cur_track = up[i]
                seek_sequence.append(cur_track)
                arr2.remove(cur_track)
                distance = abs(cur_track - head2)
                seek_count += distance
                head2 = cur_track
                # print(f"current floor:{head2}")
                # time.sleep(distance * 0.00005)
                time.sleep(2)

            direction = "down"

        run -= 1

    # print("Total number of seek operations =",
    #       seek_count)

    print("Seek Sequence is")

    if len(seek_sequence) == 0:
        exit(0)

    for i in range(len(seek_sequence)):
        print(seek_sequence[i])

    is_finished_2 = True

    # print(f"head2:{head2}")


def SCAN_E1(direction, size):
    is_finished_1 = False

    print("im in thread1")

    global arr1
    global head
    print(arr1)

    seek_count = 0
    distance, cur_track = 0, 0
    down = []
    up = []
    seek_sequence = []

    for i in range(size):
        if (arr1[i] < head):
            down.append(arr1[i])
        if (arr1[i] > head):
            up.append(arr1[i])

    down.sort()
    up.sort()

    run = 2

    while (run != 0):
        if (direction == "down"):

            for i in range(len(down) - 1, -1, -1):
                current_size = len(arr1)
                cur_track = down[i]
                seek_sequence.append(cur_track)
                arr1.remove(cur_track)
                # down.remove(cur_track)
                distance = abs(cur_track - head)
                seek_count += distance
                head = cur_track

                # print(f"current floor:{head}")
                # time.sleep(distance * 0.00005)
                time.sleep(2)

            direction = "up"

        elif (direction == "up"):
            for i in range(len(up)):
                current_size_2 = len(arr1)
                cur_track = up[i]
                seek_sequence.append(cur_track)
                arr1.remove(cur_track)
                distance = abs(cur_track - head)
                seek_count += distance
                head = cur_track
                # print(f"current floor:{head}")
                # time.sleep(distance * 0.00005)
                time.sleep(2)

            direction = "down"

        run -= 1

    # print("Total number of seek operations =",
    #       seek_count)

    print("Seek Sequence is")

    if len(seek_sequence) == 0:
        exit(0)

    for i in range(len(seek_sequence)):
        print(seek_sequence[i])

    is_finished_1 = True

    # print(f"head{head}")


# del  seek_sequence
# del  down
# del  up


def SCAN_E3(direction, size):
    is_finished_3 = False

    print("im in thread3")
    global arr3
    global head3
    print(arr3)

    seek_count = 0
    distance, cur_track = 0, 0
    down = []
    up = []
    seek_sequence = []

    for i in range(size):
        if (arr3[i] < head3):
            down.append(arr3[i])
        if (arr3[i] > head3):
            up.append(arr3[i])

    down.sort()
    up.sort()

    run = 2

    while (run != 0):
        if (direction == "down"):

            for i in range(len(down) - 1, -1, -1):
                current_size = len(arr3)
                cur_track = down[i]
                seek_sequence.append(cur_track)
                arr3.remove(cur_track)
                # down.remove(cur_track)
                distance = abs(cur_track - head3)
                seek_count += distance
                head3 = cur_track

                # print(f"current floor:{head3}")
                # time.sleep(distance * 0.00005)
                time.sleep(2)

            direction = "up"

        elif (direction == "up"):
            for i in range(len(up)):
                current_size_2 = len(arr3)
                cur_track = up[i]
                seek_sequence.append(cur_track)
                arr3.remove(cur_track)
                distance = abs(cur_track - head3)
                seek_count += distance
                head3 = cur_track
                # print(f"current floor:{head3}")
                # time.sleep(distance * 0.00005)
                time.sleep(2)

            direction = "down"

        run -= 1

    # print("Total number of seek operations =",
    #       seek_count)

    print("Seek Sequence is")

    if len(seek_sequence) == 0:
        exit(0)

    for i in range(len(seek_sequence)):
        print(seek_sequence[i])

    is_finished_3 = True


down = []
up = []


def find_direction(arr, head, array_size):
    down_sum = 0
    up_sum = 0
    for i in range(array_size):
        if (arr[i] < head):
            down.append(arr[i])
        if (arr[i] > head):
            up.append(arr[i])

    for i in range(len(down) - 1):
        down_sum = abs(down[i] - down[i + 1])

    for i in range(len(up) - 1):
        up_sum = abs(up[i] - up[i + 1])

    if down_sum < up_sum:
        return "down"
    else:
        return "up"


def choose_elavator():
    global head, head2, head3
    global arr1, arr2, arr3

    difference1 = abs(head - arr1[0])
    difference2 = abs(head2 - arr2[0])
    difference3 = abs(head3 - arr3[0])

    min_of_differences = min(difference1, difference2, difference3)

    print("dif1")
    print(difference1)
    print("dif2")

    print(difference2)
    print("dif3")

    print(difference3)
    if difference1 == min_of_differences:
        return arr1
    elif difference2 == min_of_differences:
        return arr2
    elif difference3 == min_of_differences:
        return arr3


def func():
    global arr1, arr2, arr3
    global head, head2, head3
    # global size
    # global splited_array
    while True:
        # splited_array = input().split(' ')
        message = input()

        difference1 = abs(head - int(message))
        difference2 = abs(head2 - int(message))
        difference3 = abs(head3 - int(message))

        min_of_differences = min(difference1, difference2, difference3)

        # print("dif1")
        # print(difference1)
        # print("dif2")
        #
        # print(difference2)
        # print("dif3")
        #
        # print(difference3)

        if difference1 == min_of_differences:
            arr1.append(int(message))
        elif difference2 == min_of_differences:
            arr2.append(int(message))
        elif difference3 == min_of_differences:
            arr3.append(int(message))


        # choose_elavator().append(int(message))

        # for i in range(size):
        #     if (arr[i] < head):
        #         down.append(arr[i])
        #     if (arr[i] > head):
        #         up.append(arr[i])
        #
        # down.sort()
        # up.sort()


# external_request = [1, 5, 3]
# arr.extend(external_request)
# internal_request = [9]
# arr.extend(internal_request)

# for line in sys.stdin:
#     user_input = int(line.rstrip())
#     if 'Exit' == user_input:
#         break
#     else:
# print(user_input)

# arr.append(user_input)


arr1 = [7, 9, 10, 5]
arr2 = [12, 1, 7, 24]
arr3 = [17, 28, 50, 4]

size1 = len(arr1)
size2 = len(arr2)
size3 = len(arr3)

disk_size = 200
head = 6
head2 = 0
head3 = 10

direction1 = find_direction(arr1, head, size1)
direction2 = find_direction(arr2, head, size2)
direction3 = find_direction(arr3, head, size3)

t = threading.Thread(target=func)
t.start()

while True:
    t1 = threading.Thread(target=SCAN_E1(direction1, len(arr1)))
    t2 = threading.Thread(target=SCAN_E2(direction2, len(arr2)))
    t3 = threading.Thread(target=SCAN_E3(direction3, len(arr3)))
    t1.run()
    t2.run()
    t3.run()
    # choose_elavator().start()

    #
    # # t3 = threading.Thread(target=SCAN_E3(direction, len(arr)))
    #
    # difference1 = abs(head - arr[0])
    # difference2 = abs(head2 - arr[0])
    # # difference3 = abs(head3 - arr[0])
    #
    #
    # min_of_differences = min(difference1, difference2)

    # if min_of_differences == difference2:
    #     t2 = threading.Thread(target=SCAN_E2(direction, len(arr)))
    #     t2.start()
    # print(head2)
    # elif min_of_differences == difference3:
    #     t3.start()

    # SCAN_E1(head, direction)
    #

# print(direction)
# while True:
#     SCAN_E1(head, direction)

# choose_elavator().start()
