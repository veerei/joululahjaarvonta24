import sys
from lottery import draw_lots

# DO NOT TOUCH THIS FILE

def main():
    """
    Performs the official lottery.
    """
    family_members = ["Vesa", "Saija", "Veeti", "Valtteri", "Ville"]
    lottery_result = draw_lots(family_members)
    print("Arvonnan tulos:")
    for key, value in lottery_result.items():
        print(f"{key} ostaa joululahjan {value}lle.")


if __name__ == "__main__":
    main()
