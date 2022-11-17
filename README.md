# mastodon_scripts
mastodon_list_export.py is a simple script to export accounts from a Mastodon private list to a .CSV file. This allows easy downloading of the accounts for sharing with other users who may want to import the members of that list.

To use it, create a basic Mastodon app in Development: New Application in the web app. Take the token created there and put that and other required details in config.py

You need to know the ID of the list you need. The documentation is here: https://docs.joinmastodon.org/methods/timelines/lists/
In terminal, that command is: https://mastodon.example/api/v1/lists

You need to use the token to access these API calls. In terminal that looks like:

curl \\
-H 'Authorization: Bearer token_goes_here’ \\
https://mastodon.example/api/v1/lists
