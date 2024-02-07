import os


def description(name, extensions, filenames, calculate_size, full):
    # get all the files of chosen extension
    files = list(filter(lambda file: os.path.splitext(file)[1] in extensions, filenames))
    # get the file size
    size = 0
    if calculate_size:
        size = round(sum(list(map(lambda file: os.path.getsize(file), files)))/(1024*1024), 2)
    print(f'\n{name}: {len(files)}')
    if full:
        for file in files:
            print(file)
    if calculate_size:
        print(f'Total size: {size} MB', end='\n')
    # return the list of files of chosen extension
    return files, size


def file_type_categorization(dir, calculate_size=False, full=False):
    # recursively get all the files in a directory and subdirectories
    file_names = [os.path.join(dir_path, f) for (dir_path, dir_names, file_names) in os.walk(dir) for f in file_names]
    # different file extensions
    executable_ext = ['.exe', '.com', '.bat', '.sh', '.py', '.php', '.go', '.cpp', '.cs', '.java']
    image_ext = ['.jpg', '.png', '.gif', '.pcx', '.bmp', '.tif']
    text_ext = ['.txt', '.doc', '.docx', '.rtf', '.pdf']
    archives_ext = ['.zip', '.rar', '.tar', '.7z', '.gz']
    sound_ext = ['.mp3', '.wav', '.mid']
    video_ext = ['.mp4', '.avi']

    # get the list of files of chosen extension
    executable, executable_size = description('Executable files', executable_ext, file_names, calculate_size, full)
    image, image_size = description('Image files', image_ext, file_names, calculate_size, full)
    text, text_size = description('Text files', text_ext, file_names, calculate_size, full)
    archives, archives_size = description('Archives', archives_ext, file_names, calculate_size, full)
    sound, sound_size = description('Sound files', sound_ext, file_names, calculate_size, full)
    video, video_size = description('Video files', video_ext, file_names, calculate_size, full)
    # calculate the other files list with set difference
    other_files = list(set(file_names).difference(set(executable), set(image), set(text), set(archives), set(sound),
                                                  set(video)))
    other, other_size = description('Other files', [os.path.splitext(file)[1] for file in other_files], file_names,
                        calculate_size, full)
    if calculate_size:
        return [executable_size, image_size, text_size, archives_size, sound_size, video_size, other_size]
    else:
        return [len(executable), len(image), len(text), len(archives), len(sound), len(video), len(other)]


def large_files_identification(dir, size):
    large = {}
    # recursively get all the files in a directory and subdirectories
    file_names = [os.path.join(dir_path, f) for (dir_path, dir_names, file_names) in os.walk(dir) for f in file_names]
    for file in file_names:
        # find file size in bytes
        current_size = os.path.getsize(file)
        # compare to size threshold converted to bytes
        if current_size > size * 1024 * 1024:
            # add file and its size to the dictionary
            large.update([(file, round(current_size/(1024*1024), 2))])
    print(f'Files above {size} MB: {len(large.items())}')
    for key, item in large.items():
        print(f'{key} size: {item} MB')
    return large


def file_permissions_report(dir):
    unusual = {}
    # recursively get all the files in a directory and subdirectories
    file_names = [os.path.join(dir_path, f) for (dir_path, dir_names, file_names) in os.walk(dir) for f in file_names]
    for file in file_names:
        # check file properties
        file_stat = os.stat(file)
        # convert file permission
        permission = oct(file_stat.st_mode)[-3:]
        if permission[-1] != '4' and permission[-1] != '5':
            # add file and its permission to the dictionary
            unusual.update([(file, permission)])
    print(f'Files with unusual permission settings: {len(unusual.items())}')
    for key, item in unusual.items():
        print(f'{key} permission: {item}')
    return unusual
