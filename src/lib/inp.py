def agreement(question: str) -> bool:
    inp = ""
    while inp != 'y' and inp != 'n':
        inp = input(f"{question} [y/n]: ").lower()

    return True if inp == 'y' else False