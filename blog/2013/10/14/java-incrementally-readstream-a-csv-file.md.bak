+++
draft = false
date="2013-10-14 07:27:10"
title="Java: Incrementally read/stream a CSV file"
tag=['java']
category=['Java']
+++

<p>I've been doing some work which involves reading in CSV files, for which I've been using <a href="http://opencsv.sourceforge.net/">OpenCSV</a>, and my initial approach was to read through the file line by line, parse the contents and save it into a list of maps.</p>


<p>This works when the contents of the file fit into memory but is problematic for larger files where I needed to stream the file and process each line individually rather than all of them after the file was loaded.</p>


<p>I initially wrote a variation on totallylazy's <cite><a href="https://code.google.com/p/totallylazy/source/browse/src/com/googlecode/totallylazy/Strings.java?spec=svna4a6ac3d443db02821d434a5d6560cb77ec4ef4a&r=a4a6ac3d443db02821d434a5d6560cb77ec4ef4a#55">Strings#lines</a></cite> to do this and while I was able to stream the file I made a mistake somewhere which meant the number of maps on the heap was always increasing.</p>


<p>After spending a few hours trying to fix this <a href="https://twitter.com/mesirii">Michael</a> suggested that it'd be easier to use an iterator instead and I ended up with the following code:</p>



~~~java

public class ParseCSVFile {
    public static void main(String[] args) throws IOException
    {
        final CSVReader csvReader = new CSVReader( new BufferedReader( new FileReader( "/path/to/file.csv" ) ), '\t' );
        final String[] fields = csvReader.readNext();

        Iterator<Map<String, Object>>() lazilyLoadedFile = return new Iterator<Map<String, Object>>()
        {
            String[] data = csvReader.readNext();

            @Override
            public boolean hasNext()
            {
                return data != null;
            }

            @Override
            public Map<String, Object> next()
            {
                final Map<String, Object> properties = new HashMap<String, Object>();
                for ( int i = 0; i < data.length; i++ )
                {
                    properties.put(fields[i], data[i]);
                }

                try
                {
                    data = csvReader.readNext();
                }
                catch ( IOException e )
                {
                    data = null;
                }

                return properties;
            }

            @Override
            public void remove()
            {
                throw new UnsupportedOperationException();
            }
        };
    }	
}
~~~

<p>Although this code works it's not the most readable function I've ever written so any suggestions on how to do this in a cleaner way are welcome.</p>

