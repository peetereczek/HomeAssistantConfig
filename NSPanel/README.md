Many thanks to [DeanoXX](https://github.com/DeanoXX), [jesserockz](https://github.com/jesserockz) and [Blakadder](https://github.com/Blakadder) (and many others) for investigating NSPanel from Sonoff and how to integrate it to HomeAssistant.

Important links:
- [NSPanel UI protocol](https://blakadder.github.io/nspanel/)
- [Main ticket on ESPHome project](https://github.com/esphome/feature-requests/issues/1469)
- [Pull request supporting NSPanel by ESPHome](https://github.com/esphome/esphome/pull/2702)
- [Main HA community thread](https://community.home-assistant.io/t/sonoff-nspanel-smart-scene-wall-switch-by-itead-coming-soon-on-kickstarter/332962/356)

What you can find in my configuration:
- Original UI
- Time updates
- Weather updates
- RTTTL song (sound notification on actions)
- BLE tracker (very heavy and makes NSPanel unstable)
- Light control
- RGB light control
- Scenes activations (with cheated a bit, alarm control)
- Thermostat (is not used, as I don't have any)

You can find more (such as switch control) by looking on DeanoXX configuration of NSPanel [YouTube demo](https://www.youtube.com/watch?v=7T5r5sy_rpc)

Known BUG:
- Light temperature is not working (yet)
