# Auto-GPT-Bard-Plugin
The AutoGPT Bard Plugin is a software tool that enables chat with bard.

[![GitHub Repo stars](https://img.shields.io/github/stars/RuiHirano/Auto-GPT-Bard-Plugin?style=social)](https://github.com/RuiHirano/Auto-GPT-Bard-Plugin/stargazers)

### Plugin Installation Steps

1. **Clone or download the plugin repository:**
   Clone the plugin repository, or download the repository as a zip file.

2. **Install the plugin's dependencies (if any):**
   Navigate to the plugin's folder in your terminal, and run the following command to install any required dependencies:

   ``` shell
      pip install -r requirements.txt
   ```

3. **Package the plugin as a Zip file:**
   If you cloned the repository, compress the plugin folder as a Zip file.

4. **Copy the plugin's Zip file:**
   Place the plugin's Zip file in the `plugins` folder of the Auto-GPT repository.

5. **Allowlist the plugin (optional):**
   Add the plugin's class name to the `ALLOWLISTED_PLUGINS` in the `.env` file to avoid being prompted with a warning when loading the plugin:

   ``` shell
   ALLOWLISTED_PLUGINS=AutoGPTBardPlugin,example-plugin2,example-plugin3
   ```

   If the plugin is not allowlisted, you will be warned before it's loaded.

6. **Add environment variables in .env:**
Append the following configuration settings to the end of the file:

```ini
################################################################################
### Bard
################################################################################
BARD_SESSION_TOKEN=
BARD_COMMAND_LABEL=chat_with_bard
BARD_COMMAND_NAME=Chat with bard
```
- Get bard session token. Reference is [here](https://github.com/acheong08/Bard)

