try:
    f = open('my_file.txt', 'r')
    file_data = f.read()
    f.close()
except Exception as e:
    print("{}".format(e))
