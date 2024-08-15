import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
import uuid

#REPORT_TO_COPY = 76022
#QUERY_TEMPLATE = "project.id IN ({0}) AND tracker.name IN ('User Stories', 'Tasks') AND workItemStatus IN ('InProgress')"
REPORT_TO_COPY = 76171
# QUERY_TEMPLATE = "SELECT status AS 'Status', COUNT(1) AS COUNT WHERE project.id IN ({0}) AND tracker.name IN ('User Stories', 'Tasks') AND workItemStatus IN ('In Progress') GROUP BY 'Status'"
QUERY_TEMPLATE = "SELECT priority AS 'Priority', status AS 'Status', COUNT(1) AS COUNT WHERE project.id IN ({0}) AND tracker.name IN ('User Stories', 'Tasks') AND 'Status' IN ('In Progress') GROUP BY 'Priority','Status' ORDER BY priority DESC"
# QUERY_TEMPLATE = "SELECT status AS 'Status', COUNT(1) AS COUNT WHERE project.id IN ({0}) AND tracker.name IN ('User Stories', 'Tasks') AND workItemStatus IN ('In Progress') GROUP BY 'Status'"
# QUERY_TEMPLATE = "SELECT status AS 'Status', COUNT(1) AS COUNT WHERE project.id IN ({0}) AND tracker.name IN ('User Stories', 'Tasks') AND workItemStatus IN ('In Progress') GROUP BY 'Status'"

NAME_TEMPLATE = "{0} generated report for - {1} [{2}]"

# See configuration.py for a list of all supported configuration parameters.
configuration = swagger_client.Configuration()
configuration.host = "http://localhost:8888/api"
configuration.username = "mhudman"
configuration.password = "password"

client = swagger_client.ApiClient(configuration)
projectAPI = swagger_client.ProjectApi(client)
reportAPI = swagger_client.ReportApi(client)

def log(msg):
    if False:
        pprint(msg)

try:
    # this copies the report to all projects, replace with specific list if needed
    projectList = projectAPI.get_projects()

    # unique id for testing with repeated runs and/or filtering
    uid = str(uuid.uuid4())[28:36]
    pprint("This run's unique id is: {0}".format(uid))
    
    # we must specifiy columns to display in this report
    columns = []
    reportColumns = reportAPI.get_report_by_id(REPORT_TO_COPY).columns
    log(reportColumns)
    for entry in reportColumns:
        columns.append({
            "columnIndex": entry.column_index,
            "field": {
                "id": entry.field.id,
                "trackerId": None
            }
        })

    if True:
        for project in projectList:
            query = QUERY_TEMPLATE.format(project.id)
            description = NAME_TEMPLATE.format(uid, project.name, project.id)
            name = description
            reportBody = {
                "name": name,
                "description": description,
                "cbQl": query,
                "columns": columns
            }
            log(reportBody)
            reportAPI.create_report(reportBody)

except ApiException as e:
    print("Exception when calling TrackerItemApi->get_tracker_item: %s\n" % e)
