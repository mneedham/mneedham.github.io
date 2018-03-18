+++
draft = false
date="2009-06-09 23:29:15"
title="F#: Useful for scripting"
tag=['f', 'scripting']
category=['F#']
+++

We had the need to do a bit of scripting recently to change the names of the folders where we store our artifacts to signify which artifacts were created from our build's production branch and which were generated from the main branch.

The problem we had was that we were ending up overwriting old artifacts from the main branch with the production branch's artifacts so we wanted to fix this.

We had already manually changed some of the folder names to work with the changes that had already been made to our deployment script to read from the proposed new folder names.

We therefore had a folder structure that looked like this:

<ul>
<li>Artifacts
<ul>
<li>12</li>
<li>20</li>
<li>45</li>
<li>1000</li>
<li>1001</li>
<li>Trunk-1050</li>
<li>Prod-23</li>
</ul>
</li>
</ul>

All the folders with numbers over 1000 were from the trunk build since our production build is only up to around 50. The trouble in the renaming was around the lower numbers where some could be production or trunk. 

I think this could have been calculated by checking the creation date of the folders but I decided it was quicker at the time to just scan through them and manually note which were of each type.

At the time we didn't have F# installed so I wrote the script in Ruby but I decided to rewrite it later on in an F# script file and then use F# interactive to execute the script.

This is the script I've ended up with:

(rename.fsx)

~~~ocaml

open System
open System.IO
open System.Text.RegularExpressions

let get_position_of_last_folder (dir:string) = dir.LastIndexOf('\\') + 1

let get_last_folder_name (dir:string) = dir.Substring(get_position_of_last_folder dir)
let get_rest_of_dir_name (dir:string) = dir.Substring(0, (get_position_of_last_folder dir)-1)

let create_new_dir_name dir = 
    let prodVersions = seq { yield! [47..48]; yield! [37..45]; yield! [28..34]; } 
    let folderName = get_last_folder_name dir
    let isProdDir = prodVersions |> Seq.exists (fun item -> item = Int32.Parse(folderName))
    
    let build_dir_name branch = (get_rest_of_dir_name dir) + "\\" + branch + "-" + folderName
    
    if (isProdDir) then build_dir_name "Prod" else build_dir_name "Trunk"

let rename_directories =  Array.filter (fun dir -> Regex.IsMatch(get_last_folder_name dir , "^[0-9]") ) >> 
                          Array.iter (fun dir -> Directory.Move(dir, create_new_dir_name dir))
    
rename_directories <| Directory.GetDirectories("C:\\artifacts")
~~~

I don't really like the 'get_position_of_last_folder' function but it helped to remove the duplication in the following two functions. Maybe there's a better way to remove this duplication that I'm not aware of.

We can then execute this by using the following command (note I have added 'C:\Program Files\FSharp-1.9.6.2\bin' to the path):


~~~text

fsi --exec --nologo rename.fsx
~~~

I wrote this script file in Visual Studio so that I could get all the Intellisense help that I need but it's not part of any project - it stands alone!

I learnt about the possibility to do scripting in F# from a blog post by Chris Smith <a href="http://blogs.msdn.com/chrsmith/archive/2008/09/12/scripting-in-f.aspx">where he talks about some of the ways that he's been able to use F# for scripting in his work</a>.

I thought running an F# script would be significantly slower than running an equivalent Ruby one since the F# code needs to be compiled first but I didn't notice that the F# script ran any slower than the Ruby one just from observation.
