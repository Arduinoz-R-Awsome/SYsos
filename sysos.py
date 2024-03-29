"""
This code below is not made to replace the full functionality 
of an operating system, it is experimental and is made to spark 
your imagination. Please use it as such.
"""
#Define variables
vsn = 1
cfgvsn = 1.0
tasks = ['Clearing output...', 'Loading files...', 'Creating PWDs...', 'Opening \'VirusKiller.op\'...', 'Loading index buffer...', 'Loading \'CMDs.pTx\'...']
modules = ['time', 'random', 'numpy', 'json']
Commands = ['con', 'move', 'dir', 'wipe', 'bam', 'ch', 'make', 'rmv', 'run', 'open', 'sysos']
def setCommandHelp():
    global CMDHelp
    CMDHelp = {Commands[0]: 'Lists the contents of the current directory', 
            Commands[1]: 'Changes the current directory', 
            Commands[2]: 'Lists the current directory', 
            Commands[3]: 'Clears the system output', 
            Commands[4]: 'Returns to your default terminal', 
            Commands[5]: 'A generic command that can: \n- Rename documents \n- Edit the commands\n- Change your username', 
            Commands[6]: 'This command can make files and folders', 
            Commands[7]: 'Can delete any thing from files to folders', 
            Commands[8]: 'Runs the command entered in the default terminal', 
            Commands[9]: 'Displays the contents of a file'}
    
setCommandHelp()
CmdPreset = 'SYSOS Commands'
SysosCommands = ['con', 'move', 'dir', 'wipe', 'bam', 'ch', 'make', 'rmv', 'run', 'open', 'sysos']
UnixCommands = ['ls', 'cd', 'pwd', 'clear', 'exit', 'ch', 'touch', 'rm', 'run', 'open', 'sysos']
cmdLIST = []

files = {'docs': ['/user/main', 'Direc'], 'Test.text': ['/user/main', 'Text'], 'user': ['/', 'Direc'], 'main': ['/user', 'Direc']}
Directory = '/user/main'
DirContent = []
LsCache = {}
CTemp = []
global editCmd

#Colors:
Error = 'red'
Warning = 'yellow'
SystemOut = 'cyan'
Advice = 'magenta'
Other = 'white'
cPrompt = 'dark_grey'
#File colors:
Direc = 'blue'
Text = 'magenta'
Runable = 'green'

#Import necessary modules
import time, random, numpy as np
from os import system as run
import sys, difflib, json
from termcolor import *

#Load everything
print(f'Loading Paradigm OS version {vsn}...')
for i in tasks:
    print(colored(i, 'black', 'on_cyan'))
    time.sleep(0) #random.randint(1, 3) 
    if tasks.index(i) == 0:
        run('clear')
        print(colored('Output cleared', 'cyan', attrs=['blink']))

usrN = input(colored('Enter your username: ', 'black', f'on_{cPrompt}'))

#Define functions
def typingPrint(text, end='\n'):
    text += end  
    for character in text:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.01)
  
def typingInput(text):
    for character in text:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.01)
    value = input()
    return value

def colorize(input):
    """Adds colors to the Ls() output, but it may work for other functions

    Args:
        input (list): Needs to be the DirContent list of dictionaries.

    Returns:
        List: Use this to nest in a parameter of a function.
    """
    ColorFiles = []
    index = 0
    while index < len(input):
        for key in input[index].keys():
            CTemp = input[index][key]
            if CTemp == 'Direc':
                ColorFiles.append(colored(key, Direc))
            elif CTemp == 'Text':
                ColorFiles.append(colored(key, Text))
        index += 1
    return ColorFiles

def write(*ipt):
    """
    Displays a neatly formated message to the console.
    """
    print('*')
    for i in ipt:
        print(f'* {i}')
    print('*')

def changeUserName():
    """
    Changes the username of the user.
    """
    global usrN 
    write(colored('Are you sure you want to change your username? [y/n]', Warning))
    ans = input()
    if ans == 'y':
        
        usrN = input(colored('Enter your new username: ', 'black', f'on_{cPrompt}'))
        write(colored(f'Your username has been changed to {usrN}.', SystemOut))
    elif ans == 'n':
        write(colored('No changes made.', SystemOut))
    else:
        write(colored('Invalid input.', Error))
        print(didYouMean(ans, ['y', 'n']))
        
