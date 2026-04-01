def main():
    time=input("enter the time: ")
    meal=convert(time)
    if (7<=meal<=8):
        print("breakfast time")
    elif (12<=meal<=13):
        print("lunch time")
    elif (18<=meal<=19):
        print("dinner time")
    else:
        print(" ")

def convert(time):
    h,m = time.split(":")
    h=float(h)
    m =float(m)
    m=m/60
    ans=h+m
    return ans
if __name__ == "__main__":
    main()

#CHALLENGE QUESTION
def main():
    time=input("enter the time: ")
    meal=convert(time)
    if (7<=meal<=8):
        print("breakfast time")
    elif (12<=meal<=13):
        print("lunch time")
    elif (18<=meal<=19):
        print("dinner time")
    else:
        print(" ")


def convert(time):
    h,m = time.split(":")
    if "pm" in time:
        h=float(h)+12
        m =float(m)
        m=m/60
        ans=h+m
        return ans
    elif "am" in time:
        h=float(h)
        m =float(m)
        m=m/60
        ans=h+m
        return ans
main()


