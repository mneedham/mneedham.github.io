+++
draft = false
date="2017-03-28 05:39:04"
title="Luigi: Defining dynamic requirements (on output files)"
tag=['python', 'luigi']
category=['Python']
description="In this post we show how to create requirements between Luigi tasks where those requirements aren't known at design time i.e. we have dynamic requirements."
+++

<p>In <a href="http://www.markhneedham.com/blog/2017/03/25/luigi-externalprogramtask-example-converting-json-csv/">my last blog post</a> I showed how to convert a JSON document containing meetup groups into a CSV file using Luigi, the Python library for building data pipelines. As well as creating that CSV file I wanted to go back to the <a href="https://www.meetup.com/meetup_api/">meetup.com API</a> and download all the members of those groups.</p>



<p>This was a rough flow of what i wanted to do:</p>



<ul>
<li>
Take JSON document containing all groups
</li>
<li>
Parse that document and for each group:
</li>
<ul>
<li>
Call the /members endpoint
</li>
<li>
Save each one of those files as a JSON file
</li>
</ul>
<li>
Iterate over all those JSON files and create a members CSV file
</li>
</ul>


<p>In the previous post we created the <cite>GroupsToJSON</cite> task which calls the /groups endpoint on the meetup API and creates the file /tmp/groups.json.</p>



<p>Our new task has that as its initial requirement:</p>



~~~python

class MembersToCSV(luigi.Task):
    key = luigi.Parameter()
    lat = luigi.Parameter()
    lon = luigi.Parameter()

    def requires(self):
        yield GroupsToJSON(self.key, self.lat, self.lon)
~~~

<p>But we also want to create a requirement on a task that will make those calls to the /members endpoint and store the result in a JSON file.</p>



<p>One of the patterns that Luigi imposes on us is that each task should only create one file so actually we have a requirement on a collection of tasks rather than just one. It took me a little while to get my head around that!</p>



<p>We don't know the parameters of those tasks at compile time - we can only calculate them by parsing the JSON file produced by <cite>GroupsToJSON</cite>.</p>



<p>In Luigi terminology what we want to create is a <a href="http://luigi.readthedocs.io/en/stable/tasks.html#dynamic-dependencies">dynamic requirement</a>. A dynamic requirement is defined inside the run method of a task and can rely on the output of any tasks specified in the requires method, which is exactly what we need.</p>



<p>This code does the delegating part of the job:</p>



~~~python

class MembersToCSV(luigi.Task):
    key = luigi.Parameter()
    lat = luigi.Parameter()
    lon = luigi.Parameter()


    def run(self):
        outputs = []
        for input in self.input():
            with input.open('r') as group_file:
                groups_json = json.load(group_file)
                groups = [str(group['id']) for group in groups_json]


                for group_id in groups:
                    members = MembersToJSON(group_id, self.key)
                    outputs.append(members.output().path)
                    yield members


    def requires(self):
        yield GroupsToJSON(self.key, self.lat, self.lon)
~~~

<p>Inside our run method we iterate over the output of GroupsToJSON (which is our input) and we yield to another task as well as collecting its outputs in the array outputs that we'll use later.
<cite>MembersToJSON</cite> looks like this:</p>



~~~python

class MembersToJSON(luigi.Task):
    group_id = luigi.IntParameter()
    key = luigi.Parameter()


    def run(self):
        results = []
        uri = "https://api.meetup.com/2/members?&group_id={0}&key={1}".format(self.group_id, self.key)
        while True:
            if uri is None:
                break
            r = requests.get(uri)
            response = r.json()
            for result in response["results"]:
                results.append(result)
            uri = response["meta"]["next"] if response["meta"]["next"] else None


        with self.output().open("w") as output:
            json.dump(results, output)

    def output(self):
        return luigi.LocalTarget("/tmp/members/{0}.json".format(self.group_id))
~~~

<p>This task generates one file per group containing a list of all the members of that group.</p>



<p>We can now go back to <cite>MembersToCSV</cite> and convert those JSON files into a single CSV file:</p>



~~~python

class MembersToCSV(luigi.Task):
    out_path = "/tmp/members.csv"
    key = luigi.Parameter()
    lat = luigi.Parameter()
    lon = luigi.Parameter()


    def run(self):
        outputs = []
        for input in self.input():
            with input.open('r') as group_file:
                groups_json = json.load(group_file)
                groups = [str(group['id']) for group in groups_json]


                for group_id in groups:
                    members = MembersToJSON(group_id, self.key)
                    outputs.append(members.output().path)
                    yield members

        with self.output().open("w") as output:
            writer = csv.writer(output, delimiter=",")
            writer.writerow(["id", "name", "joined", "topics", "groupId"])

            for path in outputs:
                group_id = path.split("/")[-1].replace(".json", "")
                with open(path) as json_data:
                    d = json.load(json_data)
                    for member in d:
                        topic_ids = ";".join([str(topic["id"]) for topic in member["topics"]])
                        if "name" in member:
                            writer.writerow([member["id"], member["name"], member["joined"], topic_ids, group_id])

    def output(self):
        return luigi.LocalTarget(self.out_path)

    def requires(self):
        yield GroupsToJSON(self.key, self.lat, self.lon)
~~~


<p>
We then just need to add our new task as a requirement of the wrapper task:
</p>



<p>
And we're ready to roll:
</p>



~~~bash

$ PYTHONPATH="." luigi --module blog --local-scheduler Meetup --workers 3
~~~

<p>
We've defined the number of workers here as we can execute those calls to the /members endpoint in parallel and there are ~ 600 calls to make.
</p>
 

<p>
All the <a href="https://gist.github.com/mneedham/de3c67dd198e53303923cf40739fb74c">code from both blog posts is available as a gist</a> if you want to play around with it. 
</p>


<p>
Any questions/advice let me know in the comments or I'm <a href="https://twitter.com/markhneedham">@markhneedham</a> on twitter.
</p>

