
def binary_search(arr, start, end, num):

    if(end > start):
        mid = int((start + end) / 2)

        if (arr[mid] < num):
            new_start = mid + 1
            binary_search(arr, new_start, end, num)
        elif (arr[mid] > num):
            new_end = mid - 1
            binary_search(arr, start, new_end, num)
        else:
            print("Number is found at index ", mid)

    else:
        print("No. not in the list")


if __name__ == "__main__":
    list_of_num = [i for i in range(1,101)]
    print(list_of_num)
    num_to_search = int(input("Enter no. to search between 1 to 100 : "))
    binary_search(list_of_num, 0, len(list_of_num), num_to_search)

