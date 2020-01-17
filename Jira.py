from jira import JIRA

user = ''
apikey = ''
server = ''

options = {
 'server': server
}

jira = JIRA(options, basic_auth=(user,apikey) )
ticket = 'HAR-3286'
issue = jira.issue(ticket)

summary = issue.fields.summary
print('ticket: ', ticket, summary)
