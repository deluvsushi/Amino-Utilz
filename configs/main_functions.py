import AminoLab
import concurrent.futures
from tabulate import tabulate
from configs import menu_configs

client = AminoLab.Client()

# login


def auth():
    while True:
        try:
            email = input("Email >> ")
            password = input("Password >> ")
            client.auth(email=email, password=password)
            return False
        except Exception as e:
            print(e)

# get joined communities list


def communities():
    try:
        clients = client.my_communities()
        for x, name in enumerate(clients.name, 1):
            print(f"{x}.{name}")
        while True:
            ndc_Id = clients.ndc_Id[int(input("Select the community >> ")) - 1]
            return ndc_Id
    except ValueError:
        communities()
    except Exception as e:
        print(e)

# def joined chats list


def chats(ndc_id: str):
    try:
        chats = client.my_chat_threads(ndc_Id=ndc_id, size=100)
        for z, title in enumerate(chats.title, 1):
            print(f"{z}.{title}")
        while True:
            thread_Id = chats.thread_Id[int(input("Select The Chat >> ")) - 1]
            return thread_Id
    except ValueError:
        chats(ndc_id)
    except Exception as e:
        print(e)

# spam_utilz

# spam comments to wiki


def spam_comments_wiki():
    comment = input("Comment >> ")
    wiki_info = client.get_from_link(input("Wiki Link >> "))
    wiki_id = wiki_info.object_Id
    ndc_Id = wiki_info.ndc_Id
    while True:
        try:
            client.submit_comment(
                ndc_Id=ndc_Id,
                message=comment,
                wiki_Id=wiki_id)
            print("Sended Comment")
        except Exception as e:
            print(e)

# spam commdnts to blog


def spam_comments_blog():
    comment = input("Comment >> ")
    blog_info = client.get_from_link(input("Blog Link >> "))
    blog_id = blog_info.object_Id
    ndc_Id = blog_info.ndc_Id
    while True:
        try:
            client.submit_comment(
                ndc_Id=ndc_Id,
                message=comment,
                blog_Id=blog_id)
            print("Sended Comment")
        except Exception as e:
            print(e)

# spam comments to user wall


def spam_comments_user():
    comment = input("Comment >> ")
    user_info = client.get_from_link(input("User Link >> "))
    user_id = user_info.object_Id
    ndc_Id = user_info.ndc_Id
    while True:
        try:
            client.submit_comment(
                ndc_Id=ndc_Id,
                message=comment,
                user_Id=user_id)
            print("Sended Comment")
        except Exception as e:
            print(e)

# spam messages to chat


def spam_message():
    message = input("Message >> ")
    message_type = input("Message Type >> ")
    ndc_Id = communities()
    thread_Id = chats(ndc_Id)
    while True:
        try:
            print("Spamming...")
            with concurrent.futures.ThreadPoolExecutor(max_workers=150) as executor:
                _ = [
                    executor.submit(
                        client.send_message,
                        ndc_Id,
                        thread_Id,
                        message,
                        message_type) for _ in range(200000)]
        except Exception as e:
            print(e)

# spam with join and leave to chat


def spam_join_leave():
    ndc_Id = communities()
    thread_Id = chats(ndc_Id)
    def join_and_leave():
        try:
            client.leave_thread(ndc_Id=ndc_Id, thread_Id=thread_Id)
            client.join_thread(ndc_Id=ndc_Id, thread_Id=thread_Id)
        except Exception as e:
            print(e)
    while True:
        try:
            print("Joining and Leaving...")
            with concurrent.futures.ThreadPoolExecutor(max_workers=300) as executor:
                _ = [executor.submit(join_and_leave) for _ in range(2000)]
        except Exception as e:
            print(e)

# spam reports to the chat


def spam_reports_chat():
    thread_info = client.get_from_link(input("Chat Link >> "))
    thread_id = thread_info.object_Id
    ndc_Id = thread_info.ndc_Id
    while True:
        try:
            client.report(
                ndc_Id=ndc_Id,
                reason="Spam, Trolling",
                flag_type=110,
                thread_Id=thread_id)
            print("Reported Chat")
        except Exception as e:
            print(e)

# spam reports to the user


def spam_reports_user():
    user_info = client.get_from_link(input("User Link >> "))
    user_id = user_info.object_Id
    ndc_Id = user_info.ndc_Id
    while True:
        try:
            client.report(
                ndc_Id=ndc_Id,
                reason="Trolling, Pornography, Inappropriate content",
                flag_type=5,
                user_Id=user_id)
            print("Reported User!")
        except Exception as e:
            print(e)

# spam reports to the wiki


def spam_reports_wiki():
    wiki_info = client.get_from_link(input("Wiki Link >> "))
    wiki_id = wiki_info.object_Id
    ndc_Id = wiki_info.ndc_Id
    while True:
        try:
            client.report(
                ndc_Id=ndc_Id,
                reason="Inappropriate content",
                flag_type=1,
                wiki_Id=wiki_id)
            print("Reported Wiki!")
        except Exception as e:
            print(e)

