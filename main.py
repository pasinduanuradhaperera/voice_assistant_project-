import voice_file as vo
import command_file as com

while 1:
    command= com.listening()
    if command is not None and 'hey abc' in command:
        vo.intro()
        print('you say \'', command, '\'')
        command = ''

    elif command is not None and 'exit' in command:
        print('multi is stopping ... ')
        command = ''
        exit()

    else:
        print('the command is : \'', command, '\'')
        command = ''


