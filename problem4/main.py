def count_item_and_sort(items):
    item_count = {}
    
    for item in items:
        item_count[item] = item_count.get(item, 0) + 1
    
    sorted_items = sorted(item_count.items(), key=lambda x: x[::-1])
    
    result = " ".join([f"{item[0]}->{item[1]}" for item in sorted_items])
    
    return result

if __name__ == "__main__":
    print(count_item_and_sort(["js", "js", "golang", "ruby", "ruby", "js", "js"]))
    # "golang->1 ruby->2 js->4"
    print(count_item_and_sort(["A", "B", "B", "C", "A", "A", "B", "A", "D", "D"]))
    # "C->1 D->2 B->3 A->4"
    print(count_item_and_sort(["football", "basketball", "tenis"]))
    # "basketball->1 football->1 tenis->1"