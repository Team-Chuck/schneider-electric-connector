from ewsrestgatewayclient.ebo import EBO


test = EBO()
token = test.token.get_token("Admin", "P@ssword")
hmm = test.root.retrieve(custom_headers={'Authorization':'Bearer ' + token.access_token})
test2 = 2