# spam reports to the blog


def spam_reports_blog():
    blog_info = client.get_from_link(input("Blog Link >> "))
    blog_id = blog_info.object_Id
    ndc_Id = blog_info.ndc_Id
    while True:
        try:
            client.report(
                ndc_Id=ndc_Id,
                reason="Inappropriate content",
                flag_type=1,
                blog_Id=blog_id)
            print("Reported Blog!")
        except Exception as e:
            print(e)
# spam_utilz

# active_utilz

# follow bot


def follow_bot():
    ndc_Id = communities()
    while True:
        try:
            with concurrent.futures.ThreadPoolExecutor(max_workers=100) as executor:
                for i in range(0, 2000, 250):
                    users = client.get_online_members(
                        ndc_Id=ndc_Id, start=i, size=100)
                    for user_Id, nickname in zip(
                            users.user_Id, users.nickname):
                        _ = [
                            executor.submit(
                                client.follow_user,
                                ndc_Id,
                                user_Id)]
                        print(f"Followed {nickname}")
        except Exception as e:
            print(e)

# send active object bot
# (increase active time bot)


def increase_active():
    ndc_Id = communities()
    while True:
        try:
            client.send_active_object(ndc_Id=ndc_Id)
            print("increasing active...")
        except Exception as e:
            print(e)

# like bot


def like_bot():
    ndc_Id = communities()
    blogs_count = int(input("Blogs Count >> "))
    while True:
        try:
            with concurrent.futures.ThreadPoolExecutor(max_workers=20) as executor:
                for i in range(0, 20000, 250):
                    recent_blogs = client.get_recent_blogs(
                        ndc_Id=ndc_Id, start=i, size=blogs_count).blog_Id
                    for blog_id in recent_blogs:
                        _ = [executor.submit(client.vote, ndc_Id, blog_id)]
                        print(f"Liked >> {blog_id}")
        except Exception as e:
            print(e)
# active_utilz

# other_utilz

# join active chats


def join_active_chats():
    ndc_Id = communities()
    with concurrent.futures.ThreadPoolExecutor(max_workers=50) as executor:
        try:
            chats = client.get_public_chat_threads(ndc_Id=ndc_Id, size=100)
            for title, thread_id in zip(chats.title, chats.thread_Id):
                print(f"Joined {title}, {thread_id}")
                _ = [executor.submit(client.join_thread, ndc_Id, thread_id)]
        except Exception as e:
            print(e)

# join recommended communities


def join_recommended_communities():
    with concurrent.futures.ThreadPoolExecutor(max_workers=50) as executor:
        try:
            language = input("Language (en/ru) >> ")
            clients = client.get_public_communities(
                language=language, size=100)
            for name, ndc_id in zip(clients.name, clients.ndc_id):
                print(f"Joined community {name}, {ndc_id}")
                _ = [executor.submit(client.join_community, ndc_id)]
        except Exception as e:
            print(e)

# leave from joined chats


def leave_from_joined_chats():
    ndc_Id = communities()
    with concurrent.futures.ThreadPoolExecutor(max_workers=50) as executor:
        try:
            chats = client.my_chat_threads(ndc_Id=ndc_Id)
            for title, thread_id in zip(chats.title, chats.thread_Id):
                print(f"Left From {title}, {thread_id}")
                _ = [executor.submit(client.leave_thread, ndc_Id, thread_id)]
        except Exception as e:
            print(e)

# leave from joined communities


def leave_from_joined_communities():
    with concurrent.futures.ThreadPoolExecutor(max_workers=50) as executor:
        try:
            clients = client.my_communities()
            for name, ndc_Id in zip(clients.name, clients.ndc_Id):
                print(f"Left From {name}, {ndc_Id}")
                _ = [executor.submit(client.leave_community, ndc_Id)]
        except Exception as e:
            print(e)

# get blocker and blocked users list


def get_block_list():
    try:
        block_list = client.block_full_list()
        print("Blocked >> ", block_list["result"]["blockedUidList"])
        print("Blocker >> ", block_list["result"]["blockerUidList"])
    except Exception as e:
        print(e)

# get global information about user


def get_global_user_information():
    user_info = client.get_from_link(input("User Link >> "))
    user_id = user_info.object_Id
    ndc_Id = user_info.ndc_Id
    information = client.get_user_info(user_Id=user_id)
    print(f"\tInfo \nnickname >> {information.nickname}\ncontent >> {information.content}\nuser_Id >> {information.user_Id}\nicon >> {information.icon}\ncreatedTime >> {information.createdTime}\nmodifiedTime >> {information.modifiedTime}\nweb_url >> {information.web_URL}\n \tEnd")

# delete chat. Work only if you have host


def delete_chat():
    ndc_Id = communities()
    thread_Id = chats(ndc_Id)
    try:
        print(client.delete_thread(ndc_Id=ndc_Id, thread_Id=thread_Id))
    except Exception as e:
        print(e)

