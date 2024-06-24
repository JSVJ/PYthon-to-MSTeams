# Python to MSTeams

## Table of Contents

- [About](#about)
- [Getting Started](#getting_started)

## About <a name = "about"></a>

This repository shows how we can send an notification from Python to MSTeams Channel.

## Getting Started <a name = "getting_started"></a>

### Creating and Activating a Python Environment

To create and activate a new Python environment, follow these steps:

1. Open your terminal or command prompt.

2. Navigate to the directory where you want to create the environment.

3. Run the following command to create a new Python environment:

    ```
    python -m venv myenv
    ```

    Replace `myenv` with the desired name for your environment.

4. Once the environment is created, activate it by running the appropriate command based on your operating system:

    - For Windows:

      ```
      myenv\Scripts\activate
      ```

    - For macOS and Linux:

      ```
      source myenv/bin/activate
      ```

5. After running the activation command, you should see the name of your environment in parentheses at the beginning of your command prompt or terminal.

    For example:

    ```
    (myenv) $
    ```

    This indicates that your Python environment is now active.

That's it! You have successfully created and activated a new Python environment. You can now install packages and run Python scripts within this environment.

### Getting the Webhook URL from Microsoft Teams

To send a notification from Python to a Microsoft Teams channel, you will need to obtain the webhook URL for that channel. Here's how you can get it:

1. Open Microsoft Teams and navigate to the channel where you want to send the notification.

2. Click on the three dots (...) next to the channel name and select "Connectors".

3. In the "Connectors" window, search for "Incoming Webhook" and click on it.

4. Click on the "Add" button to add the Incoming Webhook connector to the channel.

5. Provide a name for the webhook and optionally upload an image for the webhook icon. Then, click on the "Create" button.

6. Once the webhook is created, you will see a unique URL generated for it. This is the webhook URL that you will use to send notifications to the channel.

7. Copy the webhook URL and paste it into the appropriate place in your Python code.

That's it! You now have the webhook URL from Microsoft Teams that you can use to send notifications from Python to the desired channel.


### Prerequisites

1. Need a MS365 account (as of June 2024) to get webhook from the teams.