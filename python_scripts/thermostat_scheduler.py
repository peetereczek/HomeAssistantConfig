WEEK_SCHEDULE = [
    [datetime.time( 7, 0), datetime.time( 8, 30)], # from 07:00 to 09:00
    [datetime.time(17, 0), datetime.time(23, 00)] # from 18:00 to 23:59
]
WEEKEND_SCHEDULE = [
    [datetime.time(8, 0), datetime.time(13, 0)],
    [datetime.time(18, 0), datetime.time(23, 59, 59)]
]

TEMP_HIGH = 19.0
TEMP_LOW  = 17.0

climate_entity_1 = 'climate.bf87b397ec02c5a554ywfj' # set to your thermostat entity
climate_entity_2 = 'climate.bf859bbe3ceddf4c11t0qe'
current_temp_1 = hass.states.get(climate_entity_1).attributes['temperature']
current_temp_2 = hass.states.get(climate_entity_2).attributes['temperature']

now = datetime.datetime.now().time()
if datetime.datetime.now().date().weekday() < 5:
    current_schedule = WEEK_SCHEDULE
else:
    current_schedule = WEEKEND_SCHEDULE

in_high_time = False
for high_time in current_schedule:
    start = high_time[0]
    end = high_time[1]
    
    if start <= now <= end:        
        in_high_time = True
        break

new_temp = TEMP_HIGH if in_high_time else TEMP_LOW 
if new_temp != current_temp_1:
    # set the thermostat target temperature.
    hass.services.call('climate', 'set_temperature', {'entity_id': climate_entity_1, 'temperature': new_temp})
    # also send a notification so that I know that it changed the temperature.
    hass.services.call('persistent_notification', 'create', {'title' : 'HA: Changing thermostat', 
        'message': 'Zmiana temperatury na {} (było {})'.format(new_temp, current_temp_1)})
if new_temp != current_temp_2:
    hass.services.call('climate', 'set_temperature', {'entity_id': climate_entity_2, 'temperature': new_temp})