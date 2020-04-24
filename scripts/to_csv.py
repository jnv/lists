#!/usr/bin/env python3
### Quick script to parse list-of-lists to .csv
###
### By Max Woolf (@minimaxir)

import json
import csv
import urllib.request as urllib2
import os, sys

# Get personal access token from GitHub settings
access_token = os.environ['GH_TOKEN']

fields = ["name", "url", "author", "description", "homepage", "num_watch", "num_stars", "num_forks", "num_open_issues", "last_updated", "last_push"]

list_csv_writer = csv.writer(sys.stdout)
list_csv_writer.writerow(fields)

for line in sys.stdin:

	if line.startswith('*'):
		repo_url = line[line.find("(")+1:line.find(")")]

		if not repo_url.startswith('https'):
			continue

		try:
			query_url = "https://api.github.com/repos/%s?access_token=%s" % (repo_url[19:], access_token)
			headers = {'Authorization': 'token ' + access_token}
			req = urllib2.Request(query_url, headers=headers)
			response = urllib2.urlopen(req)
			data = json.loads(response.read().decode())

			name = data['name']
			url = repo_url
			author = data['owner']['login']
			description = data['description']
			homepage = data['homepage']
			num_watch = data['subscribers_count']
			num_stars = data['stargazers_count']
			num_forks = data['forks_count']
			num_open_issues = data['open_issues_count']
			last_updated = data['updated_at']
			last_push = data['pushed_at']

			list_csv_writer.writerow([name, url, author, description, homepage, num_watch, num_stars, num_forks, num_open_issues, last_updated, last_push])

		except Exception as e:
			# will catch 404s from bad entries
			print(repo_url, e, file=sys.stderr)
