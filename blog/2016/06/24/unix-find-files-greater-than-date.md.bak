+++
draft = false
date="2016-06-24 16:56:17"
title="Unix: Find files greater than date"
tag=['unix']
category=['Shell Scripting']
+++

<p>
For the latter part of the week I've been running some tests against Neo4j which generate a bunch of log files and I wanted to filter those files based on the time they were created to do some further analysis.
</p>


<p>
This is an example of what the directory listing looks like:
</p>



~~~text

$ ls -alh foo/database-agent-*
-rw-r--r--  1 markneedham  wheel   2.5K 23 Jun 14:00 foo/database-agent-mac17f73-1-logs-archive-201606231300176.tar.gz
-rw-r--r--  1 markneedham  wheel   8.6K 23 Jun 11:49 foo/database-agent-mac19b6b-1-logs-archive-201606231049507.tar.gz
-rw-r--r--  1 markneedham  wheel   8.6K 23 Jun 11:49 foo/database-agent-mac1f427-1-logs-archive-201606231049507.tar.gz
-rw-r--r--  1 markneedham  wheel   2.5K 23 Jun 14:00 foo/database-agent-mac29389-1-logs-archive-201606231300176.tar.gz
-rw-r--r--  1 markneedham  wheel    11K 23 Jun 13:44 foo/database-agent-mac3533f-1-logs-archive-201606231244152.tar.gz
-rw-r--r--  1 markneedham  wheel   4.8K 23 Jun 14:00 foo/database-agent-mac35563-1-logs-archive-201606231300176.tar.gz
-rw-r--r--  1 markneedham  wheel   3.8K 23 Jun 13:44 foo/database-agent-mac35f7e-1-logs-archive-201606231244165.tar.gz
-rw-r--r--  1 markneedham  wheel   4.8K 23 Jun 14:00 foo/database-agent-mac40798-1-logs-archive-201606231300176.tar.gz
-rw-r--r--  1 markneedham  wheel    12K 23 Jun 13:44 foo/database-agent-mac490bf-1-logs-archive-201606231244151.tar.gz
-rw-r--r--  1 markneedham  wheel   2.5K 23 Jun 14:00 foo/database-agent-mac5f094-1-logs-archive-201606231300189.tar.gz
-rw-r--r--  1 markneedham  wheel   5.8K 23 Jun 14:00 foo/database-agent-mac636b8-1-logs-archive-201606231300176.tar.gz
-rw-r--r--  1 markneedham  wheel   9.5K 23 Jun 11:49 foo/database-agent-mac7e165-1-logs-archive-201606231049507.tar.gz
-rw-r--r--  1 markneedham  wheel   2.7K 23 Jun 11:49 foo/database-agent-macab7f1-1-logs-archive-201606231049507.tar.gz
-rw-r--r--  1 markneedham  wheel   2.8K 23 Jun 13:44 foo/database-agent-macbb8e1-1-logs-archive-201606231244151.tar.gz
-rw-r--r--  1 markneedham  wheel   3.1K 23 Jun 11:49 foo/database-agent-macbcbe8-1-logs-archive-201606231049520.tar.gz
-rw-r--r--  1 markneedham  wheel    13K 23 Jun 13:44 foo/database-agent-macc8177-1-logs-archive-201606231244152.tar.gz
-rw-r--r--  1 markneedham  wheel   3.8K 23 Jun 13:44 foo/database-agent-maccd92c-1-logs-archive-201606231244151.tar.gz
-rw-r--r--  1 markneedham  wheel   3.9K 23 Jun 13:44 foo/database-agent-macdf24f-1-logs-archive-201606231244165.tar.gz
-rw-r--r--  1 markneedham  wheel   3.1K 23 Jun 11:49 foo/database-agent-mace075e-1-logs-archive-201606231049520.tar.gz
-rw-r--r--  1 markneedham  wheel   3.1K 23 Jun 11:49 foo/database-agent-mace8859-1-logs-archive-201606231049507.tar.gz
~~~

<p>
I wanted to split the files in half so that I could have the ones created before and after 12pm on the 23rd June.
</p>


<p>
I discovered that this type of filtering is actually <a href="http://serverfault.com/questions/122824/linux-using-find-to-locate-files-older-than-date">quite easy to do with the 'find' command</a>. So if I want to get the files after 12pm I could write the following:
</p>



~~~bash

