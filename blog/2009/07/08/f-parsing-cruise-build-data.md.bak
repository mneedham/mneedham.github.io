+++
draft = false
date="2009-07-08 22:46:05"
title="F#: Parsing Cruise build data"
tag=['f']
category=['F#']
+++

I've been playing around a bit with the <a href="http://studios.thoughtworks.com/cruise-continuous-integration/1.3.0/help/Properties_API.html">properties REST API</a> that Cruise exposes to try and get together some build metrics and I decided it might be an interesting task to try and use F# for.

I'm making use of the 'search' part of the API to return the metrics of all the builds run on a certain part of the pipeline and I then want to parse those results so that I can extract just the name of the agent that ran that build and the duration of that build.

The first part of this task is to parse the data and extract just the information I'm interested in.

The data is like this:


~~~text

cruise_agent,cruise_job_duration,cruise_job_id,cruise_job_result,cruise_pipeline_label,cruise_timestamp_01_scheduled,cruise_timestamp_02_assigned,cruise_timestamp_03_preparing,cruise_timestamp_04_building,cruise_timestamp_05_completing,cruise_timestamp_06_completed\n
BuildAgentOne (Sydney, PersonOne),319,14052,Passed,2223,2009-06-25 12:14:01 +1000,2009-06-25 12:14:02 +1000,2009-06-25 12:14:02 +1000,2009-06-25 12:14:35 +1000,2009-06-25 12:19:54 +1000,2009-06-25 12:19:55 +1000\n
BuildAgentTwo (Sydney, PersonTwo),422,14084,Passed,2224,2009-06-25 14:13:57 +1000,2009-06-25 14:13:58 +1000,2009-06-25 14:13:58 +1000,2009-06-25 14:14:48 +1000,2009-06-25 14:21:49 +1000,2009-06-25 14:21:50 +1000\n
~~~

I first started off trying to do this extraction all in one regular expression but after a while realised that I'd probably have more success if I ran a regular expression over each line individually. 


~~~ocaml

type CruiseData = { Agent: string; Duration: string } 
~~~


~~~ocaml

let ExtractValues (item:string) =  
   let matchBuildDuration item = Regex.Match(item, "(.*\)),([0-9]+),") 
   Regex.Split(item, "\n") |> 
   Array.map (fun item -> 
        let m = matchBuildDuration item
        if(m.Success) 
        then { Agent = m.Groups.[1].Value; Duration = m.Groups.[2].Value } 
        else { Agent = ""; Duration = ""}  ) |>
   Array.filter (fun item -> item.Agent <> "" && item.Duration <> "")
~~~

I realised when I started writing the let statement inside the Array.map function on line 4 that I was thinking about this problem way too imperatively. I actually backed out at that stage and had another go but I decided it would be interesting to see what each iteration of the solution would look like if I had actually completed it.

An improvement on that would be to not set up an empty 'CruiseData' like we are doing on line 8 but instead to make use of the Option type to define when we do and do not have a value:


~~~ocaml

let ExtractValues (item:string) =  
   let matchBuildDuration item = Regex.Match(item, "(.*\)),([0-9]+),") 
   Regex.Split(item, "\n") |> 
   Array.map (fun item -> 
    let m = matchBuildDuration item
    if(m.Success) 
    then Some({ Agent = m.Groups.[1].Value; Duration = m.Groups.[2].Value }) 
    else None ) |>
    Array.filter (fun item -> item.IsSome)  
~~~

It's still not great as we have imperative logic inside the Array.map function which looks pretty ugly. 

At this stage I realised that I needed to excluded any lines which didn't match the regular expression so that I wouldn't have to care about them at all.

This was the next solution:


~~~ocaml

let ExtractValues (response:string) =  
    let matchBuildDuration item = Regex.Match(item, "(.*\)),([0-9]+),") 
    Regex.Split(response, "\n") |> 
    Array.filter (fun x -> (matchBuildDuration x).Success) |>
    Array.map (fun x -> (matchBuildDuration x).Groups) |>
    Array.map (fun group -> { Agent = (group.[1].Value); Duration = (group.[2].Value) } )   
~~~

This is better although we are now calling the 'matchBuildDuration' function twice which is a bit wasteful. 

<a href="http://twitter.com/davcamer">Dave</a> pointed out that if we run the data straight through the 'matchBuildDuration' function after splitting the new lines we can remove the need to call the function twice and then inline the function:


~~~ocaml

let ExtractValues (response:string) =  
    Regex.Split(response, "\n") |> 
    Array.map (fun x -> Regex.Match(x, "(.*\)),([0-9]+),"))  |>
    Array.filter (fun x -> x.Success) |>
    Array.map (fun x -> x.Groups) |>
    Array.map (fun group -> { Agent = (group.[1].Value); Duration = (group.[2].Value) } )  
~~~

In all the functions we end up with the following data by executing this function:


~~~text

[|{Agent = "BuildAgentOne"; Duration = "319"};
  {Agent = "BuildAgentTwo"; Duration = "422"}|]
~~~

My current thinking is that if I have more than one expression inside a function it's very probable that there's a better way of solving the problem and if I have conditional logic in there then I've gone very wrong.

I'd be interested to see if there's an even simpler way to solve this problem.
