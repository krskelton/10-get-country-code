def get_country_codes(param):
    # your code here
    words = param.split()
    country_codes = []
    for word in words:
        new_word = ''
        for char in word:
            if char.isalpha():
                new_word += char
        country_codes.append(new_word)
        return_string = ", ".join(country_codes)
    return return_string
