+++
draft = false
date="2008-09-28 22:50:44"
title="Show pwd all the time"
tag=['pwd', 'shell']
category=['Shell Scripting']
+++

Finally back in the world of the shell last week I was constantly typing 'pwd' to work out where exactly I was in the file system until my colleague pointed out that you can adjust your settings to get this to show up automatically for you on the left hand side of the prompt.

To do this you need to create or edit your .bash_profile file by entering the following command:


~~~text

vi ~/.bash_profile
~~~

Then add the following line to this file:


~~~text

export PS1='\u@\H \w\$ '
~~~


You should now see something like the following on your command prompt:


~~~text

mneedham@Macintosh-5.local /users/mneedham/Erlang/playbox$
~~~

Another colleague pointed out that the information on the left side is completely configurable. The following entry from the manual pages of bash (Type 'man bash' then search for 'PROMPTING') show how to do this:


~~~text

PROMPTING
       When executing interactively, bash displays the primary prompt PS1 when it is ready to read a command, and the secondary prompt PS2 when it needs more input to complete a command.  Bash allows these prompt
       strings to be customized by inserting a number of backslash-escaped special characters that are decoded as follows:
              \a     an ASCII bell character (07)
              \d     the date in "Weekday Month Date" format (e.g., "Tue May 26")
              \D{format}
                     the format is passed to strftime(3) and the result is inserted into the prompt string; an empty format results in a locale-specific time representation.  The braces are required
              \e     an ASCII escape character (033)
              \h     the hostname up to the first `.'
              \H     the hostname
              \j     the number of jobs currently managed by the shell
              \l     the basename of the shell's terminal device name
              \n     newline
              \r     carriage return
              \s     the name of the shell, the basename of $0 (the portion following the final slash)
              \t     the current time in 24-hour HH:MM:SS format
              \T     the current time in 12-hour HH:MM:SS format
              \@     the current time in 12-hour am/pm format
              \A     the current time in 24-hour HH:MM format
              \u     the username of the current user
              \v     the version of bash (e.g., 2.00)
              \V     the release of bash, version + patchelvel (e.g., 2.00.0)
              \w     the current working directory
              \W     the basename of the current working directory
              \!     the history number of this command
              \#     the command number of this command
              \$     if the effective UID is 0, a #, otherwise a $
              \nnn   the character corresponding to the octal number nnn
              \\     a backslash
              \[     begin a sequence of non-printing characters, which could be used to embed a terminal control sequence into the prompt
              \]     end a sequence of non-printing characters
~~~

<a href="http://www.faqs.org/docs/abs/HTML/files.html"> This page</a> has more information on some of the other files that come in useful when shell scripting.
