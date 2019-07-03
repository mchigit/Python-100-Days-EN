def get_suffix(filename, has_dot=False):
    """

    :param filename: file name
    :param has_dot: whether the extension returned contains period
    :return: file extension
    """
    pos = filename.rfind('.')
    if 0 < pos < len(filename) - 1:
        index = pos if has_dot else pos + 1
        return filename[index:]
    else:
        return ''

print(get_suffix("file.tx.t", True))