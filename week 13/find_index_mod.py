
#["apple", "kiwi", "mango", "orange"]
if __name__ == "__main__":
    print("Running find index module", __name__)
    test_var = "Test String"
    print("Imported Find Index Mod")

def find_index(search_list, target_val):
    for idx, val in enumerate(search_list):
        if val == target_val:
            return idx
        #print(idx, val)
    return -1

print(find_index(["apple", "kiwi", "mango", "orange"], "kiwi"))