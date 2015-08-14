### Quick script to parse list-of-lists to .csv
###
### By Max Woolf (@minimaxir)

import json
import csv
import urllib2

# Get personal access token from GitHub settings
access_token = <FILL IN>

fields = ["name", "url", "author", "num_watch", "num_stars", "num_forks", "num_open_issues", "last_updated"]

with open('../README.md', 'r') as readme:
	with open('../list.csv', 'wb') as list_csv:
	
		list_csv_writer = csv.writer(list_csv)
		list_csv_writer.writerow(fields)
		
		for line in readme:
			try:
				if line.startswith('*'):
					repo_url = line[line.find("(")+1:line.find(")")]
					query_url = "https://api.github.com/repos/%s?access_token=%s" % (repo_url[19:], access_token)
					
					req = urllib2.Request(query_url)
					response = urllib2.urlopen(req)
					data = json.loads(response.read())
					
					name = data['name']
					url = repo_url
					author = data['owner']['login']
					num_watch = data['watchers_count']
					num_stars = data['stargazers_count']
					num_forks = data['forks_count']
					num_open_issues = data['open_issues_count']
					last_updated = data['created_at']
					
					list_csv_writer.writerow([name, url, author, num_watch, num_stars, num_forks, num_open_issues, last_updated])
					
			except Exception, e:
			
				# will catch 404s from bad entries
				print e
