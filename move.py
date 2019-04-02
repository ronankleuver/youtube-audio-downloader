import os


def move_file(new_dir):

    '''
    PARAMETER: path to new dir

    Moves file if the file has the .mp3 extension
    '''

    for file in os.listdir():
        if file.endswith(".mp3"):
            name = file
            new_name = new_dir + file
            os.rename(name, new_name)
            print('got one')
