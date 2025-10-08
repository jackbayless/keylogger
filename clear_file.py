

def clear_keyfile():
    with open('keyfile.txt', 'w') as f:
        pass
    print('keyfile.txt cleared')

if __name__ == '__main__':
    clear_keyfile()
