import requests

x = input("Enter the word of which you want the meaning: ")

try:
    r = requests.get(f"https://api.dictionaryapi.dev/api/v2/entries/en/{x.lower()}")
except:
    print("Please make sure that you have connection.")
    exit()

res = r.json()

try:
    meanings: list = res[0]["meanings"]
    firstResult = res[0]["meanings"][0]["definitions"][0]
except:
    print("Invalid word searched.")
    exit()

meaning = firstResult["definition"]

print(f"{x.capitalize()} - " + meanings[0]["partOfSpeech"].capitalize())
print(f"1. {meaning}")
more = input("\nFor more meanings please click m. Anything else will exit.\n")

if more == "m":
    print(f"\nAll meanings of {x.lower()}:")
    for i in range(0, len(meanings)):
        print(f"{i + 1}. " + meanings[i]["definitions"][0]["definition"])
        try:
            print("Example: " + meanings[i]["definitions"][0]["example"])
        except:
            print()
            continue
        print()           
else:
    print("Exiting...")
    exit()
