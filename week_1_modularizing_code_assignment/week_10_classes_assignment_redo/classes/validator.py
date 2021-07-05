class Validator():
    """A class for performing validation"""

    def checkCharacters(information, banned_characters):
        """Checks entered information to see if it exists and if it contains any banned characters
        Arguments:
            information -- the information that needs to be checked
            banned_characters -- the list of characters that are not allowed
        Returns:
            correct_characters -- boolean value, True if the information contains no banned characters, False if it does
        """
        correct_characters = True

        if information:
            for character in information:
                if character in banned_characters:
                    correct_characters = False
        else:
            correct_characters = False
        
        return correct_characters

    def checkID(passed_id, max_digits):
        """Checks an entered ID to see if it is made of digits and does not exceed the maximum length
        Arguments:
            passed_id -- any ID number
            max_digits -- the maximum allowed digits for the ID 
        Returns: 
            correct_id -- boolean value, True if the ID is comprised of digits and does not exceed the maximum, False if it fails either
        """
        if len(passed_id) <= max_digits and passed_id.isdigit():
            correct_id = True
        else:
            correct_id = False
        return correct_id

    def checkExists(passed_information):
        """Checks if information was entered or left blank
        Arguments:
            passed_information -- any information
        Returns:
            info_exists -- boolean value, True if a value exists, False if passed information is null
        """
        if passed_information:
            info_exists = True
        else:
            info_exists = False
        return info_exists