$ find foo -name database-agent* -newermt "Jun 23, 2016 12:00" -ls
121939705        8 -rw-r--r--    1 markneedham      wheel                2524 23 Jun 14:00 foo/database-agent-mac17f73-1-logs-archive-201606231300176.tar.gz
121939704        8 -rw-r--r--    1 markneedham      wheel                2511 23 Jun 14:00 foo/database-agent-mac29389-1-logs-archive-201606231300176.tar.gz
121934591       24 -rw-r--r--    1 markneedham      wheel               11294 23 Jun 13:44 foo/database-agent-mac3533f-1-logs-archive-201606231244152.tar.gz
121939707       16 -rw-r--r--    1 markneedham      wheel                4878 23 Jun 14:00 foo/database-agent-mac35563-1-logs-archive-201606231300176.tar.gz
121934612        8 -rw-r--r--    1 markneedham      wheel                3896 23 Jun 13:44 foo/database-agent-mac35f7e-1-logs-archive-201606231244165.tar.gz
121939708       16 -rw-r--r--    1 markneedham      wheel                4887 23 Jun 14:00 foo/database-agent-mac40798-1-logs-archive-201606231300176.tar.gz
121934589       24 -rw-r--r--    1 markneedham      wheel               12204 23 Jun 13:44 foo/database-agent-mac490bf-1-logs-archive-201606231244151.tar.gz
121939720        8 -rw-r--r--    1 markneedham      wheel                2510 23 Jun 14:00 foo/database-agent-mac5f094-1-logs-archive-201606231300189.tar.gz
121939706       16 -rw-r--r--    1 markneedham      wheel                5912 23 Jun 14:00 foo/database-agent-mac636b8-1-logs-archive-201606231300176.tar.gz
121934588        8 -rw-r--r--    1 markneedham      wheel                2895 23 Jun 13:44 foo/database-agent-macbb8e1-1-logs-archive-201606231244151.tar.gz
121934590       32 -rw-r--r--    1 markneedham      wheel               13427 23 Jun 13:44 foo/database-agent-macc8177-1-logs-archive-201606231244152.tar.gz
121934587        8 -rw-r--r--    1 markneedham      wheel                3882 23 Jun 13:44 foo/database-agent-maccd92c-1-logs-archive-201606231244151.tar.gz
121934611        8 -rw-r--r--    1 markneedham      wheel                3970 23 Jun 13:44 foo/database-agent-macdf24f-1-logs-archive-201606231244165.tar.gz
~~~

<p>And to get the ones before 12pm:</p>



~~~bash

$ find foo -name database-agent* -not -newermt "Jun 23, 2016 12:00" -ls
121879391       24 -rw-r--r--    1 markneedham      wheel                8856 23 Jun 11:49 foo/database-agent-mac19b6b-1-logs-archive-201606231049507.tar.gz
121879394       24 -rw-r--r--    1 markneedham      wheel                8772 23 Jun 11:49 foo/database-agent-mac1f427-1-logs-archive-201606231049507.tar.gz
121879390       24 -rw-r--r--    1 markneedham      wheel                9702 23 Jun 11:49 foo/database-agent-mac7e165-1-logs-archive-201606231049507.tar.gz
121879393        8 -rw-r--r--    1 markneedham      wheel                2812 23 Jun 11:49 foo/database-agent-macab7f1-1-logs-archive-201606231049507.tar.gz
121879413        8 -rw-r--r--    1 markneedham      wheel                3144 23 Jun 11:49 foo/database-agent-macbcbe8-1-logs-archive-201606231049520.tar.gz
121879414        8 -rw-r--r--    1 markneedham      wheel                3131 23 Jun 11:49 foo/database-agent-mace075e-1-logs-archive-201606231049520.tar.gz
121879392        8 -rw-r--r--    1 markneedham      wheel                3130 23 Jun 11:49 foo/database-agent-mace8859-1-logs-archive-201606231049507.tar.gz
~~~

<p>
Or we could even find the ones last modified between 12pm and 2pm:
</p>



~~~bash

$ find foo -name database-agent* -not -newermt "Jun 23, 2016 14:00" -newermt "Jun 23, 2016 12:00" -ls
121934591       24 -rw-r--r--    1 markneedham      wheel               11294 23 Jun 13:44 foo/database-agent-mac3533f-1-logs-archive-201606231244152.tar.gz
121934612        8 -rw-r--r--    1 markneedham      wheel                3896 23 Jun 13:44 foo/database-agent-mac35f7e-1-logs-archive-201606231244165.tar.gz
121934589       24 -rw-r--r--    1 markneedham      wheel               12204 23 Jun 13:44 foo/database-agent-mac490bf-1-logs-archive-201606231244151.tar.gz
121934588        8 -rw-r--r--    1 markneedham      wheel                2895 23 Jun 13:44 foo/database-agent-macbb8e1-1-logs-archive-201606231244151.tar.gz
121934590       32 -rw-r--r--    1 markneedham      wheel               13427 23 Jun 13:44 foo/database-agent-macc8177-1-logs-archive-201606231244152.tar.gz
121934587        8 -rw-r--r--    1 markneedham      wheel                3882 23 Jun 13:44 foo/database-agent-maccd92c-1-logs-archive-201606231244151.tar.gz
121934611        8 -rw-r--r--    1 markneedham      wheel                3970 23 Jun 13:44 foo/database-agent-macdf24f-1-logs-archive-201606231244165.tar.gz
~~~

