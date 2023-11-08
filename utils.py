def prettify_member_name(member):
    parts = str(member).split('#')
    if len(parts) == 2 and parts[1] == '0':
        return parts[0]
    else:
        return member
