import webbrowser as web

class video:
    def __init__(self, title, link):
        self.Title = title
        self.Link = link
    def open_brow(self):
        web.open(self.Link)


class playlist:
    def __init__(self, name, description, rating, video):
        self.name = name
        self.description = description
        self.rating = rating
        self.video = video
    
        

def create_playlist():
    name = input("Đặt tên plalist: ")
    description = input("Miêu tả: ")
    rating = select_in_range("Xếp hạng Playlist theo số từ 1->5: ", 1, 5)
    video = create_videos()
    return playlist(name, description, rating, video)

def create_videos():
    total = select_condition("Cho vào bao nhiêu video: ")
    videos = []
    for i in range(total):
        ti = input("Tên video: ")
        li = input("Link: ")
        item = video(ti, li)
        videos.append(item)
    return videos


def write_playlist_txt(playlist):
    with open("data.txt", "w") as file:
        file.write(playlist.name + '\n')
        file.write(playlist.description + '\n')
        file.write(str(playlist.rating) + '\n')
        write_video_txt(playlist.video, file)

def write_video_txt(videos, file):
    file.write(str(len(videos)) + '\n')
    for i in range(len(videos)):
        file.write(videos[i].Title + '\n')
        file.write(videos[i].Link + '\n')


def read_playlist_from_txt():
    with open("data.txt", "r") as f:
        name = f.readline().strip('\n')
        des = f.readline().strip('\n')
        rating = f.readline().strip('\n')
        vid = read_videos_from_txt(f)
        return playlist(name, des, rating, vid)

def read_videos_from_txt(f):
    videos = []
    q = int(f.readline())
    for i in range(q):
        title = f.readline().strip('\n')
        link = f.readline().strip('\n')
        class_video = video(title, link)
        videos.append(class_video)
    return videos


def print_playlist(playlist):
    print("Tên playlist: " + playlist.name)
    print("Miêu tả: " + playlist.description)
    print("Đánh giá: " + str(playlist.rating))
    print_videos(playlist.video)

def print_videos(video):
    for i in range(len(video)):
        print("Video số " + str(i+1) + ': ')  
        print(' ' + video[i].Title)
        print("url " + str(i+1) + ': ')
        print(' ' + video[i].Link)

def play_videos(playlist):
    print_videos(playlist.video)
    choice = select_in_range("Có {} video, chọn video số mấy: ".format(len(playlist.video)),1, len(playlist.video))
    playlist.video[choice - 1].open_brow()


def select_in_range(promt,min,max):
    choice = input(promt)
    while not choice.isdigit() or int(choice) < min or int(choice) > max:
        choice = input(promt)
    choice = int(choice)
    return choice

def select_condition(promt):
    choice = input(promt)
    while not choice.isdigit():
        choice = input(promt)
    choice = int(choice)
    return choice


def show_menu():
    print("\nMain Menu:")
    print("-----------------------------------")
    print("|Lựa chọn 1: Tạo playlist.        |")
    print("|Lựa chọn 2: Show cái playlist.   |")
    print("|Lựa chọn 3: Xem video            |")
    #print("|Lựa chọn 4: Create playlist  |")
    #print("|Lựa chọn 5: Create playlist  |")
    #print("|Lựa chọn 6: Create playlist  |")
    print("|Lựa chọn 7: Lưu và thoát.        |")
    print("-----------------------------------")
    print()




def main():
    try:
        playlist = read_playlist_from_txt()
        print('Successfully saved from the last time.')
    except:
        print('Chào mừng Hoàng Hà')

    while True:
        show_menu()
        choice = select_in_range("Chọn số từ 1 đến 7: ",1,7)
        if choice == 1:
            print()
            playlist = create_playlist()
            input("\nNhấn nút bất kì để tiếp tục\n")
        elif choice == 2:
            print()
            try:
                print_playlist(playlist)
            except:
                print('Chưa có playlist nào được tạo!')
            input("\nNhấn nút bất kì để tiếp tục\n")
        elif choice == 3:
            print()
            play_videos(playlist)
            input("\nNhấn nút bất kì để tiếp tục\n")
        #elif choice == 4:
        #    menu_option_4()
        #elif choice == 5:
        #    menu_option_5()
        #elif choice == 6:
        #    menu_option_6()
        elif choice == 7:
            write_playlist_txt(playlist)
            break
main()