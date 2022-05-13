#!/bin/bash
jarvis () {
  resp=`$JARVIS_LOCATION/access-json.py $1`
  echo $resp
  if [[ "$JARVIS_VOICE_RESPONSE" = true ]] && [[ $OSTYPE == *"darwin"* ]]; then
    say $resp
  fi
}