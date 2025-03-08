def parsefuncn(email):
    parts=email.split()
    email = parts[1]
    email_domain = email.split('@')[1]
    time=" ".join(parts[2:])
    return email_domain,time
    


email="From abc.jims@gmail.com Sun Jan 27 20:29:15 2023"
ans=parsefuncn(email)
print(f"The email has been sent through {ans[0]}\nIt was sent on {ans[1]}.")