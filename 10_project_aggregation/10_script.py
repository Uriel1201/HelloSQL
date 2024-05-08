
"""
#10 Project Aggregation
The projects table contains three columns: task_id, start_date, and end_date. The difference between end_date and start_date is 1 day for each row in the table. If task end dates are consecutive they are part of the same project. Projects do not overlap. Write a query to return the start and end dates of each project, and the number of days it took to complete. Order by ascending project duration, and ascending start date in the case of a tie.
"""

projects


projects['start_date'] = pd.to_datetime(projects['start_date'])
projects['end_date'] = pd.to_datetime(projects['end_date'])


openings = pd.DataFrame(projects[~projects.start_date.isin(projects['end_date'])]['start_date'])
openings.reset_index(inplace = True, drop = True)

endings = pd.DataFrame(projects[~projects.end_date.isin(projects['start_date'])]['end_date'])
endings.reset_index(inplace = True, drop = True)

project_durations = pd.concat([openings, endings], axis = 1, join = 'inner')
project_durations['project_duration'] = project_durations['end_date'] - project_durations['start_date']
project_durations.sort_values(by = 'project_duration', ascending = False)