def listContents(prt=True):
    DirContent = []
    for item in files.keys():
        if files[item][0] == Directory:
            TmpDic = {item: files[item][1]}
            DirContent.append(TmpDic)
        TmpDic = {}
    #colorize(DirContent)
    #write(' '.join(ColorFiles))
    if prt:
        print(' '.join(colorize(DirContent)))
    else:
        return DirContent
    
def NotFound(ipt, error='Fatal Error'):
    print(colored('*', Error))
    print(colored(f'*{error}!', Error))
    print(colored(f'*Command \'{ipt}\' not found.', Error))
    print(colored('*         ', Error), end='')
    for i in range(0, len(ipt)):
        print(colored('^', Error), end='')
    print()
    print(colored('*', Error))

def didYouMean(item, matches=Commands):
    """Returns a colored message if the item is not found in the list of commands.

    Args:
        item (string): The misspelled command.
        matches (list, optional): The list of options to choose from. Defaults to Commands.

    Returns:
        String: The colored error message.
    """
    fix = difflib.get_close_matches(item, matches)
    if fix != []:
        return colored(f"Maybe you meant '" + colored(', '.join(fix), Advice, attrs=["bold"])+ colored("'?", Advice), Advice, attrs=[])
    else:
        return colored('No fixes available.', Advice)

def prompt(idx):
    if idx == 'RootUserError':
        write(colored('WARNING!', Warning), colored('The action you are about to take is reserved for ROOT users. Are you sure you want to continue?', Warning))
        if input().lower().startswith('y'):
            return 'continue'

def getArgs(idx):
    """ Gets the arguments of a given prompt.

    Args:
        idx (string): The input entered by the user.

    Returns:
        RAW: a list of the arguments entered by the user.
    """
    raw = idx.split()
    return raw[1:]

def getFunction(idx):
    """ Gets the function of a given prompt.

    Args:
        idx (string): The input entered by the user.

    Returns:
        RAW: a string (the function name) entered by the user.
    """
    raw = idx.split()
    return raw[0]

def make(i):
    """Makes a file in the list of files, as well as a text file.

    Args:
        i (String): The desired file name.
    """
    try:
        filen = f'{getArgs(i)[0]}.{getArgs(i)[1].lower()}'
        files[filen] = list([Directory, getArgs(i)[1].capitalize()])
        with open(f'{getArgs(i)[0]}.txt', 'w') as f:
            f.write(f"FILE CREATED AT {time.strftime('%Y-%m-%d %H:%M')}\n")
    except IndexError:
        files[f'{getArgs(i)[0]}'] = list([Directory, 'Direc'])
    listContents()

