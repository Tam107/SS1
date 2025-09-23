def winner(votes):
    votes = sorted(votes, reverse=False)
    convert_to_dict = dict()
    for vote in votes:
        if vote in convert_to_dict:
            convert_to_dict[vote] += 1
        else:
            convert_to_dict[vote] = 1
    result =  max(convert_to_dict, key=convert_to_dict.get)
    return result

print(winner(['trump','biden','biden','biden','trump']))
print(winner(['john','johnny','jackie','johnny','john','jackie','jamie','jamie','john','johnny','jamie','johnny','john','johnny']))
print(winner(['john','johnny','jackie','johnny','john','jackie','jamie','jamie','john','johnny','jamie','johnny','john']))