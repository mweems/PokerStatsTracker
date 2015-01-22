import datetime

missingWinningInfo = {
    'winningInfo':{
        "player": "kookie4061",
        'wonPotSize': 0.16,
    },
    'flop': ['5s', 'Ks', '7c'],
    'flopPotSize': 0.08,
    'turn': '9d',
    'riverPotSize': 0.16,
    'button': 5,
    'handInfo': {
        'date': datetime.date(2014, 11, 21),
        'id': 34944307295,
        'stakes': {
            'big_blind': 0.02,
            'small_blind': 0.01}},
    'turnAction': [
        {'AAlex777718': ['bets', 0.02]},
        {'kookie4061': ['calls', 0.02]}],
    'players': [
        {'kookie4061': {
            "seat": 1,
            "stack": 8.29}},
        {'sampik87': {
            "seat": 2,
            "stack": 1.77}},
        {'Burda-sergey': {
            "seat": 3,
            "stack": 2.02}},
        {'mweems1': {
            "seat": 4,
            "stack": 1.96}},
        {'11 Hammer 1199': {
            "seat": 5,
            "stack": 1.34}},
        {'AAlex777718': {
            "seat": 6,
            "stack": 2.24}}],
    'riverAction': [
        {'AAlex777718': ['checks', 0.0]},
        {'kookie4061': ['bets', 0.16]},
        {'AAlex777718': ['folds', 0.0]}],
    'summary': [
        {'kookie4061': ['collected', '-']},
        {'Burda-sergey': ['folded', '-']},
        {'mweems1': ['folded', '-']},
        {'11 Hammer 1199': ['folded', 'Flop']},
        {'AAlex777718': ['folded', 'River']}],
    'turnPotSize': 0.12,
    'preFlopAction': [
        {'sampik87': ['calls', 0.02]},
        {'Burda-sergey': ['folds', 0.0]},
        {'mweems1': ['folds', 0.0]},
        {'11 Hammer 1199': ['calls', 0.02]},
        {'AAlex777718': ['calls', 0.01]},
        {'kookie4061': ['checks', 0.0]}],
    'cards': ['3c', 'Tc'],
    'winningHand': [],
    'river': '9c',
    'flopAction': [
        {'AAlex777718': ['bets', 0.02]},
        {'kookie4061': ['calls', 0.02]},
        {'sampik87': ['folds', 0.0]},
        {'11 Hammer 1199': ['folds', 0.0]}]}

firstHand = {
    "handInfo": {
        'id': 34944298551,
        'date': datetime.date(2014, 11, 21),
        'stakes': {
            'small_blind': .01,
            'big_blind': .02
        }
    },
    "players": [
        {"kookie4061": {
            "seat": 1,
            "stack": 8.51}},
        {"sampik87": {
            "seat": 2,
            "stack": 1.62}},
        {"Burda-sergey": {
            "seat": 3,
            "stack": 2.41}},
        {"mweems1": {
            "seat": 4,
            "stack": 2.0}},
        {"11 Hammer 1199": {
            "seat": 5,
            "stack": 1.38}},
        {"AAlex777718": {
            "seat": 6,
            "stack": 1.79}}
    ],
    "button": 2,
    "cards": ["4c", "8h"],
    "preFlopAction": [
        {"11 Hammer 1199": ["folds", 0.0]},
        {"AAlex777718": ["folds", 0.0]},
        {"kookie4061": ["calls", 0.02]},
        {"sampik87": ["calls", 0.02]},
        {"Burda-sergey": ["calls", 0.01]},
        {"mweems1": ["checks", 0.0]}
    ],
    "flop": ["Kh", "Js", "9s"],
    "flopPotSize": .08,
    "flopAction": [
        {"Burda-sergey": ["checks", 0.0]},
        {"mweems1": ["checks", 0.0]},
        {"kookie4061": ["checks", 0.0]},
        {"sampik87": ["checks", 0.0]}
    ],
    "turn": "Ks",
    "turnPotSize": .08,
    "turnAction": [
        {"Burda-sergey": ["checks", 0.0]},
        {"mweems1": ["checks", 0.0]},
        {"kookie4061": ["checks", 0.0]},
        {"sampik87": ["bets", 0.02]},
        {"Burda-sergey": ["folds", 0.0]},
        {"mweems1": ["folds", 0.0]},
        {"kookie4061": ["calls", 0.02]}
    ],
    "river": "Kc",
    "riverPotSize": .12,
    "riverAction": [
        {"kookie4061": ["checks", 0.0]},
        {"sampik87": ["bets", 0.1]},
        {"kookie4061": ["calls", 0.1]}
    ],
    "winningInfo": {
        "player": "sampik87",
        "wonPotSize": .31,
    },
    "winningHand": ["Jc", "8d"],
    "summary": [
        {"kookie4061": ["mucked", ["9d", "Ac"]]},
        {"sampik87": ["showed", "-"]},
        {"Burda-sergey": ["folded", "Turn"]},
        {"mweems1": ["folded", "Turn"]},
        {"11 Hammer 1199": ["folded", "-"]},
        {"AAlex777718": ["folded", "-"]}
    ]
}

