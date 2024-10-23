def main(s):
    """
    The s string variable is given. return four characters from the end.
    Args:
        s(str): parameter
    Returns:
        str: answer
    """
    a = s[-4:-1:1]
    b = s[-1]
    return "{}{}".format(a,b)
print (main("codesshooluz"))