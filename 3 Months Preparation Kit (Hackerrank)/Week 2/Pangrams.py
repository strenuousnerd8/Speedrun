def pangrams(s):
    # Write your code here
    return (
        "pangram"
        if all(
            [True if i in s.lower() else False for i in "abcdefghijklmnopqrstuvwxyz"]
            # Or if(len(set(s.lower().replace(' ',''))) == 26)
        )
        else "not pangram"
    )


if __name__ == "__main__":

    s = "We promptly judged antique ivory buckles for the next prize"

    result = pangrams(s)

    print(result)
