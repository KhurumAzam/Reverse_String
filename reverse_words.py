def reverse_words(s):
    # code here
    arr = s.split('.')

    count = len(arr) - 1

    while count >= 0:
        if count == 0:
            print(arr[count], end="")
        else:
            print(arr[count], end=".")
        count -= 1


if __name__ == "__main__":
    reverse_words("i.like.this.program.very.much")