infoMissing = {
    'winningInfo': {
        'player': 'sergei 2507',
        'wonPotSize': 0.05},
    'flop': None,
    'flopPotSize': None,
    'turn': None,
    'riverPotSize': None,
    'button': 4,
    'handInfo': {
        'date': datetime.date(2014, 11, 21),
        'id': 34944317861,
        'stakes': {
            'big_blind': 0.02,
            'small_blind': 0.01}},
    'turnAction': [],
    'players': [
        {'sergei 2507': {
            "seat": 1,
            "stack": 0.7}},
        {'sampik87': {
            "seat": 2,
            "stack": 1.5}},
        {'Burda-sergey': {
            "seat": 3,
            "stack": 2.46}},
        {'mweems1': {
            "seat": 4,
            "stack": 1.97}},
        {'11 Hammer 1199': {
            "seat": 5,
            "stack": 1.18}},
        {'AAlex777718': {
            "seat": 6,
            "stack": 2.18}}],
    'riverAction': [],
    'summary': [
        {'sampik87': ['folded', '-']},
        {'Burda-sergey': ['folded', '-']},
        {'mweems1': ['folded', '-']},
        {'11 Hammer 1199': ['folded', 'Flop']},
        {'AAlex777718': ['folded', 'Flop']}],
    'winningHand': [],
    'turnPotSize': None,
    'preFlopAction': [
        {'sergei 2507': ['raises', 0.07]},
        {'sampik87': ['folds', 0.0]},
        {'Burda-sergey': ['folds', 0.0]},
        {'mweems1': ['folds', 0.0]},
        {'11 Hammer 1199': ['folds', 0.0]},
        {'AAlex777718': ['folds', 0.0]}],
    'cards': ['7d', '8h'],
    'river': None,
    'flopAction': []
}

underscore = {
    'winningInfo': {
        'player': 'ru',
        'wonPotSize': 5.42},
    'flop': ['4s', 'Ks', 'Qs'],
    'flopPotSize': 5.7,
    'turn': '8s',
    'riverPotSize': None,
    'button': 6,
    'handInfo': {
        'date': datetime.date(2014, 11, 21),
        'id': 34944988428,
        'stakes': {
            'big_blind': 0.1,
            'small_blind': 0.05}},
    'turnAction': [
        {'serb_ru': ['bets', 2.5]},
        {'Cbass9': ['folds', 0.0]}],
    'players': [
        {"serb_ru": {
            "seat": 1,
            "stack": 7.42}},
        {'bcaalin': {
            "seat": 2,
            "stack": 10.15}},
        {'all1n4funn': {
            "seat": 3,
            "stack": 9.02}},
        {'hdig5tallesdb': {
            "seat": 4,
            "stack": 10.74}},
        {'mweems1': {
            "seat": 5,
            "stack": 9.59}},
        {'Cbass9': {
            "seat": 6,
            "stack": 10.0}}],
    'riverAction': [],
    'summary': [
        {'serb_ru': ['collected', '-']},
        {'bcaalin': ['folded', 'Flop']},
        {'all1n4funn': ['folded', '-']},
        {'hdig5tallesdb': ['folded', '-']},
        {'mweems1': ['folded', '-']},
        {'Cbass9': ['folded', 'Turn']}],
    'winningHand': [],
    'turnPotSize': 5.7,
    'preFlopAction': [
        {'all1n4funn': ['folds', 0.0]},
        {'hdig5tallesdb': ['folds', 0.0]},
        {'mweems1': ['folds', 0.0]},
        {'Cbass9': ['raises', 0.3]},
        {'serb_ru': ['raises', 1.0]},
        {'bcaalin': ['folds', 0.0]},
        {'Cbass9': ['raises', 2.8]},
        {'serb_ru': ['calls', 1.8]}],
    'cards': ['8d', 'Jh'],
    'river': None,
    'flopAction': [
        {'serb_ru': ['checks', 0.0]},
        {'Cbass9': ['checks', 0.0]}]
}