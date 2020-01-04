import os

def load(name):
    """
    This method creates and loads a new journal.
    :param name: this is the name of the journal to be loaded.
    :return: returns a list, 'data', which is either empty or is pre-loaded with previous journal entries.
    """
    data=[]
    filepath=get_full_file_path(name)

    if os.path.exists(filepath):
        with open(filepath) as existing_entries:
            for entry in existing_entries.readlines():
                data.append(entry.rstrip())
    return data

def save(name,data):
    filepath = get_full_file_path(name)
    print('saving to {}'.format(filepath))
    #fout=open(filepath, 'w')2
    with open(filepath, 'w') as fout:
        for entry in data:
            fout.write(entry+'\n')
    #fout.close() dont need this because once you exit the loop, you close


def get_full_file_path(name):
    filepath = os.path.abspath(os.path.join('.', 'journals', name + '.jrl'))  # .jrl is our made up filepath
    return filepath


def add_entry(text,data):
    return data.append(text)