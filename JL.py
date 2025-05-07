import ZAminofix as amino
from pyfiglet import figlet_format
from concurrent.futures import ThreadPoolExecutor

client = amino.Client()
email = input("Your email: ")
password = input("Your password: ")
chatlink = input("Chat Link: ")
client.login(email=email, password=password)
clients = client.sub_clients(start=0, size=100)
chat_info = client.get_from_code(chatlink)
chat_id = chat_info.objectId
com_id = chat_info.path[1:chat_info.path.index('/')]
sub_client = amino.SubClient(comId=com_id)

def join_and_leave():
    try:
        sub_client.leave_chat(chatId=chat_id)
        sub_client.join_chat(chatId=chat_id)
        print("-- Joining and Leaving...")
    except BaseException:
        return


def main_process():
    while True:
        
        with ThreadPoolExecutor(max_workers=100) as executor:
            _ = [executor.submit(join_and_leave) for _ in range(100000)]


main_process()
