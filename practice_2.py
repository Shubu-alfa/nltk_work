import datetime

i = 90
print("Demo hai ye " + str(i) + " number")

now = datetime.datetime.now()


def create_file():
    with open("C:/Users/shubu/PycharmProjects/nltk_project/files/" + now.strftime('%d-%b-%Y %H-%M %p') + ".txt", "w+")as file:
        file.write(str(i))  # Write empty string


create_file()
