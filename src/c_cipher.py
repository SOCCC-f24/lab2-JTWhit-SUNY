import logging
logging.basicConfig(level=logging.INFO, format='%(message)s')

'''
Jameir Whitley
Professor Beague
CSC 138/EN
29, September 2024
'''

def encrypt(email="abc012"):
    """
    TODO: What is the objective?

    The objective is to create a cypher for the email variable shifting each character down to three and printing the
    encrypted version of the email. Also verifying if the email contains only 6 characters first three being from the
    the alphabet and the second half being numbers.

    Args:
        TODO: what arguments and data types are expected? (i.e., email)

        len_flag: checks length of email
        anum_flag: checks if the first 3 characters are a-z and if the last 3 are
        0-9.
        email_list: converts email string to list
        new_ascii: shifts indexes of email up 3 and assigns it
        email_str: turns email list back into a new string

    Returns:
        TODO: what varibale and data types are being returned?

        the email variable will be returned as a string that gives the encrypted version of the string using the
        caesars cypher method.

    """
    output = "" 
    len_flag = len(email) != 6
    # TODO: fix line below and, implement functionality rather than literals
    # keep all updates in the anum_flag (bool) variable
    # i.e., 
    #     A = email[:3] (check first half)
    #     B = email[3:] (check second half)
    #     enum_flag = A or B
    anum_flag = email[:3].isalpha() != email[:3].isalpha() or email[3:].isdecimal() != email[3:].isdecimal()

    if len_flag:                         # NOTE: here we provide input validation on length
        output = "Length check failed\n"
        output += "Email must be 6 characters long."
        logging.info(output)
        return output        
    if anum_flag:                        # NOTE: here we provide input validation on alpha/num
        output = "alpha num check failed\n"
        output += "Email must have 3 letters followed by 3 digits."
        logging.info(output)
        return output     
        
    # TODO: fix line below, process our string into a list
    email_lst = list(email)
        
    # TODO: complete line(s) below, convert EACH new element into a string
    new_ascii = ord(email_lst[0]) + 3    # NOTE: here we extract and update element at 0 
    email_lst[0] = chr(new_ascii)        # NOTE: here we convert our ASCII into string
    new_ascii = ord(email_lst[1]) + 3
    email_lst[1] = chr(new_ascii)
    new_ascii = ord(email_lst[2]) + 3
    email_lst[2] = chr(new_ascii)
    new_ascii = ord(email_lst[3]) + 3
    email_lst[3] = chr(new_ascii)
    new_ascii = ord(email_lst[4]) + 3
    email_lst[4] = chr(new_ascii)
    new_ascii = ord(email_lst[5]) + 3
    email_lst[5] = chr(new_ascii)

    # TODO: fix line below, convert list into a string
    email_str = "".join(email_lst)

    # keep all updates in the retVal (str) variablei
    # i.e.,
    #    email_str = " some string updates here "
    #    email_1 = email_str.strip()
    #    retVal = email_1
    retVal = email_str
    return retVal 

def decrypt(dmail="def345"):
    """
    TODO: What is the objective?

     The objective is to take the the dmail string and decrpyt the email
     back down 3.


    Args:
        TODO: what arguments and data types are expected? (i.e., email)

        len_flag: checks length of dmail
        anum_flag: checks if the first 3 characters are a-z and if the last 3 are
        0-9.
        email_list: converts dmail string to list
        new_ascii: shifts indexes of dmail down 3 and assigns it
        dmail_str: turns email list back into a new string

    Returns:
        TODO: what varibale and data types are being returned?

        It returns the decrypted version if the email where all the characters
        are shifted down 3.
        
    """
    # input validation
    output = "" 
    len_flag = len(dmail) != 6
    # TODO: fix line below and, implement functionality rather than literals
    # keep all updates in the anum_flag (bool) variable
    # i.e., 
    #     A = email[:3] (check first half)
    #     B = email[3:] (check second half)
    #     enum_flag = A or B
    anum_flag = dmail[:3].isalpha() != dmail[:3].isalpha() or dmail[3:].isdecimal() != dmail[3:].isdecimal()

    if len_flag:                         # NOTE: here we provide input validation on length
        output = "Length check failed\n"
        output += "Email must be 6 characters long."
        logging.info(output)
        return output        
    if anum_flag:                        # NOTE: here we provide input validation on alpha/num
        output = "alpha num check failed\n"
        output += "Email must have 3 letters followed by 3 digits."
        logging.info(output)
        return output   

    # TODO: apply the encrypt pseudocode but shift down 3

    email_lst = list(dmail)

    new_ascii = ord(email_lst[0]) - 3    # NOTE: here we extract and update element at 0
    email_lst[0] = chr(new_ascii)        # NOTE: here we convert our ASCII into string
    new_ascii = ord(email_lst[1]) - 3
    email_lst[1] = chr(new_ascii)
    new_ascii = ord(email_lst[2]) - 3
    email_lst[2] = chr(new_ascii)
    new_ascii = ord(email_lst[3]) - 3
    email_lst[3] = chr(new_ascii)
    new_ascii = ord(email_lst[4]) - 3
    email_lst[4] = chr(new_ascii)
    new_ascii = ord(email_lst[5]) - 3
    email_lst[5] = chr(new_ascii)

    dmail_str = "".join(email_lst)

    
    # keep all updates in the retVal (str) variablei
    # i.e.,
    #    email_str = " some string updates here "
    #    email_1 = email_str.strip()
    #    retVal = email_1
    retVal = dmail_str
    return retVal
