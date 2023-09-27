def  write_notification(email:str, mensagem=''):
    with open('log.txt',mode='w') as email_file:
        conteudo = f'Email: {email} -  msg: {mensagem}'
        email_file.write(conteudo)