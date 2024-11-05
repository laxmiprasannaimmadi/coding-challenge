def get_results(division, n):
    # Your code here
    promote_teams = []
    relegate_teams = []
    sorted_division = sorted(division,key=lambda x:x['points'],reverse=True)

    if n < len(sorted_division) / 2:
            promote_teams = sorted_division[:n]
            relegate_teams = sorted_division[-n:]
    else:
        return "There are not enough teams to divide between promote and relegate teams. "

    result = "Promote:\n"
    result += "\n".join([team['name'] for team in promote_teams])
    result += "\n\nRelegate:\n"
    result += "\n".join([team['name'] for team in relegate_teams])
    result += "\n"

    return result

