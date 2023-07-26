projects.info()

# projects['start_date']      = pd.to_datetime(projects['start_date'])
# projects['end_date']        = pd.to_datetime(projects['end_date'])

starting_project              = pd.DataFrame(projects[~projects.start_date.isin(projects['end_date'])]['start_date'].copy())
ending_project                = pd.DataFrame(projects[~projects.end_date.isin(projects['start_date'])]['end_date'].copy()) 

starting_project.reset_index(inplace = True)
starting_project.drop(['index'], axis = 1, inplace = True)
ending_project.reset_index(inplace = True)
ending_project.drop(['index'], axis = 1, inplace = True)

projects_duration             = starting_project.join(ending_project)
projects_duration['duration'] = projects_duration['end_date'] - projects_duration['start_date']
projects_duration[['start_date','end_date','duration']].sort_values(by = ['duration','start_date'])