#Main loop
while True:
    prmt = input(colored(f'{usrN}@SYsos', 'green') + colored(' $ ', 'blue')) #f'{usrN}@ParadigmPC $ '
    
    if prmt == '': print()
    
    elif getFunction(prmt) not in Commands:
        NotFound(prmt, error='Not found error')
        print(didYouMean(prmt))
        
    elif prmt == Commands[0]: listContents()                                        #con
    
    elif getFunction(prmt) == Commands[1]:                                                       #move
        if getArgs(prmt) == []:
            write(colored(f'WARNING! Command \'{Commands[1]}\' needs a parameter', Warning))
            continue

        if ''.join(getArgs(prmt)) == 'up':
            tmp = Directory.split('/')
            del tmp[-1]
            tmp = '/'.join(tmp)
            Directory = tmp
            print(colored(Directory, Direc))

        elif ''.join(getArgs(prmt)) in [k for d in listContents(False) for k in d.keys()]:
            Directory += f'/{getArgs(prmt)[0]}'
            print(colored(Directory, Direc))
        elif ''.join(getArgs(prmt)) not in [k for d in listContents(False) for k in d.keys()]:
            write(colored('No such directory', Error))
            

    elif prmt == Commands[3]: run('clear')                                                             #wipe
    
    elif prmt == Commands[4]: raise SystemExit                                                         #bam
    
    elif prmt == Commands[2]: print(colored(Directory, SystemOut))                                     #dir

    elif getFunction(prmt) == Commands[5]:                                                             #ch
            if getArgs(prmt) == []:
                write(colored(f'WARNING! Command \'{Commands[5]}\' needs a parameter', Warning))
                continue
            if getArgs(prmt) == ['usern']: changeUserName()
            if getArgs(prmt)[0] == 'cmds':
                if '-super' not in getArgs(prmt):
                    if prompt('RootUserError') == 'continue':
                        print(colored('LISTING COMMANDS:', SystemOut))
                        for i in range(0, len(Commands)):
                            print(colored(Commands[i], SystemOut, attrs=['bold']), end=colored(', ', SystemOut, attrs=['bold']))
                            time.sleep(0.1)
                        print()
                        editCmd = typingInput(colored('Command to edit: ', cPrompt))
                        if editCmd == '': continue
                        if editCmd == 'done': flag = 'done'; continue
                        if editCmd not in Commands:
                            NotFound(editCmd, error='Not found error')
                            print(didYouMean(editCmd))
                            continue
                        changeCmd = input(colored(f'Change \'{editCmd}\' to: ', cPrompt))
                        Commands[Commands.index(editCmd)] = changeCmd
                        setCommandHelp()
                elif '-super' in getArgs(prmt):
                    print(colored('LISTING COMMANDS:', SystemOut))
                    for i in range(0, len(Commands)):
                        print(colored(Commands[i], SystemOut, attrs=['bold']), end=colored(', ', SystemOut, attrs=['bold']))
                    print()
                    editCmd = input(colored('Command to edit: ', cPrompt))
                    if editCmd == '': continue
                    if editCmd == 'done': flag = 'done'; continue
                    if editCmd not in Commands:
                        NotFound(editCmd, error='Not found error')
                        print(didYouMean(editCmd))
                        continue
                    changeCmd = input(colored(f'Change \'{editCmd}\' to: ', cPrompt))
                    Commands[Commands.index(editCmd)] = changeCmd
                    setCommandHelp()

    elif getFunction(prmt) == Commands[6]:                                                            #make
        make(prmt)
    elif getFunction(prmt) == Commands[7]:                                                            #rmv
        try:
            if getArgs(prmt)[0] in files:
                del files[getArgs(prmt)[0]]
                listContents()
            else:
                write(colored(f'No such file or directory: {getArgs(prmt)[0]}', Error))
        except IndexError:
            write(colored(f'WARNING! Command \'{Commands[7]}\' needs a parameter', Warning))
    elif getFunction(prmt) == Commands[8]:                                                            #run
        if getArgs(prmt) != []:
            run(' '.join(getArgs(prmt)))
        else:
            write(colored(f'WARNING! Command \'{Commands[8]}\' needs a parameter', Warning))
    elif getFunction(prmt) == Commands[9]:                                                            #Open
        with open(f'{getArgs(prmt)[0]}.txt', 'r') as file:
            print(file.read())
    elif getFunction(prmt) == Commands[10]:                                                           #sysos
        try:
            if getArgs(prmt)[0] == 'config':
                #Start sysos configuration
                run('clear')
                menu = 'main'
                typingPrint(colored('SYSOS CONFIGURATION TOOL', 'green', 'on_cyan'))
                typingPrint(colored(f'      version {cfgvsn}       ', 'green', 'on_cyan'))
                print(colored(f'Menu: {menu}', 'green', 'on_yellow'))
                typingPrint(colored('SETTINGS OPTIONS:', 'red'))
                typingPrint(colored('1: ', Other) + colored('Command Configuration', 'red'))
                typingPrint(colored('2: ', Other) + colored('Color Theme\n', 'red'))
                while True:
                    ans = typingInput(colored('>', cPrompt))
                    if ans == 'done': run('clear'); break
                    else:
                        if ans == '1':
                            menu = 'Command Cfg'
                            run('clear')
                            print(colored('SYSOS CONFIGURATION TOOL', 'green', 'on_cyan'))
                            print(colored(f'      version {cfgvsn}       ', 'green', 'on_cyan'))
                            print(colored(f'Menu: {menu}', 'green', 'on_yellow'))
                            typingPrint(colored('1: ', Other) + colored('Edit commands', 'red'))
                            typingPrint(colored('2: ', Other) + colored('Choose Preset\n', 'red'))                
                            ans = typingInput(colored('>', cPrompt))
                            if ans == '1':
                                flag = ''
                                while flag != 'done':
                                    run('clear')
                                    print(colored('SYSOS CONFIGURATION TOOL', 'green', 'on_cyan'))
                                    print(colored(f'      version {cfgvsn}       ', 'green', 'on_cyan'))                            
                                    print(colored('LISTING COMMANDS:', SystemOut))
                                    for i in range(0, len(Commands)):
                                        print(colored(Commands[i], SystemOut, attrs=['bold']), end=colored(', ', SystemOut, attrs=['bold']))
                                        time.sleep(0.1)
                                    print()
                                    editCmd = typingInput(colored('Command to edit: ', cPrompt))
                                    if editCmd == '': continue
                                    if editCmd == 'done': flag = 'done'; continue
                                    if editCmd not in Commands:
                                        NotFound(editCmd, error='Not found error')
                                        print(didYouMean(editCmd))
                                        continue
                                    changeCmd = input(colored(f'Change \'{editCmd}\' to: ', cPrompt))
                                    Commands[Commands.index(editCmd)] = changeCmd
                                    setCommandHelp()
                            elif ans == '2':
                                flag = ''
                                while flag != 'done':
                                    run('clear')
                                    print(colored('SYSOS CONFIGURATION TOOL', 'green', 'on_cyan'))
                                    print(colored(f'      version {cfgvsn}       ', 'green', 'on_cyan'))
                                    typingPrint(colored('COMMANDS PRESETS:', 'red'))
                                    typingPrint(colored('1: ', Other) + colored('Unix', 'red'))
                                    typingPrint(colored('2: ', Other) + colored('SYSOS\n', 'red'))
                                    ans = typingInput(colored('Chosen Preset:', cPrompt))
                                    if ans == '1':
                                        Commands = UnixCommands[:]
                                        CmdPreset = 'Unix Commands'
                                        flag = 'done'
                                    elif ans == '2':
                                        Commands = SysosCommands[:]
                                        CmdPreset = 'SYSOS Commands'
                                        flag = 'done'
                                    elif ans == 'main':
                                        pass
                                    else:
                                        time.sleep(random.randint(0, 2))
                                        typingPrint(colored(f'Invalid input: {ans}', Error))
                                        time.sleep(2)
                                typingInput(colored(f'Commands changed to {CmdPreset} ↵', SystemOut))
                            elif ans == 'main':
                                pass
                            else:
                                time.sleep(random.randint(0, 2))
                                typingPrint(colored(f'Invalid input: {ans}', Error))
                                time.sleep(2)
                        elif ans == 'main':
                            time.sleep(random.randint(0, 2))
                            typingPrint(colored(f'Already in \'main\'', Error))
                            time.sleep(2)
                        else:
                            time.sleep(random.randint(0, 2))
                            typingPrint(colored(f'Invalid input: {ans}', Error))
                            time.sleep(2)
                    menu = 'main'
                    run('clear')
                    print(colored('SYSOS CONFIGURATION TOOL', 'green', 'on_cyan'))
                    print(colored(f'      version {cfgvsn}       ', 'green', 'on_cyan'))
                    print(colored(f'Menu: {menu}', 'green', 'on_yellow'))
                    print(colored('SETTINGS OPTIONS:', 'red'))
                    print(colored('1: ', Other) + colored('Command Configuration', 'red'))
                    print(colored('2: ', Other) + colored('Color Theme\n', 'red'))
            elif getArgs(prmt)[0] == 'help':
                try:
                    typingPrint(colored(CMDHelp[getArgs(prmt)[1]], SystemOut), end=colored(' ↵', SystemOut))
                    typingInput('')
                except Exception:
                    print(colored(f'Command \'{getArgs(prmt)[1]}\' does not exist', Error))
        except Exception: typingPrint(colored(f'SYSOS Version: {vsn}', SystemOut), end=colored(' ↵', SystemOut)); input()
