from ewsrestgatewayclient.ebo import EBO
import urllib.parse


se_client = EBO()
token = se_client.token.get_token("Admin", "P@ssword")
root_result = se_client.root.retrieve(custom_headers={'Authorization':'Bearer ' + token.access_token})
set_value_result = se_client.values.update_value(urllib.parse.quote('01/Server 1/Cisco Hackathon/Team 4/Conference Room A/Values/Temp', safe=''), '28', custom_headers={'Authorization':'Bearer ' + token.access_token})
test2 = 2
