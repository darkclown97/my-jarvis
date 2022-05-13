# my-jarvis
Your own jarvis

## Prerequisites
- OPENAI API Key, Generate one <a href="http://example.com/" target="_blank">here</a>
- OPENAI API Key, Generate one [here](https://beta.openai.com/account/api-keys)
- Install python from [here](https://www.python.org/downloads/)

## Manual Installation
  - Clone the repo
  - Paste the following in `~/.zshrc` or `~/.bashrc`
    ```
    export OPENAI_API_KEY="<YOUR_OPENAI_API_KEY>"
    export JARVIS_LOCATION="<REPO_LOCATION>"
    source $JARVIS_LOCATION/jarvis.sh
    ```
    > Don't forget to replace appropriate values for `<YOUR_OPENAI_API_KEY>` and `<REPO_LOCATION>`
  - Want jarvis to read out the response? (For Mac users only), paste the following `~/.zshrc` or `~/.bashrc`
    ```
    export JARVIS_VOICE_RESPONSE=true
    ```
  - Restart Terminal

## Fig Plugin Installation  
  - Install Fig from [here](https://fig.io)
  - Open Fig & navigate to the plugin store
  - Search & Install `My Jarvis`
  - In the Configuration tab, provide the values for `OPENAI_API_KEY`
  - In terminal, run 
    ```
    fig source
    ```

## Usage