<p>Or we can filter by relative time e.g. to find the files last modified in the last 1 day, 5 hours:</p>



~~~bash

$ find foo -name database-agent* -mtime -1d5h -ls
121939705        8 -rw-r--r--    1 markneedham      wheel                2524 23 Jun 14:00 foo/database-agent-mac17f73-1-logs-archive-201606231300176.tar.gz
121939704        8 -rw-r--r--    1 markneedham      wheel                2511 23 Jun 14:00 foo/database-agent-mac29389-1-logs-archive-201606231300176.tar.gz
121934591       24 -rw-r--r--    1 markneedham      wheel               11294 23 Jun 13:44 foo/database-agent-mac3533f-1-logs-archive-201606231244152.tar.gz
121939707       16 -rw-r--r--    1 markneedham      wheel                4878 23 Jun 14:00 foo/database-agent-mac35563-1-logs-archive-201606231300176.tar.gz
121934612        8 -rw-r--r--    1 markneedham      wheel                3896 23 Jun 13:44 foo/database-agent-mac35f7e-1-logs-archive-201606231244165.tar.gz
121939708       16 -rw-r--r--    1 markneedham      wheel                4887 23 Jun 14:00 foo/database-agent-mac40798-1-logs-archive-201606231300176.tar.gz
121934589       24 -rw-r--r--    1 markneedham      wheel               12204 23 Jun 13:44 foo/database-agent-mac490bf-1-logs-archive-201606231244151.tar.gz
121939720        8 -rw-r--r--    1 markneedham      wheel                2510 23 Jun 14:00 foo/database-agent-mac5f094-1-logs-archive-201606231300189.tar.gz
121939706       16 -rw-r--r--    1 markneedham      wheel                5912 23 Jun 14:00 foo/database-agent-mac636b8-1-logs-archive-201606231300176.tar.gz
121934588        8 -rw-r--r--    1 markneedham      wheel                2895 23 Jun 13:44 foo/database-agent-macbb8e1-1-logs-archive-201606231244151.tar.gz
121934590       32 -rw-r--r--    1 markneedham      wheel               13427 23 Jun 13:44 foo/database-agent-macc8177-1-logs-archive-201606231244152.tar.gz
121934587        8 -rw-r--r--    1 markneedham      wheel                3882 23 Jun 13:44 foo/database-agent-maccd92c-1-logs-archive-201606231244151.tar.gz
121934611        8 -rw-r--r--    1 markneedham      wheel                3970 23 Jun 13:44 foo/database-agent-macdf24f-1-logs-archive-201606231244165.tar.gz
~~~

<p>Or the ones modified more than 1 day, 5 hours ago:</p>



~~~bash

$ find foo -name database-agent* -mtime +1d5h -ls
121879391       24 -rw-r--r--    1 markneedham      wheel                8856 23 Jun 11:49 foo/database-agent-mac19b6b-1-logs-archive-201606231049507.tar.gz
121879394       24 -rw-r--r--    1 markneedham      wheel                8772 23 Jun 11:49 foo/database-agent-mac1f427-1-logs-archive-201606231049507.tar.gz
121879390       24 -rw-r--r--    1 markneedham      wheel                9702 23 Jun 11:49 foo/database-agent-mac7e165-1-logs-archive-201606231049507.tar.gz
121879393        8 -rw-r--r--    1 markneedham      wheel                2812 23 Jun 11:49 foo/database-agent-macab7f1-1-logs-archive-201606231049507.tar.gz
121879413        8 -rw-r--r--    1 markneedham      wheel                3144 23 Jun 11:49 foo/database-agent-macbcbe8-1-logs-archive-201606231049520.tar.gz
121879414        8 -rw-r--r--    1 markneedham      wheel                3131 23 Jun 11:49 foo/database-agent-mace075e-1-logs-archive-201606231049520.tar.gz
121879392        8 -rw-r--r--    1 markneedham      wheel                3130 23 Jun 11:49 foo/database-agent-mace8859-1-logs-archive-201606231049507.tar.gz
~~~

<p>There are lots of other flags you can pass to find but these ones did exactly what I wanted!</p>

