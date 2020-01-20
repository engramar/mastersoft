#########################################################################################################
#   Program Name : jiradataingestion.py                                                                 #
#   Program Description:                                                                                #
#   This program prepares a SQLite table containing Mastersoft Jira issues.                             #
#                                                                                                       #
#   Comment                                         Date                  Author                        #
#   ================================                ==========            ================              #
#   Initial Version                                 20/01/2020            Engramar Bollas               #
#########################################################################################################
import sqlite3
import sys
import datetime
from datetime import datetime
from jira import JIRA
import arrow

user = ' '
apikey = ' '
server = ' '
options = {
 'server': server
}
jira = JIRA(options, basic_auth=(user,apikey) )

#######################################################################
### Create ISSUES Table                                             ### 
#######################################################################
conn = sqlite3.connect('ISSUES.sqlite')
cur = conn.cursor()

cur.executescript('''	
DROP TABLE IF EXISTS ISSUES;

CREATE TABLE issues (
	ISSUE_ID          varchar(20) PRIMARY KEY,
    PARENT_ID         varchar(20),
    ETA               varchar(20), 
    BUS_IMPACT        varchar(20),
    DEV_EFFORT        varchar(20),
	SUMMARY           varchar(100),
	CONFLUENCE        varchar(100),  
	STATUS            varchar(20),
    ASSIGNEE          varchar(20),
    CREATED           varchar(20),
	TIME_TO_ETA       varchar(20)
);
''')

fname = 'cr.txt'
fhand = open(fname)

