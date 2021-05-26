import pandas as pd


class Wtd_File_Exception(Exception):
    def __init__(self, error):
        self.error = error

    def __str__(self, *args, **kwargs):
        return self.error


def bytes_line(s: str, reverse: bool = False):
    if reverse:
        return bytes([(248 - ord(i)) % 255 for i in s])
    return bytes([ord(i) for i in s])


def bytes_recover(stream: bytes, reverse: bool = False):
    if reverse:
        return "".join([chr(255 - (7 + i) % 255) for i in stream])
    return "".join(chr(i) for i in stream)


def write_wtd(df: pd.DataFrame, texts: list, file_path, random_seed=0):
    istream = open(file_path, 'wb+')
    istream.write(bytes_line("WTDF"))
    istream.write(bytes_line("{0:06d}".format(len(texts)), reverse=True))
    istream.write(bytes_line("{0:06d}".format(df.shape[0]), reverse=True))
    istream.write(bytes_line("{0:06d}".format(random_seed), reverse=True))
    istream.write(bytes_line("{0:06d}".format(len(texts) + df.shape[0]), reverse=True))
    for line in texts:
        istream.write(bytes_line(line, reverse=True))
        istream.write(bytes_line('&', reverse=True))
    for i in range(df.shape[0]):
        istream.write(bytes_line(" ".join([str(j) for j in list(df.iloc[i])]), reverse=True))
        istream.write(bytes_line('~', reverse=True))
    istream.write(bytes_line("WTDF", reverse=True))
    istream.write(bytes_line("!", reverse=True))
    istream.write(bytes_line("!".join(df.columns), reverse=True))
    istream.close()


def read_wtd_info(file_path: str):
    ostream = open(file_path, 'rb')
    _word = ostream.readlines()[0]
    _info = bytes_recover(_word[4:], True)
    _header = bytes_recover(_word[:4])
    ostream.close()
    _seeker = 0
    if not _header == "WTDF":
        raise Wtd_File_Exception("This file is not standard well-test-data file.")
    _text_len = int(_info[_seeker: _seeker+6])
    _shape = int(_info[_seeker+6: _seeker+12])
    _seed = int(_info[_seeker+12: _seeker+18])
    _rec = int(_info[_seeker+18: _seeker+24])
    if not _rec == _text_len + _shape:
        raise Wtd_File_Exception("This file lost at least significant data.")
    _seeker += 24
    _text = _info[_seeker:].split('&')[:-1]
    _seeker += sum([len(line) for line in _text]) + _text_len
    _titles = _info.split('!')[1:]
    if not _info[_seeker:].split('~')[-1][:4] == "WTDF":
        raise Wtd_File_Exception("This file's tail is abnormal.")
    _cont = _info[_seeker:].split('~')[:-1]
    _items = [i.split(' ') for i in _cont]
    _data = pd.DataFrame(_items)
    _data.columns = _titles
    return _data, _text
