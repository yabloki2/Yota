def rot13(message):
    alp = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M']
    alp_res = ['N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    alp2 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm']
    alp2_res = ['n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    msg = list(message)
    for letter in msg:
        if letter in alp:
            ind = msg.index(letter)
            for j in alp:
                if j == letter:
                    ind2 = alp.index(j)
            msg[ind] = alp_res[ind2]
        elif letter in alp2:
            ind = msg.index(letter)
            for j in alp2:
                if j == letter:
                    ind2 = alp2.index(j)
            msg[ind] = alp2_res[ind2]
        elif letter in alp_res:
            ind = msg.index(letter)
            for j in alp_res:
                if j == letter:
                    ind2 = alp_res.index(j)
            msg[ind] = alp[ind2]
        elif letter in alp2_res:
            ind = msg.index(letter)
            for j in alp2_res:
                if j == letter:
                    ind2 = alp2_res.index(j)
            msg[ind] = alp2[ind2]
    res = ''
    for lt in msg:
        res += lt
    return res