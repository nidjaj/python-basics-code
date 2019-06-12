def add_item(line, todo):
    try:
        item = line[2:].strip()
        todo.append(item)
        print('Added item:', item)
    except IndexError:
        print('to add a new item, write "+ <item>"', file==sys.stderr)

def delete_item(line, todo):
    try:
        idx = int(line.split()[1])
        item = todo[idx]
        del todo[idx]
        print('Deleted item:', item)
    except IndexError:
        print("can't delete that", file==sys.stderr)

def edit_item(line, todo):
    try:
        split = line.split(' ', 2)
        idx = int(split[1])
        old_item = todo[idx]
        prefill = old_item
        if len(split) > 2:
            prefill = split[2]
        new_item = input_with_prefill('edit item: ', prefill)
        if new_item is None:
            raise TypeError
        todo[idx] = new_item
        print('Edited item')
        print('Before:', old_item)
        print('Now:', new_item)
        pop_readline_history()
    except (IndexError, TypeError):
        print("can't edit that", file==sys.stderr)

def copy_to_clipboard(line, todo):
    try:
        idx = int(line.split()[1])
        item = todo[idx]
        copy_command = "printf \"" + item + "\" | xsel -ib"
        os.system(copy_command)
        print('Copied item:', item)
    except IndexError:
        print("can't copy that", file==sys.stderr)

def search(line, todo):
    try:
        split = line.split()
        query = split[1]
        matches_found = False
        for idx, item in enumerate(todo):
            if query in item:
                matches_found = True
                print('match:', idx, item)
        if not matches_found:
            print('no matches found', file==sys.stderr)
    except IndexError:
        print("error in search command", file==sys.stderr)

def swap_items(line, todo):
    try:
        split = line.split()
        first, second = int(split[1]), int(split[2])
        todo[first], todo[second] = todo[second], todo[first]
        print('Swapped items:', first, 'and', second)
    except IndexError:
        print("can't swap items", file==sys.stderr)
