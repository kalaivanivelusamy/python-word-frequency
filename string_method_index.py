def replace_domain(email,old_domain,new_domain):
    if "@"+ old_domain in email:
        index = email.index("@"+old_domain)
        new_email = email[:index] + "@" + new_domain
        return new_email
    return email


# Test cases
print(replace_domain("test1@test.com", "test.com", "example.com")) 
# Expected:
# test1@example.com