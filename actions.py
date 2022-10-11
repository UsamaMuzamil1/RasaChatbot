# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions
from argparse import Action


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List
# import rasa_sdk

from rasa_sdk import Action, Tracker
from rasa_sdk.events import Restarted
from rasa_sdk.executor import CollectingDispatcher


class ActionHelloWorld(Action):

     def name(self) -> Text:
         return "action_hello_world"

     def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

         dispatcher.utter_message(text="Hello World!")

         return []

class ActionRestart(Action):
    def name(self) -> Text:
        return "action_restart"

    async def run(
        self, dispatcher, tracker: Tracker, domain: Dict[Text, Any]
        ) -> List[Dict[Text, Any]]:

 # custom behavior
     return [Restarted()]


#class ActionBack(Action):
# def name(self) -> Text:
 #       return "action_back"


# async def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#      from rasa_core_sdk.events import UserUtteranceReverted

 #     dispatcher.utter_template("utter_insurance", tracker, silent_fail=True)

  #    return [UserUtteranceReverted()]



class ActionBack(Action):
 def name(self) -> Text:
        return "action_back"


 async def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
      from rasa_core_sdk.events import ActionReverted

      dispatcher.utter_template("utter_re",tracker, silent_fail=True)

      return [ActionReverted(), ActionReverted()]
