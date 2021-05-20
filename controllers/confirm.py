def confirm_action():
    confirm = 0
    while True:
        try:
            confirm = int(input("\nTaper '1' pour confirmer, '2' pour revenir au menu précédent: "))
            if confirm in range(1, 3):
                break
        except ValueError:
            continue

    return confirm
