2 # number of integers to input
(
    010 # (input started, sign, value)
    (
        i # input
        d~!sd48*=sd25*=sd49+=s4g||| # input is delimiter
        d[
            pp2xd[pb] # input already started, break
            ![c] # input not started yet, continue
        ]
        ![3g1|3g] # input is not delimiter, input started
        d59*=[2g0-2gpc] # negative integer, change sign to -1, continue
        68*s- # input to integer
        s25** # multiply result by 10
        s+ # then add input
    )
    *sp # multiply by sign
    10-g1s- # reduce the number of integers to input by 1
    d![pb] # if it is 0, break
    10-g
)
+o # output the sum
25*`o # output a newline