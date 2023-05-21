
def encoder(raw):
    table = str.maketrans(
        "abcdefghijklmnopqrstuvwxyz", "cdefghijklmnopqrstuvwxyzab"
    )

    result = raw.translate(table)
    print(result)

s = encoder(raw="Thi's a Encrypted Text Plase Uncrypt me ;(")
