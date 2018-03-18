+++
draft = false
date="2017-01-31 05:57:11"
title="Go: Multi-threaded writing to a CSV file"
tag=['go', 'golang']
category=['Go']
description="Writing to a CSV from multiple threads in the Go programming language."
+++

As part of a Go script I've been working on I wanted to write to a CSV file from multiple Go routines, but realised that the built in CSV Writer isn't thread safe.

My first attempt at writing to the CSV file looked like this:


~~~go

package main


import (
	"encoding/csv"
	"os"
	"log"
	"strconv"
)

func main() {

	csvFile, err := os.Create("/tmp/foo.csv")
	if err != nil {
		log.Panic(err)
	}

	w := csv.NewWriter(csvFile)
	w.Write([]string{"id1","id2","id3"})

	count := 100
	done := make(chan bool, count)

	for i := 0; i < count; i++ {
		go func(i int) {
			w.Write([]string {strconv.Itoa(i), strconv.Itoa(i), strconv.Itoa(i)})
			done <- true
		}(i)
	}

	for i:=0; i < count; i++ {
		<- done
	}
	w.Flush()
}
~~~

<p>
This script should output the numbers from 0-99 three times on each line. Some rows in the file are written correctly, but as we can see below, some aren't:
</p>



~~~text

40,40,40
37,37,37
38,38,38
18,18,39
^@,39,39
...
67,67,70,^@70,70
65,65,65
73,73,73
66,66,66
72,72,72
75,74,75,74,75
74
7779^@,79,77
...
~~~

<p>
One way that we can make our script safe is to use a mutex whenever we're calling any methods on the CSV writer. I wrote the following code to do this:
</p>



~~~go

type CsvWriter struct {
	mutex *sync.Mutex
	csvWriter *csv.Writer
}

func NewCsvWriter(fileName string) (*CsvWriter, error) {
	csvFile, err := os.Create(fileName)
	if err != nil {
		return nil, err
	}
	w := csv.NewWriter(csvFile)
	return &CsvWriter{csvWriter:w, mutex: &sync.Mutex{}}, nil
}

func (w *CsvWriter) Write(row []string) {
	w.mutex.Lock()
	w.csvWriter.Write(row)
	w.mutex.Unlock()
}

func (w *CsvWriter) Flush() {
	w.mutex.Lock()
	w.csvWriter.Flush()
	w.mutex.Unlock()
}
~~~

<p>
We create a mutex when <cite>NewCsvWriter</cite> instantiates <cite>CsvWriter</cite> and then use it in the <cite>Write</cite> and <cite>Flush</cite> functions so that only one go routine at a time can access the underlying <cite>CsvWriter</cite>. We then tweak the initial script to call this class instead of calling CsvWriter directly:
</p>



~~~go

func main() {
	w, err := NewCsvWriter("/tmp/foo-safe.csv")
	if err != nil {
		log.Panic(err)
	}

	w.Write([]string{"id1","id2","id3"})

	count := 100
	done := make(chan bool, count)

	for i := 0; i < count; i++ {
		go func(i int) {
			w.Write([]string {strconv.Itoa(i), strconv.Itoa(i), strconv.Itoa(i)})
			done <- true
		}(i)
	}

	for i:=0; i < count; i++ {
		<- done
	}
	w.Flush()
}
~~~

<p>
And now if we inspect the CSV file all lines have been written successfully:
</p>



~~~text

...
25,25,25
13,13,13
29,29,29
32,32,32
26,26,26
30,30,30
27,27,27
31,31,31
28,28,28
34,34,34
35,35,35
33,33,33
37,37,37
36,36,36
...
~~~

<p>
That's all for now. If you have any suggestions for a better way to do this do let me know in the comments or on twitter - I'm <a href="https://twitter.com/markhneedham">@markhneedham</a>
</p>

