masterlist = []

try:
    with open('music.txt', 'r') as myfile:
     mastertext = myfile.read()
     music.masterlist = eval(mastertext)
     print(masterlist)
except:
    masterlist = []

def music(choice):
    if choice == 'add':
        new = {}
        new['artist'] = input('what is the artists name? ')
        new['title'] = input('what is the song title? ')
        new['album'] = input('what album? ')
        new['track'] = input('what track number? ')
        new['year'] = input('what year? ')
        new['genre'] = input('what genre? ')
        if len(masterlist) <=7:
            masterlist.append(new)
        else:
            print ("\nwoah slow down there buddy!")
        print(masterlist)
    elif choice == 'list':
        for thing in masterlist:
            print("here ya go! ;D")
            for key, value in thing.items():
                print(f'{key} is {value}')


    elif choice == 'save':
        string = str (masterlist)
        myfile = open('music.txt', 'w')
        myfile.write(string)
        myfile.close()


    elif choice == 'help':
        print('git gud ya newb!!!!')
        print('\u0028\u0ca0\u005f\u0ca0\u0029')
        
        pass


    elif choice == 'exit':
      quit()