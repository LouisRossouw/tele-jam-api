

def build_txt(txt_list):
    """ Formats the next, expects an array.
    :param txt_list: string[] """

    txt_str = ""
    for txt in txt_list:
        txt_str += str(txt)
    return str(txt_str)


if __name__ == "__main__":

    txt_list = [
        f"🎥 Hello sir",
        f"\n\n",
        f"This works!",
        f"\n\n",
        f"📡😰"
    ]

    print(build_txt(txt_list))
