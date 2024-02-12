
## Question 1

tuple1 = ("Car", [34, 23, 8], False, [12, 20, 11])
print(tuple1[3][1])
###Print statement then counting from 0 go to the set containing 20 (3), then again to 20 (1)

## Question 2

list1 = [44, 12, 578, 21, 134, 67]
print(list1[-3: ])
### Counting backwards from -1 to the 3rd spot. Then tell the program to print items from that spot to the end of the list, leaving the space after the comma blank [-3, ]

## Question 3

list1= [5, 10, 15, 20, 75, 100, 50]
elem_pos = list1.index(20)
list1[elem_pos] = 200
print(list1)
###find the location of 20, and in the next line change it to the new variable, then print

## Question 4
tuple1 = (11, [64, 33], 243, 123)
list2 = list(tuple1)
list2[1][1] = 66
tuple2 = tuple(list2)
print(tuple2)
### Change the tuple into a list, then now that we can edit it since we know the position, after editing change it back into a tuple and print

## Question 5
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}
print(set1.union(set2))
### using the union function allows us to merge the two sets and get rid of duplicates

## Question 6
list1 = [3, 6, 9, 12, 15, 18, 21]
list2 = [4, 8, 12, 16, 20, 24, 28]
list1_odds = list1[1::2]
list2_evens = list2[0::2]
list3 = list1_odds + list2_evens
print(list3)
###Make new lists where the first one counts after each number in the list starting from index 1, and the second one starts counting from index 0. Then merge the two lists into another list then print the new third list

## Question 7
list1 = [34, 54, 67, 89, 11, 43, 94]
move_var = (list1[4])
list1.remove(list1[4])
list1.append(move_var)
print(list1)
### first we find the variable at index 4, and store it. Then we remove the variable at index 4, and using the append fucntion add the stored variable to the end since the append function allways adds at the end of a list

## Question 8
list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
list1[2][2].insert(2,7000)
print(list1)
###insert the new variable into the specific index of list1, then print it

## Question 9
list1 = ['a', 'b', ['c', ['d', 'e', ['f', 'g'], 'k'], 'l'], 'm', 'n']
list2 = ['h', 'i', 'j']
list1[2][1][2].insert(2,list2)
print(list1)
### same as with question 8

## Question 10
tuple5 = (40, 19, 234, 12, 10, 123)
list5 = list(tuple5)
list5.reverse()
tuple6 = tuple(list5)
print(tuple6)
###Change the tuple into a list, once its alist it can be reversed. Turn the reversed list back into a tuple then print the tuple

## Question 11
dict1 = {
    "course": {
        "name": "Mike",
        "marks": {
            "physics": 70,
            "history": 80
        }
    }
}

print(dict1["course"]["marks"]["history"])
###Navigate to course in the dictionary, then to marks then to history. History is a subdictionary of marks, which itself is a subdictionary of course.