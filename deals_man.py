from os import listdir
from os.path import isfile, join
import random
import subprocess

def main():
    # get random

    failCount = 0

    receiptDir = "receipts/"

    receipts = [ f for f in listdir(receiptDir) if isfile(join(receiptDir, f))]

    for i in range(5):
        failCount += display_receipt(receiptDir + random.choice(receipts))
        if failCount >= 3:
            playSound("sorry_no_more_deals.ogg")
            return
    playSound("youre_a_deal_master.ogg")
    return

def playSound(fName):
    subprocess.call(['play', fName], stderr=subprocess.DEVNULL)

def playDeal(isDeal):
    if isDeal:
        playSound("wow_what_a_deal.ogg")
    else:
        playSound("what_a_terrible_price.ogg")

def display_receipt(fName):
    isDeal = None
    receiptBody = None
    answer = None

    with open(fName) as fHnd:
        isDeal = fHnd.readline()
        receiptBody = fHnd.read()

    isDeal = "true" in isDeal.lower()

    print(receiptBody)
    print("Is this a deal? (y/n)")
    answer = input()
    while (answer.lower() != "y" and
        answer.lower() != "n"):
        answer = input()
        print("Is this a deal? (y/n)")

    playDeal(isDeal)

    if (answer == "y" and isDeal
        or answer == 'n' and not isDeal):
        return 0
    return 1

if __name__ == '__main__':
    main()
