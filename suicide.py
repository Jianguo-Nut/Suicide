#-*-coding:utf8;-*-

def on_user_info(server,info):
    if info.content == '!!kill' and info.is_player:
        server.execute('kill ' + info.player)



def on_load(server,old):
    server.add_help_message('!!kill' , '自杀')
