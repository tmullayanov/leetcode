#!/usr/bin/python3
import os
import pathlib


def createFile(path, fname):
    pathlib.Path(path).mkdir(parents=True, exist_ok=True)
    fullname = os.path.join(path, fname)
    open(fullname, 'w').close()
    print(f'successfully created {fullname}')


def writeTemplateToFile(file, template):
    with open(file, 'w') as f:
        with open(template, 'r') as t:
            f.write(t.read())


def getChallengeProblemName():
    month = input('enter month\n')
    weekNo = input('enter number of week\n')
    rawProblemName = input('enter the name of the problem\n')
    problemName = rawProblemName.replace(' ', '_')
    return {
        'path': os.path.join('30days-challenge', month, f'w{weekNo}'),
        'fname': problemName + '.py'
    }


def getCommonProblemName():
    rawProblemName = input('enter the name of the problem')
    problemName = rawProblemName.replace(' ', '_')
    return {
        'path': os.path.join(problemName),
        'fname': 'solution.py'
    }


def getCardProblemName():
    cardName = input('enter the name of the card\n')
    rawProblemName = input('enter the name of the problem')
    problemName = rawProblemName.replace(' ', '_')
    return {
        'path': os.path.join(cardName),
        'fname': problemName + '.py'
    }


problemCreators = {
    'challenge': getChallengeProblemName,
    'card': getCardProblemName,
    'common': getCommonProblemName
}

if __name__ == '__main__':
    problemType = input('''enter type of problem you would like to solve
    (can be only on of these: challenge, card, common)
    In case any other type provided, common problem will be created
    ''')

    creator = problemCreators.get(problemType, problemCreators['common'])
    problemParameters = creator()
    createFile(problemParameters['path'], problemParameters['fname'])

    fullname = os.path.join(
        problemParameters['path'], problemParameters['fname'])
    writeTemplateToFile(fullname, 'codegen/template.py')