# get community information


def get_community_info():
    ndc_Id = communities()
    print(client.get_community_info(ndc_Id))

# get global information about user


def get_global_user_info():
    link_info = client.get_from_link(input("User Link >> "))
    user_info = client.get_user_info(user_Id=link_info.object_Id)
    print(
        f"""User Info:
account created time >> {user_info.createdTime}
nickname >> {user_info.nickname}
content >> {user_info.content}
icon link >> {user_info.icon}
user_Id >> {link_info.object_Id}
amino_Id >> {user_info.amino_Id}
web_url >> {user_info.web_URL}"""
    )

# get information about chat


def get_chat_info():
    link_info = client.get_from_link(input("Chat Link >> "))
    chat_info = client.get_thread(
        ndc_Id=link_info.ndc_Id,
        thread_Id=link_info.object_Id)["thread"]
    print(
        f"""Chat info:
title >> {chat_info['title']}
content >> {chat_info['content']}
members_count >> {chat_info['membersCount']}
tippers_count >> {chat_info['tipInfo']['tippersCount']}
tipped_coins >> {chat_info['tipInfo']['tippedCoins']}
thread_Id >> {thread_Id}
web_url >> {chat_info['webURL']}"""
    )

# get information about account


def get_account_info():
    account_info = client.get_account_info()["account"]
    print(
        f"""Account info:
account created time >> {account_info['createdTime']}
email >> {account_info['email']}
phoneNumber >> {account_info['phoneNumber']}
password >> {password}
nickname >> {account_info['nickname']}
user_Id >> {account_info['uid']}
amino_Id >> {account_info['aminoId']}
web_url >> {account_info['webURL']}"""
    )


# other_utilz

# profile utilz

# anti ban
def anti_ban():
    ndc_Id = communities()
    print("""[1] On AntiBan
[2] Off AntiBan""")
    select = input("Select >> ")

    if select == "1":
        try:
            content = open("antiban_text.txt").read()
            client.edit_profile(ndc_Id=ndc_Id, content=content)
            print("AntiBan Onned!")
        except Exception as e:
            print(e)

    elif select == "2":
        try:
            content = "github.com/LilZevi"
            client.edit_profile(ndc_Id=ndc_Id, content=content)
            print("AntiBan Offed")
        except Exception as e:
            print(e)

# edit profile nickname


def edit_nickname():
    ndc_Id = communities()
    nickname = input("NickName >> ")
    client.edit_profile(ndc_Id=ndc_Id, nickname=nickname)
    print(f"NickName Changed To {nickname}")

# edit profile content


def edit_content():
    ndc_Id = communities()
    content = input("Content >> ")
    client.edit_profile(ndc_Id=ndc_Id, content=content)
    print(f"Content Changed To {content}")

# profile utilz

# spam utilz functions


def spam_utilz():
    auth()
    print(tabulate(menu_configs.spam_utilz_menu, tablefmt="fancy_grid"))
    select = input("Select >> ")

    if select == "1":
        print(tabulate(menu_configs.spam_comments_menu, tablefmt="fancy_grid"))
        select = input("Select >> ")
        if select == "1":
            spam_comments_wiki()
        elif select == "2":
            spam_comments_blog()
        elif select == "3":
            spam_comments_user()

    elif select == "2":
        spam_message()

    elif select == "3":
        spam_join_leave()

    elif select == "4":
        print(tabulate(menu_configs.spam_reports_menu, tablefmt="fancy_grid"))
        select = input("Select >> ")
        if select == "1":
            spam_reports_chat()
        elif select == "2":
            spam_reports_user()
        elif select == "3":
            spam_reports_wiki()
        elif select == "4":
            spam_reports_blog()

# active utilz functions


def active_utilz():
    auth()
    print(tabulate(menu_configs.active_utilz_menu, tablefmt="fancy_grid"))
    select = input("Select >> ")

    if select == "1":
        follow_bot()
    elif select == "2":
        increase_active()
    elif select == "3":
        like_bot()

# other utilz functions


def other_utilz():
    auth()
    print(tabulate(menu_configs.other_utilz_menu, tablefmt="fancy_grid"))
    select = input("Select >> ")

    if select == "1":
        join_active_chats()
    elif select == "2":
        join_recommended_communities()
    elif select == "3":
        leave_from_joined_chats()
    elif select == "4":
        leave_from_joined_communities()
    elif select == "5":
        get_block_list()
    elif select == "6":
        get_global_user_information()
    elif select == "7":
        delete_chat()
    elif select == "8":
        get_community_info()
    elif select == "9":
        get_global_user_info()
    elif select == "10":
        get_chat_info()
    elif select == "11":
    	get_account_info()

# profile utilz functions


def profile_utilz():
    auth()
    print(tabulate(menu_configs.profile_utilz_menu, tablefmt="fancy_grid"))
    select = input("Select >> ")

    if select == "1":
        anti_ban()
    elif select == "2":
        edit_nickname()
    elif select == "3":
        edit_content()
