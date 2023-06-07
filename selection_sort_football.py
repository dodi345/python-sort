football = [
    {"Player" : "Kylian Mbappe", "Club" : "PSG", "Goal" : "40"},
    {"Player" : "Victor Oshimen", "Club" : "Napoli", "Goal" : "28"},
    {"Player" : "Robert Lewandowski", "Club" : "Decul", "Goal" : "33"},
    {"Player" : "Erling Halland", "Club" : "Mpok Siti", "Goal" : "52"},
    {"Player" : "Christopher Nkuku", "Club" : "RB Leipzig", "Goal" : "22"}
]

def selection_sort(arr):
    n = len(arr)
    for i in range(n-1):
        min_index = i
        for j in range(i+1, n):
            if arr[j]["Goal"] > arr[min_index]["Goal"]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]


selection_sort(football)
for football in football:
    print(f"Name: {football['Player']}, Club: {football['Club']}, Jumlah Goal: {football['Goal']}")