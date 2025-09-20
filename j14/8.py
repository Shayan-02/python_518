def bs(score, day):
    if 0 <= score <= 20 and 0 <= day <= 100:
        if day == 0:
            return 20
        elif day == 7:
            return score
        else:
            if score >= day:
                return score - day
            else:
                return 0

s = int(input())
d = int(input())
print(bs(s, d))
