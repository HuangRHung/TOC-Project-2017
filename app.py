import sys
from io import BytesIO

import telegram
from flask import Flask, request, send_file

from fsm import TocMachine


API_TOKEN = '350183261:AAHpq0MuJcpR2Cn4_1nIRu6JVZR0HvAfOBg'
WEBHOOK_URL = 'https://545d6117.ngrok.io/hook'

app = Flask(__name__)
bot = telegram.Bot(token=API_TOKEN)
machine = TocMachine(
    states=[
        'user','state0','state1','state2','state3','state4','state5','state6','state7','state8',
       	'state9','state10','state11','state12','state13','state14','state15','state16','state17',
        'state18','state19','state20','state21','state22','state23','state24','state25','state26',
        'state27','state28','state29','state30','state31','state32','state33','state34','state35',
        'state36','state37','state38','state39','state40','state41','state42','state43','state44',
        'state45','state46','state47','state48','state49','state50','state51','state52','state53',
	'state54','state55','state56','state57','state58','state59','state60','state61','state62',
	'state63','state64','state65','state66','state67','state68','state69','state70','state71',
       	'state72','state73','state74','state75','state76','state77','state78','state79','state80',
        'state81','state82', 'state83','state84', 'state85','state86', 'state87','state88','state89',
	'state90', 'state91','state92', 'state93','state94', 'state95','state96', 'state97',
        'state98','state99','state100', 'state101','state102', 'state103','state104', 'state105',
        'state106', 'state107','state108', 'state109','state110', 'state111','state112', 'state113',
       	'state114', 'state115','state116', 'state117'

    ],
    transitions=[
	{
	    'trigger': 'advance',
	    'source': 'user',
	    'dest': 'state0',
	    'conditions': 'is_going_to_state0'
	},
        {
            'trigger': 'advance',
            'source': 'state0',
            'dest': 'state1',
            'conditions': 'is_going_to_state1'
        },
##############################################################
	{
            'trigger': 'advance',
            'source': 'state1',
            'dest': 'state2',
            'conditions': 'is_going_to_state2'
        },
        {
            'trigger': 'advance',
            'source': 'state1',
            'dest': 'state3',
            'conditions': 'is_going_to_state3'
        },
        {
            'trigger': 'advance',
            'source': 'state1',
            'dest': 'state4',
            'conditions': 'is_going_to_state4'
        },
        {
            'trigger': 'advance',
            'source': 'state1',
            'dest': 'state5',
            'conditions': 'is_going_to_state5'
        },
############################################################
        {
            'trigger': 'advance',
            'source': 'state2',
            'dest': 'state6',
            'conditions': 'is_going_to_state6'
        },
        {
            'trigger': 'advance',
            'source': 'state2',
            'dest': 'state7',
            'conditions': 'is_going_to_state7'
        },
        {
            'trigger': 'advance',
            'source': 'state2',
            'dest': 'state8',
            'conditions': 'is_going_to_state8'
        },
        {
            'trigger': 'advance',
            'source': 'state2',
            'dest': 'state9',
            'conditions': 'is_going_to_state9'
        },
	        {
            'trigger': 'advance',
            'source': 'state2',
            'dest': 'state10',
            'conditions': 'is_going_to_state10'
        },
        {
            'trigger': 'advance',
            'source': 'state2',
            'dest': 'state11',
            'conditions': 'is_going_to_state11'
        },
        {
            'trigger': 'advance',
            'source': 'state2',
            'dest': 'state12',
            'conditions': 'is_going_to_state12'
        },

############################################################	
        {
            'trigger': 'advance',
            'source': 'state3',
            'dest': 'state13',
            'conditions': 'is_going_to_state13'
        },
        {
            'trigger': 'advance',
            'source': 'state3',
            'dest': 'state14',
            'conditions': 'is_going_to_state14'
        },
        {
            'trigger': 'advance',
            'source': 'state3',
            'dest': 'state15',
            'conditions': 'is_going_to_state15'
        },
        {
            'trigger': 'advance',
            'source': 'state3',
            'dest': 'state16',
            'conditions': 'is_going_to_state16'
        },
                {
            'trigger': 'advance',
            'source': 'state3',
            'dest': 'state17',
            'conditions': 'is_going_to_state17'
        },

###########################################################
        {
            'trigger': 'advance',
            'source': 'state4',
            'dest': 'state18',
            'conditions': 'is_going_to_state18'
        },
        {
            'trigger': 'advance',
            'source': 'state4',
            'dest': 'state19',
            'conditions': 'is_going_to_state19'
        },
        {
            'trigger': 'advance',
            'source': 'state4',
            'dest': 'state20',
            'conditions': 'is_going_to_state20'
        },
        {
            'trigger': 'advance',
            'source': 'state4',
            'dest': 'state21',
            'conditions': 'is_going_to_state21'
        },
        {
            'trigger': 'advance',
            'source': 'state4',
            'dest': 'state22',
            'conditions': 'is_going_to_state22'
        },

############################################################
        {
            'trigger': 'advance',
            'source': 'state5',
            'dest': 'state23',
            'conditions': 'is_going_to_state23'
        },
        {
            'trigger': 'advance',
            'source': 'state5',
            'dest': 'state24',
            'conditions': 'is_going_to_state24'
        },
############################################################
        {
            'trigger': 'advance',
            'source': 'state6',
            'dest': 'state25',
            'conditions': 'is_going_to_state25'
        },
        {
            'trigger': 'advance',
            'source': 'state6',
            'dest': 'state26',
            'conditions': 'is_going_to_state26'
        },

############################################################
       {
            'trigger': 'advance',
            'source': 'state7',
            'dest': 'state27',
            'conditions': 'is_going_to_state27'
        },
        {
            'trigger': 'advance',
            'source': 'state7',
            'dest': 'state28',
            'conditions': 'is_going_to_state28'
        },

############################################################
       {
            'trigger': 'advance',
            'source': 'state8',
            'dest': 'state29',
            'conditions': 'is_going_to_state29'
        },
        {
            'trigger': 'advance',
            'source': 'state8',
            'dest': 'state30',
            'conditions': 'is_going_to_state30'
        },

############################################################
       {
            'trigger': 'advance',
            'source': 'state9',
            'dest': 'state31',
            'conditions': 'is_going_to_state31'
        },
        {
            'trigger': 'advance',
            'source': 'state9',
            'dest': 'state32',
            'conditions': 'is_going_to_state32'
        },

############################################################
       {
            'trigger': 'advance',
            'source': 'state10',
            'dest': 'state33',
            'conditions': 'is_going_to_state33'
        },
        {
            'trigger': 'advance',
            'source': 'state10',
            'dest': 'state34',
            'conditions': 'is_going_to_state34'
        },

############################################################
       {
            'trigger': 'advance',
            'source': 'state11',
            'dest': 'state35',
            'conditions': 'is_going_to_state35'
        },
        {
            'trigger': 'advance',
            'source': 'state11',
            'dest': 'state36',
            'conditions': 'is_going_to_state36'
        },

############################################################
        {
            'trigger': 'advance',
            'source': 'state12',
            'dest': 'state37',
            'conditions': 'is_going_to_state37'
        },
                {
            'trigger': 'advance',
            'source': 'state12',
            'dest': 'state38',
            'conditions': 'is_going_to_state38'
        },

############################################################
        {
            'trigger': 'advance',
            'source': 'state26',
            'dest': 'state39',
            'conditions': 'is_going_to_state39'
        },
        {
            'trigger': 'advance',
            'source': 'state26',
            'dest': 'state40',
            'conditions': 'is_going_to_state40'
        },
        {
            'trigger': 'advance',
            'source': 'state26',
            'dest': 'state41',
            'conditions': 'is_going_to_state41'
        },

############################################################
        {
            'trigger': 'advance',
            'source': 'state28',
            'dest': 'state42',
            'conditions': 'is_going_to_state42'
        },
        {
            'trigger': 'advance',
            'source': 'state28',
            'dest': 'state43',
            'conditions': 'is_going_to_state43'
        },
        {
            'trigger': 'advance',
            'source': 'state28',
            'dest': 'state44',
            'conditions': 'is_going_to_state44'
        },
###########################################################
        {
            'trigger': 'advance',
            'source': 'state30',
            'dest': 'state45',
            'conditions': 'is_going_to_state45'
        },
#############################################################
       {
            'trigger': 'advance',
            'source': 'state32',
            'dest': 'state46',
            'conditions': 'is_going_to_state46'
        },
       {
            'trigger': 'advance',
            'source': 'state32',
            'dest': 'state47',
            'conditions': 'is_going_to_state47'
        },
       {
            'trigger': 'advance',
            'source': 'state32',
            'dest': 'state48',
            'conditions': 'is_going_to_state48'
        },

############################################################
       {
            'trigger': 'advance',
            'source': 'state34',
            'dest': 'state49',
            'conditions': 'is_going_to_state49'
        },
       {
            'trigger': 'advance',
            'source': 'state34',
            'dest': 'state50',
            'conditions': 'is_going_to_state50'
        },
       {
            'trigger': 'advance',
            'source': 'state34',
            'dest': 'state51',
            'conditions': 'is_going_to_state51'
        },

############################################################
       {
            'trigger': 'advance',
            'source': 'state36',
            'dest': 'state52',
            'conditions': 'is_going_to_state52'
        },
       {
            'trigger': 'advance',
            'source': 'state36',
            'dest': 'state53',
            'conditions': 'is_going_to_state53'
        },
       {
            'trigger': 'advance',
            'source': 'state36',
            'dest': 'state54',
            'conditions': 'is_going_to_state54'
        },

############################################################
       {
            'trigger': 'advance',
            'source': 'state38',
            'dest': 'state55',
            'conditions': 'is_going_to_state55'
        },
       {
            'trigger': 'advance',
            'source': 'state38',
            'dest': 'state56',
            'conditions': 'is_going_to_state56'
        },
       {
            'trigger': 'advance',
            'source': 'state38',
            'dest': 'state57',
            'conditions': 'is_going_to_state57'
        },

############################################################
        {
            'trigger': 'advance',
            'source': 'state13',
            'dest': 'state58',
            'conditions': 'is_going_to_state58'
        },
                {
            'trigger': 'advance',
            'source': 'state13',
            'dest': 'state59',
            'conditions': 'is_going_to_state59'
        },

############################################################
        {
            'trigger': 'advance',
            'source': 'state14',
            'dest': 'state60',
            'conditions': 'is_going_to_state60'
        },
                {
            'trigger': 'advance',
            'source': 'state14',
            'dest': 'state61',
            'conditions': 'is_going_to_state61'
        },

############################################################
        {
            'trigger': 'advance',
            'source': 'state15',
            'dest': 'state62',
            'conditions': 'is_going_to_state62'
        },
                {
            'trigger': 'advance',
            'source': 'state15',
            'dest': 'state63',
            'conditions': 'is_going_to_state63'
        },

############################################################
        {
            'trigger': 'advance',
            'source': 'state16',
            'dest': 'state64',
            'conditions': 'is_going_to_state64'
        },
                {
            'trigger': 'advance',
            'source': 'state16',
            'dest': 'state65',
            'conditions': 'is_going_to_state65'
        },

############################################################
        {
            'trigger': 'advance',
            'source': 'state17',
            'dest': 'state66',
            'conditions': 'is_going_to_state66'
        },
                {
            'trigger': 'advance',
            'source': 'state17',
            'dest': 'state67',
            'conditions': 'is_going_to_state67'
        },
#################################################################
       {
            'trigger': 'advance',
            'source': 'state59',
            'dest': 'state68',
            'conditions': 'is_going_to_state68'
        },
       {
            'trigger': 'advance',
            'source': 'state59',
            'dest': 'state69',
            'conditions': 'is_going_to_state69'
        },
       {
            'trigger': 'advance',
            'source': 'state59',
            'dest': 'state70',
            'conditions': 'is_going_to_state70'
        },

############################################################
       {
            'trigger': 'advance',
            'source': 'state61',
            'dest': 'state71',
            'conditions': 'is_going_to_state71'
        },
       {
            'trigger': 'advance',
            'source': 'state61',
            'dest': 'state72',
            'conditions': 'is_going_to_state72'
        },
       {
            'trigger': 'advance',
            'source': 'state61',
            'dest': 'state73',
            'conditions': 'is_going_to_state73'
        },

############################################################
       {
            'trigger': 'advance',
            'source': 'state63',
            'dest': 'state74',
            'conditions': 'is_going_to_state74'
        },
       {
            'trigger': 'advance',
            'source': 'state63',
            'dest': 'state75',
            'conditions': 'is_going_to_state75'
        },
       {
            'trigger': 'advance',
            'source': 'state63',
            'dest': 'state76',
            'conditions': 'is_going_to_state76'
        },

############################################################       
       	{
            'trigger': 'advance',
            'source': 'state65',
            'dest': 'state65',
            'conditions': 'is_going_to_state77'
        },
       {
            'trigger': 'advance',
            'source': 'state65',
            'dest': 'state78',
            'conditions': 'is_going_to_state78'
        },
       {
            'trigger': 'advance',
            'source': 'state65',
            'dest': 'state79',
            'conditions': 'is_going_to_state79'
        },

############################################################
       {
            'trigger': 'advance',
            'source': 'state67',
            'dest': 'state80',
            'conditions': 'is_going_to_state80'
        },
       {
            'trigger': 'advance',
            'source': 'state67',
            'dest': 'state81',
            'conditions': 'is_going_to_state81'
        },
       {
            'trigger': 'advance',
            'source': 'state67',
            'dest': 'state82',
            'conditions': 'is_going_to_state82'
        },

############################################################
        {
            'trigger': 'advance',
            'source': 'state18',
            'dest': 'state83',
            'conditions': 'is_going_to_state83'
        },
                {
            'trigger': 'advance',
            'source': 'state18',
            'dest': 'state84',
            'conditions': 'is_going_to_state84'
        },
#################################################################
        {
            'trigger': 'advance',
            'source': 'state19',
            'dest': 'state85',
            'conditions': 'is_going_to_state85'
        },
                {
            'trigger': 'advance',
            'source': 'state19',
            'dest': 'state86',
            'conditions': 'is_going_to_state86'
        },
#################################################################
        {
            'trigger': 'advance',
            'source': 'state20',
            'dest': 'state87',
            'conditions': 'is_going_to_state87'
        },
                {
            'trigger': 'advance',
            'source': 'state20',
            'dest': 'state88',
            'conditions': 'is_going_to_state88'
        },
#################################################################
        {
            'trigger': 'advance',
            'source': 'state21',
            'dest': 'state89',
            'conditions': 'is_going_to_state89'
        },
                {
            'trigger': 'advance',
            'source': 'state21',
            'dest': 'state90',
            'conditions': 'is_going_to_state90'
        },
#################################################################
        {
            'trigger': 'advance',
            'source': 'state22',
            'dest': 'state91',
            'conditions': 'is_going_to_state91'
        },
                {
            'trigger': 'advance',
            'source': 'state22',
            'dest': 'state92',
            'conditions': 'is_going_to_state92'
        },
#################################################################
       {
            'trigger': 'advance',
            'source': 'state84',
            'dest': 'state93',
            'conditions': 'is_going_to_state93'
        },
       {
            'trigger': 'advance',
            'source': 'state84',
            'dest': 'state94',
            'conditions': 'is_going_to_state94'
        },
       {
            'trigger': 'advance',
            'source': 'state84',
            'dest': 'state95',
            'conditions': 'is_going_to_state95'
        },

############################################################
       {
            'trigger': 'advance',
            'source': 'state86',
            'dest': 'state96',
            'conditions': 'is_going_to_state96'
        },
       {
            'trigger': 'advance',
            'source': 'state86',
            'dest': 'state97',
            'conditions': 'is_going_to_state97'
        },
       {
            'trigger': 'advance',
            'source': 'state86',
            'dest': 'state98',
            'conditions': 'is_going_to_state98'
        },

############################################################
       {
            'trigger': 'advance',
            'source': 'state88',
            'dest': 'state99',
            'conditions': 'is_going_to_state99'
        },
       {
            'trigger': 'advance',
            'source': 'state88',
            'dest': 'state100',
            'conditions': 'is_going_to_state100'
        },
       {
            'trigger': 'advance',
            'source': 'state88',
            'dest': 'state101',
            'conditions': 'is_going_to_state101'
        },

############################################################
       {
            'trigger': 'advance',
            'source': 'state90',
            'dest': 'state102',
            'conditions': 'is_going_to_state102'
        },
       {
            'trigger': 'advance',
            'source': 'state90',
            'dest': 'state103',
            'conditions': 'is_going_to_state103'
        },
       {
            'trigger': 'advance',
            'source': 'state90',
            'dest': 'state104',
            'conditions': 'is_going_to_state104'
        },

############################################################
       {
            'trigger': 'advance',
            'source': 'state92',
            'dest': 'state105',
            'conditions': 'is_going_to_state105'
        },
       {
            'trigger': 'advance',
            'source': 'state92',
            'dest': 'state106',
            'conditions': 'is_going_to_state106'
        },
       {
            'trigger': 'advance',
            'source': 'state92',
            'dest': 'state107',
            'conditions': 'is_going_to_state107'
        },

############################################################
        {
            'trigger': 'advance',
            'source': 'state23',
            'dest': 'state108',
            'conditions': 'is_going_to_state108'
        },
                {
            'trigger': 'advance',
            'source': 'state23',
            'dest': 'state109',
            'conditions': 'is_going_to_state109'
        },
#################################################################
        {
            'trigger': 'advance',
            'source': 'state24',
            'dest': 'state110',
            'conditions': 'is_going_to_state110'
        },
                {
            'trigger': 'advance',
            'source': 'state24',
            'dest': 'state111',
            'conditions': 'is_going_to_state111'
        },
#################################################################
       {
            'trigger': 'advance',
            'source': 'state109',
            'dest': 'state112',
            'conditions': 'is_going_to_state112'
        },
       {
            'trigger': 'advance',
            'source': 'state109',
            'dest': 'state113',
            'conditions': 'is_going_to_state113'
        },
       {
            'trigger': 'advance',
            'source': 'state109',
            'dest': 'state114',
            'conditions': 'is_going_to_state114'
        },

############################################################
       {
            'trigger': 'advance',
            'source': 'state111',
            'dest': 'state115',
            'conditions': 'is_going_to_state115'
        },
       {
            'trigger': 'advance',
            'source': 'state111',
            'dest': 'state116',
            'conditions': 'is_going_to_state116'
        },
       {
            'trigger': 'advance',
            'source': 'state111',
            'dest': 'state117',
            'conditions': 'is_going_to_state117'
        },

############################################################

        {
            'trigger': 'go_back',
            'source': [
                'state25','state27','state29','state31','state33','state35',
		'state37','state39','state40','state41','state42','state43',
		'state44','state45','state46','state47','state48','state49',
                'state50','state51','state52','state53','state54','state55',
                'state56','state57','state58','state60','state62','state64',
		'state66','state68','state69','state70','state71','state72',
      	       	'state73','state74','state75','state76','state77','state78',
       	       	'state79','state80','state81','state82','state83','state85',
		'state87','state89','state91','state93','state94','state95',
		'state96','state97','state98','state99','state100','state101',
                'state102','state103','state104','state105','state106','state107',
       	       	'state108','state110','state112','state113','state114','state115',
       	       	'state116','state117'
            ],
            'dest': 'user'
        }
    ],
    initial='user',
    auto_transitions=False,
    show_conditions=True,
)


def _set_webhook():
    status = bot.set_webhook(WEBHOOK_URL)
    if not status:
        print('Webhook setup failed')
        sys.exit(1)
    else:
        print('Your webhook URL has been set to "{}"'.format(WEBHOOK_URL))


@app.route('/hook', methods=['POST'])
def webhook_handler():
    update = telegram.Update.de_json(request.get_json(force=True), bot)
    machine.advance(update)
    return 'ok'


@app.route('/show-fsm', methods=['GET'])
def show_fsm():
    byte_io = BytesIO()
    machine.graph.draw(byte_io, prog='dot', format='png')
    byte_io.seek(0)
    return send_file(byte_io, attachment_filename='fsm.png', mimetype='image/png')


if __name__ == "__main__":
    _set_webhook()
    app.run()