#######################################################################
### Populate issues table                                           ### 
#######################################################################
total = 0
for line in fhand:
    fields = line.split('|')
    ISSUE_ID    = fields[0].strip()
    ETA         = fields[1].strip()
    BUS_IMPACT  = fields[2].strip()
    DEV_EFFORT  = fields[3].strip()
    STATUS      = fields[4].strip()
    ASSIGNEE    = fields[5].strip()
    CONFLUENCE  = fields[6].strip() 
    issue = jira.issue(ISSUE_ID)
    SUMMARY = str(issue.fields.summary)
    CREATED = str(issue.fields.created[:10])
    CREATED_DATE = (datetime.fromisoformat(CREATED))
    TODAY = arrow.now().format('YYYY-MM-DD')
    TODAYS_DATE = (datetime.fromisoformat(TODAY))
    ETA_DATE = (datetime.fromisoformat(ETA)) 
    ELAPSED = str(ETA_DATE - TODAYS_DATE).split(',')
    TIME_TO_ETA = ELAPSED[0]
    PARENT_ID = ISSUE_ID

    try: 
        cur.execute('''INSERT INTO ISSUES
            (
            ISSUE_ID,
            PARENT_ID,
            ETA,
            BUS_IMPACT,
            DEV_EFFORT,
            SUMMARY,
            CONFLUENCE,  
            STATUS,
            ASSIGNEE,
            CREATED,
            TIME_TO_ETA
            )  
            VALUES ( ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',   
            (
            ISSUE_ID,
            PARENT_ID,
            ETA,
            BUS_IMPACT,
            DEV_EFFORT,
            SUMMARY,
            CONFLUENCE,
            STATUS,
            ASSIGNEE,
            CREATED,
            TIME_TO_ETA        
            ))   
    except:
            print ('Duplicate found', ISSUE_ID)                 
    conn.commit()

    for link in issue.fields.issuelinks:        
        if hasattr(link, "outwardIssue"):
            outwardIssue = link.outwardIssue
            issue = jira.issue(outwardIssue.key)
            outwardIssueSummary   = issue.fields.summary
            outwardIssueCreated   = issue.fields.created
            outwardIssueStatus    = issue.fields.status
            outwardIssueAssignee  = issue.fields.assignee
            print("\t1 Outward: " + outwardIssue.key, outwardIssueSummary, outwardIssueCreated, outwardIssueStatus)
            #issueRec = str("1 Outward:"+"|"+str(outwardIssue.key)+"|"+str(outwardIssueSummary)+"|"+str(outwardIssueCreated)+"|"+str(outwardIssueStatus))                
            #issues.append(issueRec)
            ISSUE_ID    = str(outwardIssue.key)
            SUMMARY     = str(outwardIssueSummary)
            BUS_IMPACT  = ' '
            DEV_EFFORT  = ' '
            STATUS      = str(outwardIssueStatus)
            ASSIGNEE    = str(outwardIssueAssignee)
            CONFLUENCE  = ' '
            CREATED = str(issue.fields.created[:10])
            CREATED_DATE = (datetime.fromisoformat(CREATED))
            TODAY = arrow.now().format('YYYY-MM-DD')
            TODAYS_DATE = (datetime.fromisoformat(TODAY))
            ETA_DATE = (datetime.fromisoformat(ETA)) 
            ELAPSED = str(ETA_DATE - TODAYS_DATE).split(',')
            TIME_TO_ETA = ELAPSED[0]

            try: 
                cur.execute('''INSERT INTO ISSUES
                    (
                    ISSUE_ID,
                    PARENT_ID,
                    ETA,
                    BUS_IMPACT,
                    DEV_EFFORT,
                    SUMMARY,
                    CONFLUENCE,  
                    STATUS,
                    ASSIGNEE,
                    CREATED,
                    TIME_TO_ETA
                    )  
                    VALUES ( ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',   
                    (
                    ISSUE_ID,
                    PARENT_ID,
                    ETA,
                    BUS_IMPACT,
                    DEV_EFFORT,
                    SUMMARY,
                    CONFLUENCE,
                    STATUS,
                    ASSIGNEE,
                    CREATED,
                    TIME_TO_ETA        
                    ))                    
            except:
                    print ('Duplicate found', ISSUE_ID)                 
            conn.commit()

            for link in issue.fields.issuelinks:
                    if hasattr(link, "outwardIssue"):
                        outwardIssue = link.outwardIssue
                        issue = jira.issue(outwardIssue.key)
                        outwardIssueSummary = issue.fields.summary
                        outwardIssueCreated = issue.fields.created
                        outwardIssueStatus  = issue.fields.status
                        outwardIssueAssignee  = issue.fields.assignee
                        print("\t1-1 Outward: " + outwardIssue.key, outwardIssueSummary, outwardIssueCreated, outwardIssueStatus)
                        #issueRec = str("1-1 Outward:"+"|"+str(outwardIssue.key)+"|"+str(outwardIssueSummary)+"|"+str(outwardIssueCreated)+"|"+str(outwardIssueStatus))                
                        #issues.append(issueRec)
                        ISSUE_ID    = str(outwardIssue.key)
                        SUMMARY     = str(outwardIssueSummary)
                        BUS_IMPACT  = ' '
                        DEV_EFFORT  = ' '
                        STATUS      = str(outwardIssueStatus)
                        ASSIGNEE    = str(outwardIssueAssignee)
                        CONFLUENCE  = ' '
                        CREATED = str(issue.fields.created[:10])
                        CREATED_DATE = (datetime.fromisoformat(CREATED))
                        TODAY = arrow.now().format('YYYY-MM-DD')
                        TODAYS_DATE = (datetime.fromisoformat(TODAY))
                        ETA_DATE = (datetime.fromisoformat(ETA)) 
                        ELAPSED = str(ETA_DATE - TODAYS_DATE).split(',')
                        TIME_TO_ETA = ELAPSED[0]

                        try:
                            cur.execute('''INSERT INTO ISSUES
                                (
                                ISSUE_ID,
                                PARENT_ID,
                                ETA,
                                BUS_IMPACT,
                                DEV_EFFORT,
                                SUMMARY,
                                CONFLUENCE,  
                                STATUS,
                                ASSIGNEE,
                                CREATED,
                                TIME_TO_ETA
                                )  
                                VALUES ( ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',   
                                (
                                ISSUE_ID,
                                PARENT_ID,
                                ETA,
                                BUS_IMPACT,
                                DEV_EFFORT,
                                SUMMARY,
                                CONFLUENCE,
                                STATUS,
                                ASSIGNEE,
                                CREATED,
                                TIME_TO_ETA        
                                ))   
                        except:
                            print ('Duplicate found', ISSUE_ID)                
                        conn.commit()

                    if hasattr(link, "inwardIssue"):
                        inwardIssue = link.inwardIssue
                        issue = jira.issue(inwardIssue.key)
                        inwardIssueSummary = issue.fields.summary
                        inwardIssueCreated = issue.fields.created
                        inwardIssueStatus  = issue.fields.status
                        inwardIssueAssignee  = issue.fields.assignee
                        print("\t1-1 Inward: " + inwardIssue.key, inwardIssueSummary, inwardIssueCreated, inwardIssueStatus)
                        #issueRec = str("1-1 Inward:"+"|"+str(inwardIssue.key)+"|"+str(inwardIssueSummary)+"|"+str(inwardIssueCreated)+"|"+str(inwardIssueStatus))                
                        #issues.append(issueRec)
                        ISSUE_ID    = str(inwardIssue.key)
                        SUMMARY     = str(inwardIssueSummary)
                        BUS_IMPACT  = ' '
                        DEV_EFFORT  = ' '
                        STATUS      = str(inwardIssueStatus)
                        ASSIGNEE    = str(inwardIssueAssignee)
                        CONFLUENCE  = ' '
                        CREATED = str(issue.fields.created[:10])
                        CREATED_DATE = (datetime.fromisoformat(CREATED))
                        TODAY = arrow.now().format('YYYY-MM-DD')
                        TODAYS_DATE = (datetime.fromisoformat(TODAY))
                        ETA_DATE = (datetime.fromisoformat(ETA)) 
                        ELAPSED = str(ETA_DATE - TODAYS_DATE).split(',')
                        TIME_TO_ETA = ELAPSED[0]

                        try: 
                            cur.execute('''INSERT INTO ISSUES
                                (
                                ISSUE_ID,
                                PARENT_ID,
                                ETA,
                                BUS_IMPACT,
                                DEV_EFFORT,
                                SUMMARY,
                                CONFLUENCE,  
                                STATUS,
                                ASSIGNEE,
                                CREATED,
                                TIME_TO_ETA
                                )  
                                VALUES ( ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',   
                                (
                                ISSUE_ID,
                                PARENT_ID,
                                ETA,
                                BUS_IMPACT,
                                DEV_EFFORT,
                                SUMMARY,
                                CONFLUENCE,
                                STATUS,
                                ASSIGNEE,
                                CREATED,
                                TIME_TO_ETA        
                                ))                    
                        except:
                            print ('Duplicate found', ISSUE_ID)                 
                        conn.commit()

        if hasattr(link, "inwardIssue"):
            inwardIssue = link.inwardIssue
            issue = jira.issue(inwardIssue.key)
            inwardIssueSummary = issue.fields.summary
            inwardIssueCreated = issue.fields.created
            inwardIssueStatus  = issue.fields.status
            inwardIssueAssignee  = issue.fields.assignee
            print("\t1 Inward: " + inwardIssue.key, inwardIssueSummary, inwardIssueCreated, inwardIssueStatus)
            #issueRec = ("1 Inward:"+"|"+str(inwardIssue.key)+"|"+str(inwardIssueSummary)+"|"+str(inwardIssueCreated)+"|"+str(inwardIssueStatus))                
            #issues.append(issueRec)
            ISSUE_ID    = str(inwardIssue.key)
            SUMMARY     = str(inwardIssueSummary)
            BUS_IMPACT  = ' '
            DEV_EFFORT  = ' '
            STATUS      = str(inwardIssueStatus)
            ASSIGNEE    = str(inwardIssueAssignee)
            CONFLUENCE  = ' '
            CREATED = str(issue.fields.created[:10])
            CREATED_DATE = (datetime.fromisoformat(CREATED))
            TODAY = arrow.now().format('YYYY-MM-DD')
            TODAYS_DATE = (datetime.fromisoformat(TODAY))
            ETA_DATE = (datetime.fromisoformat(ETA)) 
            ELAPSED = str(ETA_DATE - TODAYS_DATE).split(',')
            TIME_TO_ETA = ELAPSED[0]

            try:
                cur.execute('''INSERT INTO ISSUES
                    (
                    ISSUE_ID,
                    PARENT_ID,
                    ETA,
                    BUS_IMPACT,
                    DEV_EFFORT,
                    SUMMARY,
                    CONFLUENCE,  
                    STATUS,
                    ASSIGNEE,
                    CREATED,
                    TIME_TO_ETA
                    )  
                    VALUES ( ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',   
                    (
                    ISSUE_ID,
                    PARENT_ID,
                    ETA,
                    BUS_IMPACT,
                    DEV_EFFORT,
                    SUMMARY,
                    CONFLUENCE,
                    STATUS,
                    ASSIGNEE,
                    CREATED,
                    TIME_TO_ETA        
                    ))   
            except:
                print ('Duplicate found', ISSUE_ID)                                  
            conn.commit()

            for link in issue.fields.issuelinks:
                    if hasattr(link, "outwardIssue"):
                        outwardIssue = link.outwardIssue
                        issue = jira.issue(outwardIssue.key)
                        outwardIssueSummary = issue.fields.summary
                        outwardIssueCreated = issue.fields.created
                        outwardIssueStatus  = issue.fields.status
                        outwardIssueAssignee  = issue.fields.assignee
                        print("\t1-1 Outward: " + outwardIssue.key, outwardIssueSummary, outwardIssueCreated, outwardIssueStatus)
                        #issueRec = ("1-1 Outward:"+"|"+str(outwardIssue.key)+"|"+str(outwardIssueSummary)+"|"+str(outwardIssueCreated)+"|"+str(outwardIssueStatus))                
                        #issues.append(issueRec)
                        ISSUE_ID    = str(outwardIssue.key)
                        SUMMARY     = str(outwardIssueSummary)
                        BUS_IMPACT  = ' '
                        DEV_EFFORT  = ' '
                        STATUS      = str(outwardIssueStatus)
                        ASSIGNEE    = str(outwardIssueAssignee)
                        CONFLUENCE  = ' '
                        CREATED = str(issue.fields.created[:10])
                        CREATED_DATE = (datetime.fromisoformat(CREATED))
                        TODAY = arrow.now().format('YYYY-MM-DD')
                        TODAYS_DATE = (datetime.fromisoformat(TODAY))
                        ETA_DATE = (datetime.fromisoformat(ETA)) 
                        ELAPSED = str(ETA_DATE - TODAYS_DATE).split(',')
                        TIME_TO_ETA = ELAPSED[0]

                        try:
                            cur.execute('''INSERT INTO ISSUES
                                (
                                ISSUE_ID,
                                PARENT_ID,
                                ETA,
                                BUS_IMPACT,
                                DEV_EFFORT,
                                SUMMARY,
                                CONFLUENCE,  
                                STATUS,
                                ASSIGNEE,
                                CREATED,
                                TIME_TO_ETA
                                )  
                                VALUES ( ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',   
                                (
                                ISSUE_ID,
                                PARENT_ID,
                                ETA,
                                BUS_IMPACT,
                                DEV_EFFORT,
                                SUMMARY,
                                CONFLUENCE,
                                STATUS,
                                ASSIGNEE,
                                CREATED,
                                TIME_TO_ETA        
                                ))
                        except:
                            print ('Duplicate found', ISSUE_ID)                 
                        conn.commit()

                    if hasattr(link, "inwardIssue"):
                        inwardIssue = link.inwardIssue
                        issue = jira.issue(inwardIssue.key)
                        inwardIssueSummary = issue.fields.summary
                        inwardIssueCreated = issue.fields.created
                        inwardIssueStatus  = issue.fields.status
                        inwardIssueAssignee  = issue.fields.assignee
                        print("\t1-1 Inward: " + inwardIssue.key, inwardIssueSummary, inwardIssueCreated, inwardIssueStatus)         
                        #issueRec = str("1-1 Inward:"+"|"+str(inwardIssue.key)+"|"+str(inwardIssueSummary)+"|"+str(inwardIssueCreated)+"|"+str(inwardIssueStatus))                
                        #issues.append(issueRec)

                        ISSUE_ID    = str(inwardIssue.key)
                        SUMMARY     = str(inwardIssueSummary)
                        BUS_IMPACT  = ' '
                        DEV_EFFORT  = ' '
                        STATUS      = str(inwardIssueStatus)
                        ASSIGNEE    = str(inwardIssueAssignee)
                        CONFLUENCE  = ' '
                        CREATED = str(issue.fields.created[:10])
                        CREATED_DATE = (datetime.fromisoformat(CREATED))
                        TODAY = arrow.now().format('YYYY-MM-DD')
                        TODAYS_DATE = (datetime.fromisoformat(TODAY))
                        ETA_DATE = (datetime.fromisoformat(ETA)) 
                        ELAPSED = str(ETA_DATE - TODAYS_DATE).split(',')
                        TIME_TO_ETA = ELAPSED[0]

                        try:
                            cur.execute('''INSERT INTO ISSUES
                                (
                                ISSUE_ID,
                                PARENT_ID,
                                ETA,
                                BUS_IMPACT,
                                DEV_EFFORT,
                                SUMMARY,
                                CONFLUENCE,  
                                STATUS,
                                ASSIGNEE,
                                CREATED,
                                TIME_TO_ETA
                                )  
                                VALUES ( ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',   
                                (
                                ISSUE_ID,
                                PARENT_ID,
                                ETA,
                                BUS_IMPACT,
                                DEV_EFFORT,
                                SUMMARY,
                                CONFLUENCE,
                                STATUS,
                                ASSIGNEE,
                                CREATED,
                                TIME_TO_ETA        
                                ))   
                        except:
                            print ('Duplicate found', ISSUE_ID)                                 
                        conn.commit()
    total += 1

print ('Total CRs : ', total)
fhand.close()

print ('Done')
