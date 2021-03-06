# my-jarvis
Your own jarvis

## Prerequisites
- OPENAI API Key, Generate one [here](https://beta.openai.com/account/api-keys)
- Install python from [here](https://www.python.org/downloads/)
- Install pip from [here](https://pip.pypa.io/en/stable/installation/)

## Manual Installation
  - Clone the repo
  - In terminal, run 
    ```
    pip install openai
    ```
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
    - [Mac users] Want jarvis to read out response? Toggle `MAKE JARVIS SPEAK [Works only on MacOS currently]`
  - In terminal, run 
    ```
    fig source
    ```

## Usage
![JARVIS](https://raw.githubusercontent.com/darkclown97/my-jarvis/main/images/jarvis.png)
