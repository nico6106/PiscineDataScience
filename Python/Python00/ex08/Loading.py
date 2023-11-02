import os


def ft_tqdm(lst: range) -> None:
    """function that creates a progress bar"""
    size = os.get_terminal_size()
    diff = 0
    if (lst.stop > 99):
        diff = 2
    nb_columns = size.columns - 38 - diff
    if nb_columns <= 0:
        nb_columns = 1
    size_bar = nb_columns
    for i, item in enumerate(lst, start=1):
        percent = str(int((i / lst.stop) * 100)).rjust(3, " ")
        nb_char = int((nb_columns / lst.stop) * i)
        show = '█' * nb_char + ' ' * (size_bar - nb_char)
        print(f"{percent}%|{show}| {i}/{lst.stop}", end="\r", flush=True)
        yield item
